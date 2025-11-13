from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://trackora-qa.techversantinfotech.com/login")

# Using find_element to locate a single element
driver.find_element(By.ID, "email").send_keys("arun@techversantinfo.com")

print("Email input field located and text entered:")
links = driver.find_elements(By.TAG_NAME, 'Input')
print(f"Total number of links: {len(links)}")


