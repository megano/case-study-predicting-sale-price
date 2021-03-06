from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd
import numpy as np
from datetime import datetime

class date_transformer(BaseEstimator, TransformerMixin):
    def __init__(self, format):
        self.format = format

    def transform(self, X, *_):
        def convert_to_time(x) :
            tim = np.NaN
            try :
                tim = datetime.strptime(x,self.format)
            except :
                pass
            return tim
        date_frm = pd.DataFrame(X.applymap(convert_to_time))
        date_frm.columns = X.columns
        return date_frm

    def fit(self, *_):
        return self

#year
class year_transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def transform(self, X, *_):
        year = X.applymap(lambda x : x.year)
        year.columns = [col+'_year' for col in X.columns]
        return pd.DataFrame(year)

    def fit(self, *_):
        return self

#month
class month_transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def transform(self, X, *_):
        year = X.applymap(lambda x : x.month)
        year.columns = [col+'_month' for col in X.columns]
        return pd.DataFrame(year)

    def fit(self, *_):
        return self
#quarter
class month_quarter_transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def transform(self, X, *_):
        year = pd.DataFrame(X.applymap(lambda x : (x.month-1)/3 + 1))
        year.columns = [col+'_quart' for col in X.columns]
        return year

    def fit(self, *_):
        return self

#day of month

class day_of_month_transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def transform(self, X, *_):
        year = pd.DataFrame(X.applymap(lambda x : x.day))
        year.columns = [col+'_dom' for col in X.columns]
        return year

    def fit(self, *_):
        return self

#day of week
class day_of_week_transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def transform(self, X, *_):
        year = X.applymap(lambda x : x.weekday())
        year.columns = [col+'_dow' for col in X.columns]
        return pd.DataFrame(year)

    def fit(self, *_):
        return self

#day of year
class day_of_year_transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def transform(self, X, *_):
        year = X.applymap(lambda x : int(x.date().strftime("%j")))
        year.columns = [col+'_doy' for col in X.columns]
        return pd.DataFrame(year)

    def fit(self, *_):
        return self

#hour of day
#day of year
class hour_of_day_transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def transform(self, X, *_):
        year = X.applymap(lambda x : x.hour)
        year.columns = [col+'_hod' for col in X.columns]
        return pd.DataFrame(year)

    def fit(self, *_):
        return self
