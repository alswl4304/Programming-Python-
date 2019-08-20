number = input("학번을 입력하시오 : ")

major = [["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
 ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
 ["인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]
]

grade = int(number[0])
classroom = int(number[1])
stuNum = int(number[2:])

print(grade, "학년", major[grade-1][(classroom-1)//2], classroom, "반", stuNum, "번입니다.")