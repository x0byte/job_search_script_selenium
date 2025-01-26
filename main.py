from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import datetime

service = Service('/home/hirun/Downloads/chromedriver-linux64/chromedriver')

def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")


    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://")

    return driver

def clean_text(text):

    pass



def main():

    driver = get_driver()
    time.sleep(2)
    val = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")

    return val.text

main()