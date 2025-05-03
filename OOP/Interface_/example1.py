import abc

class Sim(abc.ABC): #(API)
    @abc.abstractmethod
    def connect(self):
        pass

class AirtelSim(Sim):
    def connect(self): #Overriding method
        print("connect to Airtel Network")

class BsnlSim(Sim):
    def connect(self): #Overriding method
        print("Connect to BSNL Network")

class JioSim(Sim):
    def connect(self): #Overriding method
        print("Connect to Jio Network")

class Mobile:
    def insert(self,s):
        s.connect()


sim1=AirtelSim()
sim2=BsnlSim()
sim3=JioSim()
mobile1=Mobile()
mobile1.insert(sim1)
mobile1.insert(sim2)
mobile1.insert(sim3)