# Module for Selenium tests

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class MircoAppDonationTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("drivers/chromedriver")

    def test_donate_with_USD(self):
        driver = self.driver
        currency = 'USD'
        amount = 0
        driver.get("http://localhost:8080/")

        # choose option
        select = Select(driver.find_element_by_id('currency'))
        select.select_by_value(currency)

        # fill in text field
        input = driver.find_element_by_id('amount')
        input.send_keys(amount)

        # click button
        driver.find_element_by_css_selector('.btn.btn-primary.btn-block').click()
        time.sleep(2) # wait for the message loading
        paymentWidget = driver.find_element_by_css_selector('.paymentWidgets')
        # assert the message
        assert paymentWidget.text == "VISA MASTER AMEX"


    def test_donate_with_EUR(self):
        driver = self.driver
        currency = 'EUR'
        amount = 0
        driver.get("http://localhost:8080/")

        # choose option
        select = Select(driver.find_element_by_id('currency'))
        select.select_by_value(currency)

        # fill in text field
        input = driver.find_element_by_id('amount')
        input.send_keys(amount)

        # click button
        driver.find_element_by_css_selector('.btn.btn-primary.btn-block').click()
        time.sleep(3) # wait for the message loading
        paymentWidget = driver.find_element_by_css_selector('.paymentWidgets')
        #assert the message
        assert paymentWidget.text == "VISA MASTER AMEX"
   

    def test_donate_with_wrong_amount(self):
        driver = self.driver
        currency = 'USD'
        amount = "www"
        driver.get("http://localhost:8080/")

        # choose option
        select = Select(driver.find_element_by_id('currency'))
        select.select_by_value(currency)

        # fill in text field
        input = driver.find_element_by_id('amount')
        input.send_keys(amount)

        # click button
        driver.find_element_by_css_selector('.btn.btn-primary.btn-block').click()
        # assert the message
        alert = driver.find_element_by_css_selector('.alert.alert-danger.erroralert')
        assert alert.text == "Oh snap! Amount must be number!"


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
