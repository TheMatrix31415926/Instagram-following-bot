import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os

CHROME_DRIVER_PATH = r"C:\Driver_Google\chromedriver.exe"

INSTA_USERNAME = os.environ.get("hella")
INSTA_PASSWORD = os.environ.get("ur_password")
SIMILAR_ACCOUNT = "chef_steps"
INSTA_URL = "https://www.instagram.com/accounts/login/"
CHEF_STEPS_URL = "https://www.instagram.com/chef_steps/"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(service=Service(path))

    def login(self):
        self.driver.get(url=INSTA_URL)
        time.sleep(3)
        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(INSTA_USERNAME)
        time.sleep(2)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(INSTA_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(CHEF_STEPS_URL)
        time.sleep(3)
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, value="followers")
        time.sleep(2)
        followers.click()
        time.sleep(2)

    def follow(self):
        try:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for item in list_of_followers:
                print(item.text)
                if item.text == "Follow":
                    print("click")
                    item.click()
                    time.sleep(3)

        except Exception as e:
            print(e)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
