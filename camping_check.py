import re
import os
import pdb
import sys
import time
import wget
import random
import shutil
import ctypes
import requests
import datetime
import pyperclip
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from win32com.client import Dispatch
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = Options()
chrome_options.add_argument('--window-position=850,0')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('c:\\chromedriver\\chromedriver.exe', chrome_options=chrome_options)

css_path = 'td.booking_day'

driver.get('http://golohas.kr/reservation')
driver.implicitly_wait(5)
res_check = driver.find_elements_by_css_selector(css_path)
res_days = driver.find_element_by_css_selector('#w202006043d5c9f5adb1b2 > div > div > div.booking_toolbar.clearfix > div > p').text
for line in res_check:
	day , check = line.text.split('\n')[0] , line.text.split('\n')[1:]
	try:
		if '성수기' == check[0]:
			del check[0]

		if '가' in check[0] or '가' in check[1]:
			print(f'{res_days} {day}일')
	except:
		continue