__author__ = 'mbrown'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import unittest, time, re
import traceback


class SimpleStalker():
    """
    This class does nothing but layout the interface for the stalk classes (so I can test the scheduler)
    Furthermore it allows me to highlight how java-like I write my python code.

    Has the name "simple"
    """
    def __init__(self, stalk_cfg):
        self.cfg = stalk_cfg

    def stalk(self):
        """
        Stalk should return a message if there is something to notify, otherwise it will return None
        """
        return "testing notifications"

    @staticmethod
    def name():
        return "simple"


class DisneyRestaurantsStalker():
    """
    Stalk a list of restaurants for a particular date. Notify if there's a NEW value since the last check.

    Has the name "disney_restaurant"
    """
    def __init__(self, stalk_cfg):
        self.cfg = stalk_cfg
        self.urls = self.cfg['urls']
        self.web_driver = self.cfg['webdriver']
        self.date = self.cfg['date']
        self.browser = None
        self.old_times = {}

    def setup(self, url):
        if url not in self.old_times:
            self.old_times[url] = set()
        os.environ["webdriver.chrome.driver"] = self.web_driver
        self.browser = webdriver.Chrome(self.web_driver)
        self.browser.get(url)

    def reset(self, url):
        if self.browser is not None:
            self.browser.quit()
        self.browser = None

    def stalk(self):
        msgs = []
        for url in self.urls:
            print "Scanning %s" % url
            self.setup(url)
            result = None
            try:
                result = self.stalk_single_site(url)
                if result is not None:
                    msgs.append(result)
            except Exception, err:
                print "Uh oh, there was a problem"
                print(traceback.format_exc())

            self.reset(url)

        if msgs:
            return "\n".join(msgs)

        return None

    def stalk_single_site(self, url):
        """
        Stalk should return a message if there is something to notify, otherwise it will return None
        """
        #Hold up, wait a second for the date picker to clear. Javascript bullshit
        time.sleep(1)
        ### Setup search
        search_date = self.get_element_with_wait(self.browser, 10, 'diningAvailabilityForm-searchDate')
        self.browser.execute_script("document.getElementById('diningAvailabilityForm-searchDate').value = \"\"")
        search_date.send_keys(self.date)
        search_date.send_keys(Keys.TAB)

        #Hold up, wait a second for the date picker to clear. Javascript bullshit
        time.sleep(1)

        #Select time dropdown
        time_box = self.browser.find_element_by_class_name('select-toggle')
        time_box.click()
        time_box.send_keys('D')
        time_box.send_keys(Keys.ENTER)

        #####EXECUTE SEARCH
        search_button = self.get_element_with_wait(self.browser, 10, 'searchButton')
        search_button.click()

        ###########Results
        #first check for no results
        no_results_element = None
        try:
            no_results_element = self.get_element_with_wait(self.browser, 20, 'ctaNoAvailableTimesContainer', by=By.CLASS_NAME)
        except TimeoutException:
            print "There are results!"

        new_times = set()
        if no_results_element is None:
            result_div = self.browser.find_element_by_class_name('ctaAvailableTimesContainer')
            times = result_div.find_elements_by_class_name("buttonText")
            new_times = set([x.text for x in times])


        #########Determine new times
        msg = None
        update_times = self.determine_update_times(self.old_times[url], new_times)
        if update_times:
            msg = "There are new times for %s: %s" % (url, ', '.join(update_times))

        self.old_times[url] = new_times
        return msg

    def determine_update_times(self, old, new):
        return new - old

    def get_element_with_wait(self, browser, timeout, element_id, by=By.ID):
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, element_id))
        )
        return element

    @staticmethod
    def name():
        return "disney_restaurant"


def get_stalker(stalk_cfg):
    name = stalk_cfg['name']
    if name == SimpleStalker.name():
        return SimpleStalker(stalk_cfg)
    if name == DisneyRestaurantsStalker.name():
        return DisneyRestaurantsStalker(stalk_cfg)
    else:
        return SimpleStalker(stalk_cfg)