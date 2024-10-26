# Weather App

The web application allows users to enter a city name to view real-time weather information, including temperature, humidity, pressure, and geographic coordinates, using data from the OpenWeatherMap API.

---

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)

---

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default database, can be configured for others)
- Other dependencies listed in `requirements.txt`

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yzaazaa/weather_app.git
cd weather_app
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

```bash
SECRET_KEY=your-secret-key
WEATHERAPI_KEY=your-api-key
```
Generate Secret key: https://djecrety.ir/

Generate weather api key: https://openweathermap.org/appid


### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit http://localhost:8000 in your browser

