from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.w3schools.com/Jsref/tryit.asp?filename=tryjsref_alert2")


driver.switch_to.frame("iframeResult")


driver.find_element(By.XPATH, "//button[text()='Try it']").click()

time.sleep(2)

alert=driver.switch_to.alert
alert.text
print(f"Alert text is: {alert.text}")

time.sleep(2)
alert.accept()

