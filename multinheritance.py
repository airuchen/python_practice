class Vehicle:
    def __init__(self,name,engine):
        self.__name = name
        self.__engine = engine

    def getName(self):
        return self.__name

    def getEngine(self):
        return self.__engine

class Electric:
    def __init__(self, Powerelectric):
        self.__powerelectric = Powerelectric

    def getPower(self):
        return self.__powerelectric

    def setPower(self,Powerelectric):
        self.__powerelectric = Powerelectric

class Car(Vehicle,Electric):
    def __init__(self,name,engine,Powerelectric,auto):
        Vehicle.__init__(self,name,engine)
        self.setPower(Powerelectric)
        self.__Auto = auto

    def getCarName(self):
        print('nameeee'+self.getName())
        print('engine'+self.getEngine())
        print('electric'+self.getPower())

    def getAuto(self):
        return self.__Auto

mycar = Car('Tesla','ele_engine','ele','autopilot')
mycar.getCarName()
print(mycar.getAuto())
