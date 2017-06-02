"""
pipeline example:

    ##
    from hackaton_eet.data.pipeline import get_all_data, process_features, dat_to_numpy
    from hackaton_eet.data.features import add_day_as_feature
    from hackaton_eet.data.transformers import align_data
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    ## load dataframes target/feature
    feature_data, target_data = get_all_data()

    ## add/select (combined) features
    feature_data = process_features(feature_data, [add_day_as_feature])

    ## convert to numpy for scikit
    X, y, names_feat, names_target = dat_to_numpy(feature_data, target_data)

"""

from hackaton_eet.data.loaders import get_data
from hackaton_eet.data.transformers import align_data
import numpy as np


## helper function to get all features for certain lags
def get_all_data(lags=None):
    """

    :param lags:
    :return:
     X, y
    """
    if not lags:
        lags = [1, 2, 6, 13]
    # lags = list(np.arange(1, 14))

    feature_datasets = {
        'tennet.biedprijsladder': {
            'lags': lags,
            'columns': ['totaal_min', 'minmax', 'min600', 'min300', 'min100',
                        'pos100', 'pos300', 'pos600', 'posmax', 'totaal_plus']
        },
        'tennet.igcc': {
            'lags': lags,
        #     'columns': ['mean_IGCC_op', 'max_IGCC_op', 'mean_IGCC_af', 'max_IGCC_af',
        #                 'mean_opregelen', 'mean_Afregelen', 'mean_opregelen_reserve',
        #                 'mean_afregelen_reserve', 'mean_Mid_prijs_opregelen',
        #                 'max_Hoogste_prijs_opregelen', 'min_Laagste_prijs_afregelen',
        #                 'max_rampUp', 'avg_rampUp', 'max_rampCrossOpregel',
        #                 'IGCCBijdrage_op', 'IGCCBijdrage_af', 'Hoogste_prijs_opregelen',
        #                 'Mid_prijs_opregelen', 'Laagste_prijs_afregelen']
        },
        'tennet.ladderomvang': {
            'lags': lags,
            'columns': ['af_vereist', 'af_res', 'af_reg', 'op_reg',
                        'op_res', 'op_vereist']
        },
        'tennet.verrekenprijzen': {
            'lags': lags,
            'columns': ['opregelen', 'Afregelen']
        },
        # 'tennet.onbalans': {
        #     'lags': [1, 6],
        # },
        'reuters.dayahead': {
            'lags': lags,
            'columns': ['CON_BEL', 'CON_DEU', 'CON_FRA', 'CON_GBR',
                        'CON_NLD', 'Solar_BEL', 'Solar_DEU', 'Solar_FRA',
                        'Wind_BEL', 'Wind_DEU', 'Wind_FRA', 'Wind_GBR',
                        'Wind_NLD'],
        },
        'pricehub.pricehub': {
            'lags': lags,
            'columns': ['EEXSPOT', 'PNSPOT', 'APXSPOT', 'BPXSPOT',
                        'EEXCHSPOT', 'N2EXSPOT', 'TTF', 'EUA',
                        'SPARK_NL', 'APIEUR', 'DARK_DE'],
        },
        # 'feestdagen': {
        #     'lags': [1, 6],
        #     'columns': ['type', 'holiday'],
        # },
        # 'gen.enecogen': {
        #     'lags': [1, 6],
        #     'columns': ['ALLOC_EET.AMC.ENECOGEN'],
        # },
        'gen.gendemand.realisation': {
            'lags': lags,
            'columns': ['allocatie_gendemand', 'h2qt_allocation_demand'],
        },
        'gen.gendemand.forecast': {
            'lags': lags,
            'columns': ['da_forecast_gendemand', 'h2qt_forecast_demand'],
        },
        'gen.weather.forecast': {
            'lags': lags,
            'columns': ['APX_MC_TEMP_RDAM', 'APX_MC_STRALING_RDAM',
                        'APX_MC_WINDSNELHEID_RDAM', 'APX_MC_NEERSLAG_RDAM',
                        'APX_MC_Gevoelstemp_Rdam', 'APX_MC_TEMP_UTRECHT',
                        'APX_MC_STRALING_UTRECHT', 'APX_MC_WINDSNELHEID_UTRECHT',
                        'APX_MC_NEERSLAG_UTRECHT', 'APX_MC_Gevoelstemp_Utrecht']
        },
        'gen.weather.realisation': {
            'lags': lags,
            'columns': ['LUCHTTEMP_H_UTR_MC', 'STRALING_H_UTR_MC',
                        'WINDSNELHEID_H_UTR_MC', 'NEERSLAGHH_H_UTR_MC',
                        'GEVOELSTEMP_H_UTR_MC', 'Luchttemp_H_Rdam_MC',
                        'Straling_H_Rdam_MC', 'Windsnelheid_H_Rdam_MC',
                        'Neerslaghh_H_Rdam_MC', 'Gevoelstemp_H_Rdam_MC']
        },
        'gen.wind.forecast': {
            'lags': lags,
            'columns': ['h2qt_forecast_wind_total', 'forecast_wind_total',
                        'nominal_power_wind_total']
        },
        'gen.wind.realisation': {
            'lags': lags,
            'columns': ['allocation_wind_total', 'h2qt_allocation_wind_total']
        },
        'apx_bidding_curve': {
            'lags': lags,
            'columns': ['apx_volume', 'apx_price', 'sell_price_50mw',
                        'sell_price_100mw', 'sell_price_200mw', 'buy_price_50mw',
                        'buy_price_100mw', 'buy_price_200mw']
        }
    }

    target_dataset = {
        'tennet.target': {
            'columns': ['invoeden', 'Afnemen'],
            'lags': [1]
        }
    }

    #
    feature_data = get_data(feature_datasets)
    target_data = get_data(target_dataset)

    # ad hourly index here:
    # ..
    return feature_data, target_data


def process_features(feature_data, funcs):
    for func in funcs:
        feature_data = func(feature_data)

    return feature_data


def dat_to_numpy(feature_data, target_data):

    X = feature_data.fillna(0).values
    y = target_data.fillna(0).values

    X, y = align_data(X, y)

    X, y = X.T, y.T

    names_feat = np.array(feature_data.T.columns)
    names_target = np.array(target_data.T.columns)

    return X, y, names_feat, names_target
