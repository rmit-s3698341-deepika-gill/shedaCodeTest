#Data Preparation
# I started by loading the CSV data from the file (using appropriate pandas functions) and checking whether the loaded data is equivalent to the data in the source CSV file.
# Then, I cleaned the data in order to produce appropriate visualisations. I dealt with the potential issues/errors in the data (such as: typos, extra whitespaces, sanity checks for impossible values, and missing values etc). "

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix

data_set = pd.read_csv("Automobile.csv", delimiter='#', names=['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price'])


# Finds the columns with missing data
missingData = data_set.columns[data_set.isnull().any()]

# Code to fill in the missing data
data_set['normalized-losses'] = data_set['normalized-losses'].fillna(round(data_set['normalized-losses'].mean()), inplace=False)
data_set['bore'] = data_set['bore'].fillna(round(data_set['bore'].mean(),2), inplace=False)
data_set['stroke'] = data_set['stroke'].fillna(round(data_set['stroke'].mean(),2), inplace=False)
data_set['horsepower'] = data_set['horsepower'].fillna(round(data_set['horsepower'].mean()), inplace=False)
data_set['peak-rpm'] = data_set['peak-rpm'].fillna(round(data_set['peak-rpm'].mean()), inplace=False)
data_set['price'] = data_set['price'].fillna(round(data_set['price'].mean()), inplace=False)

data_set = data_set.apply(lambda d:d.fillna(d.value_counts().index[0]) if d.dtype == "object" else d)


data_set.to_csv('auto_test.csv', mode='w', index=False)

# Removing the white spaces from data
data_set = data_set.apply(lambda s: s.str.strip() if s.dtype == "object" else s)

# Sanity check for impossible values
data_set['symboling'] = data_set['symboling'].mask(data_set['symboling'] < -3, np.NAN)
data_set['symboling'] = data_set['symboling'].mask(data_set['symboling'] > 3, np.NAN)

data_set['normalized-losses'] = data_set['normalized-losses'].mask(data_set['normalized-losses'] < 65, np.NAN)
data_set['normalized-losses'] = data_set['normalized-losses'].mask(data_set['normalized-losses'] > 256, np.NAN)

data_set['wheel-base'] = data_set['wheel-base'].mask(data_set['wheel-base'] < 86.6, np.NAN)
data_set['wheel-base'] = data_set['wheel-base'].mask(data_set['wheel-base'] >  208.1, np.NAN)

data_set['length'] = data_set['length'].mask(data_set['length'] < 141.1, np.NAN)
data_set['length'] = data_set['length'].mask(data_set['length'] > 208.1, np.NAN)

data_set['width'] = data_set['width'].mask(data_set['width'] < 60.3, np.NAN)
data_set['width'] = data_set['width'].mask(data_set['width'] > 72.3, np.NAN)

data_set['height'] = data_set['height'].mask(data_set['height'] < 47.8, np.NAN)
data_set['height'] = data_set['height'].mask(data_set['height'] > 59.8, np.NAN)

data_set['curb-weight'] = data_set['curb-weight'].mask(data_set['curb-weight'] < 1488, np.NAN)
data_set['curb-weight'] = data_set['curb-weight'].mask(data_set['curb-weight'] > 4066, np.NAN)

data_set['engine-size'] = data_set['engine-size'].mask(data_set['engine-size'] < 61, np.NAN)
data_set['engine-size'] = data_set['engine-size'].mask(data_set['engine-size'] > 326, np.NAN)

data_set['bore'] = data_set['bore'].mask(data_set['bore'] < 2.54, np.NAN)
data_set['bore'] = data_set['bore'].mask(data_set['bore'] > 3.94, np.NAN)

data_set['stroke'] = data_set['stroke'].mask(data_set['stroke'] < 2.07, np.NAN)
data_set['stroke'] = data_set['stroke'].mask(data_set['stroke'] > 4.17, np.NAN)

data_set['compression-ratio'] = data_set['compression-ratio'].mask(data_set['compression-ratio'] < 7, np.NAN)
data_set['compression-ratio'] = data_set['compression-ratio'].mask(data_set['compression-ratio'] > 23, np.NAN)

data_set['horsepower'] = data_set['horsepower'].mask(data_set['horsepower'] < 48, np.NAN)
data_set['horsepower'] = data_set['horsepower'].mask(data_set['horsepower'] > 288, np.NAN)

data_set['peak-rpm'] = data_set['peak-rpm'].mask(data_set['peak-rpm'] < 4150, np.NAN)
data_set['peak-rpm'] = data_set['peak-rpm'].mask(data_set['peak-rpm'] > 6600, np.NAN)

data_set['city-mpg'] = data_set['city-mpg'].mask(data_set['city-mpg'] < 13, np.NAN)
data_set['city-mpg'] = data_set['city-mpg'].mask(data_set['city-mpg'] > 49, np.NAN)

data_set['highway-mpg'] = data_set['highway-mpg'].mask(data_set['highway-mpg'] < 16, np.NAN)
data_set['highway-mpg'] = data_set['highway-mpg'].mask(data_set['highway-mpg'] > 54, np.NAN)

data_set['price'] = data_set['price'].mask(data_set['price'] < 5118, np.NAN)
data_set['price'] = data_set['price'].mask(data_set['price'] > 45400, np.NAN)

# Code to correct the typos in the data
data_set["num-of-doors"] = data_set["num-of-doors"].replace(['fourR', 'Four'], 'four')

data_set["make"] = data_set["make"].replace(['Peugot'], 'peugot')
data_set["make"] = data_set["make"].replace(['vol00112ov'], 'volvo')
data_set["make"] = data_set["make"].replace(['Nissan'], 'nissan')

data_set["fuel-type"] = data_set["fuel-type"].replace(['Gas'], 'gas')
data_set["fuel-type"] = data_set["fuel-type"].replace(['Diesel'], 'diesel')

data_set["aspiration"] = data_set["aspiration"].replace(['Std'], 'std')
data_set["aspiration"] = data_set["aspiration"].replace(['turrrrbo'], 'turbo')

data_set["body-style"] = data_set["body-style"].replace(['Sedan'], 'sedan')
data_set["body-style"] = data_set["body-style"].replace(['Wagon'], 'wagon')

data_set["drive-wheels"] = data_set["drive-wheels"].replace(['Fwd'], 'fwd')

data_set["engine-location"] = data_set["engine-location"].replace(['Front','FRONT'], 'front')
data_set["engine-location"] = data_set["engine-location"].replace(['Rear','REAR'], 'rear')

data_set["num-of-cylinders"] = data_set["num-of-cylinders"].replace(['Four'], 'four')

data_set["fuel-system"] = data_set["fuel-system"].replace(['Mpfi'], 'mpfi')

# stacked-bar-min-max-body-style-curb-weight

color = ['red', 'blue']
agg_data = data_set.groupby('body-style')['curb-weight'].agg({'Lowest Value':'min','Highest Value':'max'}).plot(kind='bar', stacked=True, colors=color)
agg_data.set_xlabel("Body Styles")
agg_data.set_ylabel("Curb weights")
agg_data.set_title("Min, max curb weight for body style")
agg_data.legend(loc="upper right")
plt.show()

# bar-fuel-system-highway-mpg

barplot = data_set.groupby('fuel-system')['highway-mpg'].mean().plot(kind='bar')
barplot.set_xlabel("Fuel Systems")
barplot.set_ylabel("Highway miles per gallon")
barplot.set_title("Average Highway miles per gallon for each fuel system type")
plt.show()