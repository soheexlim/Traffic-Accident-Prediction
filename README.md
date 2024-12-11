# Final Project: Predicting Traffic Accidents Based on Weather and Time Data in the Greater Boston Area

## 1. Project Overview

This project leverages machine learning models to predict the likelihood of traffic accidents in the Greater Boston Metropolitan Area. By using historical crash data and integrating weather and time-related features, the project provides actionable insights into traffic accident risks. 

The outcomes of this project are designed to assist city planners, transportation agencies, and navigation services in implementing proactive safety measures. Additionally, the interactive Flask web application allows users to input specific conditions (e.g., time, weather, location) and receive predictions about accident likelihood.

---

## 2. Goals and Objectives

### Primary Goal
Develop a robust machine learning model to predict the likelihood of traffic accidents based on key variables, such as weather conditions, road surface states, and temporal factors (e.g., day of the week, rush hour).

### Secondary Goal
Analyze the influence of individual and combined factors (e.g., weather during rush hour or nighttime) to identify key contributors to accident risks. These insights will be critical for designing data-driven interventions and safety campaigns.

---

## 3. Data Sources and Features

### Data Sources
The dataset combines crash data from 2022 and 2023, sourced from the [Massachusetts Crash Portal](https://massdot-impact-crashes-vhb.opendata.arcgis.com/). The dataset includes crash details such as location, time, weather conditions, and road surface conditions. Additional features were engineered to enrich the data, including holiday indicators and rush hour classifications.

### Key Features
The dataset contains the following critical features:
- **Crash Timing**: 
  - `CRASH_HOUR` (hour of the crash)
  - `DAY_OF_WEEK` (day of the week)
  - `IS_NIGHT` (nighttime indicator)
  - `IS_RUSH_HOUR` (rush hour indicator)
  - `IS_HOLIDAY` (holiday indicator)
- **Weather Conditions**:
  - `WEATHER_SIMPLIFIED_ENCODED` (e.g., Clear, Rain, Snow)
- **Road Conditions**:
  - `ROAD_SURF_COND_ENCODED` (e.g., Wet, Dry, Ice)
  - `SPEED_LIMIT_ENCODED` (categorized speed limits: <30 mph, 30–50 mph, >50 mph)
- **Interaction Terms**:
  - `WEATHER_RUSH_HOUR`, `WEATHER_NIGHT`, and `WEATHER_WEEKEND` capture combined effects of weather and temporal factors.

These features were selected based on their relevance to accident risk prediction and ease of interpretability.

---

## 4. Data Processing and Feature Engineering

### Data Cleaning
- Removed columns with over 50% missing values or irrelevant information (e.g., street names).
- Filtered the dataset to include only crashes within the Greater Boston area, based on a predefined list of cities and towns.
- Addressed missing values by imputing or dropping rows/columns, depending on feature importance.

### Feature Engineering
- **Datetime Features**: Derived features such as `DAY_OF_WEEK`, `IS_NIGHT`, `IS_RUSH_HOUR`, and `IS_HOLIDAY` using the `CRASH_DATETIME` column.
- **Simplified Weather Descriptions**: Grouped detailed weather conditions into categories like "Clear," "Rain," and "Snow."
- **Categorized Speed Limits**: Grouped speed limits into ranges (<30 mph, 30–50 mph, >50 mph) and encoded them numerically.
- **Interaction Terms**: Created features to analyze combined effects, such as `WEATHER_RUSH_HOUR` and `WEATHER_NIGHT`.

### Synthetic Data Generation
To address data imbalance, synthetic non-accident data was generated. Weighted probabilities were assigned to features such as weather and time of day, ensuring the synthetic data mirrored real-world conditions. 

---

## 5. Modeling

### Machine Learning Models
- **Random Forest**: Optimized using Bayesian hyperparameter tuning for accuracy and generalizability.
- **Gradient Boosting (XGBoost)**: Captures complex, non-linear relationships between features and the target variable.
- **Neural Network**: A two-layer model with dropout regularization to prevent overfitting.
- **Stacking Classifier**: Combines predictions from Random Forest, Gradient Boosting, and XGBoost using Logistic Regression as the meta-classifier.

### Calibration and Evaluation
- Models were calibrated using isotonic and sigmoid methods to ensure reliable probability predictions.
- Evaluation metrics included:
  - **Accuracy**: Overall correctness of predictions.
  - **F1 Score**: Balance between precision and recall.
  - **Confusion Matrix**: Provides detailed breakdowns of true/false positives and negatives.

---

## 6. Flask Web Application

An interactive web application was developed using Flask to provide users with real-time predictions. Users can input specific conditions (e.g., CRASH_HOUR, CITY_TOWN_NAME_ENCODED, WEATHER_SIMPLIFIED_ENCODED) via a form with dropdown menus. 

### Dropdown Options
Key dropdown options include:
- **CRASH_HOUR**: 0–12
- **CITY_TOWN_NAME**:
  - Examples: ABINGTON, BOSTON, CAMBRIDGE, NEWTON
- **TIME_OF_DAY**:
  - Morning, Afternoon, Evening, Night
- **SPEED_LIMIT**:
  - Less than 30, Between 30 and 50, Greater than 50
- **WEATHER**:
  - Blowing Sand/Snow, Clear, Fog/Smoke, Rain, Snow
- **ROAD_SURF_COND_ENCODED**:
  - Wet, Dry, Ice, Snow, Slush
- **DAY_OF_WEEK**:
  - Monday, Tuesday, Wednesday, etc.
- **IS_WEEKEND, IS_NIGHT, IS_HOLIDAY, IS_RUSH_HOUR**:
  - Yes or No

The application outputs either "Likely to Crash" or "Not Likely to Crash" based on the user inputs.

---

## 7. Results and Visualizations

### Key Insights
- **Rush Hour and Weather**:
  - Accidents are more likely during rush hour, particularly in rainy or snowy conditions.
- **Nighttime Accidents**:
  - Nighttime accidents, though less frequent, tend to be more severe.
- **Speed Limit Impact**:
  - Higher speed limits correlate with a greater risk of accidents.

### Sample Visualizations
1. **Accidents During Rush Hour**:
   - Bar charts show increased accident counts during rush hour.
2. **Weather and Rush Hour Interaction**:
   - Highlighted elevated risks when adverse weather coincides with rush hour.
3. **Correlation Heatmap**:
   - Revealed strong relationships between weather, rush hour, and accident occurrence.

---

## 8. Future Work and Applications

### Next Steps
1. **Expand Features**:
   - Integrate additional datasets (e.g., traffic volume, seasonal trends).
2. **Improve Deployment**:
   - Deploy the web application to a cloud service for broader access.
3. **Optimize Models**:
   - Experiment with advanced ensemble techniques and larger datasets.

### Applications
This project has practical applications for:
- Transportation agencies to deploy real-time alerts and interventions.
- Navigation services (e.g., Google Maps) to warn users about high-risk areas and times.
- Policy recommendations for infrastructure and public safety improvements.

---

## 9. Midterm Report and Presentation
- **YouTube Link**: [https://youtu.be/xDtrSEpDA7s](https://youtu.be/xDtrSEpDA7s)

---

## 10. Technical References

### Key Python Libraries
- **Flask**: For building the web application.
- **scikit-learn**: For machine learning models and calibration.
- **XGBoost**: For gradient boosting.
- **pandas, numpy**: For data manipulation and analysis.
- **seaborn, matplotlib**: For visualizations.

### Links
- [Massachusetts Crash Portal](https://massdot-impact-crashes-vhb.opendata.arcgis.com/)
- [GitHub Repository](https://github.com/soheexlim/final-project)

---
