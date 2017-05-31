
info can be found at
http://www.tennet.org/bedrijfsvoering/Systeemgegevens_voorbereiding/Aangeboden_regel_en_reservevermogen/ladderomvang_15.aspx

-------------------------------------------------------------------------------------------

Headers clean file  
[datetime]: local time including UTC offset
[datetime_local]: local time
[af_vereist]:aanbevolen hoeveelheid secondary reserve ENTSO-E, afregelend
[af_res]:afregelreserve afroeptijd tot een kwartier
[af_reg]:biedingen regelvermogen af
[op_reg]:biedingen regelvermoggen op 
[op_res]:opregelreserve afroeptijd tot een kwartier
[op_vereist]:aanbevolen hoeveelheid secondary reserve ENTSO-E, afregelend

--------------------------------------------------------

* You can assume that this data is available before the start of the PTU.
* So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from this dataset is 30-05-2016 10:00

Hypothesis: the feature [op_reg] says something about the supply of steering capacity to balance the country in case of imbalance. As the imbalance price is the result of supply and demand the feaure [op_reg]
could have influence on the imbalance price. However if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 you do not know the value of this feature. Therefore you have to forecast
it (e.g. use the latest known value as a forecast). 




