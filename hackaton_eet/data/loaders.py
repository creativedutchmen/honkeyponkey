import pandas as pd
from hackaton_eet import settings
from hackaton_eet.conf import init_cls_from_settings
import numpy as np
import os
import pytz


class Data(object):

    name = None
    file_location = None
    date_col = 'datetime'
    columns = []
    lags = [x for x in range(1, 4)]  # Default lags: past hour
    data = None

    def __init__(self, lags=None, **kwargs):
        if lags:
            self.lags = [x for x in np.abs(lags)]
        for name, value in kwargs.items():
            try:
                getattr(self, name)
                setattr(self, name, value)
            except:
                pass
        self.load()

    def load(self, **kwargs):
        data = pd.read_csv(
            os.path.join(settings.DATA_PATH, self.file_location),
            index_col=self.date_col,
            parse_dates=True,
            usecols=[self.date_col] + self.columns,
            **kwargs
        )
        self.data = data.set_index(
            data.index
            .tz_localize('UTC')
            .tz_convert(pytz.timezone('Europe/Amsterdam'))
        ).resample('15min').ffill()

    def get_ptu_lag_data(self):
        # Lags are in days here. Makes working with AR models easier
        start_date = self.data.index.min()
        end_date = self.data.index.max().date()

        date_offset = pd.DateOffset(days=self.get_offset())

        start = (
            start_date +
            pd.DateOffset(days=int(max(self.lags))) +
            date_offset
        ).date()

        end = (
            end_date -
            date_offset
        )

        ptus = pd.date_range(
            start=start,
            end=end,
            freq='15min'
        ).tz_localize('UTC').tz_convert(
            pytz.timezone('Europe/Amsterdam')
        )

        ptulocs = np.array(
            self.data.index.get_indexer_for(self.data.loc[ptus].index)
        )

        locs = np.add(
            ptulocs.reshape(1, -1),
            -np.tile(96 * np.array(self.lags), (len(ptulocs), 1)).T
        )

        res_data = (
            self.data
            .iloc[
                locs.flatten()
            ]
            .values
            .reshape(-1, len(self.columns)).T
            .reshape(len(self.columns) * len(self.lags), -1)
        )

        return pd.DataFrame(
            res_data,
            index=self.get_row_names(),
            columns=self.data.iloc[
                ptulocs
            ].index
        )

    def get_row_names(self):
        names = []
        for column in self.columns:
            for lag in self.lags:
                names += ["%s.%s.lag_%s" % (self.name, column, lag)]
        return names

    def get_offset(self):
        return 0


class RealisedData(Data):
    def get_offset(self):
        return 1


class PredictedData(Data):
    pass


class TargetData(Data):
    lags = [1, ]

    def get_row_names(self):
        names = []
        for column in self.columns:
            names += ["%s" % (column)]
        return names


def get_data_dict(datasets):
    dataloaders = init_cls_from_settings(settings.DATA)
    res = {}
    for dataset, dataloader in dataloaders.items():
        if dataset in datasets:
            (defaults, dataloader_class) = dataloader
            config = defaults.copy()
            config.update(datasets[dataset])
            res[dataset] = dataloader_class(name=dataset, **config)
    return res


def get_data(datasets):
    sets = get_data_dict(datasets)
    res = pd.DataFrame()
    for dataset in sets.values():
        res = res.append(dataset.get_ptu_lag_data())
    return res