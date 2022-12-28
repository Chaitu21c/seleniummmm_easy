from  selenium import webdriver
from LIBRARY import configreader
global driver
def open_browser():
    global driver
    browser=configreader.read_date("Details","browser")
    if browser=="Chrome":
        driver=webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get(configreader.read_date("Details","url"))
        driver.maximize_window()
    return driver