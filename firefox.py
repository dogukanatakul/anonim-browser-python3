#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
import time
import settings as setting
from webdriver_manager.firefox import GeckoDriverManager
import sys
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

profile = webdriver.FirefoxProfile()
profile.set_preference("geo.prompt.testing", False)
profile.set_preference("geo.prompt.testing.allow", False)
profile.set_preference("geo.wifi.scan", True)
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference('network.http.use-cache', False)
profile.accept_untrusted_certs = True
profile.set_preference("security.cert_pinning.enforcement_level", 0)
profile.set_preference("security.enterprise_roots.enabled", True)

if setting.getSetting('fakeGeo') == "on":
    profile.set_preference("geo.provider.network.url", 'data:application/json,{"location":{"lat":' + setting.getLocation()[0] + ',"lng":' + setting.getLocation()[1] + '},"accuracy": 100.0}')
if setting.getSetting('userAgent') == "on":
    profile.set_preference("general.useragent.override", str(setting.getDevice()))

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['handleAlerts'] = True
firefox_capabilities['acceptSslCerts'] = True
firefox_capabilities['acceptInsecureCerts'] = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile, capabilities=firefox_capabilities)
time.sleep(2)
driver.maximize_window()
if setting.getSetting('vpn') == "on":
    # PLUGIN INSTALL
    driver.install_addon(os.path.abspath("vpn.xpi"), temporary=True)
    # PLUGIN INSTALL
    while len(driver.window_handles) < 2:
        time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(setting.getSetting('workSleep'))
    driver.get("about:config")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="warningButton"]').click()
    time.sleep(setting.getSetting('workSleep'))
    driver.find_element(By.XPATH, '//*[@id=\"about-config-search\"]').send_keys("extensions.webextensions.uuids")
    time.sleep(3)
    plugin = json.loads(driver.find_element(By.XPATH, '/html/body/table/tr/td[1]/span/span').get_attribute('innerHTML'))
    driver.get("moz-extension://" + plugin["{fca67f41-776b-438a-9382-662171858615}"] + "/popup/index.html")
    time.sleep(setting.getSetting('workSleep'))
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/strong[2]').click()
    time.sleep(setting.getSetting('workSleep'))
    driver.find_element(By.XPATH, '//*[@class="primary agreement_agree"]').click()
    time.sleep(setting.getSetting('workSleep'))
    driver.find_element(By.XPATH, '//*[@class="play_button play_button--play"]').click()
time.sleep(setting.getSetting('workSleep'))
driver.get("https://faucet.chainflag.org/")
time.sleep(99999)
driver.close()
sys.exit()
