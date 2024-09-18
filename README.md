# Predicting the Number of Bicycle That Was Currently Rented by Customers in Metro D.C.

Note: *Update with the addition of bike-sharing.ipynb, day.csv for the dataset, and .json model using Prophet*.

Disclaimer: *This project is a capstone project as a requirement for Data Science bootcamp held by Purwadhika Digital Technology School. Datasets used may or may not changed to ensure that the notebook and the model is not a plagiarized documentation. The notebook provided in this git is also in Indonesian, please contact me if you need an English translation of the Jupyter notebook. Other than general regression model, I also enclose a time-series regression model (not pickled yet) in the notebook, please kindly check if you want to.*

This project involves building a regression model to predict the number of bikes rented per hour from the Capital Bike Share system in Washington, D.C.

The dataset includes historical data on weather conditions, seasonal factors, and other variables that influence bike rental usage.

## Table of Contents
* [Overview](#overview)
* [Dataset](#dataset)
* [Model](#model)
* [Limitations](#limitations)
* [Acknowledgements](#acknowledgements)

## Overview
Bike sharing system has been around in Metro D.C. for more than a decade. As a district supported bike sharing system, Capital Bikeshare needs accurate prediction of bike demand to help in efficient resources (mainly bikes) allocation and minimizing cost of bike damage risk. This project aims to create a regression model that can predict the number of currently rented bicycles based on various influencing factors such as time of day, weather conditions, and day of the week.

## Dataset
The dataset used in this project is provided by Capital Bikeshare, that includes hourly data on bike rentals from January 1st, 2011 to December 31st, 2012. The factors included were:
  * Date: the date of the record
  * Time: the hour of the record
  * Season: the season in which the record was observed (1: Winter, 2: Spring, 3: Summer, 4: Fall)
  * Hoiday: whether the day is a holiday or not
  * Weather: weather situation (1: Clear, 2: Mist/Cloudy, 3: Light Rain/Snow, 4: Heavy Rain/Snow - weather condition 4 is dropped from the data)
  * Temperature: the actual temperature and feeler temperature in Celcius
  * Humidity: the relative humidity
  * Count: the number of total bike currently rented during the hour, which was divided into three parts: casual, registered, and total

The dataset can be accessed from [Kaggle](https://www.kaggle.com/datasets/marklvl/bike-sharing-dataset) (I also enclosed the link in the Jupyter notebook).

## Model
~~Please kindly note that the app.py file is still not complete. I plan to update the app.py and any necessary file after this project is graded by Purwadhika Digital Technology School.
The model used in this project is eXtreme Gradient Booster, which is an ensemble method that iterate the process of decision trees using gradient descent optimization.~~
For forecasting model, please use the `serialized_model.json`.

### Feature Selection and Engineering
~~This model uses feature of 'day' (binary-encoded), 'day of the week' (one-hot encoded), 'time' (binned, ordinal-encoded, and scaled), 'season' (one-hot encoded), 'humidity', and 'feeler temperature' (normalized). The target in this model though is 'count' of bike currently rented, however due to heavily right-skewed properties of the target, the model was transformed using a logarithmic function, so until further notice **please use an exponential function to interpret the prediction value if it returns a single-digit value**!~~
The features used were `weathersit` (encoded with OneHot), `hum` (imputted with KNN), any date variables, `temp`, and `windspeed`, with the target of the forecast used was `cnt` (later renamed as `y` to be used in fbprophet).

### Evaluation Metrics and Results
This model performance is evaluated using following metrics:
* Mean Absolute Percentage Error (MAPE) as the main metrics
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

It should be noted that this model is an undefit model, with both train set and test set MAPE return numbers above 60%. For detail results and analysis, refer to the Jupyter notebook `Bike Sharing Count - V8.ipynb` (yes, this is the 8th version, with features in V1-7 were engineered with different ways using trial and error).

## Limitations
There are various limitations in this git, listed below:
* This model is heavily underfit, details please refer to the notebook enclosed;
* This model cannot extrapolate data with specification below:
    - Actual temperature below -8&deg; Celcius or above 39&deg; Celcius,
    - Feeler temperature below -16&deg; Celcius or above 50&deg; Celcius,
    - Weather situation of 4 (heavily raining or snowing),
    - and any input that defies logic;

## Acknowledgements
Thank you for Capital Bikeshare for providing the dataset, python community (especially for dataframe communities, scikit-learn community, and streamlit community) for the tools provided, and Purwadhika for the lesson which I greatly indebted for.
