
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
IN BETA: Undergoing evaluation. Feedback appreciated! 300x300mm printbed minimum required!
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <https://github.com/0ndsk4/VoronUsers/tree/0ndsk4/printer_mods/0ndsk4/Nevermore_Air_Filter">
    <img src="images/New_Nevermore_Max v33.png" alt="Logo">
  </a>

  <h3 align="center">Nevermore Max 3D printer Air Filter</h3>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#About-The-Nevermore">About: Why a Nevermore Max?</a>
      <ul>
        <li><a href="#Why">Why Nevermore?</a></li>
		<li><a href="#But-we-already-have-a-filtered-exhaust">But we already have a filtered exhaust?</a></li>
		<li><a href="#I-have-worked-with-plastics-and-I-am-fine">I've worked with plastics, and I'm fine!</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#BOM">BOM (AND IMPORTANT CARBON INFO)</a></li>
        <li><a href="#installation">Installation</a></li>
		<li><a href="#Built-with">Built with</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About Nevermore Max



Why a Max when the Micro works well? The little bugger is an easy print, nimble, looks great... Why bother making a large unit chewing filament?
			 
	 Well - there are a few reasons, that may or may not affect your decision on what filter is best for you.
			  
	1. We're **LAZY**. A micro cartridge is small and may not last very long. Some will 
	have filament smell again in two weeks.   And while the change is quick and easy,
	its still a chore! A Max has 20x the carbon. 20x the carbon lasts...longer.  
	
	2. We need **BETTER**. Carbon filtration gets better and better the deeper the carbon 
	bed. At the small airflow area of a micro, a deep bed quickly chokes air flow. 
	Ever wondered why a Micro XL cartridge is only 10mm longer than a standard cartridge? 
	Air flow degrades _that_ fast. The surface area of a micro cartridge is just 
	above 1000 mm2. A hefty max filter increases that over ten times at the inside 
	perimeter, and 50 times on the outside perimeter. This means the same powered
	fan could move _much_ more air at _less_ pressure drop.  
	
	3. We catch **PARTICLES**: 3D printer extrusion creates both VOCs and particles. 
	The micro focuses on VOCs, as thats what give off the worst smell and has direct 
	toxic effects, and are difficult to catch once outside of the print chamber. 
	Yet again, PM particles are among the leading causes of death in the world and 
	shouldnt be ignored. I've advocated using a regular room-size hepa for particles 
	in conjunction with a micro before, but with the Max a hepa filtration system is
	 built in. 99+ per cent of particles creat6ed by your printer will be removed 
	 every pass and you wont add dirty air to your room or lungs.  
	 
	4. We need **COOLER**: 3D printing and 3D printing filtration require different things.
	For instance, we _love_ to have a 60C chamber for less ABS warping. At the same
	time, with increasing heat, the VOCs get more heat energy and desorb from the 
	carbon. Sensor testing has shown that turning on a well used carbon filter can 
	_increase_ chamber VOCs. Anything above 50C is generally not good for bads stuff to
	stay attached to the carbon. And while the micro has been shown to work even at 
	80C intake air under a heated bed, it most definitely decreases the time between 
	carbon changes a lot! Having the filter unit outside of the printer allows for the
	carbon to be a few degrees cooler than the printer. That does much for longevity.  
	   
	5. We haz to needz **TECHz**: More space for cooler gadgets. Ever wondered when 
	its time to swap carbon? Well, on the max you could add VOC sensors to both intake
	and exhaust and measure how well the filter is doing its job! Thanks to Dr Dave
	there are even data on which sensors reliably detect the aromatic VOCs we strive
	to catch (a lot of sensors hardly detect extrusion VOCs at all as theyre intended
	for other applications). I've chosen to divide the project into a Basic version
	with just hepa+carbon+fan, but entirely upgradeable to the Pro version 
	including VOC sensors (temp, humidity, filter efficiency), LED/Screen
	/Controller board, servo carbon sealing for (optimal carbon longevity with no
	room VOC carbon depletion) and a 4010 exhaust (negative pressure+vent 
	control).  

	7. Less **NOISE**: Lets face it. A high powered 5015 creates some noise. Two creates
	even more. By increasing the size of the carbon filter, decreasing pressure drop,
	we can run the filter fan slower while still getting the same air flow. We can 
	run the fan at a higher rpm:s and clean the chamber in a jiffy as well.  
			    
			  Convinced? Well, then the Max is for you!
			  
			
