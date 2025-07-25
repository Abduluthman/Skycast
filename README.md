# ☁️ SkyCast - Weather Forecast Application

SkyCast is a lightweight, responsive weather forecast application built with **Flask (Python)** on the backend and **HTML/CSS** for the frontend. It integrates with the [WeatherAPI](https://www.weatherapi.com/) to fetch real-time weather data and a 5-day forecast.

---

## 🌟 Features

- 🔍 Search weather by **City and Country**
- 📊 Displays **current weather** (temperature, humidity, wind, condition)
- 📅 Shows **5-day weather forecast**
- 🎨 Beautiful **glassmorphism UI** with responsive design
- 📱 Optimized for **mobile and desktop**

---

## 🧰 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML + CSS
- **API**: [WeatherAPI](https://weatherapi.com)
- **Templating**: Jinja2

---

## 📂 Project Structure
```bash
skycast/
│
├── app.py                # Flask backend
├── templates/
│   └── index.html        # HTML frontend
├── static/
│   └── style.css         # Optional: CSS styles
├── requirements.txt      # Dependencies
└── README.md             # Project info
```

---

## ▶️ How to Run Locally

1. **Clone or download the repo**:
```bash
git clone https://github.com/AbdulUthman/skycast.git
cd skycast
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
python app.py
```
4. Open your browser and go to:
```bash
http://127.0.0.1:5000/
```

---

## 📱 Test on Mobile
To test on your mobile device:

1. Ensure your phone and computer are on the same Wi-Fi network
2. Find your local IP address (e.g. 192.168.1.5)
3. Run Flask with:
    ``` bash
    python app.py
4. Visit: http://192.168.1.5:5000 on your mobile browser

---

## 🔑 API Configuration
- Update the API key in app.py:
    ```bash
    API_KEY = ''
- Get your free key at: weatherapi.com

---

## 📦 Packaging
To zip the project:
Ensure the following files/folders are present:
- app.py
    - templates/index.html
    - static/style.css
- requirements.txt
- README.md

Select all files → Right-click → Send to > Compressed (zipped) folder

## 🧑‍💻 Author
Abdulwahab Uthman
For questions or collaboration: Abduluthman278@gmail.com
