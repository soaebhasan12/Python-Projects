# ISS Overhead Notifier 🚀

A Python automation project that notifies you via email whenever the International Space Station (ISS) is flying above your location at night.

## Features

- Tracks the real-time position of the ISS using the open-notify API
- Checks if the ISS is within ±5 degrees of your latitude and longitude
- Uses the sunrise-sunset.org API to determine if it’s currently dark at your location
- Sends an email notification when both conditions are met
- Runs automatically every 60 seconds

## Tech Stack

- Python 3
- [requests](https://pypi.org/project/requests/) (API calls)
- [datetime](https://docs.python.org/3/library/datetime.html) (time handling)
- [smtplib](https://docs.python.org/3/library/smtplib.html) (email automation)
- [time](https://docs.python.org/3/library/time.html) (scheduling)

## How It Works

1. Fetches the ISS’s current latitude and longitude.
2. Checks if the ISS is overhead (within ±5 degrees of your coordinates).
3. Fetches sunrise and sunset times for your location.
4. Determines if it’s currently nighttime.
5. If both conditions are true, sends you an email notification.
6. Repeats the check every 60 seconds.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/iss-overhead-notifier.git
   cd iss-overhead-notifier
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Configure your details:**
   - Set your latitude and longitude in the script.
   - Add your email and an app password (recommended for Gmail).

4. **Run the script:**
   ```bash
   python main.py
   ```

## Notes

- For Gmail, you may need to enable "App Passwords" and allow less secure apps.
- The script runs indefinitely; stop it manually when needed.
- Never share your real email password in public repositories.

## License

This project is licensed under the MIT License.
