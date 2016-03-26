def additionMenu():
	print("Addition Menu")

def subtractionMenu():
	print("Subtraction Menu")

def multiplicationMenu():
	print("Multiplication Menu")

def mainMenuOptions(selection):
	argumentOptions = {
		"1":additionMenu,
		"2":subtractionMenu,
		"3":multiplicationMenu
	}

	func = argumentOptions.get(selection, lambda: print("Incorrect Selection"))
	return func()

def terminalMenu():
	# Let's poll the user for how they would like to create the worksheet
	print("Hello, and welcome to the worksheet generator program.")
	print("Please select from the following options.  Enter \"exit\" to terminate the program")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	while True:
		response = input("Please choose a number from the options: ")
		mainMenuOptions(response)
		#print(response)
		if(response == "exit"):
			print("Thank you for using the worksheet program!  See you again next time.")
			break

