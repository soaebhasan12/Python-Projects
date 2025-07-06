# ☔ Rain Alert System

Automated weather alerts sent via SMS when rain is predicted in your area.

## 🚀 Features
- 12-hour rain prediction using OpenWeatherMap API
- SMS notifications via Twilio
- PythonAnywhere deployment support
- Environment variable configuration

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/rain-alert.git
cd rain-alert
pip install requests python-dotenv
```

## 🔐 Configuration
1. Create `.env` file:
```ini
OWM_API_KEY=your_openweathermap_key
AUTH_TOKEN=your_twilio_auth_token
```

2. Update `main.py` with:
```python
account_sid = "ACxxxxxxxxxxxxxx"  # Twilio SID
weather_params = {
    "lat": "YOUR_LATITUDE",  # eg. "51.5074"
    "lon": "YOUR_LONGITUDE", # eg. "-0.1278"
    "exclude": "current,minutely,daily"
}
```

## 🖥️ Usage
### Local Execution
```bash
python main.py
```

### PythonAnywhere Setup
1. Upload files via dashboard
2. Create scheduled task:
```bash
python3 main.py
```
3. Set to run daily at desired UTC time

## 📁 File Structure
```
rain-alert/
├── main.py            # Main application logic
├── .env               # Environment variables
├── README.md          # This file
└── requirements.txt   # Dependencies
```

## 📜 Requirements
- Python 3.6+
- `requests` package
- Twilio trial account
- OpenWeatherMap API key

## ⚠️ Notes
- Free PythonAnywhere accounts require proxy configuration
- Twilio trial only sends to verified numbers
- All time calculations use UTC

## 📄 License
MIT License - Part of #100DaysOfCode