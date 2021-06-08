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
driver.get('https://lostark.game.onstove.com/Auction')