<!-- GETTING STARTED -->
## Getting Started

You're ready to build a Nevermore? Cool! The New Max is alot simpler to assemble compared to the first version!

### BOM

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
*6mm* - **16x**
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
*65mm* - **2x** (if four corner mounting points these should be 75mm too - these can be shortened/cut 75mm bolts in either case, as perfect thread at the tip doesnt matter)
*75mm* - **2x** (for 2020 extrusion mounting)

**M3 ULTRA THIN HEAD** (Misumi CBSKE-8 or similar with flat head and head thickness <=0.8mm. For reference, a m3 shcs bolt head is 3mm and a bhcs bolt head is 1.6mm)
*8mm* - 24X
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

### Installation

...TBD...

### Built with
The Voron nevermore Air Filter was modelled in Fusion 360.
* [Fusion 360](http://autodesk.com)

<!-- USAGE EXAMPLES -->


### Why

At the end of the day, a fresh single-pass filtered exhaust (at brand new) has perhaps 70% VOC removal efficiency while still exhausting 30% of the nasty into the air you breathe. A recirculation filter achieving four passes at worn-in 50% efficiency could still remove 94% of the bas stuff. Or 99% at six passes!

The number of passes you get all depends on how well you can seal your build chamber. The better sealed the chamber, the less room VOCs will circulate the carbon and deplete the filter too (VOCs from onions, wall paper or farts might not be as unhealthy as melted plastics VOCs, but they block space in the carbonall the same).

Some will have a hard time achieving a good chamber seal, which creates the biggest drawback of recirculation filters - they're air flow neutral. Meaning, as nothing pulls air into the chamber, air can diffuse freely to the outside through any remaining gaps. And that air could be <i>zero per cent</I> cleaned...

To both have the cake and eat it (yes you can!), a Max can incorporate a 4010 exhaust fan, that is used to keep a slight negative pressure inside the chamber - air will still just get pulled _into_ the chamber through any remaning cracks, not leak outside. Dont ramp it up high, its meant to just barely evict air so that the majority of air flow through the filter is still recirculated.

Air evicted through the exhaust will at least have passed through the carbon filter, dust-filter and HEPA filter at least once (hopefully many more times) - so its a good security measure to have if you dont want to bet on your chamber being hermetically sealed.


### But we already have a filtered exhaust?

Yup, but aside from being one-pass, regular mesh carbon filters mainly consists of...mesh. And active carbon sprinkle - miniscule amounts, not meant to be used 24/7 in a 3d printer.

Just running regular  air through a mesh filter will still depete it in weeks (carbon can't opt to just bind the nasty stuff). Filter exposed to air depletes it too, in time. Friggin' everything depletes carbon. Thats why we need *more*.


<b>The Nevermore</B> has a <i>kilo</i>, or two pounds, of active carbon. Not single-digit grams. And its can be sealed off from the surroundings, so when its not running, its not depleting. Any off-gassing between prints will likewise be kept inside the filter! And when is does run, it has alot of VOC binding capacity! At least a hundred times more compared to a generic solder fume carbon mesh filter. 

This is the filter for the low maintenence crowd (who still want to be safe).

### I have worked with plastics and I am fine!

If you live alone - not impacting other people ??? and feel that way, this filter is not for you! <br>
After all, you???re perfectly allowed to smoke two packs a day or become a opposition politician in Russia too, even though it???s probably not optimal for your health. And on an individual level one can never be sure what the health effects will be, if any - the oldest person ever used to smoke until she was 118 years or so???

But speaking of what we do know, we can say for sure that:<BR>

The WHO:s <I>International Agency for Research of Cancer (IARC)</i> classifies chemical compounds based on the known evidence of human carcinogenics, into four classes (<I>carcinogenic, probably carcinogenic, possibly carcinogenic or not classifiable as carcinogenic to humans</i>).<BR><BR>
Most chemicals fall into the last category, but in the known carcinogenic groups we find several known 3d printer byproducts:<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<B>o Benzene</b><BR>
One of the main fumes from ABS printing. 3ppm regarded as safe, whereas up to 280 ppm of VOCs are produced ABS printing every hour in a small space. Proven to cause different leukemias, and suspected of causing a multitude of other cancers. Female workers in a shoe factory exposed to 40ppm for a long time had a hundredfold higher risk of dying from breast cancer, for instance. Class 1 carcinogenic.<br><BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>o Styrene</B><BR>
Main pollutant in ABS fumes, recently upgraded from possible to probable carcinogenic based on mounting evidence of connection with a close to tripled risk of different leukemias.<br><BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<B>o Butadiene</b><BR>
Another component of ABS printing, and the reason why styrene didn???t get the carcinogenic label for so long (as both are ABS byproducts it was long impossible to know if a cancer type was due to butadiene or styrene. Butadiene is also a known cause and/or cofactor in cardiovascular disease, so you might get your heart attack or stroke a few years earlier by breathing it in for a long time.<br><br>
<u>Other knowns:</U><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;??? What creates the most particles/VOCs from plastics handling is <i>heated extrusion</i>.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;??? Injection molding, vacuum forming and other common industrial methods creates less air pollutants due to less melted plastic surface per kg with direct air/oxygen access/airflow.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;??? 3D printing extrusion takes this to another VOC creation level, as you???re extruding thin layer by thin layer, not trapping any of the extruded melted material from access to oxygen or airflow. Thus, per kilogram of product, it???s the most particle and VOC generating plastic process there is.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;??? Home 3d printers are often used in places without industrial ventilation or industrial wet scrubbing. Indeed, a recent study showed that levels of VOC carcinogenics in plastics recycling plants using heated extrusion processes were mostly within safe limits. However, in surrounding residential homes of those safe-to-work plants, VOC levels were up to <B>42 times</b> the safe limits and consisted of the ventilated byproducts from the plastic plants, due to lower ventilation requirements in homes. The study showed a clear increased lifetime cancer risk, even for the workers in the plants.<br><br>

This is a short list of some key knowns, and only address the most common ABS fumes. Other materials have different VOCs. PETG for instance, releases Toluene, Acetaldehyde, Formaldehyde ??? all of which are known health hazards. Regular PLA and Nylons without additives are usually safer, but still release lower levels of acetone, methyl-methacrylate, and iso-butanol (PLA) and Propylene Glycol and Cyclopentanone (Nylon). Not all fumes are created equal.<br><br>




<!-- CONTRIBUTING -->
## Contributing

Please contribute! I'd like to incorporate VOC sensors, making the filter smart (running on low-noise mode at an acceptable VOC level, then ramp up at the end to clean more thoroughly before doors open).


<!-- LICENSE -->
## License

Distributed under GNU General Public License version 3.0 (GPLv3)



<!-- CONTACT -->
## Contact

0ndsk4#5933  - (http://discord.com/user/0ndsk4#5933) <BR>
Nevermore: [https://github.com/0ndsk4/VoronUsers/tree/0ndsk4/printer_mods/0ndsk4/Nevermore_Air_Filter](https://github.com/0ndsk4/VoronUsers/tree/0ndsk4/printer_mods/0ndsk4/Nevermore_Air_Filter)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [The Voron Dev Team](https://vorondesign.com/)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/screenshot.png

