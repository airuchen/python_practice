class Vehicle:
    def __init__(self,name,engine):
        self.__name = name
        self.__engine = engine

    def getName(self):
        return self.__name

    def getEngine(self):
        return self.__engine


class Car(Vehicle):
    def __init__(self,name,engine,electric):
        Vehicle.__init__(self,name,engine)
        self.__electric = electric

    def getCarName(self):
        print('name'+self.getName())
        print('engine'+self.getEngine())
        print('electric'+self.__electric)

    def getAuto(self):
        print('Auto pilote')

mycar = Car('Tesla','ele_engine','ele')
mycar.getCarName()
print(mycar.getAuto())
