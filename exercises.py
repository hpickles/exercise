import util

class Exercise:
	def calculateResult(self):
		pass

class Addition(Exercise):
	def __init__(self, numberOfOperands=5, minValue=0, maxValue=12):
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.operands = util.generateTuple(numberOfOperands, minValue, maxValue)

		# Then we will calculate the answer
		self.calculateResult()

	def calculateResult(self):
		self.answer = util.calculateSum(self.operands)

class Subtraction(Exercise):
	def __init__(self, numberOfOperands=5, minValue=0, maxValue=12):
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.operands = util.generateTuple(numberOfOperands, minValue, maxValue)

		# Then we will calculate the answer
		self.calculateResult()

	def calculateResult(self):
		self.answer = util.calculateDifference(self.operands)

class Multiplication(Exercise):
	def __init__(self, numberOfOperands=4, minValue=1, maxValue=3):
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.operands = util.generateTuple(numberOfOperands, minValue, maxValue)

		# Then we will calculate the answer
		self.calculateResult()

	def calculateResult(self):
		self.answer = util.calculateProduct(self.operands)



