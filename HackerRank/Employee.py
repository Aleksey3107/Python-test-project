class Employee:
	def __init__(self, name):
		self.name = name

	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 20.00


class PartTimeEmployee(Employee):
	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 12.00

	def full_time_wage(self, hours):
		return super(PartTimeEmployee, self).calculate_wage(hours)


web_developer_fulltime = Employee('Alex')
print(web_developer_fulltime.calculate_wage(10))

milton = PartTimeEmployee('Milton')
print(milton.full_time_wage(10))