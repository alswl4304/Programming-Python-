class car:
    count=0
    @classmethod
    def get_count(cls):  
        return cls.count

    def __init__(self,type,speed):
        self.type=type
        self.speed = speed
        car.count += 1

    def move(self):
            print(self.type+"가"+str(self.speed)+"속도로 움직입니다.")

    def speed_up(self,amount):
            self.speed += amount

    def speed_down(self,amount):
            self.speed -= amount


print(car.get_count())
c1= car("스포츠카",100)
c2=car("트럭",50)
c3 = car("재규어",300)
print(car.get_count())