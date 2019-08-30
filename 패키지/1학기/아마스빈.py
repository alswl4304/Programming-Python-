#아마스빈앱
#Drink<-Coffe
#  <-Bubbletea
#Order
#메뉴 보여주자
#음료 주문하자
#주문한 음료 보여주자
#총 금액 계산하자
class Drink:
    _cups = ["레귤러","점보"]
    _ices = ["0%","50%","100%","150%"]
    _sugars = ["0%","50%","100%","150%"]

    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.cup=0      #기본값 초기화 
        self.ice=2
        self.sugar=2
        
    def __str__(self):
        return "이름: "+self.name+"\t가격: "+str(self.price)+"원 \t컵:"+Drink._cups[self.cup]\
            +"\t얼음량: "+Drink._ices[self.ice]+"\t 당도: "+Drink._sugars[self.sugar]

    def set_cup(self):
        self.cup=input("컵을 선택하세요(0: 레귤러, 1:점보) ")
        if self.cup=="":  #사용자가 엔터만 치면 기본값 0을 넣자
            self.cup=0
        else:
            self.cup=int(self.cup)  #숫자로 저장하기 위해서 
        #점보면 300원 추가
        if self.cup == 1:
            self.price += 300


    def set_ice(self):
        self.ice=input("얼음량을 선택하세요.(0:0%, 1:50%, 2:100%, 3:150%) ")
        if self.ice=="":
            self.ice=2
        else:
            self.ice=int(self.ice)

    def set_suger(self):
        self.suger=input("당도를 선택하세요. (0:0%, 1:50%, 2:100%, 3:150%)")
        if self.suger=="":
            self.suger=2
        else:
            self.suger=int(self.suger)


    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_suger()


class Coffe(Drink):   #상속
    pass


class Bubbletea(Drink):
    _pearls = ["타피오카","코코","잴리","알로에"]

    def __init__(self, name, price):
         super().__init__(name, price)
         self.pearl = 0

    def set_pearl(self):
        self.pearl=input("펄을 선택하세요(0:타피오카, 1:코코펄, 2:젤리, 3:알로에)")
        if self.pearl=="":
            self.pearl=0
        else:
            self.pearl=int(self.pearl)

    def __str__(self):
        return super().__str__() + "\t펄: "+Bubbletea._pearls[self.pearl]


    def order(self):
        super().order()
        self.set_pearl()

class Order:
    _menus=[Coffe("아메리노",1800),Bubbletea("딸기요거트",3500)]

    def __init__(self):
        self.order_menu = []
        self.order=None

    def show_menu(self):
        print("0:아메리카노 1800원, 1:딸기요거트 3500원")

    def sum_price(self):
        for drink in self.order_menu:
            sum += drink.price

        return sum

    def order_drink(self):
        #반복↓
        while True:
            #메뉴 보여주자
            self.show_menu()
            #주문받자
            #음료를 선택하자
            self.order = input("음료를 선택하세요: ")
            # 음료 객체 생성하자
            if self.order == "":
                break
            drink = Order._menus[int(self.order)]
            #음료 옵션 정하자
            drink.order()
            # 주문한 음료 리스트에 추가하자
            self.order_menu.append(drink)
            #반복↑
        #주문한 음료 출력하자
        for drink in self.order_menu:
            print(drink)
        #금액 합계 구하자
        print("총금액: "+str(self.sum_price())+"원입니다.")
            
o = Order()
o.order_drink()

#아메리카노 = Coffe("아메리카노",1800)   #이름: 아메리카노\t가격:1800
#아메리카노.order()

#print(아메리카노)  #<__main__.Drink object at 0x0000016227A4BDA0>에러는 def함수 안만들어서 생김 
#타로밀크티=Bubbletea("타로밀크티",3500)
#타로밀크티.order()
#print(타로밀크티)