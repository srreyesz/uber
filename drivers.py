from vehicle import Vehicle

class Drivers:
    def __init__(self, first_name, last_name, id, age, city, veh):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age
        self.city = city
        self.veh = veh
        self.active = False

    def getVehicle(self):
        return self.veh

    def working(self):
        self.active = True

    def notWorking(self):
        self.active = False


