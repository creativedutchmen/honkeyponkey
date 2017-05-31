Source: pricehub (= database with prices at eneco energy trade)
the file is resampled form hour to PTU level to be in line with imbalance prices

------------------------------------------------------------------------------

Headers clean file:
[datetime]: local time including UTC offset. The date is the delivery date of the power 
[datetime_local]:
[hour_seq]: sequential hour counter
[EEXSPOT]: Germany spot price in EUR/MWh
[PNSPOT]: France spot price in EUR/MWh
[APXSPOT]: Holland spot price in EUR/MWh
[BPXSPOT]: Belgium spot price in EUR/MWh
[EEXCHSPOT]: Swiss spot price in EUR/MWh
[N2EXSPOT]: UK spot in GBP!!!!! 
[TTF]: Day ahead TTF price in EUR/MWh (TTF = gas for delivery Dutch grid)
[EUA]: emission price (if you run a powerplant you have to buy emission rights. This is the price of those rights in EUR/ton 
[SPARK_NL]: spark spread in NL -->APXSPOT-2*TTF-0.4*EUA. Gas plant earns the difference between power and (gas+emission).
[APIEUR]: Coal price in EUR
[DARK_DE]: dark spread in DE-->EEXSPOT-0.4*APIEUR-0.9*EUA-3. Coal plant earns the difference between power and (coal+emission)

---------------------------------------------------------------------------------------------------

* You can assume that this data is available before 10:00 the previous day. We assume that we can forecast spot prices perfectly.
* So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from this dataset is 31-05-2016 23:45

Hypothesis 1: Any imbalance in the country is absorbed by running power plants. powerplants are running when they can make money.
They make money when the power price is high and the gas+emission is low. Thus when the SPARK_NL is high. So you could try [SPARK_NL] as a feature.

Hypothesis 2: Any imbalance short could be traded away intraday by dispatchers if there is border capacity. 
There is (in general) border capacity from Germany towards holland if the APXSPOT<=EEXSPOT.
There is (in general) border capacity from belgium towards holland if the APXSPOT<=BPXSPOT.
There is (in general) border capacity from France towards holland if the BPXSPOT<=PNSPOT AND APXSPOT<=BPXSPOT.

So you could add these spreads as a feature.

The reverse hold for imbalance long.


