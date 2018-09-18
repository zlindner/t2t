from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime

accounts = [
    {
        "first_name": "Zachary",
        "last_name": "Lindner",
        "email": "zlindner@uoguelph.ca",
        "times": ["12:00", "12:30", "1:00", "1:30", "2:00", "2:30"]
    },
    {
        "first_name": "Meghan",
        "last_name": "McLeod",
        "email": "mmcleo07@uoguelph.ca",
        "times": ["3:00", "3:30", "4:00", "4:30", "5:00", "5:30"]
    },
    {
        "first_name": "Alexandra",
        "last_name": "Ramsey",
        "email": "aramsey@uoguelph.ca",
        "times": ["6:00", "6:30", "7:00", "7:30", "8:00", "8:30"]
    },
    {
        "first_name": "Hamad",
        "last_name": "Ahmed",
        "email": "hamad@uoguelph.ca",
        "times": ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30"]
    }
]

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

browser = webdriver.Chrome()

for account in accounts:
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
