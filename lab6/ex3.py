class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The mileage of the car is {self.mileage} miles per gallon."


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The mileage of the motorcycle is {self.mileage} miles per gallon."


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"The towing capacity of the truck is {self.towing_capacity} pounds."


car = Car(make="Toyota", model="Camry", year=2022, mileage=30)
print(car.display_info())
print(car.calculate_mileage())

motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2022, mileage=45)
print(motorcycle.display_info())
print(motorcycle.calculate_mileage())

truck = Truck(make="Ford", model="F-150", year=2022, towing_capacity=8000)
print(truck.display_info())
print(truck.calculate_towing_capacity())
