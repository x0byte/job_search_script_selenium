from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import re

def get_output_file_name(url):
    # Remove non-alphanumeric characters from the URL 
    sanitized_url = re.sub(r'\W+', '_', url)
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_name = f"{sanitized_url}_{current_time}.html"

    return output_file_name

def download_html(url):
    output_file = get_output_file_name(url)
    # Initialize the WebDriver (assuming you have the appropriate driver installed)
    driver = webdriver.Chrome()

    try:
        # Navigate to the specified URL
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # Get the page source (HTML content)
        html_content = driver.page_source

        # Write the HTML content to the specified file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"HTML content downloaded and saved to {output_file}")

    except Exception as e:
        print(f"Error downloading HTML content: {e}")

    finally:
        # Close the driver
        driver.quit()


download_html("https://www.seek.com.au/Software-Engineer-jobs/in-Melbourne-VIC-3000")
