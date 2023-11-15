# Support for SGP40 VOC sensor
#
# Copyright (C) 2022 Adrien Le Masle
#
# This file may be distributed under the terms of the GNU GPLv3 license.

import logging
import math
from . import bus
from struct import unpack_from
from .voc_algorithm import VOCAlgorithm

SGP40_REPORT_TIME = 1
SGP40_CHIP_ADDR = 0x59
SGP40_WORD_LEN = 2

SGP40_CMD = {
    "GET_SERIAL" : [0x36, 0x82],
    "SOFT_RESET" : [0x00, 0x06],
    "SELF_TEST" : [0x28, 0x0E],
    "MEASURE_RAW_NO_COMP" : [0x26, 0x0F, 0x80, 0x00, 0xA2, 0x66, 0x66, 0x93]
}

class SGP40:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.name = config.get_name().split()[-1]
        self.reactor = self.printer.get_reactor()
        self.i2c = bus.MCU_I2C_from_config(
            config, default_addr=SGP40_CHIP_ADDR, default_speed=100000)
        self.temp_sensor = config.get('ref_temp_sensor', None)
        self.humidity_sensor = config.get('ref_humidity_sensor', None)
        self.voc_scale = config.getfloat('voc_scale', 1. )
        self.mcu = self.i2c.get_mcu()
        self.raw = 0
        self.voc = 0
        self.temp = 0
        self.humidity = 0
        self.min_temp = self.max_temp = 0
        self.plot_voc = config.getboolean('plot_voc', False)
        self.max_sample_time = 1
        self.sample_timer = None
        self.printer.add_object("sgp40 " + self.name, self)
        self._voc_algorithm = VOCAlgorithm()
        self._voc_algorithm.vocalgorithm_init()
        if self.printer.get_start_args().get('debugoutput') is not None:
            return
        self.printer.register_event_handler("klippy:connect",
                                            self.handle_connect)

    def handle_connect(self):
        self._init_sgp40()

        # Dirty way of using more retries
        # This is harcoded in serialhdl.py in Klipper
        def get_response(self, cmds, cmd_queue, minclock=0, reqclock=0):
            retries = 15
            retry_delay = .010
            while 1:
                for cmd in cmds[:-1]:
                    self.serial.raw_send(cmd, minclock, reqclock, cmd_queue)
                self.serial.raw_send_wait_ack(cmds[-1], minclock, reqclock,
                                              cmd_queue)
                params = self.last_params
                if params is not None:
                    self.serial.register_response(None, self.name, self.oid)
                    return params
                if retries <= 0:
                    self.serial.register_response(None, self.name, self.oid)
                    raise error("Unable to obtain '%s' response" % (self.name,))
                reactor = self.serial.reactor
                reactor.pause(reactor.monotonic() + retry_delay)
                retries -= 1
                retry_delay *= 2.
        self.i2c.i2c_read_cmd._xmit_helper.get_response = get_response

        self.reactor.update_timer(self.sample_timer, self.reactor.NOW)

    def setup_minmax(self, min_temp, max_temp):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def setup_callback(self, cb):
        self._callback = cb

    def get_report_time_delta(self):
        return SGP40_REPORT_TIME

    def _init_sgp40(self):
        
        # Self test
        self_test = self._read_and_check(SGP40_CMD["SELF_TEST"], wait_time_s = 0.5)
        if self_test[0] != 0xD400:
           logging.exception("sgp40: Self test error")
		
        self.sample_timer = self.reactor.register_timer(self._sample_sgp40)

    def _sample_sgp40(self, eventtime):
        if self.temp_sensor != None:
            self.temp = self.printer.lookup_object("{}".format(self.temp_sensor)).get_status(eventtime)["temperature"]
        else:
            # Temperatures defaults to 25C
            self.temp = 25
        if self.humidity_sensor != None:
            try:
                self.humidity = self.printer.lookup_object("{}".format(self.humidity_sensor)).get_status(eventtime)["humidity"]
            except KeyError:
                 self.humidity = 50
        else:
            # Interpolate relative humidity assuming a CLOSED chamber and INITIAL 50% HUMIDITY at 25C;
	        #   humidity = P(water_vapour) / P(saturation_vapour_pressure)
            #   
	        #   Relationship between temp and saturation vapor pressure:
            #     https://www.engineeringtoolbox.com/water-vapor-saturation-pressure-d_599.html
            #     
            #   Approximate change in Saturation Vapor pressure at temperature T [25<T<80]
	        #     P(Saturation_vapor_pressure_T) / P(Saturation_vapor_pressure_25C) = exp(0.0499860*T - 1.1674630)
            self.humidity = 50. / math.exp(0.0499860*self.temp - 1.1674630)
        cmd = [0x26, 0x0F] + self._humidity_to_ticks(self.humidity) + self._temperature_to_ticks(self.temp)
        value = self._read_and_check(cmd)
        self.raw = value[0]

        self.voc = self._voc_algorithm.vocalgorithm_process(self.raw)

        measured_time = self.reactor.monotonic()
        self._callback(self.mcu.estimated_print_time(measured_time), self.voc * self.voc_scale)
        return measured_time + SGP40_REPORT_TIME

    def _read_and_check(self, cmd, read_len=1, wait_time_s=0.05):
        reply_len = read_len * (SGP40_WORD_LEN + 1) # CRC every word

        self.i2c.i2c_write(cmd)

        if reply_len == 0:
            return None

        # Wait
        self.reactor.pause(self.reactor.monotonic() + wait_time_s)

        params = self.i2c.i2c_read([],reply_len)
        response = bytearray(params['response'])

        data = []

        for i in range(0, reply_len, 3):
            if not self._check_crc8(response[i : i + 2], response[i + 2]):
                logging.warn("sgp40: Checksum error on read!")
            data.append(unpack_from(">H", response[i : i + 2])[0])

        return data

    def _check_crc8(self, data, crc):
        return crc == self._generate_crc(data)

    def _temperature_to_ticks(self, temperature):
        ticks = int(round(((temperature + 45) * 65535) / 175)) & 0xFFFF
        data = [(ticks >> 8) & 0xFF, ticks & 0xFF]
        crc = self._generate_crc(data)

        return data + [crc]

    def _humidity_to_ticks(self, humidity):
        ticks = int(round((humidity * 65535) / 100)) & 0xFFFF
        data = [(ticks >> 8) & 0xFF, ticks & 0xFF]
        crc = self._generate_crc(data)

        return data + [crc]

    def _generate_crc(self, data):
        # From SGP40 data sheet
        crc = 0xFF
        for i in range(2):
            crc ^= data[i]
            for bit in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ 0x31
                else:
                    crc = crc << 1
        return crc & 0xFF

    def get_status(self, eventtime):
        # HACKL can only plot on mainsail/fluidd if VOC index is a temperature
        if self.plot_voc:
            return {"temperature": self.voc * self.voc_scale }
        else:
            return {
              'temperature': self.temp,
              'humidity': self.humidity,
              'gas': self.raw,
	      'voc': self.voc
            }


def load_config(config):
    # Register sensor
    pheaters = config.get_printer().load_object(config, "heaters")
    pheaters.add_sensor_factory("SGP40", SGP40)
