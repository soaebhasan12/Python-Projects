# 🎵 Musical Time Machine ⏳

A Python script that creates Spotify playlists from Billboard's Top 100 songs of any date in history - perfect for nostalgic trips down memory lane!

## 🌟 Features
- **Date-Based Playlists**: Enter any date (YYYY-MM-DD) to get that week's hits
- **One-Click Creation**: Fully automated playlist generation
- **Private Playlists**: All created playlists are private by default
- **Error Resilient**: Skips unavailable songs automatically

## 🛠️ Tech Stack
- **Web Scraping**: `BeautifulSoup4` to extract Billboard data
- **Spotify Integration**: `spotipy` library for API interactions
- **OAuth 2.0**: Secure authentication without storing credentials

## ⚡ Quick Start

### Prerequisites
- Python 3.8+
- Spotify account (free tier works)
- Spotify Developer account

### Installation
```bash
git clone https://github.com/yourusername/musical-time-machine.git
cd musical-time-machine
pip install -r requirements.txt
```

### Configuration
1. Create a Spotify App at [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Get your `CLIENT_ID` and `CLIENT_SECRET`
3. Create `.env` file:
```ini
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
```

### Usage
```bash
python main.py
```
▶️ Enter your target date when prompted (format: YYYY-MM-DD)  
▶️ Authenticate with Spotify when browser opens  
▶️ Enjoy your new nostalgic playlist!

## 📚 How It Works
1. Scrapes Billboard's Hot 100 for the specified date
2. Searches Spotify for each track
3. Creates a new private playlist
4. Adds all available tracks

## 🚀 Future Enhancements
- [ ] Add GUI interface
- [ ] Include album artwork in playlist description
- [ ] Support for international charts
- [ ] Automatic anniversary playlist creation

## 🤝 Contributing
PRs welcome! Please open an issue first to discuss changes.

## 📜 License
MIT

---

Made with ❤️ during #100DaysOfCode  
