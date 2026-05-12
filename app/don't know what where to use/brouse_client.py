from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



driver = None


def start_browser():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return "Browser started"


def search_google(query,wait_and_see):
    global driver
    print("Start ... ")    
    if driver is None:
        return "Browser not running"
    
    driver.get("https://www.google.com/maps")

    box = driver.find_element(By.NAME, "q")
    box.send_keys(query)
    search_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Search']"))
    )

    search_btn.click()
    print("end")
    time.sleep(wait_and_see)

    return driver.title


def close_browser():
    global driver
    
    if driver:
        driver.quit()
        driver = None
    
    return "Browser closed"