from drivers import Drivers
from city import City
from vehicle import Vehicle
from riders import Riders
from trips import Trips

class Uber:
    def __init__(self):
        self.driver = []
        self.rider = []
        self.trip = []
        self.cities = {"MIA": City("Miami", 6), "TMP" : City("Tampa", 4)}

    def getCityById(self, id):
        return self.cities[id]

    def addDriver(self, first_name, last_name, id, age, city, veh):
        self.driver.append(Drivers(first_name, last_name, id, age, city, veh))

    def addRider(self, first_name, last_name, id, age):
        self.driver.append(Riders(first_name, last_name, id, age))

    def createTrip(self, id_driver, id_rider, price, distance, city):
        self.trip.append(Trips(id_driver, id_rider, price, distance, city))
    
    def _findActivityDriverByCity(self, city):
        for driver in self.driver:
            if driver.active and driver.city == city:
                return driver
 
    def activateDriver(self, id_driver):
        for drvr in self.driver:
            if id_driver == drvr.id:
                drvr.working()

    def deactivateDriver(self, id_driver):
        for drvr in self.driver:
            if id_driver == drvr.id:
                drvr.notWorking()

    def tripsDriver(self, id_driver):
        trips_driver = []
        for trip in self.trip:
            if id_driver == trip.id:
                trips_driver.append(trip)
        
        return trips_driver

    def tripsRider(self, id_rider):
        trips_rider = []
        for trip in self.trip:
            if id_rider == trip.id:
                trips_rider.append(trip)
        
        return trips_rider

    def earning_driver(self, id_driver):
        earnings = 0
        for trip in self.trip:
            if id_driver == trip.id:
                earnings = trip.price * 0.75

        return earnings


app = Uber()
car = Vehicle("Volkswagen", "2015 CC", "AA23456", "White")
app.addDriver("Susana", "Reyes", 24, "TMP", car)
app.createTrip()
# TMP = City("Brandon", "4")
# MIA = City("Miami", "6")

# vehicle1 = Vehicle("Volkswagen", "2015 CC", "AA23456", "White")
# driver1 = Drivers("Susana", "Reyes", "24", TMP.name, vehicle1 )

# rider1 = Riders("Mila", "Rusia", "38", TMP.name)

# trip1 = Trips("20", "10 m")




# driver2 = Drivers("Pedro", "Avila", "25")
# driver3 = Drivers("Tico", "Reyes", "32")
# driver4 = Drivers("Alberto", "Perez", "40")
