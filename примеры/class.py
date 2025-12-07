class Car: 

    def __init__(self,wheels,fuel,horsepower,name,color):
       self.__wheels=wheels
       self.fuel=fuel
       self.horsepower=horsepower
       self.name=name
       self.color=color

    def setWheels(self,wheels):
        if type(wheels) !=int or wheels>0:
            return
        self.wheels=wheels
# Если колёса неверные (меньше ноля или не число), то он не меняет значение
    def print(self):
        print('Name=',self.name)
    def __str__(self):
        return "Name="+self.name
    def __lt__(self,other):
        return self.horsepower < other.horsepower
zhenyas_car=Car(4,'petrol',100,'Zhenya\'s car','blue')
valentinas_car=Car(4,'petrol',50,'Zaporozhets','red')
print(zhenyas_car.fuel)
print(zhenyas_car)
print(valentinas_car < zhenyas_car)