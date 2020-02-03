from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class StatesTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(StatesTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(StatesTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')

        drop_down_states = Select(selenium.find_element_by_id("id_state"))
        input_sick_people = selenium.find_element_by_id('id_sick_people')

        submit = selenium.find_element_by_name('register')

        # Fill the form with data
        time.sleep(2)
        drop_down_states.select_by_visible_text('Antioquia')
        time.sleep(2)
        input_sick_people.send_keys('one thousand two hundred fifty')
        time.sleep(2)

        # submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(2)

        # get report for sick people
        calculate_button = submit = selenium.find_element_by_name('get_data')
        submit.send_keys(Keys.RETURN)
        time.sleep(2)
