class Engine: # Component Class
    def start(self):
        print("Engine Start....")
    def stop(self):
        print("Engine Stop...")
class Car: # Composit Class
    def __init__(self):
        self.__e=Engine()
    def car_start(self):
        self.__e.start()
    def car_stop(self):
        self.__e.stop()

audi=Car()
audi.car_start()
audi.car_stop()



# In composition the lifetime of component object is until composite object is exists. Once composite object is deleted it also deletes component object. 