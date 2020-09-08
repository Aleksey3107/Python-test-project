class Car:
	condition = 'new'

	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg = mpg

	def __str__(self):
		return f'This is a {self.color} {self.model} with {self.mpg} MPG and its {self.condition}'

	def drive_car(self):
		self.condition = 'used'


class ElectricCar(Car):
	def __init__(self, model, color, mpg, battery_type):
		self.model = model
		self.color = color
		self.mpg = mpg
		self.battery_type = battery_type

	def drive_car(self):
		self.condition = 'like new'


my_car = Car('DeLorean', 'silver', 88)
print(my_car)
my_car.drive_car()
print(my_car)
tesla = ElectricCar('tesla', 'black', 140, 'electric')
print(tesla)
print(my_car.condition)
tesla.drive_car()
print(tesla.condition)