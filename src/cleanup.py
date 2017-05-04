import pandas as pd
import numpy as np
from zipfile import ZipFile
from Helper import pandas_column_utilities as pcu
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from Helper import FeatureTransformer as ft, pandas_broadcast_functions as pbf

# Check into Normalizer. Seems to be setting all values to 0 and 1 instead of scaling. 

class DataClass :

    def __init__(self, path) :
        self.path = path

    #getdata
    #feature engineering
        # cleanup
        # date, ordinal, categorical
        # scaling
        # imputing
    # select features

    def load_csv_to_df(self):
        print "loading csv"
        df = pd.read_csv(self.path)
        return df

    def feature_engineer(self, df, continuous_columns, ordinal_columns, date_columns, categorical) :
        print "feature engineering"
        '''
        Steps :
            1. continuous_columns :
                    - impute,
                    - normalize
            2. ordinal_columns :
                    - get a map of the ordinal values to their numbers and cpply the map
                    e,g. {'L':1, 'M':2,'L':3, 'XL':4}
                    - impute
            4. date_columns
                    - convert the date columns from string to dates
                    - split them in to multiple columns for day, day of year, month, quarter, year etc.,
                    - impute
            5. categorical
                    - impute
                    - one hot encoding
            6. remove columns which are fully zero or have the same value throughout.
        '''
        # #Begin : Creating continuous pipeline
        cont_impute = ft.imputing_transformer(Imputer(strategy='most_frequent'), empty_values = [float('nan'), np.NaN, None, "None or Unspecified"])
        cont_normalize = Normalizer()
        cont_pipeline = Pipeline([('impute',cont_impute),('normalize',cont_normalize)])
        cont_pipeline.fit(df[continuous_columns])
        import pdb; pdb.set_trace()
        print cont_pipeline.transform(df[continuous_columns])
        # #END : Creating continuous pipeline


        #Begin : Creating categorical pipeline
        # create encoder object
        # import pdb; pdb.set_trace()
        categ_encode = ft.HotEncoder()
        categ_impute = Imputer(strategy='most_frequent')
        categ_pipeline = Pipeline([('encode',categ_encode),('impute',categ_impute)])
        # for debugging
        # categ_encode = categ_encode.fit(df[categorical])
        # print categ_encode.transform(df[categorical])
        #END : Creating categorical pipeline
        return df

    def select_features(self, df):
        print "select features"
        return df

    def get_data(self, df, continuous_columns, ordinal_columns, date_columns, categorical) :
        # df = self.load_csv_to_df()
        df = self.feature_engineer(df, continuous_columns, ordinal_columns, date_columns, categorical)
        df = self.select_features(df)
        return df

continuous_columns = ['Undercarriage_Pad_Width']

categorical_columns = ['Steering_Controls', 'Differential_Type', 'Blade_Type', \
'Travel_Controls', 'Grouser_Type', 'Coupler', 'Tip_Control', 'Ripper', \
'Hydraulics', 'Engine_Horsepower', 'Transmission', 'Pad_Type', 'Stick', \
'ModelID' , 'datasource',  'fiModelDesc' ,'fiBaseModel', 'fiSecondaryDesc', \
'fiModelSeries', 'fiModelDescriptor' , 'state', 'ProductGroup', \
'ProductGroupDesc', 'Drive_System',  'Enclosure' ]

# add categorical column back in after testing: 'Pad_Type'

#
# zf = ZipFile('data/Train.zip')
#
# df = pd.read_csv('data/Train.csv')
#
# year = df['YearMade']
# year = year[year != 1000]
#
# price_v_year = df[['SalePrice', 'YearMade']]
#
data_class = DataClass('../data/Train.csv')
df = data_class.load_csv_to_df()
#
#EDA
# pcu.info(df)
# Cleaning up inches data to numbers
df['Undercarriage_Pad_Width'] = df['Undercarriage_Pad_Width'].apply(lambda x  :
pbf.feet_inches_to_feet( x, feet_symb = "'", inches_symb = 'inch'))

print df['Undercarriage_Pad_Width'].unique()
df = data_class.get_data(df, continuous_columns, [], [], categorical_columns)
