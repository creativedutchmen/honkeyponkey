Source: gen ebase (= database with demand/wind/weather data at eneco energy trade)

------------------------------------------------------------------------------------------------

[datetime] : time with utc offset.
[LUCHTTEMP_H_UTR_MC]: realized air temperature in deg C in Utrecht
[STRALING_H_UTR_MC]: realized radiation in deg C in Utrecht
[WINDSNELHEID_H_UTR_MC]: realized wind speed in m/s
[NEERSLAGHH_H_UTR_MC]: realized amount of precipitation in mm in Utrecht
[GEVOELSTEMP_H_UTR_MC]: realize windchill in deg C in utrecht

[Luchttemp_H_Rdam_MC]: see above but then location=Rotterdam
[Straling_H_Rdam_MC]
[Windsnelheid_H_Rdam_MC]
[Neerslaghh_H_Rdam_MC]
[Gevoelstemp_H_Rdam_MC]

[APX_MC_TEMP_RDAM]: forecasted (10:00 previous day) air temperature in deg C in Rotterdam
[APX_MC_STRALING_RDAM]:
[APX_MC_WINDSNELHEID_RDAM]:
[APX_MC_NEERSLAG_RDAM]:
[APX_MC_Gevoelstemp_Rdam]:

[APX_MC_TEMP_UTRECHT]: forecasted (10:00 previous day) air temperature in deg C in Utrecht
[APX_MC_STRALING_UTRECHT]:
[APX_MC_WINDSNELHEID_UTRECHT]:
[APX_MC_NEERSLAG_UTRECHT]
[APX_MC_Gevoelstemp_Utrecht]

---------------------------------------------------------------------------------------------------

* You can assume that the realized data is only available after the fact.
So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from the realized data is 30-05-2016 09:45. 

** You can assume that the forecasted data is available at 10:00 the previous day.
So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from the forecasted data is 31-05-2016 23:45. 

Hypothesis 1: When the forecasted temperature is high  (i.e. heat wave) power consumption is high due to usage of airco.
Somehow the 'airco' effect is difficult to forecast and sometimes leasd to high imbalance prices.

Hypothesis 2: Also lots of radiation leads sometimes to low imbalance prices due to solar panels which are not forecasted by utilities.

Hypothesis 3: Forecasted of demand tend to have difficulties when the weather deviates a lot of the seasonal norm.   


