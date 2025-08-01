from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        
        # Click on 'Go' button
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(60)  # Wait for test to complete

        # Get download and upload speeds
        self.down = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                      '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        ).text
        self.up = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                      '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        # Login process
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(3)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # Compose Tweet
        tweet_compose = self.driver.find_element(
            By.CSS_SELECTOR, 'div[aria-label="Tweet text"]'
        )
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)

        time.sleep(3)
        tweet_button = self.driver.find_element(
            By.XPATH, '//div[@data-testid="tweetButtonInline"]'
        )
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


# Use the bot
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
