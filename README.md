# Final Project: Predicting Traffic Accidents Based on Weather and Time Data in Greater Boston Area

## 1. Description of the Project
This project aims to predict the likelihood of traffic accidents occurring at specific times and locations in the Greater Boston Metropolitan Area. By integrating historical accident data with weather and time data, the model is designed to provide actionable insights about accident probability under various conditions, such as rainy rush hours or nighttime during snowy weather.

The project is intended to support transportation agencies, navigation services, and urban planners in developing real-time advisory systems and risk-mitigation strategies. The model focuses on analyzing the interplay between weather, time-based factors, and traffic accident occurrences.

## 2. Goals
### Primary Goal
- Develop a predictive model to estimate the likelihood of a traffic accident occurring at a given location, time, and under specific weather conditions.
  * Example: “There is a 70% chance of an accident at 5 PM on a rainy weekday at this location.”

### Secondary Goal
- Analyze feature importance to identify the most significant predictors of traffic accidents.
  * Example: Discovering that rush hour during rain increases the likelihood of accidents by 50% compared to non-rush hour periods.

## 3. Data Collection and Sources
### 1. Traffic Accident Data
- **Source**: [Massachusetts Crash Portal](https://massdot-impact-crashes-vhb.opendata.arcgis.com/)
- **Details**:
  - Data from 2022 and 2023, including information on accident location, time, and conditions.
  - Features collected:
    - `CITY_TOWN_NAME`: City where the crash occurred
    - `CRASH_DATE_TEXT` and `CRASH_TIME_2`: Date and time of the crash
    - `ROAD_SURF_COND_DESCR`: Road surface conditions (e.g., dry, wet, snowy)
    - `WEATH_COND_DESCR`: Weather at the time of the crash (e.g., clear, rain, snow)

### 2. Weather Data
- **Source**: Historical weather services (e.g., OpenWeatherMap API).
- **Features Collected**:
  - Temperature
  - Precipitation (e.g., rain, snow)
  - Visibility
  - Weather conditions (e.g., fog, thunderstorms)

### 3. Time-Based Data
- **Derived Features**:
  - `IS_RUSH_HOUR`: Whether the crash occurred during rush hours (6–10 AM and 3–7 PM).
  - `IS_NIGHT`: Nighttime crashes (8 PM–6 AM).
  - `IS_WEEKEND`: Weekend crashes (Saturday and Sunday).
  - `IS_HOLIDAY`: Crashes on U.S. public holidays.

## 4. Data Processing
### Merging and Cleaning Data
- Accident data from 2022 and 2023 was **merged into a single dataset** for training and testing.
- Removed columns with >50% missing values or irrelevant information, such as unique IDs, street names, and overly specific geographic details.
- Filtered the dataset to include only crashes within the **Greater Boston Metropolitan Area** using a predefined list of cities.

### Feature Engineering
- **Datetime Features**:
  - Combined `CRASH_DATE_TEXT` and `CRASH_TIME_2` into a new `CRASH_DATETIME` feature for consistency.
  - Extracted:
    - `DAY_OF_WEEK` (e.g., Monday = 0, Sunday = 6)
    - `IS_WEEKEND` (1 for Saturday/Sunday, 0 otherwise)
    - `IS_NIGHT` (1 for crashes occurring between 8 PM–6 AM, 0 otherwise)
  - Used the Python `holidays` library to create an `IS_HOLIDAY` feature.

- **Weather Simplification**:
  - Simplified weather conditions (e.g., grouping all rainy conditions into "Rain").
  - Encoded simplified weather categories numerically for use in models.

- **Interaction Terms**:
  - Created features to capture combined effects of weather and time:
    - `WEATHER_RUSH_HOUR`: Weather conditions during rush hours.
    - `WEATHER_NIGHT`: Weather conditions at night.
    - `WEATHER_WEEKEND`: Weather conditions on weekends.

- **Speed Limits**:
  - Grouped speed limits into categories (`<30 mph`, `30–50 mph`, `>50 mph`) and encoded them numerically.

### Synthetic Data Generation
- To balance the dataset (as crashes were overrepresented), synthetic non-accident data was generated using:
  - Weighted distributions for weather, time of day, road conditions, and speed limits based on observed crash patterns.
- The synthetic data was merged with the real crash data to create a balanced dataset for training.

## 5. Data Modeling
### Train-Test Split
- The combined dataset was shuffled and split into **80% training data** and **20% test data**.

### Models Used
1. **Logistic Regression**: A baseline model for binary classification.
2. **Random Forest**: Optimized using Bayesian search for hyperparameters like the number of trees and maximum depth.
3. **Gradient Boosting (XGBoost)**: Captures complex relationships between variables.
4. **Neural Network**: Designed with layers to predict accident occurrence using weather and time features.
5. **Stacking Classifier**: Combined predictions from Random Forest, XGBoost, and Gradient Boosting to improve accuracy.

### Model Calibration
- Applied **isotonic** and **sigmoid calibration** to Random Forest and Gradient Boosting models for better probability estimates.

## 6. Preliminary Visualizations
### Key Visual Insights
1. **Accidents by Weekend vs. Weekday**:
   - More accidents occur on weekdays than weekends, likely due to higher traffic volumes.

2. **Accidents During Day vs. Night**:
   - Nighttime accidents are less frequent but often more severe.

3. **Accidents by Weather Condition**:
   - Rain and snow significantly increase accident likelihood compared to clear weather.

4. **Heatmap of Correlations**:
   - Features like `IS_RUSH_HOUR` and `IS_WEEKEND` showed moderate correlations with crash frequency.

### Sample Visualizations
#### Bar Chart: Accidents by Rush Hour
![Accidents by Rush Hour](https://github.com/user-attachments/assets/70507ae4-2b5e-4b24-b651-a55ce0dddab1)

#### Heatmap: Correlation of Numeric Features
![Correlation Heatmap](https://github.com/user-attachments/assets/6b148ea5-7b51-4089-b353-76524613e535)

#### Interaction Term: Weather and Rush Hour
![Weather and Rush Hour](https://github.com/user-attachments/assets/3f98db15-184b-4fb2-99ae-9e24d2397093)

## 7. Future Steps
- **Finalize Results**:
  - Evaluate model performance on test data.
  - Compare accuracy, F1 scores, and feature importance across all models.
- **Analyze Limitations**:
  - Assess potential biases in data collection.
  - Address challenges in modeling rare events like severe accidents.
- **Deployment**:
  - Build an interactive dashboard to visualize accident likelihood in real time.

## Midterm Report and Presentation
- **YouTube Link**: [https://youtu.be/xDtrSEpDA7s](https://youtu.be/xDtrSEpDA7s)

## 4. Preliminary results
- Finally, we evaluated the calibrated model’s performance by checking its accuracy and F1 score, integrated its calibrated probabilities with those from other models, and saved high-probability predictions to a submission file for further analysis.
- We averaged the probability predictions from the calibrated models to produce a final probability estimate for each record. A threshold of 0.5 was applied to classify each record as either an accident (1) or non-accident (0), adjusting the sensitivity and specificity of the model as needed.
- Our models achieved accuracy of accuracy of 88.73%, indicating strong results given that this was a balanced dataset. Our F1 score  is 0.8859, which shows a good balance between precision and recall. This performance suggests that our models are well-calibrated and effective for predicting accident occurrences under the simulated conditions

