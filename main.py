def add_numbers(num1,num2):
    '''
    This function takes two numbers and returns their sum
    '''
    return num1 + num2


result = add_numbers(5,6)
print(result)


def is_even(num):
    '''
    This function takes a number and checks the number is even and returns true if the number divided by 2 has no remainder, otherwise return false
    '''
    return num % 2 == 0

example1 = is_even(4)
example2 = is_even(7)
print(example1)
print(example2)



def reverse_string(text):
    '''
    This function takes a string and returns the reversed version of the string
    '''
    return text[::-1]

result = reverse_string("hello")
print(result)


def count_vowels(text):
    '''
    This function counts the number of vowels of the inputted string
    '''
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

result = count_vowels("Hello World")
print(result)


def calculate_factorial(n):
    '''
    This function calculates the factorial of a non-negative integer
    The factorial of a number is the product of all positive integers less thab or equal to that number
    '''
    if n == 0 or n == 1:
        '''
        The factorial of 0 and 1 is 1
        '''
        return 1 
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

result = calculate_factorial(5)
print(result)


def apply_decorator(func):
    # This function takes another function as input and applies a decorator to it
    def decorator_func():
        # This is the decorator func that prints a message before calling the original func
        print("Decorator Applied")
        # call the original func
        func()
    return decorator_func

def say_hi():
    print("Hi!")

decorated_function = apply_decorator(say_hi)
decorated_function()

def sort_by_age(person_list):
    # This func takes a  list of tuples and sorts them in ascending order
    return sorted(person_list, key=lambda x: x[1])

people = [("James", 35), ("Mary", 22), ("Ian", 40) ]
sort_people = sort_by_age(people)
print(sort_people)

def merge_dicts(dict1, dict2):
    # This function merges two dicts. If there are common keys, their values are added up

    # Start with copy of the first dictionary
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            # Adds values for common keys
            merged_dict[key] += value
        else:
            # Add new key-value pairs
            merged_dict[key] = value
    return merged_dict

dict_a = {'a': 5, 'b': 3, 'c': 8}
dict_b = {'b': 2, 'c': 1, 'd': 4}

merged = merge_dicts(dict_a, dict_b)
print(merged)


class Car:
    def __init__(self, make, model, year):
        # Initialize the attributes of the Car class
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        # Method that prints car info
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


my_car = Car("Lamborghini", "Urus", 2018)
my_car.display_info()