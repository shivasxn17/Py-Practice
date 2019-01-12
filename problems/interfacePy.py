from abc import ABCMeta,abstractmethod

# its a interface cant be instatiated only implemented
class Shape(object):
	"""interface for Shape"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Rectangle(Shape):
	"""derived class for Rectangle"""
	def __init__(self, width,height):
		self.width = width
		self.height = height
		super(Rectangle,self).__init__()

	def area(self):
		return self.width + self.height

	def perimeter(self):
		return self.width * 2 + self.height * 2		

rect = Rectangle(10, 20)
print(rect.area())	
print(rect.perimeter())	