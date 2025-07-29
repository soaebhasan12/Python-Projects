# 📶 Internet Speed Twitter Complaint Bot 🤖🐦

Automate your internet complaints with style. This Python bot checks your internet speed using **Speedtest.net** and tweets your **internet service provider (ISP)** when you're not getting the promised speed. Perfect use case for customer accountability via social media!

---

## 🚀 What This Bot Does

- ⏱️ Measures your **download** and **upload** speed using `speedtest.net`
- ⚠️ Compares it with the **promised internet speed**
- 🐍 Automates login to Twitter using **Selenium**
- 🗣️ Tweets a complaint to your ISP if your speed is lower than expected

---

## 🧰 Technologies Used

- **Python 3**
- **Selenium** for browser automation
- **ChromeDriver** (via `webdriver_manager`)
- **Speedtest.net** for speed testing
- **Twitter Web UI** for tweeting

---

## 🏗️ How It Works

1. Opens [speedtest.net](https://www.speedtest.net) and initiates a speed test
2. Waits for the result and fetches:
   - `Download Speed`
   - `Upload Speed`
3. Logs into [twitter.com/login](https://twitter.com/login) using Selenium
4. Tweets the following complaint if speed is below the promised:

```
Hey Internet Provider, why is my internet speed {download} down / {upload} up when I pay for {promised_down} / {promised_up}? Fix your service!
```

---

## 🔐 Environment Setup

> ⚠️ Never store your credentials directly in code. Use a `.env` file or secure vault.

### Required Setup:

- Python 3
- Google Chrome browser
- Create a `.env` file with:

```
TWITTER_EMAIL=youremail@example.com
TWITTER_USERNAME=yourusername
TWITTER_PASSWORD=yourpassword
PROMISED_DOWN=150
PROMISED_UP=50
```

### Install Required Packages:

```bash
pip install selenium webdriver-manager
```

---

## 🧪 How to Run

```python
from selenium import webdriver

bot = InternetSpeedTwitterBot(driver)
bot.get_internet_speed()
bot.tweet_at_provider()
```

You can also schedule this bot to run daily using cron (Linux/macOS) or Task Scheduler (Windows).

---

## 💡 Use Cases

- Hold your ISP accountable for poor service
- Public complaints may result in quicker responses
- Great project to learn:
  - Web automation
  - Selenium browser control
  - Handling login & time delays

---

## ⚙️ Features to Add

- Use .env or config.yaml for credentials
- Switch from UI-based automation to Twitter API
- Add GUI with Tkinter or Streamlit
- Store speed history in CSV/JSON
- Add multi-ISP support

---

## 🤝 Contributing

Pull requests are welcome!
Find a bug or want to improve compatibility? Fork the repo and submit a PR.
Let's make internet fair together 🚀

---

## 📄 License

MIT License.
Use freely — but don't spam ISPs 😉

---

## 🙌 Acknowledgements

- Inspired by real complaints on Twitter (Comcast Case)
- Speedtest powered by speedtest.net
- Built with ❤️ during #100DaysOfCode

---

## 🔗 Connect With Me

- Twitter: [@soaebism_02](https://twitter.com/soaebism_02)
- GitHub: [github.com/your-username](https://github.com/soaebhasan12)

---