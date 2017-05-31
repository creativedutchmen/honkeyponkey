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

    def get_lag_data(self):
        start_date = self.data.index.min().date()
        end_date = self.data.index.max().date()

        date_offset = self.get_date_offset()
        start = (
            start_date +
            max(self.lags) * pd.DateOffset(minutes=15) +
            pd.DateOffset(hours=10)
        ).date() + pd.DateOffset(hours=10)

        days = (
            pd.date_range(
                start=start + pd.DateOffset(days=1) - date_offset,
                end=end_date - date_offset
            )
            .tz_localize('Europe/Amsterdam')
            # .tz_convert(pytz.timezone('Europe/Amsterdam'))
        )

        daylocs = np.array(
            self.data.index.get_indexer_for(self.data.loc[days].index)
        )
        locs = np.add(
            daylocs.reshape(1, -1),
            -np.tile(np.array(self.lags), (len(daylocs), 1)).T
        )

        res_data = (
            self.data
            .iloc[
                locs.flatten()
            ]
            .sort_index()
            .values
        )
        # Numpy. Why you no allow chaining?
        res_data = (
            np.array(
                np.vsplit(
                    res_data,
                    len(res_data) / len(self.lags)
                )
            )
            .T
            .reshape(len(self.lags) * len(self.columns), -1)
        )

        row_names = self.get_row_names(locs)

        return pd.DataFrame(
            res_data,
            columns=(days + date_offset).date,
            index=row_names
        )

    def get_row_names(self, locs):
        names = []
        for column in self.columns:
            for lag in reversed(self.lags):
                names += ["%s.%s.lag_%s" % (self.name, column, lag)]
        return names

    def get_date_offset(self):
        return pd.DateOffset(days=0)


class RealisedData(Data):
    def get_date_offset(self):
        return pd.DateOffset(days=1)


class PredictedData(Data):
    pass


class TargetData(Data):
    lags = [x for x in range(0, 24*4)]


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
        res = res.append(dataset.get_lag_data())
    return res