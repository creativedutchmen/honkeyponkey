Source: reuters

This file contains the day ahead forecast for electricity consumption, solar generation and wind generation for different countries (France,Belgium, Netherlands,Germany) 

-------------------------------------------------------------------------------------------

Headers clean file  
[datetime]: local time including UTC offset. The date is the delivery date of the power 
[datetime_local]:
[CON_BEL]: consumption forecast belgium
[CON_DEU]: consumption forecast germany
[CON_FRA]: consumption forecast france
[CON_GBR]: consumption forecast great britain
[CON_NLD]: consumption forecast holland
[Solar_BEL]: solar forecast belgium
[Solar_DEU]: solar forecast germany
[Solar_FRA]: solar forecast france
[Wind_BEL]: wind forecast belgium
[Wind_DEU]: wind forecast germany
[Wind_FRA]: wind forecast france
[Wind_GBR]: wind forecast great britain
[Wind_NLD]: wind forecast holland

---------------------------------------------------------------------------------------------------

* You can assume that this data is available before 10:00 the previous day.
* So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from this dataset is 31-05-2016 23:00

Hypothesis 1: Suppose there is no wind predicted. The possible wind deviation is then asymmetric.That is it there can only be more wind and not less. This will lead to the country being 'long' and therfore low inbalance prices.
The reverse could be true for days when there is a maxium wind predicted. That is the actual wind could only be less (i.e. high imbalance prices).   
It could be that utilities with wind already compensate for this effect when selling there wind on the spot.  

Hypothesis 2: Any imbalance in the country is absorbed by running power plants. So if there are a lot of power plants running than there is a lot of flexibility to absorb any imbalance (=low imbalance price). There are many power
plants running when there is high power demand and low wind. Thus you could try adding the difference between demand and wind as a feature. Or you could try the ratio demand to wind 



