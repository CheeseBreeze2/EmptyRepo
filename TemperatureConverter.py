#Temperature Converter, Script to convert temperature from Farenheit to Celsius or vice versa, Author: Isaac Martinec, Last Modified: 1/30/25, Choose your conversion then input a number and the script will convert it for you.
import pyinputplus as pyip
from colorama import Fore, Style, init

#Initialize Colorama and reset colors after it prints
init(autoreset=True)

#Welcome Message
print(Fore.BLUE + "Welcome to the Temperature Converter")

while True:
    #Celsius to Farenheit or Farenheit to Celsius?
    tempType = input(Fore.YELLOW + "Please select which conversion you would to perfrom 1. Celsius to Fahrenheit or 2. Fahrenheit to Celsius? Please type 1 or 2: ")

    #Number that will be converted
    number = pyip.inputFloat(Fore.YELLOW + "Please write the number you would like to convert: ")

    #If converting Celsius is chosen
    if tempType == '1':
        convertedTemp =  (number * 9/5) + 32
        print(Fore.GREEN + f"{number} is {convertedTemp} degrees Fahrenheit")
    #If converting Fahrenheit to chosen
    elif tempType == '2':
        convertedTemp = (number - 32) * 5/9
        print(Fore.GREEN + f"{number} is {convertedTemp} degrees Celsius")
    #If they put anything else in
    else:
        print(Fore.RED + "Not an option, try again.")
        continue

    continueChoice = input(Fore.YELLOW + 'Do you want to continue (y/n)? ')
    #Loop script if y
    if continueChoice.lower() != 'y':
        #End Script
        print(Fore.MAGENTA + "Goodbye")
        break
