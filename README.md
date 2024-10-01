# Final Project: Predicting Traffic Accidents Based on Weather and Time Data in Greater Boston Area

## 1. Description of the Project
The project will focus on predicting the likelihood of traffic accidents occurring at specific times and locations based on external factors such as weather conditions (rain, snow, visibility, temperature) and time-related factors (rush hour, night/day, holidays) in Greater Boston Metroplitan area. The goal is to use historical accident data in combination with weather and time data to build a predictive model that can estimate the probability of accidents occurring at certain locations and times under different weather conditions.

This project could be useful for transportation agencies or navigation services that want to provide real-time warnings or advisories based on predicted accident likelihood.

## 2. Clear Goals
- Primary Goal: Build a model that predicts the likelihood of traffic accidents at given times and locations based on weather and time data.
  * Example: “There is a 70% chance of an accident occurring at 5 pm on a rainy weekday at this location.”
- Secondary Goal: Analyze which factors (weather conditions, time of day, holidays, etc.) have the most influence on accident occurrence.
  * Example: We may find that rain combined with rush hour significantly increases accident risk.

## 3. Data Collection

1. Traffic Accident Data:
  - Data Source: Many cities and countries have public traffic accident data, such as Open Data Portals (e.g., New York City, Chicago, etc.) or government transportation websites.
  - Features to Collect:
    1. Location (latitude, longitude)
    2. Time and date of the accident
    3. Severity of the accident (minor, major, fatal, etc.)
    4. Other factors like road conditions, type of vehicles involved (if available).

2. Weather Data:
  - Data Source: You can use the OpenWeatherMap API or other weather services to collect real-time or historical weather data.
  - Features to Collect:
    1. Temperature
    2. Precipitation (rain, snow)
    3. Humidity
    4. Wind speed
    5. Visibility
    6. Weather conditions (e.g., fog, thunderstorms)
  
3. Time-Based Data:
   - Rush Hour: Based on predefined times (e.g., 7-9 AM, 4-6 PM on weekdays).
   - Day/Night: You can compute this based on the time of day.
   - Holiday Information: Include holidays in your model by collecting public holiday data for the Greater Boston or New England.

## 4. Modeling the Data
1. Logistic Regression
This model would a good starting point for binary classification problems where you want to predict the probability of an event (e.g., accident happening or not). It will model the relationship between the dependent variable (accident occurrence) and independent variables (weather, time) as a probability.
2. Decision Trees/Random Forests:
Decision trees are great for understanding which features (weather, time of day) are most important for accident prediction. Random forests, in particular, can capture complex, non-linear relationships between the features. Random forests are an ensemble method that builds multiple decision trees and averages the results, reducing overfitting and improving accuracy.
3. Gradient Boosting (e.g., XGBoost):
We could use XGBoost, which is a powerful boosting algorithm for handling non-linear relationships and interactions between variables. It will iteratively builds models and corrects the errors made by previous models, improving accuracy.

## 5. Visualization Plan
1. Heatmaps:
  - Show areas with high accident probabilities based on weather and time factors.
    - Example: A heatmap of a city showing regions with the highest accident risks under different weather conditions.
    
 2. Bar Charts:
  - Show how accident risk varies based on different weather conditions (e.g., accident likelihood in rain vs. snow vs. clear weather).
    - Example: Compare accident probabilities between weekdays and weekends, or rush hour vs. non-rush hour.

3. Time Series Plots:
  - Visualize accident occurrences over time, segmented by weather conditions (e.g., spikes in accidents during heavy rain or snowstorms).
    
4. Scatter Plots:
  - Show the relationship between different weather variables (e.g., temperature, wind speed) and accident occurrence.

## 6. Test Plan
- Train/Test Split: Withhold 20% of your data as a test set, and use the remaining 80% for training.
- Time-Based Validation: Train the model on accident and weather data from one year (2022) and test it on data from the following year (2023). If the selected times (years) are not available, we will use the two most recent years of data available.
- Cross-Validation: You could also use k-fold cross-validation to ensure the model is robust and generalizes well across multiple subsets of the data.

