import os

DATA_PATH = os.path.abspath(os.path.join(__file__, '..', '..', 'data'))

DATA = {
    'tennet.target': {
        'driver': 'hackaton_eet.data.loaders.TargetData',
        'file_location': 'tennet/verrekenprijzen/verrekenprijzen_clean.csv',
        'columns': ['opregelen', 'Afregelen']
    },
    'tennet.biedprijsladder': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/biedprijsladder/biedprijsladder_clean.csv',
        'columns': ['totaal_min', 'minmax', 'min600', 'min300', 'min100',
                    'pos100', 'pos300', 'pos600', 'posmax', 'totaal_plus']
    },
    'tennet.igcc': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/igcc/igcc_clean.csv',
        'columns': ["mean_IGCC_op", "max_IGCC_op", "mean_IGCC_af", "max_IGCC_af",
                    "mean_opregelen", "mean_Afregelen", "mean_opregelen_reserve",
                    "mean_afregelen_reserve", "mean_Mid_prijs_opregelen",
                    "max_Hoogste_prijs_opregelen", "min_Laagste_prijs_afregelen",
                    "max_rampUp", "avg_rampUp", "max_rampCrossOpregel",
                    "max_rampCrossOpregel_sqr"]
    },
    'tennet.ladderomvang': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/ladderomvang/ladderomvang_clean.csv',
        'columns': ['af_vereist', 'af_res', 'af_reg', 'op_reg',
                    'op_res', 'op_vereist']
    },
    'tennet.verrekenprijzen': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/verrekenprijzen/verrekenprijzen_clean.csv',
        'columns': ['opregelen', 'Afregelen']
    },
    'tennet.onbalans': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/onbalans/onbalans_clean.csv'
    },
    'reuters.dayahead': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'reuters/reuters_clean.csv',
        'columns': ['CON_BEL', 'CON_DEU', 'CON_FRA', 'CON_GBR',
                    'CON_NLD', 'Solar_BEL', 'Solar_DEU', 'Solar_FRA',
                    'Wind_BEL', 'Wind_DEU', 'Wind_FRA', 'Wind_GBR',
                    'Wind_NLD'],
    },
    'pricehub.pricehub': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'price_hub/pricehub_clean.csv',
        'columns': ['EEXSPOT', 'PNSPOT', 'APXSPOT', 'BPXSPOT',
                    'EEXCHSPOT', 'N2EXSPOT', 'TTF', 'EUA',
                    'SPARK_NL', 'APIEUR', 'DARK_DE'],
    },
    'feestdagen': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'general_data/feestdagen_clean.csv',
        'columns': ['type', 'holiday'],
    },
    'gen.enecogen': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'gen/enecogen_clean.csv',
        'columns': ['ALLOC_EET.AMC.ENECOGEN'],
    },
    'gen.gendemand.realisation': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'gen/gendemand_clean.csv',
        'columns': ['allocatie_gendemand', 'h2qt_allocation_demand'],
    },
    'gen.gendemand.forecast': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'gen/gendemand_clean.csv',
        'columns': ['da_forecast_gendemand', 'h2qt_forecast_demand'],
    },
    'gen.weather.forecast': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'gen/weather_clean.csv',
        'columns': ['APX_MC_TEMP_RDAM', 'APX_MC_STRALING_RDAM',
                    'APX_MC_WINDSNELHEID_RDAM', 'APX_MC_NEERSLAG_RDAM',
                    'APX_MC_Gevoelstemp_Rdam', 'APX_MC_TEMP_UTRECHT',
                    'APX_MC_STRALING_UTRECHT', 'APX_MC_WINDSNELHEID_UTRECHT',
                    'APX_MC_NEERSLAG_UTRECHT', 'APX_MC_Gevoelstemp_Utrecht']
    },
    'gen.weather.realisation': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'gen/weather_clean.csv',
        'columns': ['LUCHTTEMP_H_UTR_MC', 'STRALING_H_UTR_MC',
                    'WINDSNELHEID_H_UTR_MC', 'NEERSLAGHH_H_UTR_MC',
                    'GEVOELSTEMP_H_UTR_MC', 'Luchttemp_H_Rdam_MC',
                    'Straling_H_Rdam_MC', 'Windsnelheid_H_Rdam_MC',
                    'Neerslaghh_H_Rdam_MC', 'Gevoelstemp_H_Rdam_MC']
    },
    'gen.wind.forecast': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'gen/wind_clean.csv',
        'columns': ['h2qt_forecast_wind_total', 'forecast_wind_total',
                    'nominal_power_wind_total']
    },
    'gen.wind.realisation': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'gen/wind_clean.csv',
        'columns': ['allocation_wind_total', 'h2qt_allocation_wind_total']
    },
    'apx_bidding_curve': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'apx_bidding_curve/apx_flex_in_curve.csv',
        'columns': ['apx_volume', 'apx_price', 'sell_price_50mw',
                    'sell_price_100mw', 'sell_price_200mw', 'buy_price_50mw',
                    'buy_price_100mw', 'buy_price_200mw']
    }
}
