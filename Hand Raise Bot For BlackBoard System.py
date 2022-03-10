'''
Consider using chrome extension "XPath Helper".

This project idea is make a raise hand bot for blackboard system. 
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import time

user_id = input("Enter your user ID: ")
password = input("Enter your password: ")

PATH = "D:\\ChromeDriver\\chromedriver.exe" # We need a chrome or other web driver .exe path.
driver = webdriver.Chrome(PATH)

driver.get("https://blackboard.maltepe.edu.tr/") # Get Blackboard website request.
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agree_button"]'))).click()

inputElement = driver.find_element_by_id("user_id")
inputElement.send_keys(user_id)
inputElement = driver.find_element_by_id("password")
inputElement.send_keys(password)

link = driver.find_element_by_id('entry-login')
link.click()
driver.get("https://blackboard.maltepe.edu.tr/ultra/courses/_71623_1/outline")

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Oturuma katıl']"))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Ders Odası']"))).click()
print(driver.current_url)
time.sleep(5)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
print(driver.current_url)
newURL = driver.current_url
driver.get(newURL)
time.sleep(10)

driver.find_element_by_xpath('//div[@class="techcheck-permissions"]//button').click()
time.sleep(3)
driver.find_element_by_xpath("//div[@id='announcement-modal-page-wrap']//button[@class='close']").click()
wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'raise-hand'))).click()