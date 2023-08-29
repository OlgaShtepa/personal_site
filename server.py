from flask import Flask, render_template, request
from weather_api import get_weather_data
import datetime

app = Flask(__name__)

certificate_count = 4

@app.route("/")
def home():
    current_year=datetime.datetime.now().year
    return render_template("index.html", certificate_count=certificate_count, year=current_year)


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return 'City not provided', 400

    data = get_weather_data(city)
    if data:
        return data
    else:
        return 'Weather data not available', 404


if __name__ == "__main__":
    app.run(debug=True)
