import math
import random

def generateTuple(length, minValue, maxValue, forceInteger = True):
	if(forceInteger == True):
		# We want to return integers.  Add the math.floor option.
		result = tuple(math.floor(random.uniform(minValue, maxValue)) for x in range(length))
	else:
		# don't need integer values.  Remove the floor option
		result = tuple(random.uniform(minValue, maxValue) for x in range(length))
		
	return result

def calculateSum(operands):
	base = 0
	for operand in operands:
		base += operand
	return base
	
def calculateDifference(operands):
	base = 0
	for operand in operands:
		base -= operand
	return base
		

def calculateProduct(operands):
	base = 1
	for operand in operands:
		base *= operand
	return base

def calculateQuotient(operands):
	### NOT WORKING PROPERLY ###
	base = 1
	for operand in operands:
		base = base/operand
	return base

