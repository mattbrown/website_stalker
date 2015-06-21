# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class SeleniumRC():
    def start(self):
        self.selenium = selenium("localhost", 4444, "*firefox", "https://disneyworld.disney.go.com")
        self.selenium.start()
    
        sel = self.selenium
        print "HAIDFHASDFLKH"
        sel.open("/dining/polynesian-resort/ohana/")
        sel.run_script("document.getElementById('diningAvailabilityForm-searchDate').value = \"\"")
        sel.send_keys("id=diningAvailabilityForm-searchDate", "09/19/2015")
        sel.click("css=div.select-toggle.hoverable")
        sel.click("css=#diningAvailabilityForm-searchTime-1 > span.rawOption")
        sel.click("css=span.buttonText")
    
        self.selenium.stop()

if __name__ == "__main__":
    SeleniumRC().start()
