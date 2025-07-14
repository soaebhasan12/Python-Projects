# 🛒 Amazon Price Tracker Bot

An automated Python bot that monitors the price of an Amazon product and sends an email alert when the price drops below your target value. Never miss a deal again! 🤑

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Web Scraping](https://img.shields.io/badge/Web--Scraping-BeautifulSoup-green)
![SMTP](https://img.shields.io/badge/Email-SMTP-yellow)
![Status](https://img.shields.io/badge/Build-Stable-brightgreen)

---

## 📌 Features

- 🔍 Scrapes Amazon product price using `requests` and `BeautifulSoup`
- 📤 Sends email alert when price falls below your target
- 🧠 Clean data extraction with `.strip()`, `.split()`, and price conversion
- 🔐 Supports Gmail, Outlook, Yahoo via SMTP
- 🕒 Can be scheduled daily using task scheduler / cron

---

## 💻 Tech Stack

- Python 3.10+
- BeautifulSoup (`bs4`)
- Requests
- lxml
- smtplib (SMTP for emails)

---

## 🚀 How It Works

1. Fetches the Amazon product page using `requests`  
2. Parses the HTML and extracts:
   - Product title
   - Current price (as float)  
3. Compares the price with your set `BUY_PRICE`  
4. If price is below target → sends an email with:
   - Title
   - Current price
   - Product link  

---

## 🧪 Setup Instructions

### 🔧 Prerequisites

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
````

### 📬 Gmail SMTP Setup

> For Gmail users, follow these steps:

1. Turn ON 2-Step Verification:
   [https://myaccount.google.com/security](https://myaccount.google.com/security)

2. Generate an App Password under "Security" settings

3. Use this app password in the code instead of your actual password

> For other providers like Outlook/Yahoo, update the SMTP host in code:

```python
smtplib.SMTP("smtp.outlook.office365.com", port=587)
```

---

## ⚙️ How to Use

1. Clone this repo

```bash
git clone https://github.com/soaebhasan12/Day-47 - Create an Automated Amazon Price Tracker.git
cd Day-47 - Create an Automated Amazon Price Tracker
     cd 00 Build Challengewise
     cd 01 Final Project - Automated Price Tracker
```

2. Update these variables in your script:

```python
url = "YOUR_AMAZON_PRODUCT_LINK"
BUY_PRICE = 100  # Set your desired target price
app_password = "YOUR_APP_PASSWORD"
```

3. Run the script:

```bash
python main.py
```

You’ll get an email if the price is below your target 🎉

---

## 📆 Schedule It Daily (Optional)

Use `cron` on Linux/macOS or `Task Scheduler` on Windows to check the price daily at a specific time (e.g., 9:00 AM).

---

## 🤝 Contributing

If you have suggestions, bug fixes, or want to add more features (like SMS alerts, CSV logs, etc.), feel free to open a PR or issue. Let’s improve it together!

---

## 📧 Contact

Created with 💙 by [Shoaib Hasan](https://github.com/soaebhasan12)
Email: [saibuhasan22@gmail.com](mailto:saibuhasan22@gmail.com)

---

## 🌟 If you found this useful

Give this repo a ⭐ and consider sharing it!
Let’s automate smart shopping for everyone 💸

