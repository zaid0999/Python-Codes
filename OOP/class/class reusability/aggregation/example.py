class Engine: # Component Class
    def start(self):
        print("Engine Start...")
    def stop(self):
        print("Engine Stop...")

class Car: # Composit Class
    def __init__(self,eng):
        self.__e=eng
    def car_start(self):
        self.__e.start()
    def car_stop(self):
        self.__e.stop()

audi_eng=Engine()
audi=Car(audi_eng)
audi.car_start()
audi.car_stop()