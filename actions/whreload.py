import RPi.GPIO as GPIO
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#By default Router Tenda 301N has only web interface to communication.
def reloaders(resettype):
    if resettype=='web':
        browser=webdriver.Chrome()
        browser.get('http://192.168.0.1')
        textarea=browser.find_element_by_name("Password")
        # ******** - your Router password
        textarea.send_keys("********")
        textarea.send_keys(Keys.ENTER)
        browser.get("http://192.168.0.1/system_reboot.asp")
        rebbtn=browser.find_element_by_class_name("btn")
        rebbtn.click()
        alertok=browser.switch_to.alert
        alertok.accept()
        browser.close()
    elif resettype=='hard':
        #Pin number(18) can be changed according to Raspberry Pi GPIO pinout.
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(18, GPIO.LOW)
        GPIO.cleanup()
    else:
        pass
