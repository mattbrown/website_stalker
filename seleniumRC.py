# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import unittest, time, re

class SeleniumRC():
    def __init__(self):
        self.old_times = set()

    def start(self):
        msg = None

        chromedriver = "/Users/mbrown/Downloads/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        browser = webdriver.Chrome(chromedriver)
        sanaa = "https://disneyworld.disney.go.com/dining/animal-kingdom-villas-kidani/sanaa/"
        ohana = 'https://disneyworld.disney.go.com/dining/polynesian-resort/ohana/'
        browser.get(sanaa)
        search_date = self.get_element_with_wait(browser, 10, 'diningAvailabilityForm-searchDate')
        browser.execute_script("document.getElementById('diningAvailabilityForm-searchDate').value = \"\"")
        search_date.send_keys("09/19/2015")

        #Select time dropdown
        time_box = browser.find_element_by_class_name('select-toggle')
        time_box.click()
        time_box.send_keys('D')
        time_dropdown = browser.find_element_by_id('diningAvailabilityForm-searchTime-1')
        time_dropdown.click()


        #Search
        search_button = self.get_element_with_wait(browser, 10, 'searchButton')
        search_button.click()
        search_button.click()

        ###########Results
        #first check for no results
        no_results_element = None
        try:
            no_results_element = self.get_element_with_wait(browser, 10, 'ctaNoAvailableTimesContainer', by=By.CLASS_NAME)
        except TimeoutException:
            print "There are results!"

        new_times = set()
        if no_results_element is None:
            result_div = browser.find_element_by_class_name('ctaAvailableTimesContainer')
            times = result_div.find_elements_by_class_name("buttonText")
            new_times = set([x.text for x in times])


        #########Determine method
        update_times = self.determine_update_times(self.old_times, new_times)
        if update_times:
            msg = "There are new times for sanaa: %s" % (', '.join(update_times))

        #####Cleanup run####
        #Set last times
        self.old_times = new_times

        browser.close()

        #Create

        return msg

    def determine_update_times(self, old, new):
        return new - old

    def get_element_with_wait(self, browser, timeout, element_id, by=By.ID):
        element =  WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, element_id))
        )
        return element

if __name__ == "__main__":
    stalker = SeleniumRC()
    print "first run result %s " % stalker.start()
    print "second run result %s " % stalker.start()


