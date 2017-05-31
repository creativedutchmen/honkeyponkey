Source: gen ebase (= database with demand/wind/weather data at eneco energy trade)

------------------------------------------------------------------------------------------------

## FEATURES 

[datetime]:local time
[ALLOC_EET.AMC.ENECOGEN] : allocation of Enecogen production in kW

-------------------------------------------------------------------------------------------------

* You can assume that the realized data is available at 10:00 for the next day. We can predict quite accurately what the production will be of enecogen the next day.

So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from the realized data is 31-05-2016 23:45.

Hypothesis 1: When encogen is running it used to steer in the R2 market. This could leas to mild imbalance prices.


# CLEANING

- no cleaning done


## SUMMARY

   datetime         ALLOC_EET.AMC.ENECOGEN
 Length:70176       Min.   :-11600        
 Class :character   1st Qu.: -3600        
 Mode  :character   Median :348060        
                    Mean   :335530        
                    3rd Qu.:640960        
                    Max.   :877240  