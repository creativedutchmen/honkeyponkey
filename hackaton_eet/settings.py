import os

DATA_PATH = os.path.abspath(os.path.join(os.getcwd(), '..', 'data'))

DATA = {
    'tennet.biedprijsladder': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/biedprijsladder/biedprijsladder_clean.csv',
        'columns': ['totaal_min', 'minmax', 'min600', 'min300', 'min100',
                    'pos100', 'pos300', 'pos600', 'posmax', 'totaal_plus']
    },
    'tennet.igcc': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/igcc/igcc_clean.csv'
    },
    'tennet.ladderomvang': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/ladderomvang/ladderomvang_clean.csv'
    },
    'tennet.target': {
        'driver': 'hackaton_eet.data.loaders.TargetData',
        'file_location': 'tennet/verrekenprijzen/verrekenprijzen_clean.csv',
        'columns': ['opregelen', 'Afregelen']
    },
    'tennet.verrekenprijzen': {
        'driver': 'hackaton_eet.data.loaders.RealisedData',
        'file_location': 'tennet/verrekenprijzen/verrekenprijzen_clean.csv',
        'columns': ['opregelen', 'Afregelen']
    },
    'reuters.dayahead': {
        'driver': 'hackaton_eet.data.loaders.PredictedData',
        'file_location': 'reuters/reuters_clean.csv',
        'columns': ['CON_BEL', 'CON_DEU', 'CON_FRA', 'CON_GBR',
                    'CON_NLD', 'Solar_BEL', 'Solar_DEU', 'Solar_FRA',
                    'Wind_BEL', 'Wind_DEU', 'Wind_FRA', 'Wind_GBR', 'Wind_NLD'],
    },
}
