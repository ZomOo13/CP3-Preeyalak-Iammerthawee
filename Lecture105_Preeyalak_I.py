class Vehicle:
    LCode =""
    SCode =""
    def airOn(self):
        print("Turn On : Air~")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1=Car()
car1.airOn()

pickUp1=PickUp()
pickUp1.airOn()

van1=Van()
van1.airOn()

estateCar1=EstateCar()
estateCar1.airOn()
