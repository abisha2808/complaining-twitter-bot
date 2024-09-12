from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
promised_down = 150
promised_up = 10
username = "jane00739285217"


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = self.down.text
        print(self.down)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = self.up.text
        print(self.up)
        #self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys("jane4241778@gmail.com")
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(10)
        user_name = self.driver.find_element(By.NAME, "text")
        user_name.send_keys(username)
        user_name.send_keys(Keys.ENTER)
        time.sleep(10)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("Janeabisha@28")
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        post.click()

        time.sleep(10)
        write = self.driver.find_element(By.CSS_SELECTOR, '[aria-autocomplete="list"]')
        write.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up?")

        time.sleep(2)
        write.send_keys(Keys.CONTROL, Keys.ENTER)

        time.sleep(2)
        self.driver.quit()


internet = InternetSpeedTwitterBot()
internet.get_internet_speed()
internet.tweet_at_provider()
