Source: gen ebase (= database with demand/wind/weather data at eneco energy trade)

------------------------------------------------------------------------------------------------

[datetime]: datetime
[allocatie_gendemand]: allocation of Eneco's demand portfolio in kW (allocation=realization)
[da_forecast_gendemand]: day-ahead forecast logging op EET's demand portfolio in kW
[h2qt_forecast_demand]: quarterly value of the forecast minus hourly mean of the forecast
[h2qt_allocation_demand]: quarterly value of the allocation minus hourly mean of the allocation

--------------------------------------------------------------------------------------------------

* You can assume that the allocation data is only available after the fact.
So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from the realized data is 30-05-2016 09:45. 

** You can assume that the forecasted data is available at 10:00 the previous day.
So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from the forecasted data is 31-05-2016 23:45. 

Hypothesis 1: The APX has hourly granularity. Whereas our customers have 15 min granluarity. Therefore the feature [h2qt_forecast_demand] could be included in model. 