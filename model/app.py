import joblib
from flask import Flask, request, render_template
import pandas as pd

# Load the model
model = joblib.load('calibrated_rf_model.joblib')

# Initialize Flask app
app = Flask(__name__)

# Define the home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect user input from the form
        crash_hour = int(request.form["CRASH_HOUR"])
        city_town = int(request.form["CITY_TOWN_NAME_ENCODED"])
        time_of_day = int(request.form["TIME_OF_DAY_ENCODED"])
        speed_limit = int(request.form["SPEED_LIMIT_ENCODED"])
        weather = int(request.form["WEATHER_SIMPLIFIED_ENCODED"])
        road_surface = int(request.form["ROAD_SURF_COND_ENCODED"])
        day_of_week = int(request.form["DAY_OF_WEEK"])
        is_weekend = int(request.form["IS_WEEKEND"])
        is_night = int(request.form["IS_NIGHT"])
        is_holiday = int(request.form["IS_HOLIDAY"])
        is_rush_hour = int(request.form["IS_RUSH_HOUR"])

        # Create a DataFrame for the input
        input_data = pd.DataFrame({
            'CRASH_HOUR': [crash_hour],
            'CITY_TOWN_NAME_ENCODED': [city_town],
            'TIME_OF_DAY_ENCODED': [time_of_day],
            'SPEED_LIMIT_ENCODED': [speed_limit],
            'WEATHER_SIMPLIFIED_ENCODED': [weather],
            'ROAD_SURF_COND_ENCODED': [road_surface],
            'DAY_OF_WEEK': [day_of_week],
            'IS_WEEKEND': [is_weekend],
            'IS_NIGHT': [is_night],
            'IS_HOLIDAY': [is_holiday],
            'IS_RUSH_HOUR': [is_rush_hour],
        })

        # Make prediction
        prediction = model.predict(input_data)[0]


        # Display the result
        #return render_template("index.html", prediction=f"{crash_likelihood}%")


        # Display the result
        return render_template("index.html", prediction=prediction)

    return render_template("index.html", prediction=None)


if __name__ == "__main__":
    app.run(debug=True)
