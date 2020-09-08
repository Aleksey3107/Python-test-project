class Point3D:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return "(%d, %d, %d)" % (self.x, self.y, self.z)


mypoint = Point3D(1, 2, 3)
print(mypoint)