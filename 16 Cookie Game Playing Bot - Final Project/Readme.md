# 🍪 Cookie Clicker Automation Bot

A Selenium-powered bot that plays the popular Cookie Clicker game autonomously, optimizing cookie production through strategic upgrades.

![Cookie Clicker Automation Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDhyZ2NtY3B6dW0ya3JtY2VlZGN5Z2VjeHp4eG5qY2VjZzZzbmZ6biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohzdQFPJt7L3GRQSY/giphy.gif)

## 🚀 Features

- **High-speed clicking**: 600+ clicks per minute
- **Smart upgrades**: Automatically purchases optimal upgrades
- **Performance tracking**: Reports cookies-per-second (CPS) metrics
- **Headless mode**: Optional background operation

## ⚙️ Technical Implementation

```python
# Core Game Loop
while True:
    cookie.click()  # Main clicking action
    
    if time.time() > timeout:  # Upgrade check
        # 1. Parse current cookie count
        # 2. Identify affordable upgrades 
        # 3. Purchase most expensive upgrade
        timeout = time.time() + 5  # Reset timer
```

## 🛠️ Setup

1. Install dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```

2. Run the bot:
   ```bash
   python main.py
   ```


## 🔍 Key Techniques

1. **Element Location Strategies**:
   - `By.ID` for main cookie
   - `By.CSS_SELECTOR` for upgrades

2. **Text Parsing**:
   ```python
   cost = int(price.text.split("-")[1].strip().replace(",", ""))
   ```

3. **Optimal Upgrade Logic**:
   ```python
   max(affordable_upgrades)  # Always buys best available upgrade
   ```

## 🌟 Future Enhancements

- [ ] Add headless mode support
- [ ] Implement adaptive timing
- [ ] Add visual progress tracking
- [ ] Support for custom upgrade priorities

## 📚 Resources

- [Cookie Clicker Game](http://orteil.dashnet.org/experiments/cookie/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)
