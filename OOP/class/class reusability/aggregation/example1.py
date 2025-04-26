class Sim:
    def connect(self):
        print("Connect to network")

class Mobile:
    def __init__(self,s):
        self.__sim=s
        self.__sim.connect()
    def set_sim(self,s):
        self.__sim=s
        self.__sim.connect()

airtel=Sim()
bsnl=Sim()
mobile1=Mobile(airtel)
mobile1.set_sim(bsnl)
mobile1.set_sim(airtel)