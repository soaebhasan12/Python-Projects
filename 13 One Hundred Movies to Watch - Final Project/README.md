# Day 45: Web Scraping with Python

## 📋 Overview
This repository contains my Day 45 work from #100DaysOfCode, focusing on web scraping techniques using Python's BeautifulSoup and requests libraries.

## 🎯 Projects

### 1. Hacker News Scraper
Scrapes the top stories from Hacker News (news.ycombinator.com) and identifies the article with the most upvotes.

**Features:**
- Extracts article titles, links, and upvote counts
- Identifies the highest-voted story
- Implements rate limiting to respect `robots.txt`

### 2. Top 100 Movies Scraper
Scrapes Empire Magazine's "100 Greatest Movies" list and saves them in proper ranked order.

**Features:**
- Parses movie titles from the webpage
- Reverses the order (from #1 to #100)
- Saves results to `movies.txt`

## ⚙️ Setup

### Prerequisites
- Python 3.6+
- pip package manager

### Installation
pip install beautifulsoup4 requests





## ⚠️ Ethical Considerations
1. Always check the website's `robots.txt` (e.g., `website.com/robots.txt`)
2. Add delays between requests (`time.sleep(30)`)
3. Respect copyright and terms of service
4. Never scrape personal or sensitive data
5. Prefer official APIs when available

## 📚 Resources
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/)
- [Web Scraping Best Practices](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)

## 📝 License
This project is for educational purposes only.
