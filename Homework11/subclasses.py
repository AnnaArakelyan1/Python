from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, year, color, mileage, num_doors, fuel_type):
        super().__init__(make, year, color, mileage)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def __str__(self):
        return f"{super().__str__()}, Number of Doors: {self.num_doors}, Fuel Type: {self.fuel_type}"


class RaceCar(Car):
    def __init__(self, make, year, color, mileage, num_doors, fuel_type, top_speed):
        super().__init__(make, year, color, mileage, num_doors, fuel_type)
        self.top_speed = top_speed

    def __str__(self):
        return f"{super().__str__()}, Top Speed: {self.top_speed} mph"


class Plane(Vehicle):
    def __init__(self, make, year, color, mileage, max_altitude):
        super().__init__(make, year, color, mileage)
        self.max_altitude = max_altitude

    def __str__(self):
        return f"{super().__str__()}, Max Altitude: {self.max_altitude} feet"


class Boat(Vehicle):
    def __init__(self, make, year, color, mileage, max_speed):
        super().__init__(make, year, color, mileage)
        self.max_speed = max_speed

    def __str__(self):
        return f"{super().__str__()}, Max Speed: {self.max_speed} knots"


car = Car("Toyota", 2020, "Blue", 15000, 4, "Gasoline")
plane = Plane("Boeing", 2018, "White", 5000, 35000)
boat = Boat("Yamaha", 2021, "Red", 200, 45)
racecar = RaceCar("Ferrari", 2022, "Red", 2000, 2, "Gasoline", 211)


print("Car: ",car)
print("Plane: ",plane)
print("Boat: ",boat)
print("Racecar: ",racecar)
