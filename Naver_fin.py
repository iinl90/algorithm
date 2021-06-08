import re
import sys
import os
import time
import random
import urllib.request
import pyperclip
import wget
import shutil
import ctypes
import pdb
import datetime
import telegram
import requests
import telegram_message as tm
from win32com.client import Dispatch
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = Options()
chrome_options.add_argument('--window-position=850,0')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('c:\\chromedriver\\chromedriver.exe', chrome_options=chrome_options)

# while True:
driver.get('https://finance.naver.com/item/main.nhn?code=003490')
	
stock = int(driver.find_element_by_css_selector('p.no_today').text.replace('\n','').replace(',',''))

if stock >= 30000:
	tm.get_message(stock)
