import time

from selenium import webdriver
from LIBRARY import configreader
from BASE.initiate_browser import open_browser
from selenium.webdriver.common.by import By
import time
global driver
class input:
    def __init__(self,webpage):
        global driver
        driver=webpage
    def exampls(self):
        driver.find_element(By.XPATH, configreader.read_date("Details", "input_forms")).click()
        time.sleep(5)
    def simple_form(self):
        driver.find_element(By.LINK_TEXT, configreader.read_date("Details", "Simple Form Demo")).click()
        time.sleep(3)
    def send_keys(self):
        driver.find_element(By.ID,configreader.read_date("Details","user-message")).send_keys("chaithanya prasad")
        time.sleep(5)
    def submit(self):
        driver.find_element(By.XPATH,configreader.read_date("Details","submit")).click()
        time.sleep(5)
    def display(self):
        display=driver.find_element(By.ID, configreader.read_date("Details","display"))
        print(display.text)
    def checkbox(self):
        driver.find_element(By.XPATH,configreader.read_date("Details","Checkbox")).click()
    def click_checkbox(self):
        list=driver.find_elements(By.XPATH,configreader.read_date("Details","checkboxlist"))
        for checkbox in list:
            time.sleep(2)
            checkbox.click()