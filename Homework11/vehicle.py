class Vehicle:
    def __init__(self, make, year, color, mileage):
        self.make = make
        self.year = year
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"Make: {self.make}, Year: {self.year}, Color: {self.color}, Mileage: {self.mileage} miles"
