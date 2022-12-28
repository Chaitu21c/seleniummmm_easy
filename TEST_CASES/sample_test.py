from BASE.initiate_browser import open_browser
from LIBRARY import configreader
from selenium.webdriver.common.by import By
import time
driver=open_browser()
time.sleep(5)
input_forms=driver.find_element(By.XPATH,configreader.read_date("Details","input_forms")).click()
time.sleep(5)
simple_forms=driver.find_element(By.LINK_TEXT,configreader.read_date("Details","Simple Form Demo")).click()
time.sleep(3)
message=driver.find_element(By.ID,"user-message").send_keys("chaithanya prasad")
submit=driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()
display=driver.find_element(By.ID,"display")
print(display.text)
input_forms1=driver.find_element(By.XPATH,configreader.read_date("Details","input_forms")).click()
checkbox=driver.find_element(By.XPATH,"(//a[@href='./basic-checkbox-demo.html'])[2]").click()
list=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for item in list:
    time.sleep(3)
    item.click()
    time.sleep(5)


