**PANEL**

Front panel in 6mm or 1/4" transparent plastic. Polycarbonate, PET or *molded* Acrylic will work fine. 
Size depends on your Max material of choice because of shrinkage factor. Actual measurments TBD (slightly smaller than 300x300mm).

Mid and back panels are now 3D printed!

**FANS**
* CENTER fan: has two options. The expensive choice is the **Sanyo 9TD12P6G001**. A 70x20mm radial blower capable of over 500Pa of static pressure or >40cfm, excellent build quality and made to work in up to 70C temperatures, as well as low noise capability. Its very pricey ($50), and has been hard to get hold of during the chip shortage. The other option is the **DELTA BFB0712HF 65mm GPU fan.** which was originally made to push alot of air through restrictive and hot 1060 grahics card coolers, and should hold upp well for this similar job. On Ali they go from as low as $5 up to about $15, and are thus alot more affordable and practically always in stock. They also perform *almost* as well as the Sanyo.

## **SEALING**

*2mm* **neoprene/silicone/rubber *sponge cord*** (~2meters). The *soft and squishy kind*, Shore 00 range hardness (anything around 50 +-15 will work well). 

*3mm* **neoprene/silicone/rubber sponge cord** (~1meter).

RTV (preferably clear or in the color of your printed panels (or side shrouds, if not using 2mm spong cord)

*5-6mm* wide **Closed cell foam tape** *or* **self expanding PU tape**(mainly for sealing of the back panel or possibly under the front panel if not using 3mm sponge cord - not too thick, made to cover a ~1mm gap or so).


## BOLTS

**M3 BHCS**
*6mm* - **21x**
*8mm* - **20x** (in most places, shcs will work too or even be preferable. 12 are visible at the side shrouds, the smaller profile can be nice at this spot)

**M3 SHCS**
*6mm* - **2x**
*10mm* - **1x** (center mounting, can also be 8mm if not using rolling t-nuts) 
*12mm* - **8x**
*16mm* - **5x**
*20mm* - **12x**
*25mm* - **4x**
*30mm* - **2x**
*40mm* - **4x**
*65mm* - **2x** (if four corner mounting points these should be 70mm too, standard mounting hanging on a top extrusion is 65mm)
*70mm* - **2x** (for 2020 extrusion mounting)

**M3 ULTRA THIN HEAD** (Misumi CBSKE-8 or similar with flat head and head thickness <=0.8mm. For reference, a m3 shcs bolt head is 3mm and a bhcs bolt head is 1.6mm)
*8mm* - 19X
*6mm* - 2x (optional)

***OPTIONAL ELECTRONICS*****
 - (2x) SGP40 VOC sensor + BME280 humidity/temp sensor (Gravity ENS160 sensor is  being evaluated too).**
 - HS-125MG Servo**
 - Generic 4010 Fan**
 - 16 neopixel ring**
 - 2 individual neopixels**

**for pimped up Pro version of the filter.

## *CARBON*

* Active carbon: 4mm activated  carbon pellets. Pellets are preferred because they're less dusty and has lower pressure drop than granules (GAC). 4x6 mesh GAC is the most similar to 4mm pellets if thats what you can get hold of. 4x8 mesh and smaller will impact air flow due to higher pressure drop, but potentially increase filtering efficiency for air that *does* pass through.
* If you wish to *support the project* and get the best possible filtration at the same time, **Nevermore carbon** bags are available in several 3D printer shops and is a *safe* and optimal choice with the market leading filtration efficiency/longeivity, and porosity optimized for 3D printing aromatic VOCs and use in Nevermore filters. Ther carbon comes *de-dusted* and *vacuum packed* to avoid shipping grinding and new dust generation, so you can use it right out of the bag with no pre-treatment. It also has the best adsorbtion specs of any carbon currently available on the market, up to **4x better** (*2x efficiency, 2x longevity*) compared to no-name carbon (surface area >1250, benzene adsorbtion up to 48pct.wt, CTC 80, ball pan hardness 98). The cost is the downside though, if you look for good suppliers you can probably find options that are 80% as good at 60% the cost;

* **IMPORTANT**! Since first release the *varying quality carbon out there has become increasingly evident*. Users has both gotten bad carbon as well as outright dangerous stuff (in one case oxidizing most metal surfaces in a new voron in minutes. Be sure to vet your carbon supplier! 

* When sourcing the *optimal carbon* for 3D printer VOC adsorbtion, look for ***virgin coconut*** or ***anthracite*** carbon, not wood/bitumen/charcoal/bamboo/lignin. Why are these better? Well, while there are certain high grade, say bituminous activated carbon, there are also even more low grade bituminous carbon. For virgin coconut and anthracite from a vetted supplier, you'd be hard pressed to get bad carbon for #D printer VOC filtration. Grade and porosity matters;
	* Porosity for each and every source varies greatly (i.e, for aquarium or moonshine use you want large *macroporosity* to filter larger impurities, like oils. For that reason, water/liquid use carbon  has a large macropore area, defined as >100nm. Printer VOCs are generally less than 0.5 nm, meaning that for optimal capture rate and efficiency we want carbon with a high *microporosity* ratio, defined as <1nm). 
	* A higher **iodine count** >1000 usually indicates at least some micro/mesoporosity, and a higher **hardness** (>95%) will create less dust in air filtration. CTC number doesnt translate well to our VOCs, but toluene/benzene adsorbtion - which sometimes is available - is a good metric. 
	* **Avoid acid washed carbon**. Residues from bad acid washed carbon have oxidized printers! Go for steam activated, non acid-washed. By not using pH treated carbon, you will also adsorb a larger range of gasses.  A blend of different pH adsorbants might be the best choice in the future, but is currently impossible to source from trustworthy manufacturers. Good acid washed carbon shouldn't inherintly be harmful to the printer (the acids are supposed to should stay locked inside the carbon), but it will catch a lesser range of VOCs and there's always the risk of that bad batch that has lots of acid residue left - so its best to avoid.
	* **Don't wash carbon** meant for air filtration. You will just bind water and water electrolytes to the carbon, so even if you dry it afterwards you will have lost a noticable percentage of capacity. If you have dusty carbon, blow away the dust (for a micro cartridge, blowing harmonica style out a window is a good option).
* Finding carbon that fills all criteria is hard, but will hopefully become easier in time (working on that). Look around, ask suppliers about the carbon, hear what others recommend.

* **HEPAs**: 4x *Chuwi iLife 40x80mm* filters (get a ten pack for three bucks on ali)<br>
Example Seller: https://www.aliexpress.com/item/1005001615722382.html<br>

**PRINTED PARTS:**
* 300x300mm print bed minimum (the frame piece is a square 298mm by 278mm, so your printer needs to be able to print over the entire surface and watch out for any skirts extending more than 2 mm outside the print job if doing this on a 300 machine).
* This was developed with and for **ABS+** material. Regular ABS *may* work depending on your printer, chamber heat and settings, but can also create *alot of unneccesary woes*! Printing a full bed size piece **will cause warping** in warp prone materials - hence do consider ABS+. I print in titanX - an ABS+ material - on PEI with no issues. Since this will be positioned outside the printer, there is also the option to print in other matierals. While I wouldn't print this in PLA if you plan on filtering a hot chamber that might reach above 60-70C under certain circumstances, PETG is probably fine. 
	* I use 3 walls and 16% gyroid infill. It might be wise to go to 4%+40% - or even solid for maximum rigidity - but after several kilos of prototyping I'm minimizing waste...
	* **Parts shrinkage** 
		* If using shrinking materials like ABS/ABS+/etc, parts shrinkage could be a factor. Parts do not always shrink evenly, for instance the square frame shrinks very little as its supported from all sides, while I needed to make the printer intake/exhaust piece 1% longer (with titanX ABS+ type filament) to fit into the frame. The other pieces have been usable as is without shrinkage compensation.
		* 
