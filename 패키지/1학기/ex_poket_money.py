#국어, 영어, 수학, 자바, 파이썬, JSP
#총점, 평점 구하기
#용돈구하기
k = input ("국어 점수는?")
m = input ("수학 점수는?")
e = input ("영어 점수는?")
j = input ("자바 점수는?")
p = input ("파이썬 점수는?")
js = input ("JSP 점수는?")
sum = int(k) + int(m) + int(e) + int(j) + int(p) + int(js)
print("총점은",sum)
avg = sum/6
print("평균은", round(avg,2))

#4
if avg >= 90:
    print("용돈 : 100000원")
elif avg >= 80:
    print("용돈 : 800000원")
elif avg >= 70:
    print("용돈 : 700000원")
elif avg >= 60:
    print("용돈 : 600000원")
else:
    print("용돈 : 500000원")