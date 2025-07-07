# Stock News Alert System

A Python application that monitors stock price movements and sends SMS alerts with relevant news when significant changes occur.

## Features
- Real-time stock price monitoring using Alpha Vantage API
- Automated news fetching via NewsAPI
- SMS notifications through Twilio
- Configurable price change thresholds
- Formatted alerts with change indicators

## How It Works
1. Fetches daily closing prices for specified stocks
2. Calculates percentage change from previous day
3. When change exceeds threshold (default: 5%):
   - Retrieves top 3 relevant news articles
   - Formats SMS message with stock info and articles
4. Sends alerts via Twilio SMS

## Prerequisites
- Python 3.8+
- API keys for Alpha Vantage, NewsAPI, and Twilio

## Installation
1. Clone the repository:
git clone https://github.com/yourusername/stock-news-alert.git
cd stock-news-alert

2. Install dependencies:
pip install -r requirements.txt

3. Set up environment variables:
cp .env.example .env
Edit .env with your API credentials

## Configuration
Edit :
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc" 
THRESHOLD_PERCENT = 5

## Usage
Run the main script:
python main.py

For scheduled alerts (cron):
0 9 * * * cd /path/to/project && python main.py



## License
MIT