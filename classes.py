import random
import math

class Util:
	def generateTuple(self, length, minValue, maxValue, forceInteger = True):
		if(forceInteger == True):
			# We want to return integers.  Add the math.floor option.
			result = tuple(math.floor(random.uniform(minValue, maxValue)) for x in range(length))
		else:
			# don't need integer values.  Remove the floor option
			result = tuple(random.uniform(minValue, maxValue) for x in range(length))
			
		return result

	def calculateSum(self, operands):
		base = 0
		for operand in operands:
			base += operand
		return base
		
	def calculateDifference(self, operands):
		base = 0
		for operand in operands:
			base -= operand
		return base
			

	def calculateProduct(self, operands):
		base = 1
		for operand in operands:
			base *= operand
		return base

	def calculateQuotient(self, operands):
		### NOT WORKING PROPERLY ###
		base = 1
		for operand in operands:
			base = base/operand
		return base

class Menu:
	def additionMenu(self):
		print("Addition Menu")

	def subtractionMenu(self):
		print("Subtraction Menu")
	
	def multiplicationMenu(self):
		print("Multiplication Menu")

	def mainMenuOptions(self, selection):
		argumentOptions = {
			"1":self.additionMenu,
			"2":self.subtractionMenu,
			"3":self.multiplicationMenu
		}

		func = argumentOptions.get(selection, lambda: print("Incorrect Selection"))
		return func()

	def terminalMenu(self):
		# Let's poll the user for how they would like to create the worksheet
		print("Hello, and welcome to the worksheet generator program.")
		print("Please select from the following options.  Enter \"exit\" to terminate the program")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		while True:
			response = input("Please choose a number from the options: ")
			self.mainMenuOptions(response)
			#print(response)
			if(response == "exit"):
				print("Thank you for using the worksheet program!  See you again next time.")
				break

class Exercise:
	def calculateResult(self):
		pass

class Addition(Exercise):
	def __init__(self, numberOfOperands=5, minValue=0, maxValue=12):
		self.util = Util()
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.operands = self.util.generateTuple(numberOfOperands, minValue, maxValue)

		# Then we will calculate the answer
		self.calculateResult()

	def calculateResult(self):
		self.answer = self.util.calculateSum(self.operands)

class Subtraction(Exercise):
	def __init__(self, numberOfOperands=5, minValue=0, maxValue=12):
		self.util = Util()
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.operands = self.util.generateTuple(numberOfOperands, minValue, maxValue)

		# Then we will calculate the answer
		self.calculateResult()

	def calculateResult(self):
		self.answer = self.util.calculateDifference(self.operands)

class Multiplication(Exercise):
	def __init__(self, numberOfOperands=4, minValue=1, maxValue=3):
		self.util = Util()
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.operands = self.util.generateTuple(numberOfOperands, minValue, maxValue)

		# Then we will calculate the answer
		self.calculateResult()

	def calculateResult(self):
		self.answer = self.util.calculateProduct(self.operands)

class Worksheet:
	menu = Menu()
	def __init__(self):
		self.menu.terminalMenu()


if __name__ == '__main__':

	worksheet = Worksheet()

'''
	addition = Addition()
	print(addition.__dict__)

	subtraction = Subtraction()
	print(subtraction.__dict__)

	multiplication = Multiplication()
	print(multiplication.__dict__)
'''
