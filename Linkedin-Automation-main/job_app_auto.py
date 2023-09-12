import time
# from jmespath import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

URL='https://www.linkedin.com/jobs/search/?currentJobId=3116907507&f_AL=true&f_E=2&f_JT=F%2CI&f_WT=2&geoId=102713980&keywords=software%20developer&location=India&refresh=true&sortBy=R'

driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')

# open the linkedin page for jobs, according to the filters in URL
driver.get(URL)
uname="your username"
pwd="your password"
# find sign in button
sign_in=driver.find_element(By.LINK_TEXT,"Sign in")
sign_in.click()
time.sleep(2)

# enter the sign in details
time.sleep(3)
email=driver.find_element(By.ID,"username")
email.click()
email.clear()
email.send_keys("uname")
time.sleep(2)
password=driver.find_element(By.ID,"password")
password.click()
password.send_keys("pwd")
# press enter
password.send_keys(Keys.ENTER)
time.sleep(2)


# find list
listing=driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

# case when there is next button, review button, and submit button
for l in listing:
    print("Called")
    l.click()
    time.sleep(2)
    try:
        apply_btn=driver.find_element(By.CSS_SELECTOR,".job-s-apply")
        apply_btn.click()
        time.sleep(2)
        next_btn=driver.find_element(By.CSS_SELECTOR,"footer button")
        next.btn.click()
        time.sleep(2)
        review_btn=driver.find_element(By.CLASS_NAME,"artdeco-button--primary")
        if review_btn.get_attribute("data-control-name")=="continue-unify":
            close_btn=driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_btn.click()
            time.sleep(2)
            discard_btn=driver.find_element(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
            discard_btn.click()
            print("Complex Application")
            continue
        else:
            review_btn.click()
            time.sleep(2)
            submit_btn=driver.find_element(By.CLASS_NAME,"artdeco-button--primary")
            submit_btn.click()
            if(submit_btn.get_attribute("data-control-name")=="submit-unify"):
                submit_btn.click()
                time.sleep(2)
                close_btn=driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
                close_btn.click()
            else:
                close_btn=driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
                close_btn.click()
                time.sleep(2)
                discard_btn=driver.find_element(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
                discard_btn.click()
                print("Complex Application")
                continue
    except NoSuchElementException:
        print("NO application button, skipped")
        continue

    
        

    

