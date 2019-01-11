class Person(initialAge):
	"""docstring for Person"""
	def __init__(self, initialAge):
		super(Person, self).__init__()
		if initialAge >= 0:
			self.age = initialAge
		else:
			print("Age is not valid, setting age to 0.")
			self.age = 0
		
	def yearPasses():
		self.age += 1

	def amIOld():
		if self.age < 13:
			print("You are young.")
		elif self.age < 18:
			print("You are a teenager.")
		else:	
			print("You are old.")