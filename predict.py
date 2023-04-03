import os
import pandas as pd
import json
import pickle
import warnings
import argparse
import plotly
from prophet import Prophet
from prophet.serialize import model_to_json, model_from_json

# Suppress unnecessary warnings from Prophet code (appears to be a Prophet bug)
warnings.filterwarnings('ignore')

columns = [
    'Min Temp',
    'Max Temp',
    'Total Precipitation',
    #'Max Gust',
    'Min Humidity',
    'Max Humidity',
    'Min Wind Speed',
    'Max Wind Speed',
    'Min Visibility',
    'Max Visibility',
    'Min Pressure',
    'Max Pressure',
]

def get_df_value(df, date, column):
    series = df[df['ds'] == date][column]
    return series.head(1).item()

def predict(dates):
    data = {}
    
    for column in columns:
        # Sanitize the column name to create a model name
        model_name = column.replace(' ', '_').lower()
        
        with open(os.path.join('Models', model_name + '.json'), 'r') as f:
            prophet = model_from_json(f.read())
        
        future_df = pd.DataFrame(dates, columns=[ 'ds' ])
        
        data[column] = prophet.predict(future_df)
    
    predict_rows = []
    
    # Combine the data into a single DataFrame
    for date in dates:
        predict_row = [ date, int(date[5:7]), int(date[8:10]) ]
        
        for column in columns:
            predict_row.append(get_df_value(data[column], date, 'yhat'))
        
        predict_rows.append(predict_row)
    
    predict_columns = [ 'ds', 'Month', 'Day' ]
    predict_columns.extend(columns)
    
    return pd.DataFrame(predict_rows, columns=predict_columns)

# Create a parser to parse the command line arguments
parser = argparse.ArgumentParser(description='Forecasts the weather using machine learning models.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--seven-day', action='store_true', help='create a 7 day forecast', default=False)
parser.add_argument('date', help='the date to start the forecast from (YYYY-MM-DD)', nargs='?', default='now')

# Get the command line arguments
args = parser.parse_args()
config = vars(args)

base_date = config['date']
seven_day = config['seven_day']

dates = []

# If the base date is 'now', then use the current date
if base_date == 'now':
    dates.append(pd.Timestamp.now())
else:
    dates.append(pd.Timestamp(base_date))

# If the seven_day flag is set, then add the next 6 days
if seven_day:
    for i in range(1, 7):
        dates.append(pd.Timestamp(base_date) + pd.Timedelta(days=i))

# Convert the Timestamps to strings that Prophet can use
str_dates = [ date.strftime('%Y-%m-%d') for date in dates ]

# Get the forecast
predict_df = predict(str_dates)

# Load the condition model
with open(os.path.join('Models', 'condition.pkl'), 'rb') as f:
    classifier = pickle.load(f)

# Predict the condition for each day
conditions = classifier.predict(predict_df.drop('ds', axis=1))
print(len(conditions))

for i in range(0, len(str_dates)):
    str_date = str_dates[i]

    print(str_date)
    print("----------")
    
    print("Temperature: {:.2f}°C to {:.2f}°C".format(get_df_value(predict_df, str_date, 'Min Temp'), get_df_value(predict_df, str_date, 'Max Temp')))
    print("Humidity: {:.2f}% to {:.2f}%".format(get_df_value(predict_df, str_date, 'Min Humidity'), get_df_value(predict_df, str_date, 'Max Humidity')))
    print("Wind Speed: {:.2f} km/h to {:.2f} km/h".format(get_df_value(predict_df, str_date, 'Min Wind Speed'), get_df_value(predict_df, str_date, 'Max Wind Speed')))
    print("Visibility: {:.2f} km to {:.2f} km".format(get_df_value(predict_df, str_date, 'Min Visibility'), get_df_value(predict_df, str_date, 'Max Visibility')))
    print("Atmospheric Pressure: {:.2f} kPa to {:.2f} kPa".format(get_df_value(predict_df, str_date, 'Min Pressure'), get_df_value(predict_df, str_date, 'Max Pressure')))
    print("Precipitation: {}".format('yes' if conditions[i] else 'no'))
    
    print()
