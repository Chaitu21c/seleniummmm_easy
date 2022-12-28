from PAGES import pages_creation
from BASE.initiate_browser import open_browser
from selenium import webdriver
from LIBRARY import configreader
driver=open_browser()
page=pages_creation.input(driver)
input_forms=page
input_forms.exampls()
sample_form=page
sample_form.simple_form()
input=page
input.send_keys()
show_message=page
show_message.submit()
diaplay=page
diaplay.display()
input_forms.exampls()
checkbox=page
checkbox.checkbox()
click_checkbox=page
click_checkbox.click_checkbox()


