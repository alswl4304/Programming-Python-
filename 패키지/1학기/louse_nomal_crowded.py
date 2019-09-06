# 버스 여유,보통,혼잡
# 탑승객, 하차객 입력받자
# 0이상 10미만: 여유
# 10이상 20미만: 보통
# 20 이상: 혼잡
#1
# -----
while True:
in0 = input("탑승객 수는?")
in0 = int(in0)
out = input("하차객 수는?")
out = int(out)
if in0 == -1:
    break
sum = in0 - out
# -----
print("버스에 있는 사람수는",sum)
if 0<= sum <10:
    print("여유")
if 0<= sum <20:
    print("보통")
if 0<= sum <30:
    print("혼잡")
