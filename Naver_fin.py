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

def check_chromedriver():

	# 폴더에 chromedriver 있으면 지우기
	import requests
	from win32com.client import Dispatch
	try:
		os.remove('chromedriver.exe')
	except:
		pass

	# chromedriver 현재 버전 구하기 -------------------------------
	filepath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
	if os.path.exists(filepath):
		pass
	else:
		filepath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
	parser = Dispatch("Scripting.FileSystemObject")
	version = parser.GetFileVersion(filepath)

	chrome_version = int(version[0:2])


	# chromedriver 사이즈 웹에서 확인 ------------------------------- 

	chromedriver_size_from_web = {}
	response = requests.get('http://wkwk.kr/chromedriver')
	text = response.text
	source = text.split('||')
	for i in source:
		i = i.strip()
		chromedriver_size_from_web[int(i.split('@')[0])] = int(i.split('@')[1])

	print('chrome_version : {}'.format(chrome_version))

	# input(chromedriver_size_from_web)
	# print(chromedriver_size_from_web['75'])

	size = 0
	flag_download = 0

	try:
		# 파일은 있음. 용량이 일치하는지 확인
		size = os.path.getsize("c:\\chromedriver\\chromedriver.exe")

		if size != chromedriver_size_from_web[chrome_version]:

			flag_download = 1    # 파일은 있으나 용량이 일치하지 않으므로 다운로드 필요
			print('크롬드라이버 용량 불일치. 다운시작.')

	except FileNotFoundError:

		print('파일없음. 다운시작.')

		if not os.path.isdir('c:\\chromedriver'):
			os.mkdir('c:\\chromedriver')

		flag_download = 1

	if flag_download == 1:

		url = 'http://wkwk.kr/chromedriver/{}/chromedriver.exe'.format(chrome_version)

		wget.download(url)
		shutil.move("./chromedriver.exe", "c:\\chromedriver\\chromedriver.exe")

check_chromedriver()    # 크롬드라이버 최신 확인 및 다운로드 모듈

chrome_options = Options()
chrome_options.add_argument('--window-position=850,0')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('c:\\chromedriver\\chromedriver.exe', chrome_options=chrome_options)

# while True:
driver.get('https://finance.naver.com/item/main.nhn?code=003490')
	
stock = int(driver.find_element_by_css_selector('p.no_today').text.replace('\n','').replace(',',''))

if stock >= 30000:
	tm.get_message(stock)

