from selenium import webdriver
from selenium.webdriver.support.ui import Select
import json
import time
import datetime

f = open("accounts.json")
json_data = json.load(f)

f.close()

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

browser = webdriver.Chrome()

for account in json_data:
    browser.get("https://cal.lib.uoguelph.ca/reserve/5-person-study-rooms")

    for i in range(6):
        browser.find_element_by_xpath(
            "//*[@title='" + account["times"][i] + "pm " + tomorrow.strftime("%A, %B %d, %Y") + " - Room 533']").click()

        time.sleep(2)

    browser.find_element_by_name("submit_times").click()

    time.sleep(2)

    browser.find_element_by_id("terms_accept").click()

    time.sleep(2)

    browser.find_element_by_id("fname").send_keys(account["first_name"])
    browser.find_element_by_id("lname").send_keys(account["last_name"])
    browser.find_element_by_id("email").send_keys(account["email"])

    browser.find_element_by_id("btn-form-submit").click()
