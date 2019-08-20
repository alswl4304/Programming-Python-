# input("현재의 input() 함수는 사용자 정의 함수입니다.")

# def input(s):
#     print(s)

# input("현재의 input() 함수는 사용자 정의 함수입니다.")

# import random

# #n = random.rendrange(1,6+1)
# def rolling_dice():
#     n = random.randint(1,6)
#     print("결과 :",n)

# rolling_dice()
# rolling_dice()
# rolling_dice()

# #star함수 정의
# def star():
#     print("****")
    
# star()
# star()
# star()

# #def rolling_dice(pip):
#  #   n = random.randint(1, pip)
#    # print(pip,"면 주사위 굴린 결과 : ",n)

#   # rolling_dice()

# #     def rolling_dice(pip,repeat):
# #         for r in range(1, repeat+1):
# #             n + random.randint(1,pip)
# #             print(pip,"면 주사위 굴린 결과",r," : ",n)

# # rolling_dice(6,1)
# # rolling_dice(6,2)
# # rolling_dice(12,0)
# # rolling_dice(20,-3)

# #가변인수
# print("가변인수---------------")
# print("♡")
# print("♡","♪")
# print("♡","♪","♣")
# print("♡","♪","♣","♠")
# print("♡","♪","♣","♠","★")

# def p(*args):
#     string =""
#     for a in args:
#         string+=a
#     print(string)
#     p("♡")
#     p("♡","♪")
#     p("♡","♪","♣","♥")

#     #안녕 ()함수를 만들고,
#     def 안녕(*args):
#         for a in args:
#             print("안녕,",a)

#     안녕("가연아","수빈아","정윤아","채린아")
#     #안녕, 가연아
#     #안녕, 수빈아
#     #안녕, 정윤아

#     def p (space, space_num, *args):
#     #def p(*args,space. space_num):  *args는 앞에 있을 수 없음
#         string =  args[0]
#         for i in range (1, len(args)):
#             string +=(space * space_num)+ args[i]
#             print(string)

# p(",",3,"♥","♪")
# p("★",2,"♥","♪","♣")
# p("_",3,"♥","♪","♣","♠")

# #p.115 혼자해보기
# def star(word,*args):
#     for i in args:
#         print(word*i)

#     star("♬",3)
#     star("♡",1,2,3)

#     #p.116 키워드 인자를 사용한 함수
#     def fn(a,b,c,d,e):
#         print(a,b,c,d,e)
    
#     fn(1,2,3,4,5)
#     fn(10,20,30,40,50)
#     fn(5,6,7,8,9)
#     fn(a=1,b=2,c=3,d=4,e=5)
#     fn(a=5,b=4,c=3,d=2,e=1)
#     fn(1,2,c=3,d=4,e=5)

# def fn(a,b,c,*d)
#     print(a,b,c,d)

# fn(c=3,b=2,a=1,4,5) #에러
# fn(1,2,,c=3,4,5) #에러
# fn(4,5,a=1,b=2,c=3) #에러

#p118 혼자해보기
# def star (mark,repeat,space,space_repeat,line):
#     for i in range(1.line):
#         String= (mark*repeat)
#     for j in range(2,repeat):
#         String +=(space*space_repeat)+(mark*repeat)
#          print(String)

# star("*",2,"+",3,5)
# print("------------------------------")
# star(mark="*",repeat=2,space="+",space_repeat=3,line=5)

# def star2(mark,repeat,space,space_repeat,line):
#     string=(mark*repeat)+(space*space_repeat)+(mark*repeat)
#     for n in range(line):
#         print(string)

# star("x",3,"_",2,3)
# print("------------------------------")
# star(mark="x", repeat=3, space="_", space_repeat=2, line=3)

#119
def hello(msg="안녕하세요"):
     print(msg + "!")

hello("오랜만이에요")
hello("이영희")
hello()

def hello2 (name="무명", msg="안녕하세요"):
    print(name+"님,"+msg+"!")

hello2("김철수","오랜만이에요")
hello2()
hello2("김민지")

def hello3(name,msg="안녕하세요"):
    print(name+"님, "+msg+"!")

hello3("김봄이","오랫만이에요")
hello3("김소현")
#hello3()  #error name을 줘야한다

def fn2(a, b=[]):
        b.append(a)
        print(b)

fn2(3)
fn2(5)
fn2(10)

def gugudan(dan):
    for i in range(1,9+1):
       # print(str(dan)+"*"+str(i)+"=",i*dan)
       print("{} X {} = {}".format(dan,i,dan*i))
       print()
 

    

gugudan(3)
gugudan(2)

#125
def sum(*numbers):
    sum_value=0
    for number in numbers:
        sum_value=sum_value+number
    return sum_value

result = sum(1,3)
print("1+3=",result)
print("1+3+5+7=",sum(1,3,5,7))

#126
def min(*numbers):
    min_value=numbers[0]
    for number in numbers:
        if min_value > number:
            min_value=number

        return min_value

print("min(1,3)=",min (1,3))
print("min(0,3,-11)=",min (0,3,-11))

#127
def multi_num(multi,start,end):
    result=[]
    for n in range(start,end):
        if n % multi == 0:
            result.append(n)
    return result
multi2 = multi_num(17,1,200)
print("multi_num(17,1,200) : ", multi2)
print()
multi3=multi_num(3,1,100)
print("multi_num(3,1,100) :",multi3)

#128
def min_max(*args):
    min=args[0]
    max=args[0]
    for arg in args:
        if min>arg:
            min=arg
        if max<arg:
            max=arg
    return min,max

print(min_max(52,-3,23,89,-21))
min_value,max_value=min_max(52,-3,23,89,-21)
print("최저값:",min_value)
print("최고값:",max_value)