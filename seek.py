from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

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


def get_from_seek(keyword, location):
    processed_keyword = keyword.replace(" ", "-")
    processed_location = location.replace(" ", "-")

    url = f"https://www.seek.com.au/{processed_keyword}-jobs/in-{processed_location}"
    driver = get_driver(url)
    time.sleep(5)  

    filename = f"Job_Search/seek_jobs_{datetime.date.today().strftime('%Y-%m-%d')}.txt"
    with open(filename, "a", encoding="utf-8") as f:

        # Get all job cards
        job_cards = driver.find_elements(By.XPATH, "//article[contains(@data-automation, 'normalJob')]//a[contains(@href, '/job/')]")

        print(f"Found {len(job_cards)} job listings.")

        job_links = [card.get_attribute("href") for card in job_cards if card.get_attribute("href")]
        
        for job_url in job_links[:5]:  #first 5 jobs
            try:
                # Open job listing in new tab
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])  # Switch to new tab
                driver.get(job_url)
                time.sleep(3)  

                title = driver.find_element(By.XPATH, "//h1[contains(@data-automation, 'job-detail-title')]").text
                advertiser = driver.find_element(By.XPATH, "//span[contains(@data-automation, 'advertiser-name')]").text
                work_type = driver.find_element(By.XPATH, "//span[contains(@data-automation, 'job-detail-work-type')]").text
                description = driver.find_element(By.XPATH, "//div[contains(@data-automation, 'jobAdDetails')]").text

                f.write(f"Title: {title}\n")
                f.write(f"Advertiser: {advertiser}\n")
                f.write(f"Work Type: {work_type}\n")
                f.write(f"Description: {description}\n")
                f.write("-" * 50 + "\n")

                # Close job tab and return
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
                print(f"Error extracting job data: {e}")
                driver.close()
                driver.switch_to.window(driver.window_handles[0])  # Ensure returning to main tab

    driver.quit()


get_from_seek("Software Engineer", "Melbourne")
