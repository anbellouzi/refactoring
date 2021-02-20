# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

# captures user input and total
def get_user_input(num_students):
    grade_list = []
    total = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    # Get the inputs from the user
    for _ in range(0, num_students):
        user_input = int(input('Enter a number: '))
        grade_list.append(user_input)
        total += user_input
        
    return grade_list, total

# calculates standard deviation
def get_standard_deviation(grade_list, mean):
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
        
    return math.sqrt(sum_of_sqrs / len(grade_list))

def print_stat():
    # returns user input and total sum
    grade_list, total = get_user_input(5)
    # Calculate the mean and standard deviation of the grades
    mean = total / len(grade_list)
    # returns calculated sd
    sd = get_standard_deviation(grade_list, mean)
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

print_stat()