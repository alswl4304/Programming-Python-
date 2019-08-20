class DeletableClass:
    def __del__(self):
        print("delete")

d = DeletableClass()
del d


#p.203
class Person:
    def __init__(self, name, age, height):
        self.name =  name
        self.age = age
        self.height = height

    def __str__(self):
        return "Person 설명, 이름은 "+ self.name+"키는" +str(self.height)

    def __len__(self):
        return self.height

    def __getitem__ (self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None


p = Person("철수",18 ,170)
print(len(p))
print(p['age'])
print(p['weight'])

del p
print(p)
p = Person("철수",18,189)