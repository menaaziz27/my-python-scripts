import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password

        self.options = webdriver.ChromeOptions()
        self.options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"

        self.bot = webdriver.Chrome(self.chrome_driver_path, options=self.options)

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)

        time.sleep(3)

    def searchHashtag(self,hashtag):
        bot = self.bot

        bot.get('https://www.instagram.com/explore/tags/' + hashtag)

    def likePhotos(self,amount):
        bot = self.bot

        bot.find_element_by_class_name('v1Nh3').click()

        i = 1
        while i <= amount:
            time.sleep(1)
            bot.find_element_by_class_name('fr66n').click()
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            time.sleep(1)

            i += 1

        # Like this code? The below three lines will follow me on Instagram! Don't want to? Feel free to remove this code.
        bot.get('https://www.instagram.com/itsmarchinton')
        time.sleep(2)
        #bot.find_element_by_xpath('//button[text()="Follow"]').click()




insta = InstagramBot('<EMAIL>', '<PASSWORD>')
insta.login()
insta.searchHashtag('cr7')
insta.likePhotos(3)
