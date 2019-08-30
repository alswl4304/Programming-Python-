#2402_곽가연
# 맛있는 피자를 주문하기 위한 프로그램 이다.

class Pizza:
    #피자 크기 정하기위해
    _sizes = ["M","L","S"]  


    def __init__(self,name,price):      #기본값 초기화 
        self.name=name
        self.price=price
        self.size=0      

        # 출력하는 문
    def __str__(self):
        return "이름: "+self.name+"\t가격: "+str(self.price)+"원 \t사이즈:"+Pizza._sizes[self.size]
#사이즈 선택하기
    def set_size(self):
        self.size=input("사이즈를 선택하세요(0: M, 1:L , 2:S) ")
        if self.size=="":  
            self.size=0
        else:
            self.size=int(self.size)  #숫자로 저장하는것
                            #사이즈가 S면 500원 빼고 L은 500원추가            
        if self.size == 1:
            self.price += 500
        if self.size == 2:
            self.price -= 500


    def order(self):
        self.set_size()


#피자 토핑 
class pizzass(Pizza):
    _topping = ["케이준 새우살","파인애플", "버섯"," 불고기" ," 옥수수", "올리브", "베이컨" ," 양파" , "페퍼로니" , "피망" ,"햄"]

    def __init__(self, name, price):
         super().__init__(name, price)
         self.topping = 0
# 토핑 보여주기
    def set_topping(self): 
        self.topping=input("토핑 선택하세요(0:케이준 새우살, 1:파인애플, 2:버섯, 3:불고기 , 4:옥수수, 5:올리브, 6:베이컨 , 7:양파 , 8:페퍼로니 , 9:피망 , 10 : 햄)")
        if self.topping=="":
            self.topping=0
        else:
            self.topping=int(self.topping)

    def __str__(self):
        return super().__str__() + "\t토핑: "+pizzass._topping[self.topping]


    def order(self):
        super().order()
        self.set_topping()
#피자 메뉴 OR 가격
class Order:
    _menus=[pizzass("불고기피자",7000),pizzass("치즈피자",6000),pizzass("콤보피자",6000),pizzass("고구마",7000),pizzass("하와이안피자",8000),pizzass("포테이토피자",7000),pizzass("베이컨체더피자",8000),pizzass("슈프림피자",8000)]

    def __init__(self):
        self.order_menu = []
        self.order=None

    def show_menu(self): # 피자메뉴 보여주기
        print("0:불고기피자 7000원, 1:치즈피자 6000원,2:콤보피자 6000원,3:고구마 7000원,4:하와이안피자 8000원,5:포테이토피자 7000원,6:베이컨체더피자 8000원,7:슈프림피자 8000원")

# 가격 계산
    def sum_price(self):
        sum = 0
        for i in self.order_menu:
            sum += i.price

        return sum

    def order_Pizza(self):
        #반복↓
        while True:
            #메뉴 보여주자
            self.show_menu()
            #주문받자
            
            #피자를 선택
            self.order = input("피자를 선택하세요: ")
            # 피자 객체 생성
            if self.order == "":
                break
            Pizza = Order._menus[int(self.order)-1]
            Pizza.order()
            # 주문한 피자 리스트에 추가
            self.order_menu.append(Pizza)
            ans = input("추가 주문 하시겠습니까?(y/n)")
            if ans!="y":
                break
          
        #주문한 피자 출력
        for Pizza in self.order_menu:
            print(Pizza)
            #금액 합계 구하기
        
        print("총금액: "+str(self.sum_price())+"원입니다.")

          

        while True :
            address = input("배달받으실 주소를 입력해주세요 : ")
            if address=="":
                print("다시 입력해주세요.")
            else : break
            
        print(address, "(으)로 배달을 시작합니다.")

#함수 호출
o = Order()
o.order_Pizza()