import math
# Display your name
print("My name is Saksham Rai")

# A simple Calculator
print("5 + 4 =", 5+4)

# Interactive greeting 
name = input("What's your name? \n")
print(f"Hello, {name}!")


age = input("What's your age? \n")
print(f"I am {age} years old.")

print("Good Morning")

# Intro Practical Exercises
# 1.
print("Good Morning, Saksham Rai.")
# 2. 
print ("Product of 6 and 7 is ", 6 * 7)

# Data types practical exercise.
# 1.
my_name = "Saksham Rai"
# 2.
my_age = 22
# 3.
double_age = my_age * 2

# Opearators practical exercise 
a, b = 5, 2
sum, diff, prod, div = a+b,a-b,a*b,a/b
print(sum)
print(diff)
print(prod)
print(div)
is_a_greater = a > b
complex_condition = (a > b) and (a % 2 == 0)
print (complex_condition, is_a_greater)

# Numbers 
print(abs(-42))
print(math.ceil(34.2))
print(max(1, 2, 5))

def abs_diff(a, b):
    return abs(a-b)

def highest_lowest(num_list):
    return (max(num_list), min(num_list))

def sqr_root(num):
    return math.sqrt(num)

print(abs_diff(5, 94))
print(highest_lowest([1,2,-5,87,45,133]))
print(sqr_root(4))



# Exercise 11.
print(my_name.format("Rai"))

# Exercise 9.
print(ord(my_name[0]))
print("hello world".title())

# Exercise 8.
sl = "Pythonista"
print(sl[4:9])

# Exercise 7.
contains = "p" in "apple"
print("contains")

# Exercise 6.
print("python - " * 5 + "python")

# Exercise 1.
print(len(my_name))

# Exercise 2. 
print("".type())

# Exercise 3.
print("hello, \t" , "")



