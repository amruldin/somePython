# Function that takes two argument ratio and n and returns ration^0+ration^n



# the math library will help in calculating  an integer to the power of n
import math


# This function is used to get user input
def getUserInput(prompt):
    return int(input(prompt))


# This function is used to calculate and return the gemeteric sum
def geometricsum(ration,n):

    sum = 0         #  This the running total of the geometric sum

    # This for loop will calculate geometric value and add it the the sum
    for i in range(0,n+1):
        sum += math.pow(ration,i)

    # Finally we will return the sum value
    return sum

# The main function will call the get user input function and geometric sum function and then print the sum to the user
def main():

    # get user ration value
    ratio = getUserInput('Please enter the ration value : ')

    # get n value 
    n = getUserInput('Please enter the n value : ')

    # call geometricsum for calculation
    geometricSumResult = geometricsum(ratio,n)

    # Print the result to the user
    print("The Geomertic sum is : " + str(geometricSumResult))
    

# call main function to run the program
main()
