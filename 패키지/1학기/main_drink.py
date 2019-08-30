#from foods.drink import milk
#milk.drink()

#from foods.drink.milk import drink
#drink()

from foods.drink.milk import drink
drink()

#import foods.drink.milk
#foods.drink.milk.drink()

#import foods.drink.milk
#foods.drink.milk.drink()

#foods.drink.milk.drink() #error

#from: 폴더 or 모듈
#import: 모듈 or 함수

from foods.drink import milk as m
m.drink()