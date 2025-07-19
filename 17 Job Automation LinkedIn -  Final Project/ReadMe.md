# LinkedIn Job Application Bot 🤖

Automate your job search by applying to LinkedIn "Easy Apply" positions with this Python Selenium bot. Saves hours of manual applications while you focus on preparing for interviews.

## 🌟 Features
- **Automated Login**: Securely logs into your LinkedIn account
- **Smart Job Search**: Targets "Easy Apply" positions based on your criteria
- **Application Filling**: Auto-fills phone number and submits applications
- **Error Handling**: Skips complex applications and unavailable jobs
- **Safety Features**: Respects LinkedIn's policies with human-like delays

## 🛠️ Tech Stack
- Python 3
- Selenium WebDriver
- ChromeDriver
- python-dotenv (for secure credential management)

## 🚀 Getting Started

### Prerequisites
- Chrome/Firefox browser installed
- LinkedIn account (with 2FA disabled temporarily)
- Python 3.8+

### Installation
1. Clone the repository:
```bash
git clone "https://github.com/saoebhasan12/Day-49 Automating Job Applications on LinkedIn.git"
cd "01 Final Project - Job Automation LinkedIn"
```

2. Install dependencies:
```bash
pip install selenium python-dotenv webdriver-manager
```

3. Set up environment variables:
Create a `.env` file with your credentials:
```ini
USERNAME=your_linkedin_email@example.com
PASSWORD=your_linkedin_password
CONTACT=your_phone_number
```

## ⚙️ Configuration
Customize the job search URL in the script:
```python
job_application_url = "https://www.linkedin.com/jobs/search-results/?f_AL=true&keywords=Marketing%20Intern"
```
Modify the keywords and filters as needed.

## 🏃 Running the Bot
Execute the script:
```bash
python main.py
```

The bot will:
1. Log in to LinkedIn
2. Search for jobs matching your criteria
3. Apply to each suitable position
4. Skip complex applications automatically

## 🛡️ Ethical Considerations
- Only apply to jobs you're genuinely interested in
- Limit application rate to avoid triggering anti-bot measures
- Consider using a test account for development
- Be prepared to solve occasional CAPTCHAs manually

## � Troubleshooting
**Common Issues:**
1. **CAPTCHA Challenges**: Solve manually when prompted
2. **Element Not Found**: Adjust sleep timings if your connection is slow
3. **Account Restrictions**: Avoid making too many applications quickly

**Solutions:**
- Increase delay times between actions
- Update ChromeDriver if browser updates
- Verify LinkedIn hasn't changed its UI structure

## 📈 Future Enhancements
- [ ] Add support for multi-page applications
- [ ] Implement job tracking in Google Sheets
- [ ] Add randomized human-like behavior patterns
- [ ] Support for Indeed and other job platforms

## 📜 License
MIT License - use responsibly
-