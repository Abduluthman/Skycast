from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'e42f49d22d5b4b81b2491611251807'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None

    if request.method == 'POST':
        city = request.form['city'].strip()
        country = request.form['country'].strip()
        location = f"{city},{country}"

        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days=5&aqi=no&alerts=no"
        response = requests.get(url)

        try:
            data = response.json()
            if "error" in data:
                weather_data = {'error': data['error']['message']}
            else:
                weather_data = data['current']
                forecast_data = data['forecast']['forecastday']
                location_info = data['location']
        except Exception:
            weather_data = {'error': 'Failed to fetch weather data'}

    return render_template('index.html', weather=weather_data, forecast=forecast_data, location=location_info if weather_data and not weather_data.get("error") else None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)