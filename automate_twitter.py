# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:31:58 2018

@author: Himanshi
"""
from selenium import webdriver     
import time  .
from selenium.webdriver.common.keys import Keys  

browser = webdriver.Chrome() 
browser.get('https://www.twitter.com')
login = browser.find_elements_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div/a')
login[0].click()
print("Loggin in Twitter")
 
user = browser.find_elements_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
with open('username.txt', 'r') as myfile:  
    Username = myfile.read().replace('\n', '')
user[0].send_keys(Username)
user = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
with open('password.txt', 'r') as myfile:  
    Password = myfile.read().replace('\n', '')
user.send_keys(Password)
 
LOG = browser.find_elements_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
LOG[0].click()
print("Login Sucessfull")

time.sleep(3)
elem = browser.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')
elem.click()
elem.clear()
elem = browser.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')
elem.send_keys('AUTOMATED TWEET DEDICATED TO SOFTVISION')
tweet = browser.find_elements_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]')
tweet[0].click()
print ("Tweet Posted Successfully")

time.sleep(5)
browser.close() 
