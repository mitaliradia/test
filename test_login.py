from pathlib import Path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

try:
    file_path=Path("login.html").resolve().as_uri()
    driver.get(file_path)
    time.sleep(2)

    driver.find_element(By.ID,"username").send_keys("admin")
    time.sleep(2)

    driver.find_element(By.ID,"password").send_keys("admin123")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(2)

    success_message=wait.until(EC.text_to_be_present_in_element((By.ID,"message"),"Login successful!"))
    time.sleep(2)

    assert success_message

    print("Valid login test passed")

    driver.find_element(By.ID,"username").clear()
    driver.find_element(By.ID,"password").clear()

    driver.find_element(By.ID,"username").send_keys("wronguser")
    time.sleep(2)

    driver.find_element(By.ID,"password").send_keys("wrongpass")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(2)

    
    error_message=wait.until(EC.text_to_be_present_in_element((By.ID,"message"),"Invalid username or password."))
    time.sleep(2)
    
    assert error_message

    print("Invalid login test passed")

finally:
    driver.quit()
