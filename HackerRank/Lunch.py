class Lunch:
	def __init__(self, menu):
		self.menu = str(menu)

	def menu_price(self, menu):
		if menu[-1] == '1':
			print(f'Your choice: {menu} price 12.00')
		elif menu[-1] == '2':
			print(f'Your choice: {menu} price 13.40')
		else:
			print(f'Error in menu')


paul = Lunch("menu 1")
paul.menu_price(paul.menu)