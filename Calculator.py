#Create a menu function that lists the modes in the calculator
def menu():
  mode = input("""Choose a mode by entering the number:
              "1: Addition
              "2: Subtraction
              "3: Multiplication
              "4: Division
              "5: Powers
              "6: Exit""").strip()
  return mode
  
#Addition function
def add(number1, number2):
  answer = number1 + number2
  return answer

#Subtraction function
def subtract(number1, number2):
  answer = number1 - number2
  return answer

#Multiplication function
def multiply(number1, number2):
  answer = number1 * number2
  return answer

#Division Function
def divide(number1, number2):
  answer = number1 / number2
  return answer

#Powers function
def powers(number1, number2):
  answer = number1 ** number2
  return answer
  
#Main program loop
while True:
  
  #Print menu and get user's mode choice
  mode  =menu()
  
  #Check it's a valid math option
  if mode in ["1", "2", "3", "4", "5"]:
    
    #Ask user for numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    #Do chosen math with numbers
    
    
  #Break out of loop if exit is chosen
  elif mode == "6":
    break
    
  #Otherwise, tell the user that wasn't an option
  else:
    print("Oops, that wasn't an option, try again!")

#Farewell the user when they exit
  if mode == "1":
    solution = add(num1, num2)
    print(solution)
  elif mode == "2":
    solution = subtract(num1, num2)
    print("{} - {} = {}".format(num1, num2, solution))
  elif mode == "3":
    solution = multiply(num1, num2)
    print("{} x {} = {}".format(num1, num2, solution))
  elif mode == "4":
    solution = divide(num1, num2)
    print("{} / {} = {}".format(num1, num2, solution))
  elif mode == "5":
    solution = powers(num1, num2)
    print("{} ^ {} = {}".format(num1, num2, solution))
  
  elif mode == "6":
    break
  
  else:
    print("Oops, that wasn't an option, try again!")
    
print("Goodbye!")