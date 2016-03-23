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
		base = 1
		for operand in operands:
			base = base/operand
		return base

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

if __name__ == '__main__':
	addition = Addition()
	print(addition.__dict__)

	subtraction = Subtraction()
	print(subtraction.__dict__)
