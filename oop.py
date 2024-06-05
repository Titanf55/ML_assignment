class Car:
    def __init__(self, make, model, year):
        self._make = make  # private attribute
        self._model = model  # private attribute
        self._year = year  # private attribute
    
    def get_make(self):
        return self._make
    
    def set_make(self, make):
        self._make = make
    
    def get_model(self):
        return self._model
    
    def set_model(self, model):
        self._model = model
    
    def get_year(self):
        return self._year
    
    def set_year(self, year):
        if year > 0:  # additional validation
            self._year = year
        else:
            print("Invalid year.")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accessing private attributes using getter methods
print("Make:", my_car.get_make())  # Output: Make: Toyota
print("Model:", my_car.get_model())  # Output: Model: Camry
print("Year:", my_car.get_year())  # Output: Year: 2020

# Modifying private attributes using setter methods
my_car.set_year(2019)
print("Year:", my_car.get_year())  # Output: Year: 2019

# Trying to modify private attributes directly (which is discouraged)
my_car._year = -1  # This bypasses the encapsulation
print("Year:", my_car.get_year())  # Output: Year: -1 (which is incorrect)
