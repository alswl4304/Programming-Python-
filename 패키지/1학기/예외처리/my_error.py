#219
#class MyError(Exception):
#   pass

class OddError(Exception):
    def __init__(self, message= "홀수는 ㄴㄴ"):
        self.message = message

    def __str__(self):
        return  self.message

n =11
try:
    if n % 2 != 0:      #홀수
        raise OddError
    else:               #짝수
        print(n, ", n/2=",n/2)
except OddError as e:
    print("에러발생", e)

