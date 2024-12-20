# 1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"
def greet(name):
    print(f"Hello, {name}!")
greet("shivakumar") 
# 2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
def add_numbers(a, b):
    return a + b
    return a - b
    return a * b
    return a / b
    return a % b
sum = add_numbers (5,2)
print(sum)

# 3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def is_even(n):
    return n % 2 == 0
print(is_even(4))  # True
print(is_even(3))  # False
print(is_even(10))  # True
print(is_even(11))     # False

# 4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
"""def factorial(n):
    if n == 0 and n <= 1:  
        return 1
    else:
        return n * factorial(n - 1)
 
n = int(input("enter the nmber: "))
print(factorial(n))"""

# 5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
"""def find_max(n1, n2, n3):
    print(max(n1, n2, n3))

n1 = input("enter the first number: ")
n2 = input("enter the second number: ")
n3 = input("enter the third number: ")
find_max(n1, n2, n3)"""

# 6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
def count_vowels(s):

    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("hello"))

# 7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
print(is_prime(25))  # False
print(is_prime(23))  # True
print(is_prime(37))  # True
print(is_prime(48))  # False    

# 8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).
def recursive_sum(n):          # Base case: if n is 1, return 1
    if n == 1:
        return 1               # Recursive case: add n to the sum of numbers from 1 to n-1
    else:
        return n + recursive_sum(n-1)
    
# 9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.
def calculator(num1, num2, operator):
    """
    Performs a mathematical operation on two numbers based on the given operator.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operator (str): The mathematical operator (+, -, *, /).

    Returns:
        float: The result of the operation.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operator")

# Example usage:
print(calculator(10, 2, "+"))   # Output: 12
print(calculator(10, 2, "-"))      # Output: 8
print(calculator(10, 2, "*"))    # Output: 20
print(calculator(10, 2, "/"))  # Output: 5.0

# 10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print(common_elements)  # [4, 5]
print("-----------")

# 11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
def reverse_string(n):
    return n[::-1]
print(reverse_string("Shivakumar"))

# 12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.
def sort_dict_by_value(d): 
    return sorted(d.items(), key=lambda x: x[1]) 

print(sort_dict_by_value({'a': 3, 'b': 1, 'c': 2})) 
print(sort_dict_by_value({'x': 10, 'y': 30, 'z': 20})) 
print(sort_dict_by_value({'apple': 5, 'banana': 2, 'cherry': 8}))