# Final Project: Predicting Traffic Accidents Based on Weather and Time Data in Greater Boston Area

## 1. Project Overview
This project aims to predict the likelihood of traffic accidents at specific locations and times in the Greater Boston Metropolitan Area. By integrating historical crash data with weather and temporal information, we developed a predictive model to estimate the probability of accidents under different conditions.

The model's primary purpose is to enable real-time risk assessments for transportation agencies, navigation services, and city planners. It can serve as a foundation for targeted interventions, such as advisory systems for drivers or policy changes aimed at reducing accident risks.

---

## 2. Goals and Objectives

### Primary Goals:
- Build a robust predictive model that estimates the likelihood of accidents based on key features such as weather conditions, time of day, rush hour, and road surface conditions.
  - Example Output: “There is a 70% chance of an accident at 5 PM on a rainy weekday in Boston.”

### Secondary Goals:
- Analyze the factors most strongly correlated with accident occurrence to provide actionable insights.
  - Example Insight: “Nighttime rain during rush hour increases the accident likelihood by 50%.”

---

## 3. Data Sources and Features

### Data Sources
1. **Crash Data**:
   - **Source**: [Massachusetts Crash Portal](https://massdot-impact-crashes-vhb.opendata.arcgis.com/)
   - **Years Covered**: 2022 and 2023
   - **Features**:
     - **Location**: City/town name (`CITY_TOWN_NAME`), latitude, and longitude.
     - **Crash Timing**: Date (`CRASH_DATE_TEXT`), time (`CRASH_TIME_2`).
     - **Weather Conditions**: Reported weather at the time of the crash (`WEATH_COND_DESCR`).
     - **Road Conditions**: Road surface condition (`ROAD_SURF_COND_DESCR`), ambient lighting, and junction type.
     - **Crash Severity**: Indicators of crash outcomes (e.g., fatal or non-fatal).

2. **Weather Data**:
   - **Source**: Historical weather services (e.g., OpenWeatherMap API).
   - **Features**:
     - Temperature, precipitation (rain, snow), humidity, visibility, and wind speed.
     - Simplified conditions: Rain, clear, fog, etc.

3. **Temporal Data**:
   - **Derived Features**:
     - `IS_RUSH_HOUR`: Rush hour indicator (6–10 AM, 3–7 PM).
     - `IS_WEEKEND`: Weekend indicator (Saturday/Sunday).
     - `IS_NIGHT`: Nighttime indicator (8 PM–6 AM).
     - `IS_HOLIDAY`: U.S. public holidays, using the `holidays` library.

---

## 4. Data Processing and Engineering

### Initial Cleaning
1. **Column Filtering**:
   - Removed over 100 unnecessary columns, including those with:
     - Over 50% missing values.
     - Unique identifiers irrelevant to modeling.
     - Duplicative or overly granular information (e.g., street names).

2. **Filtering for Greater Boston**:
   - Filtered the dataset to include only crashes in cities and towns within the Greater Boston Metropolitan Area.
   - Used a predefined list of cities and encoded them numerically using `LabelEncoder`.

### Feature Engineering
1. **Datetime Features**:
   - Combined `CRASH_DATE_TEXT` and `CRASH_TIME_2` into `CRASH_DATETIME` for consistency.
   - Extracted:
     - `DAY_OF_WEEK`: Numeric representation (Monday = 0, Sunday = 6).
     - `IS_NIGHT`: 1 if crash occurred between 8 PM and 6 AM.
     - `IS_RUSH_HOUR`: 1 for rush hours (6–10 AM and 3–7 PM).
     - `IS_HOLIDAY`: 1 if crash occurred on a public holiday.

2. **Weather Simplification**:
   - Grouped detailed weather descriptions into broader categories:
     - Clear, rain, snow, fog/smoke, and others.
   - Encoded these categories numerically for modeling.

3. **Speed Limit Ranges**:
   - Grouped speed limits into `<30 mph`, `30–50 mph`, and `>50 mph`.
   - Encoded these ranges numerically.

4. **Interaction Terms**:
   - Created features capturing combined effects:
     - `WEATHER_RUSH_HOUR`: Interaction between weather and rush hour.
     - `WEATHER_NIGHT`: Interaction between weather and nighttime.
     - `WEATHER_WEEKEND`: Interaction between weather and weekends.

### Synthetic Data Generation
- **Purpose**: Balance the dataset, as crashes were overrepresented.
- **Method**:
  - Generated synthetic non-accident data by simulating realistic conditions where accidents are less likely to occur.
  - Assigned weighted probabilities for features like weather, time of day, and road conditions based on observed crash data.

---

## 5. Data Modeling

### Train-Test Split
- The merged dataset was shuffled and split into:
  - **80% Training Data**: Used for model training and hyperparameter tuning.
  - **20% Test Data**: Used for evaluating model performance.

### Models Used
1. **Baseline: Logistic Regression**
   - Simple model for binary classification.

2. **Random Forest**
   - Optimized with Bayesian hyperparameter tuning for:
     - Number of trees (`n_estimators`), maximum depth, and minimum samples per split.

3. **Gradient Boosting (XGBoost)**
   - Captures non-linear relationships between features and target.

4. **Neural Network**
   - Trained using a sequential architecture:
     - Input layer, two hidden layers (64 and 32 nodes), and a final sigmoid activation for binary classification.

5. **Stacking Classifier**
   - Combined predictions from Random Forest, XGBoost, and Gradient Boosting using Logistic Regression as a meta-classifier.

### Calibration
- Applied isotonic and sigmoid calibration to improve the reliability of predicted probabilities.

---

## 6. Preliminary Visualizations
### Key Insights
1. **Accidents by Weekend vs. Weekday**:
   - Weekdays had significantly more accidents, likely due to higher traffic volumes.

2. **Accidents by Weather Condition**:
   - Rain and snow increased accident frequency compared to clear weather.

3. **Accidents During Day vs. Night**:
   - Nighttime accidents, though fewer, were often more severe.

4. **Heatmap of Correlations**:
   - `IS_RUSH_HOUR` and `DAY_OF_WEEK` were moderately correlated with crash frequency.

### Sample Visualizations
#### Bar Chart: Accidents by Rush Hour
![Accidents by Rush Hour](https://github.com/user-attachments/assets/70507ae4-2b5e-4b24-b651-a55ce0dddab1)

#### Correlation Heatmap
![Correlation Heatmap](https://github.com/user-attachments/assets/6b148ea5-7b51-4089-b353-76524613e535)

#### Interaction Term: Weather and Rush Hour
![Weather and Rush Hour](https://github.com/user-attachments/assets/3f98db15-184b-4fb2-99ae-9e24d2397093)

---

## 7. Evaluation Metrics
- **Accuracy**: Percentage of correct predictions.
- **F1 Score**: Balance between precision and recall, especially useful for imbalanced datasets.
- **Confusion Matrix**: Evaluated false positives/negatives for accident prediction.

---

## 8. Future Work
1. **Refinement**:
   - Incorporate additional features such as road type, traffic control devices, or driver demographics (if available).
   - Improve synthetic data generation with more realistic weights.

2. **Analysis of Feature Importance**:
   - Quantify the contribution of weather, time, and interaction terms to accident likelihood.

3. **Deployment**:
   - Create an interactive dashboard for real-time accident prediction.
   - Collaborate with transportation agencies for practical implementation.

---

## Midterm Report and Presentation
- **YouTube Link**: [https://youtu.be/xDtrSEpDA7s](https://youtu.be/xDtrSEpDA7s)
- 

## 4. Preliminary results
- Finally, we evaluated the calibrated model’s performance by checking its accuracy and F1 score, integrated its calibrated probabilities with those from other models, and saved high-probability predictions to a submission file for further analysis.
- We averaged the probability predictions from the calibrated models to produce a final probability estimate for each record. A threshold of 0.5 was applied to classify each record as either an accident (1) or non-accident (0), adjusting the sensitivity and specificity of the model as needed.
- Our models achieved accuracy of accuracy of 88.73%, indicating strong results given that this was a balanced dataset. Our F1 score  is 0.8859, which shows a good balance between precision and recall. This performance suggests that our models are well-calibrated and effective for predicting accident occurrences under the simulated conditions

