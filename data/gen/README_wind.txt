
## FEATURES
- datetime = local time
- FL<00> = the allocated wind power in kW, per forecast location
- APX_WFC_FL<00>_FINAL  = day-ahead wind power forecast in Kw, per forecast location
- NOM_FL<00> = the estimated capacity of a forecast location in kW
- allocation_wind_total = sum all forecast locations
- forecast_wind_total = sum of all forecast locations
- nominal_power_wind_total = sum of all forecast locations
- h2qt_allocation_wind_total = quarterly values minus the hourly mean
- h2qt_forecast_wind_total = quarterly values minus the hourly mean --> N.B. quarterly wind values only available after march 2015

------------------------------------------------------------------------

* You can assume that the allocation (realized) data is only available after the fact.
So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from the realized data is 30-05-2016 09:45. 

** You can assume that the forecasted data is available at 10:00 the previous day.
So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from the forecasted data is 31-05-2016 23:45. 

Hypothesis 1: Lots of wind forecasted can only be less hence high imbalance prices.

ypothesis 2: Big hour versus quarter position is relected in imbalance volume/price



























## CLEANING
-  removed FL18,30,33 (empty), FL101 (chaos) from data completely
- converted time stamp from local time (wind_raw.xlsx) to UTC (wind_raw.csv) to local time with time zone (wind_clean.csv)


## RESULTS

