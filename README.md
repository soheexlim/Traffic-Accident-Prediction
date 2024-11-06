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

# Midterm Report and Presentation

## 1. Preliminary visualizations of data
  - To visualize and get a better grasp on the relationships between the features in our data, we firstly created many bar charts for comparison. We looked at accidents occuring on Weekends vs. Weekdays, Day vs. Night, Holidays vs. Non-Holidays, weather condition occurence counts, Rush Hour vs. Non-Rush Hour, Speed limit range occurence counts, Speed Limit and Weather conditions occurence counts, Ambient Light condition counts, type of Road Surface counts, type of Road Junction counts, type of Traffic Control device counts, Weather/Rush Hour interaction, and Weather/Night interaction.
  - Secondly, we created a Correlation Heatmap showing the correlations between the Numeric Features. Some of the coorelations were obvious: CRASH_HOUR and IS_NIGHT had a high negative inverse relationship, due to a confounding factor (CRASH_HOUR would be low due to it being night). Another obvious relationship that gives us no information would be the high relationship between IS_WEEKEND and DAY_OF_WEEK (When it is the weekend, day of week would be 0, and vice versa). The most interesting and telling coorelation we found was the moderate relationship (.23) between CRASH_HOUR and IS_RUSH_HOUR. This shows us that during rush hour, when more are on the road, there are more likely to be crashes. This is very intuitive, but it is still important to be able to show this in our data.
<img width="657" alt="Screenshot 2024-11-05 at 11 35 07 PM" src="https://github.com/user-attachments/assets/77bf5bb1-cd8c-4fba-9e41-6adc1ce5ec45"><img width="673" alt="Screenshot 2024-11-05 at 11 36 25 PM" src="https://github.com/user-attachments/assets/b84df3a1-da77-45a1-a130-642cca0cc9e8">
<img width="1336" alt="Screenshot 2024-11-05 at 11 36 50 PM" src="https://github.com/user-attachments/assets/70507ae4-2b5e-4b24-b651-a55ce0dddab1">
<img width="1330" alt="Screenshot 2024-11-05 at 11 37 15 PM" src="https://github.com/user-attachments/assets/3ee90fb2-f903-4723-b1b1-a0020ce7c48a">
<img width="599" alt="Screenshot 2024-11-05 at 11 37 57 PM" src="https://github.com/user-attachments/assets/32c6111b-2959-439a-8824-77af4a58a239">
<img width="1393" alt="Screenshot 2024-11-05 at 11 39 27 PM" src="https://github.com/user-attachments/assets/6b148ea5-7b51-4089-b353-76524613e535">
<img width="1392" alt="Screenshot 2024-11-05 at 11 39 40 PM" src="https://github.com/user-attachments/assets/3f98db15-184b-4fb2-99ae-9e24d2397093">
<img width="664" alt="Screenshot 2024-11-05 at 11 39 52 PM" src="https://github.com/user-attachments/assets/14d1d4e2-3ae0-4a76-b92f-6a62d4926e0a">




## 2. Data Processing
 - Feature Reduction: Our dataset initially had 123 Columns. After filtering out unnecessary columns, we were left with 16. Columns were deemed unnecessary if they were >50% missing values, had no correlation to our prediction, or were too vague/unique (like street names)
 - Location Filtering: We are only focused on the Greater Boston Area in our objective, so we excluded accidents form cities outside this zone. We used ChatGPT to generate a list of the greater boston cities based on the cities that appeared in our dataset. Using this list, we filtered out any observation that occured outside these zones.
 - Date and Time-Based Feature Engineering: To prepare for further analysis, we added a method that adds holiday and time-based information. This included creating a new feature that combined CRASH_DATE_TEXT and CRASH_TIME_2, which we later dropped. This new feature, CRASH_DATETIME, was created to be in the same format as the holidays we imported from a holidays database. We also added dummy variables for DAY_OF_WEEK, IS_WEEKEND, and IS_NIGHT to further help us interpret the data.
 - Finally, uur dataset initially only contains the occurrences of crashes. In order to test the predictive power of our model, we generated synthetic, non-accident data by simulating realistic conditions where accidents are less likely to occur.

## 3. Data Modeling
- The first thing we did in our model was balance the dataset with our geneated non-crash occurrences. Balancing the dataset helps avoid a model that always predicts the more common class (accidents), leading to more accurate predictions for both accidents and non-accidents. We combined this synthetic data with real accident data, then upsampled non-accidents to match the number of accidents to create a balanced dataset. We also used LabelEncoder to convert categorical variables, such as SPEED_LIMIT_RANGE and WEATHER_SIMPLIFIED, into numeric values. I combined training and test sets for each variable to ensure consistent encoding across both sets.
- For our predictive model, we used Random Forest. We used GridSearchCV to optimize the Random Forest hyperparameters, such as the number of trees and tree depth, to find the best configuration for accurate predictions. The optimized hyperparameters allowed the Random Forest model to make more precise predictions and reduce overfitting, leading to a more generalized model that could perform well on unseen data. After identifying the best Random Forest model, we applied isotonic calibration to improve the reliability of its probability predictions, making sure they reflect the true likelihood of an accident. 

## 4. Preliminary results
- Finally, we evaluated the calibrated model’s performance by checking its accuracy and F1 score, integrated its calibrated probabilities with those from other models, and saved high-probability predictions to a submission file for further analysis.
- We averaged the probability predictions from the calibrated models to produce a final probability estimate for each record. A threshold of 0.5 was applied to classify each record as either an accident (1) or non-accident (0), adjusting the sensitivity and specificity of the model as needed.
- Our models achieved accuracy of accuracy of 88.73%, indicating strong results given that this was a balanced dataset. Our F1 score  is 0.8859, which shows a good balance between precision and recall. This performance suggests that our models are well-calibrated and effective for predicting accident occurrences under the simulated conditions

Youtube Link: https://youtu.be/xDtrSEpDA7s
