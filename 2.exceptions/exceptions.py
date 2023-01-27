import sys

def print_old(number):
    if (number < 0 or number > 100):
        raise ValueError("The number must be betwenn 0 and 100")
    else:
        return print("Your age is {0}".format(number))

try:
    entry = (int(input("Enter your age:")))
    print(print_old(entry))
except ValueError as ValueIsNotBetween:
    print("ValueIsNotBetween and shows the following error: {0}".format(ValueIsNotBetween))
except:
    print("Unexpected error:", sys.exc_info()[0])
finally:
    print("The program has finished")
