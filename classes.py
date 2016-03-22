import random
import math

class Exercise:
	pass


class Addition(Exercise):
	def __init__(self, numberOfOperands=5, minValue=0, maxValue=12):
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.generateQuestion()

	def generateQuestion(self):
		# We will generate a question based on the input parameters
		# First we will make an aray of the operands
		self.operands = tuple(math.floor(random.uniform(self.minValue, self.maxValue)) for x in range(self.numberOfOperands))

		# Then we will calculate the answer
		self.answer = sum(self.operands)


class Subtraction(Exercise):
	def __init__(self, numberOfOperands=5, minValue=0, maxValue=12):
		self.numberOfOperands = numberOfOperands
		self.minValue = minValue
		self.maxValue = maxValue
		self.generateQuestion()

	def generateQuestion(self):
		# We will generate a question based on the input parameters
		# First we will make an aray of the operands
		self.operands = tuple(math.floor(random.uniform(self.minValue, self.maxValue)) for x in range(self.numberOfOperands))

		# Then we will calculate the answer
		self.answer = sum(self.operands)

if __name__ == '__main__':
	exercise = Addition()
	print(exercise.__dict__)
