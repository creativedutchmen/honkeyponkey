Source: http://www.tennet.org/bedrijfsvoering/ExporteerData.aspx

info can be found at
http://www.tennet.org/bedrijfsvoering/Systeemgegevens_uitvoering/Systeembalans_informatie/balansdeltaIGCC.aspx#PanelTabDescription

IGCC=International Grid Control Cooperation. IGCC is a mechanism that TSO's use to net the imbalance between countries.
So if Germany has a long position (i.e. more energy than expected) 
AND Holland has short position 
AND there is capacity on the transmission cable between Germany and Holland. In general there is transmission capacity to Holland when German spot price >= Holland spot price
THEN both TSO's will net their imbalance position. 

The IGCC data is published with minute granularity. This file has minute data resampled to 15 minutes.

IGCC_op means a short position in Holland is netted with a long position outside hollland
IGCC_af means a long position in Holland is netted with a short position outside hollland  
-------------------------------------------------------------------------------------------
Headers clean file  
[datetime]: local time including UTC offset
[datetime_local]: local time
[mean_IGCC_op]: The mean of [IGCCBijdrage_op] in this PTU
[max_IGCC_op]: The max of [IGCCBijdrage_op] in this PTU
[mean_IGCC_af]: The mean of [IGCCBijdrage_af] in this PTU
[max_IGCC_af]: The max of [IGCCBijdrage_af] in this PTU
[mean_opregelen]: the average of opregel volume in MW in this PTU 
[mean_Afregelen]: the average of Afregel volume in MW in this PTU
[mean_opregelen_reserve]: the average of opregel reserve volume in MW in this PTU 
[mean_afregelen_reserve]: the average of Afregel reserve volume in MW in this PTU
[mean_Mid_prijs_opregelen]: the mean of the minute price opregelen
[max_Hoogste_prijs_opregelen]: the max of the opregel prijs in this PTU
[min_Laagste_prijs_afregelen]: the min of the afregel price in this PTU
[max_rampUp]:maximum minute ramp up in this PTU
[avg_rampUp]:average minute ramp up in this PTU
[max_rampCrossOpregel]: maximum of ramp*opregelen in this PTU
-------------------------------------------------------------------------------------------------
[IGCCBijdrage_op]:de levering van vermogen door IGCC aan TenneT
[IGCCBijdrage_af]:de levering van vermogen door TenneT aan IGCC  
[Hoogste_prijs_opregelen]:inzetprijs van de geactiveerde bieding met de hoogste biedprijs
[Mid_prijs_opregelen]:de berekende default inzetprijs (gemiddelde van de startprijzen van de op- en afregelladders; van toepassing wanneer TenneT geen vermogen heeft geactiveerd in de PTE waartoe deze minuut behoort)
[Laagste_prijs_afregelen]:inzetprijs van de geactiveerde bieding met de laagste biedprijs

---------------------------------------------------------------------------------------------------

* You can assume that this data is available at the start of the next 15 min interval.
* So if you forecast the imbalance price (Afnemen;invoeden) at 30-05-2016 10:00 for 31-05-2016 23:45 the last point you can use from this dataset is 30-05-2016 09:45

Hypothesis: When there is IGCC flow the imbalance in Holland will be (partly) gone, this will influence imbalance prices. So if you can forecast the availability of IGCC you might want to include this as a feature. 