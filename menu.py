import math
import os
import worksheet
import exercises

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
        "exerciseType":"addition",
        "action":"add",
        "numberOfQuestions": numberOfQuestions, 
        "numberOfOperands": numberOfOperands,
        "minValue":minValue,
        "maxValue":maxValue
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
        "exerciseType":"subtraction",
        "action":"add",
        "numberOfQuestions": numberOfQuestions, 
        "numberOfOperands": numberOfOperands,
        "minValue":minValue,
        "maxValue":maxValue
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
        "exerciseType":"multiplication",
        "action":"add",
        "numberOfQuestions": numberOfQuestions, 
        "numberOfOperands": numberOfOperands,
        "minValue":minValue,
        "maxValue":maxValue
    }

def mainMenuOptions(selection):
    argumentOptions = {
        "1":additionMenu,
        "2":subtractionMenu,
        "3":multiplicationMenu
    }

    func = argumentOptions.get(selection, lambda: {"status":"invalid"})
    return func()

def processMainMenuOption(menuResponse, worksheet):
    os.system('clear')
    if(menuResponse['status'] == 'exit'):
        #nothing to add
        print("Nothing to add")
    elif(menuResponse['status'] == 'invalid'):
        #nothing to add
        print("It appears you have entered an invalid response.")
    else:
        updateWorksheetResponse = updateWorksheet(menuResponse, worksheet)
        if(updateWorksheetResponse['status'] == "success"):
            print("Successfully updated the worksheet!")
        else:
            print("There were some errors")
        print("Add stuff to the worksheet")

def updateWorksheet(options, worksheet):
    updateOptions = {
        "addition":updateWorksheetAddition,
        "subtraction":updateWorksheetSubtraction,
        "multiplication":updateWorksheetMultiplication
    }

    func = updateOptions.get(options['exerciseType'], lambda: {"status":"invalid"})
    return func(options, worksheet)

def terminalMenu():
    # Let's create a worksheet opject for the menu to store information in.
    sheet = worksheet.Worksheet()
    os.system('clear')
    print("Hello, and welcome to the worksheet generator program.")
    while True:
        # Let's poll the user for how they would like to create the worksheet
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
            #print(menuResponse)
            processMainMenuOption(menuResponse, sheet)
        #os.system('clear')

def updateWorksheetAddition(options, worksheet):
    # we are assuming it is all adding at the moment
    # we will need to check later on for action

    print(options)
    print(type(worksheet.exercises))
    for i in range(options['numberOfQuestions']):
        worksheet.exercises.append(exercises.Addition(options['numberOfOperands'], options['minValue'], options['maxValue']))

    print(worksheet.exercises)
    for exercise in worksheet.exercises:
        print(exercise.__dict__)
    return {"status":"success"}

def updateWorksheetSubtraction(options, worksheet):
    for i in range(options['numberOfQuestions']):
        worksheet.exercises.append(exercises.Subtraction(options['numberOfOperands'], options['minValue'], options['maxValue']))

    print(worksheet.exercises)
    for exercise in worksheet.exercises:
        print(exercise.__dict__)
    return {"status":"success"}

def updateWorksheetMultiplication(options, worksheet):
    for i in range(options['numberOfQuestions']):
        worksheet.exercises.append(exercises.Multiplication(options['numberOfOperands'], options['minValue'], options['maxValue']))

    print(worksheet.exercises)
    for exercise in worksheet.exercises:
        print(exercise.__dict__)
    return {"status":"success"}
