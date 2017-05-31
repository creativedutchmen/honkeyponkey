Source: http://www.tennet.org/bedrijfsvoering/ExporteerData.aspx

------------------------------------------------------------------------------

Headers clean file:
[datetime]: local time including UTC offset
[datetime_local]: local time
[regeltoestand]:De Regeltoestand wordt altijd vermeld en heeft de waarde –1, 0, 1 of 2 en is van invloed op de vaststelling van de onbalansprijs.
[afnemen_EURMWh]:Afnemen wordt altijd vermeld en geldt de verrekenprijs van onbalans van de PV's met tekort: de PV betaalt TenneT TSO deze prijs (indien negatief betaalt TenneT de PV).
[invoeden_EURMWh]:Invoeden wordt altijd vermeld en geldt de verrekenprijs van onbalans van PV's met overschot: TenneT betaalt de PV deze prijs (indien negatief betaalt de PV TenneT)

[afregelvermogen_MW]: [afregelvermogen_kWhPTE]/1000*4
[opregelvermogen_MW]: [opregelvermogen_kWhPTE]/1000*4
[saldo_MW:] [saldo_kWhPTE]/1000*4   'negative means country is long'
[onbalans_MW]:[onbalans_kWhPTE]/1000*4 'positive means country is long'
[onbalans_MWh]:[onbalans_kWhPTE]/1000 'positive means country is long'
[inkoop_MW]:[inkoop_kWhPTE]/1000*4
[verkoop_MW]:[verkoop_kWhPTE]/1000*4

-----------------------------------------------------

[afregelvermogen_kWhPTE]:afregelvermogen: op basis van inzet van biedingen regelvermogen door FVR
[opregelvermogen_kWhPTE]:opregelvermogen: op basis van inzet van biedingen regelvermogen door FVR
[saldo_kWhPTE]:[afregelreserve_kWhPTE]+[afregelvermogen_kWhPTE]+[opregelvermogen_kWhPTE]+[opregelreserve_kWhPTE]+[noodvermogen_kWhPTE]
[afregelreserve_kWhPTE]:op basis van afroep van biedingen reservevermogen (tertiary control). Max -225 MW. 8 hours per year
[opregelreserve_kWhPTE]:opregelreserve: op basis van afroep van biedingen reservevermogen
[noodvermogen_kWhPTE]:op basis van inzet noodvermogen . Max 380 MW. 30 hours per year

[onbalans_kWhPTE]:[inkoop_kWhPTE]+[verkoop_kWhPTE]

[inkoop_kWhPTE]:energie van Programma Verantwoordelijken met overschot aan TenneT 
[verkoop_kWhPTE]:energie van TenneT aan Programma Verantwoordelijken met tekort

--------------------------------------------------------

* You can assume that this data is available at the start of the next 15 min interval.
* So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from this dataset is 30-05-2016 09:45

Hypothesis: there might be a correlation between the feature [opregelvermogen_MW] and the imbalance price (Afnemen). However you only know the value of the feature [opregelvermogen_MW] after the fact.
Therefore you might want to forecast this feature and use this instead in your model (e.g. use the lastest know value as a forecast).   









