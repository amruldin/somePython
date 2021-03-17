# Author : 
# Date   : 
# Description

#Psudocode 
# Ask user to Enter their height in inches
# Ask User to Enter their weight in pounds
# Compute the BMI as ((weight/height^2)*703)
# Print BMI to the user


# def prompt and getIntInput -> int
# Def computeBMI , takes weight and height as argements and returns BMI
# Def Main calls the functions above to ask the user for height and weight, compute the BMI and print it out


# Write test case below each function
# Write header comments for each function



"""
    The following function will take input as a float value from the user and then return it back.
    You could also take an integer however float would more accurate
"""
def getIntInput(prompt):
    # get user input
    return float(input(prompt))

"""
    The following function will compute the body mass index and then return the result as an integer
"""

def computeBMI(weight, height):
    return int(((weight/(height*height)*703)))
    

def main():
    # Call getIntInput to prompt and store users height
    height = getIntInput("\nPlease Enter Your Height In Inches : ")


    # Call getIntInput to prompt and store users weight
    weight = getIntInput("\nPlease Enter your Weight In Pounds : ")

    # Call computeBMI function to calculate and store BMI
    userBMI = computeBMI(weight, height)
    print("\nYour BMI is : " + str(userBMI))

main()


"""
Some test scenario are as following

    Please Enter Your Height In Inches : 65
    Please Enter your Weight In Pounds : 230
    Your BMI is : 38

    Please Enter Your Height In Inches : 55.5
    Please Enter your Weight In Pounds : 215.2
    Your BMI is : 49

    This program will only take float and integer values as input. All other types are invalid and will cause the program to crash!

"""
