Source: amsterdam power exchange
------------------------------------------------------------------------------------------------

## FEATURES 
[datetime]:
[apx_volume]:estimated volume cleared on apx (MWh). Based on true apx price, the intersection of supply and demand is estimated and the corresponding volume.
[apx_price]:settled APX price
[sell_price_50mw]: the price delta on the sell curve corresponding to the cleared volume + 50 MW (the first bid with a volume at least 50 MW larger).
[sell_price_100mw]:
[sell_price_200mw]:
[buy_price_50mw]: the price delta on the buy curve corresponding to the cleared volume + 50 MW (the first bid with a volume at least 50 MW larger).
[buy_price_100mw]:
[buy_price_200mw]:
[datetime_local]:

-----------------------------------------------------------------------------------------------------------

Hypothesis: The feature says [sell_price_50mw] gives an indication what would have happened with the APX price if there was 50 MW more demand for that hour.
It could be an indicator of the available power that is available to ramp up in the intraday market (assuming that all sellers on APX are also sellers in the ID market). 

## CLEANING

- no real cleaning done

## SUMMARY

- N.B. if NA value, there was no bid anymore at that volume

> summary(apx_flex_in_curve)
                      datetime       apx_volume     apx_price      sell_price_50mw  sell_price_100mw  sell_price_200mw 
 2014-06-01 00:00:00+02:00:    1   Min.   :2102   Min.   :  0.12   Min.   : 0.010   Min.   :  0.010   Min.   :   0.05  
 2014-06-01 00:15:00+02:00:    1   1st Qu.:4322   1st Qu.: 29.84   1st Qu.: 1.190   1st Qu.:  2.500   1st Qu.:   5.15  
 2014-06-01 00:30:00+02:00:    1   Median :4818   Median : 36.95   Median : 2.495   Median :  4.810   Median :   9.49  
 2014-06-01 00:45:00+02:00:    1   Mean   :4834   Mean   : 37.61   Mean   : 3.527   Mean   :  6.346   Mean   :  13.07  
 2014-06-01 01:00:00+02:00:    1   3rd Qu.:5341   3rd Qu.: 45.01   3rd Qu.: 4.590   3rd Qu.:  8.060   3rd Qu.:  15.95  
 2014-06-01 01:15:00+02:00:    1   Max.   :8549   Max.   :123.62   Max.   :41.600   Max.   :101.380   Max.   :1896.60  
 (Other)                  :70170                                                                                       
 buy_price_50mw    buy_price_100mw   buy_price_200mw            datetime_local 
 Min.   :-46.060   Min.   :-74.500   Min.   :-526.55   25-10-2015 02:00:    2  
 1st Qu.: -8.670   1st Qu.:-12.090   1st Qu.: -16.04   25-10-2015 02:15:    2  
 Median : -4.060   Median : -6.240   Median :  -8.86   25-10-2015 02:30:    2  
 Mean   : -6.053   Mean   : -8.429   Mean   : -11.79   25-10-2015 02:45:    2  
 3rd Qu.: -1.300   3rd Qu.: -2.380   3rd Qu.:  -4.20   26-10-2014 02:00:    2  
 Max.   : -0.010   Max.   : -0.010   Max.   :  -0.01   26-10-2014 02:15:    2  
 NA's   :12        NA's   :28        NA's   :596       (Other)         :70164 