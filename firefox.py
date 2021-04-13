#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
import time
import requests
import settings as setting
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import sys
import json
import os

profile = webdriver.FirefoxProfile()
profile.set_preference("geo.prompt.testing", True)
profile.set_preference("geo.prompt.testing.allow", True)
profile.set_preference("geo.wifi.scan", True)
profile.set_preference("geo.provider.network.url", 'data:application/json,{"location":{"lat":' + setting.getLocation()[0] + ',"lng":' + setting.getLocation()[1] + '},"accuracy": 100.0}')
if setting.getSetting('user-agent') == "on":
    profile.set_preference("general.useragent.override", str(setting.getDevice()))
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
time.sleep(2)
driver.maximize_window()
# PLUGIN INSTALL
driver.install_addon(os.path.abspath("vpn.xpi"), temporary=True)
# PLUGIN INSTALL
time.sleep(setting.getSetting('workSleep'))
driver.close()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(setting.getSetting('workSleep'))
driver.get("about:config")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="warningButton"]').click()
time.sleep(setting.getSetting('workSleep'))
driver.find_element_by_xpath('//*[@id=\"about-config-search\"]').send_keys("extensions.webextensions.uuids")
time.sleep(3)
plugin = json.loads(driver.find_element_by_xpath('/html/body/table/tr/td[1]/span/span').get_attribute('innerHTML'))
driver.get("moz-extension://" + plugin["touch-vpn@anchorfree.com"] + "/panel/index.html")
time.sleep(setting.getSetting('workSleep'))
driver.find_element_by_xpath('//*[@class="button button--red data-consent__accept-button"]').click()
time.sleep(setting.getSetting('workSleep'))

driver.find_element_by_xpath('//*[@id="ConnectionButton"]').click()
time.sleep(setting.getSetting('workSleep'))
driver.get("https://google.com")
time.sleep(99999)
driver.close()
sys.exit()
