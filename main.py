from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.common.by import By

service = Service('/home/hirun/Downloads/chromedriver-linux64/chromedriver')

def get_driver(url):

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    return driver

def get_from_seek_au(keywords, city):

    driver = get_driver("https://www.seek.com.au/")
    time.sleep(2)

    # Open the output file
    with open(f"seek_jobs_{datetime.date.today().strftime('%Y-%m-%d')}.txt", "a") as f:
        for keyword in keywords:
            # Search for jobs
            driver.find_element(By.ID, "keywords-input").send_keys(keyword)
            driver.find_element(By.ID, "SearchBar__Where").send_keys(city)
            driver.find_element(By.ID, "searchButton").send_keys(Keys.ENTER)
            time.sleep(5)

            # Click the first job card
            try:
                driver.find_element(By.XPATH, "//article[@data-testid='job-card']").click()
                time.sleep(3)

                # Collect job data
                title = driver.find_element(By.XPATH, "//h1[contains(@data-automation, 'job-detail-title')]").text
                advertiser = driver.find_element(By.XPATH, "//span[contains(@data-automation, 'advertiser-name')]").text
                work_type = driver.find_element(By.XPATH, "//span[contains(@data-automation, 'job-detail-work-type')]").text
                description = driver.find_element(By.XPATH, "//div[contains(@data-automation, 'jobAdDetails')]").text

                # Write the data to the file
                f.write(f"Title: {title}\n")
                f.write(f"Advertiser: {advertiser}\n")
                f.write(f"Work Type: {work_type}\n")
                f.write(f"Description: {description}\n")
                f.write("-" * 50 + "\n")

            except Exception as e:
                print(f"Error extracting job data: {e}")

    # Close the driver
    driver.quit()

def main():

    city = "Melbourne"
    keywords = ["Software Engineer"]

    # get_from_seek_au(keywords, city)

main()