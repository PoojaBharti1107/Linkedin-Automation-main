import time
# from jmespath import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL='https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')

#TestCase 1
#Wrong email
driver.get(URL)
driver.maximize_window()
time.sleep(2)
email=driver.find_element(By.ID,"username")
email.click()
email.clear()
email.send_keys("wrong_email@gmail.com") 
time.sleep(2)
password=driver.find_element(By.ID,"password");
password.click()
password.send_keys("wrong_pass")
signin_button=driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)

#TestCase 2
#Wrong Password
driver.get(URL)
email=driver.find_element(By.ID,"username")
email.click()
email.clear()
email.send_keys("correct_email@gmail.com")
time.sleep(5)
password=driver.find_element(By.ID,"password")
password.click()
password.send_keys("wrong_pass")
signin_button=driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)

#TestCase 3
#Correct Password Wrong id
driver.get(URL)
driver.maximize_window()
time.sleep(10)
email=driver.find_element(By.ID,"username")
email.click()
email.clear()
email.send_keys("wrong_email@gmail.com")
time.sleep(2)
password=driver.find_element(By.ID,"password")
password.click()
password.send_keys("correct_pass")
signin_button=driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)

#TestCase 4
#Correct ID and PASSWORD
driver.get(URL)
driver.maximize_window()
time.sleep(3)
email=driver.find_element(By.ID,"username")
email.click()
email.clear()
email.send_keys("correct_email@gmail.com")
time.sleep(2)
password=driver.find_element(By.ID,"password")
password.click()
password.send_keys("correct_pass")
signin_button=driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button")
signin_button.click()
print('\n Test case ==> Passed')
time.sleep(3)