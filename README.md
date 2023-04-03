# Project (Group 14)

Before running, ensure that you have the requirements installed:

```python
pip install -r requirements.txt
```

## `predict.py`

To create a prediction for the current day, just run predict.py:

```
$ python3 predict.py

2023-04-02
----------
Temperature: 0.47°C to 9.93°C
Humidity: 44.39% to 88.98%
Wind Speed: 6.27 km/h to 33.14 km/h
Visibility: 15.65 km to 23.62 km
Atmospheric Pressure: 98.82 kPa to 99.81 kPa
```

To create a prediction for a certain day, append it to the command (in ``YYYY-MM-DD`` format):

```
$ python3 predict.py 2023-06-01

2023-06-01
----------
Temperature: 13.70°C to 25.21°C
Humidity: 43.92% to 86.62%
Wind Speed: 5.29 km/h to 29.81 km/h
Visibility: 19.29 km to 23.97 km
Atmospheric Pressure: 98.97 kPa to 99.48 kPa
```

To create a seven day forecast, use the ``--seven-day`` switch:

```
$ predict.py --seven-day 2023-06-01

2023-06-01
----------
Temperature: 13.70°C to 25.21°C
Humidity: 43.92% to 86.62%
Wind Speed: 5.29 km/h to 29.81 km/h
Visibility: 19.29 km to 23.97 km
Atmospheric Pressure: 98.97 kPa to 99.48 kPa

2023-06-02
----------
Temperature: 13.54°C to 25.15°C
Humidity: 43.04% to 86.22%
Wind Speed: 5.26 km/h to 30.32 km/h
Visibility: 19.80 km to 25.03 km
Atmospheric Pressure: 98.97 kPa to 99.51 kPa

2023-06-03
----------
Temperature: 13.53°C to 25.07°C
Humidity: 43.52% to 85.82%
Wind Speed: 4.87 km/h to 29.18 km/h
Visibility: 20.36 km to 24.17 km
Atmospheric Pressure: 99.05 kPa to 99.57 kPa

2023-06-04
----------
Temperature: 13.97°C to 25.45°C
Humidity: 42.89% to 86.44%
Wind Speed: 5.14 km/h to 29.05 km/h
Visibility: 19.81 km to 24.23 km
Atmospheric Pressure: 98.98 kPa to 99.51 kPa

2023-06-05
----------
Temperature: 14.17°C to 25.64°C
Humidity: 43.28% to 87.00%
Wind Speed: 4.94 km/h to 29.28 km/h
Visibility: 18.99 km to 24.37 km
Atmospheric Pressure: 98.95 kPa to 99.48 kPa

2023-06-06
----------
Temperature: 14.51°C to 25.69°C
Humidity: 44.08% to 87.53%
Wind Speed: 4.70 km/h to 28.99 km/h
Visibility: 18.97 km to 24.49 km
Atmospheric Pressure: 98.91 kPa to 99.41 kPa

2023-06-07
----------
Temperature: 14.63°C to 25.87°C
Humidity: 42.39% to 87.00%
Wind Speed: 5.33 km/h to 29.77 km/h
Visibility: 19.53 km to 24.55 km
Atmospheric Pressure: 98.86 kPa to 99.41 kPa
```
