from datetime import datetime

print("현재 날짜 시각 객체 얻기")
today =  datetime.now()
print("today = datetime.now() : ",today)
print("년 월 일 : ", today.year, today.month, today.day)
print("시 분 초 : ", today.hour, today.minute, today.second)
print("요일 : ", today.weekday())  #0:월요일
print("특정 날짜 시각 객체 만들기")
day = datetime(2019,1,1,0,0,0)
print("day = datetime(2019,1,1,0,0,0) : ",day)
print("2019년부터 지나온 시간 구하기")
print("today - day : ", today - day)
#태어난지 며칠?
print("태어난지 며칠? ", today - datetime(2002,7,18,12,12,0))
#올해 크리스마스 며칠남았는지?
print("올해 크리스마스 며칠? ", today - datetime(2019,12,25,0,0,0))
#내남친이랑 며칠 되었는지?
print("내남친이랑 며칠? ", today - datetime(2019,5,27,0,0,0))