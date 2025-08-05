# In this file we will control the mathematical operations of this project.
import math

def add_num(*args):
    return sum(args)

def sub_num(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def mul_num(*args):
    result = 1
    for num in args:
        result *= num
    return result

def div_num(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Division by zero"
        result /= num
    return result

def mod_num(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Division by zero"
        result %= num
    return result

def pow_num(*args):
    result = args[0]
    for num in args[1:]:
        result **= num
    return result

def sqrt_num(a):
    if a < 0:
        return "Error: Square root of negative number"
    return a ** 0.5

def cube_num(a):
    return a ** 3

def cube_root_num(a):
    if a < 0:
        return "Error: Cube root of negative number"
    return a ** (1/3)

def factorial_num(a):
    if a < 0:
        return "Error: Factorial of negative number"
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result

def square_num(a):
    return a ** 2

def table_of_num(a):
    table = ""
    for i in range(1, 11):
        table += f"{a} X {i} = {a*i}\n"
    return table

def percentage_marks(marks, total):
    return round((marks / total) * 100, 2)

def simple_interest(principle, rate, time):
    if principle == 0 or rate == 0 or time == 0:
        return 0
    return ((principle * rate * time) / 100)

def complex_interest(principle, rate, time):
    if principle == 0 or rate == 0 or time == 0:
        return 0
    return principle * ((1 + rate / 100) ** time)

def average_num(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def rectangle(l, w):
    return l * w

def check_prime(num):
    if num < 2:
        return "Not prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"({num}) is not Prime number"
    return f"({num}) is Prime number"

def GCD_hcf(*args):
    result = int(args[0])
    for num in args[1:]:
        result = math.gcd(result, int(num))
    return result

def lcm(*args):
    def lcm_two(a, b):
        return abs(a * b) // math.gcd(a, b)
    result = int(args[0])
    for num in args[1:]:
        result = lcm_two(result, int(num))
    return result

def area_circle(radius):
    return math.pi * radius ** 2

def sin(Angle):
    return math.sin(math.radians(Angle))

def cos(Angle):
    return math.cos(math.radians(Angle))

def tan(Angle):
    return math.tan(math.radians(Angle))

def asin(Radian):
    return math.degrees(math.asin(Radian))

def acos(Radian):
    return math.degrees(math.acos(Radian))

def atan(Radian):
    return math.degrees(math.atan(Radian))

def pythagoian_theoram(a, b):
    return a ** 2 + b ** 2