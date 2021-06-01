import re
import requests
import telegram

def get_message(stock):
	# 토큰 입력
	TELEGRAM_TOKEN = '1725000222:AAGsyVOVONgPVeQ4rAJZU9Vx-H-MRaptNIA' # token 자리에 본인의 토큰 입력
	bot = telegram.Bot(token=TELEGRAM_TOKEN)

	# 텔레그렘 봇 id 추출
	response = requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates')
	api_data = response.text.encode('cp949').decode('unicode_escape')

	chat_ids = re.findall('"id":[0-9]+',api_data)
	chat_id = chat_ids[-1].replace('"id":','')

	# 텔레그렘 메세지 보내기
	bot.sendMessage(chat_id=chat_id, text=f'현재 주가는 {stock}입니다.')
