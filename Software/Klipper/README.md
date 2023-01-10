**Installation instructions**

* Copy sgp40.py and voc_algorithm.py to klippy/extras
* The printer.cfg syntax is as follows
```
[sgp40]

[temperature_sensor voc_exhaust]
sensor_type: SGP40
#i2c_mcu:
#   The name of the micro-controller that the chip is connected to.
#   The default is "mcu".
#i2c_bus:
#   If the micro-controller supports multiple I2C busses then one may
#   specify the micro-controller bus name here. The default depends on
#   the type of micro-controller.
#i2c_speed:
#   The I2C speed (in Hz) to use when communicating with the device.
#   The Klipper implementation on most micro-controllers is hard-coded
#   to 100000 and changing this value has no effect. The default is
#   100000.
# ref_temp_sensor:
# The name of the temperature sensor to use as reference for temperature
# compensation of the VOC raw measurement
# ref_humidity_sensor:
# The name of the temperatur sensor to use as reference for humidity
# compensation of the VOC raw measurement
```

**Example configuration**

The following is an example using a BME280 and SGP40 on both the intake and the exhaust.
The intake sensors are connected to GP12/GP13 bus on the Raspberry Pi Pico and the exhaust sensors
are connected to GP14/GP15.

```
[sgp40]

[temperature_sensor temp_intake]
sensor_type: BME280
i2c_mcu: pico
i2c_bus: i2c0d
i2c_speed: 400000

[temperature_sensor temp_exhaust]
sensor_type: BME280
i2c_mcu: pico
i2c_bus: i2c1d
i2c_speed: 400000

[temperature_sensor voc_intake]
sensor_type: SGP40 # Sensor on the top left
i2c_mcu: pico
i2c_bus: i2c0d
ref_temp_sensor: bme280 temp_intake
ref_humidity_sensor: bme280 temp_intake
i2c_speed: 400000

[temperature_sensor voc_exhaust]
sensor_type: SGP40 # Sensor on the right
i2c_mcu: pico
i2c_bus: i2c1d 
ref_temp_sensor: bme280 temp_exhaust
ref_humidity_sensor: bme280 temp_exhaust
i2c_speed: 400000
```

**Mainsail**

In order to display the full VOC sensor information in Mainsail, the following command needs to be run **once** in the mainsail directory:
```
grep -l additionalSensors * -R | xargs sed -i 's+additionalSensors=\[+additionalSensors=\["sgp40",+g'
```
This command will need to be rerun each time Mainsail is updated

**Sources**

The voc_algorithm.py module is a slightly modified version of the module found in the [Adafruit CircuitPython SGP40 repository](https://github.com/adafruit/Adafruit_CircuitPython_SGP40).
