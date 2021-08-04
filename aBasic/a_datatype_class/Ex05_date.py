
import datetime
today = datetime.date.today();
print('today is ', today)

print()

from datetime import date
today = date.today();
print('today is ', today)

# 년 / 월 / 일 추출해서 출력
print('년도', today.year)
print('월', today.month)
print('일', today.day)

print()
# 날짜 계산
from datetime import timedelta
today = date.today();
print('어제 날짜 :',  today + timedelta(days=-1))
print('일주일전 날짜 :', today + timedelta(days=-7))
print('열흘 후 날짜 :', today + timedelta(days=10))



'''
1) 날짜형을 문자열로 변환 : strftime()
2) 문자열을 날짜형으로 변환 : strptime()

print()
from datetime import date
today = date.today()
print(today.strftime('%m/%d/%y'))
print(today.strftime('%Y %m %d %H : %M'))

naljja = '2020-08-10 12:55:30'
naljja2 = datetime.strptime(naljja, '%Y %m %d %H : %M')
print(naljja2)
'''