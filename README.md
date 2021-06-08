## 210525 telegram_message.py
텔레그램에 내가 원하는 메세지를 보낸다.

## 210526 Naver_fin.py
셀레니움을 이용해 네이버 금융에서 원하는 주식의 현재 호가를 크롤링한다.
- 문제점1 한라인으로 크롤링 되는 것이 아닌 여러줄에 한글자씩 크롤링됨
    + 해결 : replace를 통해 문자열 정렬

## 210531 lost_ark.py
셀레니움을 이용해 로스트아크 경매장 물품의 가격을 크롤링한다.


## 210602 telegram_message.py , Naver_fin.py
telegram_message.py를 함수화하여 Naver_fin.py에서 호출하고 내가 원하는 주가 이상이 되면 메세지를 보낸다.

## 210608 camping_check.py
셀레니움을 이용해 캠핑장 예약상태를 크롤링한다.
