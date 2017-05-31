Source: http://www.tennet.org/bedrijfsvoering/ExporteerData.aspx

info can be found on: http://www.tennet.org/bedrijfsvoering/Systeemgegevens_afhandeling/verrekenprijzen/index.aspx

--------------------------------------------------------------------------------

Headers clean file
datetime: local datetime with UTC offset. This is the start time of the quarter.

datime_local:local datetime

noodvermogen: if noodvermogen is called 1 otherwise zero

opregelen: price for ramping up powerplant

Afregelen: price for ramping down powerplant

prikkelcomponent:
http://www.tennet.org/bedrijfsvoering/Systeemgegevens_afhandeling/prikkelcomponent/prikkelcomponent_2006.aspx
De prikkelcomponent is onderdeel van de onbalansprijs en is bedoeld ter stimulering van het daadwerkelijk nakomen door marktpartijen van door TenneT gebruikte biedingen regel- en reservevermogen voor balanshandhaving en balansherstel en als prikkel om de te verrekenen onbalans te minimaliseren.

Afnemen: price for being short. Extracting from the grid. This is the price in EUR/MWh you pay when you're short. I.e. there is less wind than expected

invoeden: price for being long. Feeding to the grid. This is the price you receive in EUR/MWh when you're long. I.e there is more wind than expected.

regeltoestand: indicator for the 'toestand' of the country. 1=opregelen,-1=afregelen

--------------------------------------------------------------------------------

* You can assume that this data is available at the start of the next 15 min interval. 
* So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from this dataset is 30-05-2016 09:45

Hypothesis: There might be a correlation between the imbalance price on a certain PTU (=15 min interval) and that same PTU the previous day (or same day and PTU previous week).
So if you want to forecast you could add as a feature that same PTU but the previous week.


