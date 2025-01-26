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

    return float(text.split(": ")[1])

def generate_file_name():
    x = datetime.datetime.now()

    return x.strftime("%Y-%m-%d.%H:%M:%S") + ".txt"


def main():

    driver = get_driver()
    time.sleep(2)
    val = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")

    while True:

        f = open(f"Dyn_Val_Storage/{generate_file_name()}", "w")
        f.write(str(clean_text(val.text)))
        f.close()
        time.sleep(2)


main()