> summary(wind_clean)
                      datetime          FL11             FL01            FL02            FL12            FL10      
 2014-06-01 00:00:00+02:00:    1   Min.   :  -320   Min.   : -196   Min.   :  -80   Min.   : -240   Min.   : -440  
 2014-06-01 00:15:00+02:00:    1   1st Qu.:   908   1st Qu.:  832   1st Qu.:  784   1st Qu.: 1108   1st Qu.: 1200  
 2014-06-01 00:30:00+02:00:    1   Median :  3640   Median : 3574   Median : 2880   Median : 3936   Median : 5120  
 2014-06-01 00:45:00+02:00:    1   Mean   :  9399   Mean   : 6261   Mean   : 4203   Mean   : 7458   Mean   : 8789  
 2014-06-01 01:00:00+02:00:    1   3rd Qu.: 10933   3rd Qu.: 8920   3rd Qu.: 7248   3rd Qu.:10484   3rd Qu.:12440  
 2014-06-01 01:15:00+02:00:    1   Max.   :105920   Max.   :55120   Max.   :12192   Max.   :35304   Max.   :42760  
 (Other)                  :70170                                                                                   
      FL03            FL04            FL05            FL06        FL07             FL08            FL09      
 Min.   : -216   Min.   : -240   Min.   : -480   Min.   :0   Min.   : -1800   Min.   : -108   Min.   : -432  
 1st Qu.:    0   1st Qu.: 1300   1st Qu.: 3356   1st Qu.:0   1st Qu.: 10088   1st Qu.:  736   1st Qu.: 1956  
 Median :    0   Median : 5216   Median :10950   Median :0   Median : 36784   Median : 2628   Median : 6740  
 Mean   : 2495   Mean   : 8639   Mean   :16674   Mean   :0   Mean   : 48889   Mean   : 4220   Mean   :14558  
 3rd Qu.:  248   3rd Qu.:13256   3rd Qu.:24728   3rd Qu.:0   3rd Qu.: 93600   3rd Qu.: 6476   3rd Qu.:20170  
 Max.   :35732   Max.   :31980   Max.   :62380   Max.   :0   Max.   :117636   Max.   :14952   Max.   :88528  
                                                                                                             
      FL19            FL22           FL23           FL24           FL25            FL26           FL42       
 Min.   : -156   Min.   : -64   Min.   : -52   Min.   : -52   Min.   : -484   Min.   : -44   Min.   : -28.0  
 1st Qu.:  600   1st Qu.: 304   1st Qu.: 232   1st Qu.: 324   1st Qu.: 1712   1st Qu.:  76   1st Qu.:   0.0  
 Median : 2604   Median :1168   Median : 956   Median : 904   Median : 5572   Median : 268   Median :   0.0  
 Mean   : 4601   Mean   :1847   Mean   :1519   Mean   :1646   Mean   : 9714   Mean   : 511   Mean   : 143.6  
 3rd Qu.: 6800   3rd Qu.:2736   3rd Qu.:2204   3rd Qu.:2248   3rd Qu.:12096   3rd Qu.: 568   3rd Qu.:   0.0  
 Max.   :18840   Max.   :7552   Max.   :5940   Max.   :6992   Max.   :74356   Max.   :3700   Max.   :2036.0  
                                                                                                             
      FL39            FL38            FL40            FL41            FL44            FL45           FL46       
 Min.   : -292   Min.   :  -68   Min.   :-5640   Min.   :  -84   Min.   : -136   Min.   : -12   Min.   : -76.0  
 1st Qu.: 1928   1st Qu.:    4   1st Qu.:  484   1st Qu.:  752   1st Qu.:  128   1st Qu.:   0   1st Qu.:   0.0  
 Median : 6832   Median : 2160   Median : 1612   Median : 3108   Median : 1896   Median :   0   Median :   0.0  
 Mean   :10315   Mean   : 4321   Mean   : 2398   Mean   : 5218   Mean   : 3587   Mean   : 209   Mean   : 545.7  
 3rd Qu.:15657   3rd Qu.: 7184   3rd Qu.: 3484   3rd Qu.: 8109   3rd Qu.: 5244   3rd Qu.:   0   3rd Qu.: 612.0  
 Max.   :41136   Max.   :15296   Max.   : 9904   Max.   :17476   Max.   :15792   Max.   :4672   Max.   :5948.0  
                                                                                                                
      FL47             FL50             FL51            FL56       allocation_wind_total APX_WFC_FL01_FINAL
 Min.   : -28.0   Min.   : -2388   Min.   :-1164   Min.   :  -52   Min.   : -5136        Min.   : -131     
 1st Qu.:   0.0   1st Qu.:     0   1st Qu.:    0   1st Qu.:    0   1st Qu.: 59604        1st Qu.: 1000     
 Median :   0.0   Median :     0   Median :  576   Median :    0   Median :154058        Median : 3460     
 Mean   : 293.4   Mean   : 33045   Mean   : 2045   Mean   : 1043   Mean   :214587        Mean   : 5972     
 3rd Qu.:  60.0   3rd Qu.: 60795   3rd Qu.: 3348   3rd Qu.:    0   3rd Qu.:341660        3rd Qu.: 8120     
 Max.   :6144.0   Max.   :125904   Max.   : 9888   Max.   :15996   Max.   :809396        Max.   :37468     
                                                                                         NA's   :768       
 APX_WFC_FL02_FINAL APX_WFC_FL03_FINAL APX_WFC_FL04_FINAL APX_WFC_FL05_FINAL APX_WFC_FL06_FINAL APX_WFC_FL07_FINAL
 Min.   :  -28      Min.   : -139      Min.   : -120      Min.   : -356      Min.   :0          Min.   :  -753    
 1st Qu.:  872      1st Qu.:    0      1st Qu.: 1640      1st Qu.: 4320      1st Qu.:0          1st Qu.: 11281    
 Median : 2729      Median :    0      Median : 5072      Median :11311      Median :0          Median : 37830    
 Mean   : 4130      Mean   : 2740      Mean   : 8263      Mean   :16616      Mean   :0          Mean   : 48999    
 3rd Qu.: 6904      3rd Qu.: 2629      3rd Qu.:12265      3rd Qu.:23806      3rd Qu.:0          3rd Qu.: 90084    
 Max.   :12085      Max.   :30221      Max.   :31747      Max.   :61935      Max.   :0          Max.   :117544    
 NA's   :768        NA's   :14396      NA's   :768        NA's   :768        NA's   :14108      NA's   :768       
 APX_WFC_FL08_FINAL APX_WFC_FL09_FINAL APX_WFC_FL10_FINAL APX_WFC_FL11_FINAL APX_WFC_FL12_FINAL APX_WFC_FL19_FINAL
 Min.   :  -91.0    Min.   : -137      Min.   : -205      Min.   :  -238     Min.   : -208      Min.   :  -99     
 1st Qu.:  949.8    1st Qu.: 2230      1st Qu.: 1864      1st Qu.:  1122     1st Qu.: 1385      1st Qu.:  706     
 Median : 2700.0    Median : 5891      Median : 5502      Median :  3677     Median : 3814      Median : 2417     
 Mean   : 4155.8    Mean   :12217      Mean   : 8978      Mean   :  8878     Mean   : 7172      Mean   : 4254     
 3rd Qu.: 6210.0    3rd Qu.:15271      3rd Qu.:12616      3rd Qu.: 10266     3rd Qu.: 9787      3rd Qu.: 6001     
 Max.   :14951.0    Max.   :85943      Max.   :42309      Max.   :102819     Max.   :34661      Max.   :18760     
 NA's   :768        NA's   :768        NA's   :768        NA's   :768        NA's   :768        NA's   :768       
 APX_WFC_FL22_FINAL APX_WFC_FL23_FINAL APX_WFC_FL24_FINAL APX_WFC_FL25_FINAL APX_WFC_FL26_FINAL APX_WFC_FL38_FINAL
 Min.   : -20       Min.   : -31       Min.   :  -7       Min.   : -184      Min.   :  -5.0     Min.   :  -36     
 1st Qu.: 375       1st Qu.: 331       1st Qu.: 385       1st Qu.: 2121      1st Qu.:  70.0     1st Qu.: 1301     
 Median :1116       Median : 973       Median : 878       Median : 5616      Median : 232.0     Median : 3680     
 Mean   :1714       Mean   :1478       Mean   :1584       Mean   : 9876      Mean   : 502.9     Mean   : 5293     
 3rd Qu.:2379       3rd Qu.:2083       3rd Qu.:2156       3rd Qu.:12483      3rd Qu.: 536.0     3rd Qu.: 8365     
 Max.   :7409       Max.   :5900       Max.   :6848       Max.   :72954      Max.   :3529.0     Max.   :15232     
 NA's   :768        NA's   :768        NA's   :768        NA's   :768        NA's   :768        NA's   :14492     
 APX_WFC_FL39_FINAL APX_WFC_FL40_FINAL APX_WFC_FL41_FINAL APX_WFC_FL42_FINAL APX_WFC_FL44_FINAL APX_WFC_FL45_FINAL
 Min.   : -246      Min.   : -23.0     Min.   :  -39      Min.   :  -6.0     Min.   : -117      Min.   :  -4.0    
 1st Qu.: 2242      1st Qu.: 614.8     1st Qu.: 1046      1st Qu.:   0.0     1st Qu.:  122      1st Qu.:   0.0    
 Median : 6847      Median :1581.0     Median : 3402      Median :   0.0     Median : 1343      Median :   0.0    
 Mean   : 9992      Mean   :2257.7     Mean   : 5328      Mean   : 159.7     Mean   : 3312      Mean   : 206.2    
 3rd Qu.:14912      3rd Qu.:3136.0     3rd Qu.: 8130      3rd Qu.:   0.0     3rd Qu.: 4451      3rd Qu.:   0.0    
 Max.   :40617      Max.   :9583.0     Max.   :17500      Max.   :2048.0     Max.   :15879      Max.   :4650.0    
 NA's   :768        NA's   :768        NA's   :768        NA's   :768        NA's   :768        NA's   :768       
 APX_WFC_FL46_FINAL APX_WFC_FL47_FINAL APX_WFC_FL50_FINAL APX_WFC_FL51_FINAL APX_WFC_FL56_FINAL forecast_wind_total
 Min.   : -29.0     Min.   :  -6.0     Min.   : -1995     Min.   : -24.0     Min.   :    0      Min.   : -3003     
 1st Qu.:   0.0     1st Qu.:   0.0     1st Qu.: 15337     1st Qu.: 559.8     1st Qu.: 1185      1st Qu.: 52200     
 Median :   0.0     Median :   0.0     Median : 46684     Median :1630.0     Median : 3097      Median :135453     
 Mean   : 542.3     Mean   : 330.5     Mean   : 59389     Mean   :2437.1     Mean   : 4883      Mean   :198081     
 3rd Qu.: 664.0     3rd Qu.: 257.0     3rd Qu.:113545     3rd Qu.:3618.0     3rd Qu.: 7490      3rd Qu.:308111     
 Max.   :5896.0     Max.   :6063.0     Max.   :129000     Max.   :9940.0     Max.   :15915      Max.   :795777     
 NA's   :4512       NA's   :18236      NA's   :34560      NA's   :26404      NA's   :56260                         
    NOM_FL01        NOM_FL02        NOM_FL03        NOM_FL04        NOM_FL05        NOM_FL06    NOM_FL07     
 Min.   :35000   Min.   :12100   Min.   :    0   Min.   :31870   Min.   :57000   Min.   :0   Min.   :117000  
 1st Qu.:42500   1st Qu.:12100   1st Qu.:    0   1st Qu.:31870   1st Qu.:60000   1st Qu.:0   1st Qu.:120000  
 Median :44500   Median :12100   Median :    0   Median :31870   Median :62300   Median :0   Median :120000  
 Mean   :43722   Mean   :12100   Mean   :10193   Mean   :31870   Mean   :61111   Mean   :0   Mean   :119503  
 3rd Qu.:44500   3rd Qu.:12100   3rd Qu.:34650   3rd Qu.:31870   3rd Qu.:62300   3rd Qu.:0   3rd Qu.:120000  
 Max.   :44500   Max.   :12100   Max.   :34650   Max.   :31870   Max.   :62300   Max.   :0   Max.   :120000  
                                                                                                             
    NOM_FL08        NOM_FL09        NOM_FL10        NOM_FL11         NOM_FL12        NOM_FL19        NOM_FL22   
 Min.   :15000   Min.   :26600   Min.   :42500   Min.   : 13800   Min.   :26200   Min.   : 9800   Min.   :7500  
 1st Qu.:15000   1st Qu.:26600   1st Qu.:42500   1st Qu.: 14000   1st Qu.:27000   1st Qu.: 9800   1st Qu.:7500  
 Median :15000   Median :36500   Median :42500   Median : 57600   Median :35800   Median :18760   Median :7500  
 Mean   :15000   Mean   :52882   Mean   :42500   Mean   : 50543   Mean   :32765   Mean   :16173   Mean   :7570  
 3rd Qu.:15000   3rd Qu.:83000   3rd Qu.:42500   3rd Qu.:105000   3rd Qu.:35800   3rd Qu.:18760   3rd Qu.:7680  
 Max.   :15000   Max.   :94600   Max.   :42500   Max.   :106900   Max.   :36000   Max.   :18760   Max.   :7680  
                                                                                                                
    NOM_FL23       NOM_FL24       NOM_FL25        NOM_FL26       NOM_FL38        NOM_FL39        NOM_FL40   
 Min.   :5900   Min.   :6900   Min.   :14900   Min.   : 600   Min.   :    0   Min.   :24500   Min.   :9600  
 1st Qu.:5900   1st Qu.:6900   1st Qu.:16300   1st Qu.: 600   1st Qu.:15250   1st Qu.:34500   1st Qu.:9600  
 Median :5900   Median :6900   Median :24800   Median :2300   Median :15250   Median :34500   Median :9600  
 Mean   :5900   Mean   :6900   Mean   :34922   Mean   :1762   Mean   :12142   Mean   :34975   Mean   :9600  
 3rd Qu.:5900   3rd Qu.:6900   3rd Qu.:50800   3rd Qu.:2300   3rd Qu.:15250   3rd Qu.:34500   3rd Qu.:9600  
 Max.   :5900   Max.   :6900   Max.   :75550   Max.   :3724   Max.   :15250   Max.   :41000   Max.   :9600  
                                                                                                            
    NOM_FL41        NOM_FL42         NOM_FL44        NOM_FL45         NOM_FL46       NOM_FL47       NOM_FL50     
 Min.   :15500   Min.   :   0.0   Min.   :    0   Min.   :   0.0   Min.   :   0   Min.   :   0   Min.   : 24000  
 1st Qu.:15500   1st Qu.:   0.0   1st Qu.: 5900   1st Qu.:   0.0   1st Qu.:   0   1st Qu.:   0   1st Qu.:129000  
 Median :17500   Median :   0.0   Median :15700   Median :   0.0   Median :   0   Median :   0   Median :129000  
 Mean   :16972   Mean   : 434.1   Mean   :12479   Mean   : 992.1   Mean   :2695   Mean   :1506   Mean   :116911  
 3rd Qu.:17500   3rd Qu.:   0.0   3rd Qu.:15700   3rd Qu.:   0.0   3rd Qu.:5870   3rd Qu.:   0   3rd Qu.:129000  
 Max.   :17500   Max.   :2048.0   Max.   :15900   Max.   :4680.0   Max.   :5932   Max.   :6150   Max.   :129000  
                                                                                                 NA's   :34560   
    NOM_FL51        NOM_FL56     nominal_power_wind_total h2qt_forecast_wind_total h2qt_allocation_wind_total
 Min.   : 2500   Min.   :15900   Min.   :534560           Min.   :-71192.0         Min.   :-156468           
 1st Qu.: 9800   1st Qu.:15900   1st Qu.:639780           1st Qu.:  -368.5         1st Qu.:  -4223           
 Median : 9800   Median :15900   Median :699570           Median :     0.0         Median :      1           
 Mean   : 9207   Mean   :15923   Mean   :705580           Mean   :     0.0         Mean   :      0           
 3rd Qu.:10000   3rd Qu.:15900   3rd Qu.:754880           3rd Qu.:   364.5         3rd Qu.:   4265           
 Max.   :10000   Max.   :16020   Max.   :886416           Max.   : 71323.0         Max.   : 158888 