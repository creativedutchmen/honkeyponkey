Source: http://www.tennet.org/bedrijfsvoering/ExporteerData.aspx

info can be found at
http://www.tennet.org/bedrijfsvoering/Systeemgegevens_voorbereiding/Aangeboden_regel_en_reservevermogen/Biedprijsladder.aspx

Biedprijsladder ≤ 15 minuten

De grafiek en de tabel Biedprijsladder ≤ 15 minuten tonen per datum per programmatijdseenheid (PTE) prijsinformatie over alle biedingen regelvermogen en reservevermogen met een afroeptijd ≤ 15 minuten, die aan TenneT ter beschikking zijn gesteld. De biedprijsladder ≤ 15 minuten dient als referentie voor partijen om hun biedingen regelvermogen en reservevermogen met een afroeptijd ≤ 15 minuten te positioneren. De biedprijsladder ≤ 15 minuten kan slechts in zeer beperkte mate gebruikt worden om in combinatie met de balans-delta een inschatting te maken van real-time verrekenprijzen:

-------------------------------------------------------------------------------------------

Headers clean file  
[datetime]: local time including UTC offset
[datetime_local]:
[totaal_min]: totaal geboden afregel volume (einde biedladder)
[minmax]: prijs (afgerond) einde biedladder afregelen
[min600]: prijs (afgerond) bij –600 MW
[min300]: prijs (afgerond) bij –300 MW
[min100]: prijs (afgerond) bij –100 MW
[pos100]: prijs (afgerond) bij 100 MW
[pos300]: prijs (afgerond) bij 300 MW
[pos600]: prijs (afgerond) bij 600 MW
[posmax]: prijs (afgerond) einde biedladder opregelen
[totaal_plus]: totaal geboden opregel volume (einde biedladder)

---------------------------------------------------------------------------------------------------

* You can assume that this data is available before the start of the PTU.
* So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from this dataset is 30-05-2016 10:00

Hypothesis: this data show at which price providers of balancing capacity are willing to ramp up or ramp down. It is this price together with the actual imbalance that is steered away by tennet
that actually determines the imbalance price in the end.

However if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 you do not know the value of this feature. Therefore you have to forecast
it (e.g. use the latest known value as a forecast).

