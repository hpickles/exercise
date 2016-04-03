import math
import os

def additionMenu():
	os.system('clear')
	print("Welcome to the Addition Menu!")
	print("You will be asked a series of questions.  You can return to the main manu at any point by typing 'exit'")

	# input loop
	while True:
		numberOfQuestionsInput = input("Please choose the number of addition questions: ")
		if(numberOfQuestionsInput == 'exit'):
			return {"status":"exit"}
		try:
			numberOfQuestions = int(numberOfQuestionsInput)
			if(numberOfQuestions<1):
				raise ValueError
			break
		except ValueError as err:
			print("Please enter an integer greater than or equal 1")

	while True:
		numberOfOperandsInput = input("Please enter the number of operands for the addition the questions: ")
		if(numberOfOperandsInput == 'exit'):
			return {"status":"exit"}
		try:
			numberOfOperands = int(numberOfOperandsInput)
			if(numberOfOperands<2):
				raise ValueError
			break
		except ValueError as err:
			print("Please enter an integer greater than or equal 2")

	while True:
		minValueInput = input("Please enter the minimum value to use: ")
		if(minValueInput == 'exit'):
			return {"status":"exit"}
		try:
			minValue = float(minValueInput)
			break
		except ValueError as err:
			print("Please enter a valid number")

	while True:
		maxValueInput = input("Please enter the maximum value to use: ")
		if(maxValueInput == 'exit'):
			return {"status":"exit"}
		try:
			maxValue = float(maxValueInput)
			break
		except ValueError as err:
			print("Please enter a valid number")

	return {
		"status":"return",
		"numberOfQuestions": numberOfQuestions, 
		"numberOfOperands": numberOfOperands,
		"minValue":minValue,
		"maxvalue":maxValue
	}

def subtractionMenu():
	os.system('clear')
	print("Welcome to the Subtraction Menu!")
	print("You will be asked a series of questions.  You can return to the main manu at any point by typing 'exit'")

	# input loop
	while True:
		numberOfQuestionsInput = input("Please choose the number of subtraction questions: ")
		if(numberOfQuestionsInput == 'exit'):
			return {"status":"exit"}
		try:
			numberOfQuestions = int(numberOfQuestionsInput)
			if(numberOfQuestions<1):
				raise ValueError
			break
		except ValueError as err:
			print("Please enter an integer greater than or equal 1")

	while True:
		numberOfOperandsInput = input("Please enter the number of operands for the subtraction the questions: ")
		if(numberOfOperandsInput == 'exit'):
			return {"status":"exit"}
		try:
			numberOfOperands = int(numberOfOperandsInput)
			if(numberOfOperands<2):
				raise ValueError
			break
		except ValueError as err:
			print("Please enter an integer greater than or equal 2")

	while True:
		minValueInput = input("Please enter the minimum value to use: ")
		if(minValueInput == 'exit'):
			return {"status":"exit"}
		try:
			minValue = float(minValueInput)
			break
		except ValueError as err:
			print("Please enter a valid number")

	while True:
		maxValueInput = input("Please enter the maximum value to use: ")
		if(maxValueInput == 'exit'):
			return {"status":"exit"}
		try:
			maxValue = float(maxValueInput)
			break
		except ValueError as err:
			print("Please enter a valid number")

	return {
		"status":"return",
		"numberOfQuestions": numberOfQuestions, 
		"numberOfOperands": numberOfOperands,
		"minValue":minValue,
		"maxvalue":maxValue
	}

def multiplicationMenu():
	os.system('clear')
	print("Welcome to the Multiplication Menu!")
	print("You will be asked a series of questions.  You can return to the main manu at any point by typing 'exit'")

	# input loop
	while True:
		numberOfQuestionsInput = input("Please choose the number of multiplication questions: ")
		if(numberOfQuestionsInput == 'exit'):
			return {"status":"exit"}
		try:
			numberOfQuestions = int(numberOfQuestionsInput)
			if(numberOfQuestions<1):
				raise ValueError
			break
		except ValueError as err:
			print("Please enter an integer greater than or equal 1")

	while True:
		numberOfOperandsInput = input("Please enter the number of operands for the multiplication the questions: ")
		if(numberOfOperandsInput == 'exit'):
			return {"status":"exit"}
		try:
			numberOfOperands = int(numberOfOperandsInput)
			if(numberOfOperands<2):
				raise ValueError
			break
		except ValueError as err:
			print("Please enter an integer greater than or equal 2")

	while True:
		minValueInput = input("Please enter the minimum value to use: ")
		if(minValueInput == 'exit'):
			return {"status":"exit"}
		try:
			minValue = float(minValueInput)
			break
		except ValueError as err:
			print("Please enter a valid number")

	while True:
		maxValueInput = input("Please enter the maximum value to use: ")
		if(maxValueInput == 'exit'):
			return {"status":"exit"}
		try:
			maxValue = float(maxValueInput)
			break
		except ValueError as err:
			print("Please enter a valid number")

	return {
		"status":"return",
		"numberOfQuestions": numberOfQuestions, 
		"numberOfOperands": numberOfOperands,
		"minValue":minValue,
		"maxvalue":maxValue
	}

def mainMenuOptions(selection):
	argumentOptions = {
		"1":additionMenu,
		"2":subtractionMenu,
		"3":multiplicationMenu
	}

	func = argumentOptions.get(selection, lambda: print("Incorrect Selection"))
	return func()

def terminalMenu():
	while True:
		# Let's poll the user for how they would like to create the worksheet
		print("Hello, and welcome to the worksheet generator program.")
		print("Please select from the following options.  Enter \"exit\" to terminate the program")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		response = input("Please choose a number from the options: ")
		if(response == "exit"):
			print("Thank you for using the worksheet program!  See you again next time.")
			break
		else:
			menuResponse = mainMenuOptions(response)
			print(menuResponse)
		#os.system('clear')

