"""
Placeholder for all feature engineering
"""

def add_day_as_feature(feature_data):
    # add day index
    dayidx = feature_data.T.index.weekday_name

    feature_data = feature_data.T
    feature_data['day_idx'] = dayidx
    feature_data = feature_data.T

    return feature_data

def add_ptu_as_feature(feature_data):
    ptu = feature_data.T.index.hour * 4 + (1 + feature_data.T.index.minute / 15)

    feature_data = feature_data.T
    feature_data['ptu'] = ptu
    feature_data = feature_data.T

    return feature_data

