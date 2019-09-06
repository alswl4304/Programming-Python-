# 알바비 계산기
# 일주일에 몇시간 일하는지 입력받자
# 몇주 일하는지 입력받자
# 시급 얼마인지 입력받자
# 주 15시간 이상이면, 주휴수당 지급
# 주휴수당: 주 5일 근무로 생각하고 1일치 더줌
#1
week_time = input("일주일에 몇시간 일해?")   #workinghour_per_week
week_time = int(week_time)
how_long = input("몇 주 일해?")
how_long = int(how_long)
how_much = input("시급 얼마야?")
how_much = int(how_much)
#2주휴수당 계산
if week_time >= 15:
    week_time += (week_time/5)
#3
salary = int(week_time) * int(how_long) * int(how_much)
print("알바비는", salary)