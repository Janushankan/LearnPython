# print("Janushankan")
# print("o----")
# print(" ||||")
# print('*' * 10)

# variables -------------------------------------

# price = 10
# price = 20
# rating = 4.9
# name= 'Janus'
# is_published = False    # case sensitive -> True, False
# print(price)
# print(rating)
# print(name)
# print(is_published)

# full_name = 'John Smith'
# age = 20
# is_new = True

# receiving input -------------------------------------

# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color) 

# Type Conversion -------------------------------------

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print (age)

# weight_lbs = input('Weight(lbs): ')
# weight_kgs = int(weight_lbs) * 0.45
# print(weight_kgs)

# Strings -------------------------------------

# course = "Python's Course for Beginners"
# print(course)
# course = 'Python Course for "Beginners"'
# print(course)

# multi line string
# course = '''
# Hii John,

# Here is our first email to you.

# Thank you,
# The support team

# '''
# print(course)

# course = 'Python for Beginners'
# #         0123456789.........
# #              .....-5-4-3-2-1
# print(course[0])    # P
# print(course[-1])   # s
# print(course[0:3])  # Pyt
# print(course[0:])   # Python for Beginners
# print(course[1:])   # ython for Beginners
# print(course[:5])   # Pytho
# another = course[:]
# print(another)      # Python for Beginners

# name = 'Jennifer'
# print(name[1:-1])   # ennife


# Formatted Strings -------------------------------------

# first = 'John'
# last = 'smith'
# message = first + ' [' + last + '] is a coder.'
# msg = f'{first} [{last}] is a coder.'   # f'___'  -> formatted string
# print(message)  # John [smith] is a coder.
# print(msg)  # John [smith] is a coder.


# String Methods -------------------------------------

# course = 'Python for Beginners'
# print(len(course))     # 20
# print(course.upper())  # PYTHON FOR BEGINNERS
# print(course)          # Python for Beginners
# print(course.lower())  # python for beginners
# print(course.title())  # Python For Beginners
# print(course.find('P'))   # 0
# print(course.find('o'))   # 4
# print(course.find('O'))   # -1 -> not found uppercase O
# print(course.find('Beginners'))   # 11
# print(course.replace('beginners', 'Absolute Beginners'))   # Python for Beginners
# print(course.replace('Beginners', 'Absolute Beginners'))   # Python for Absolute Beginners
# print(course.replace('P', 'J'))   # Jython for Beginners
# # in operator -> '...' in course
# print('Python' in course)   # True
# print('python' in course)   # False

# Arithmetic Operations -------------------------------------

# print(10 + 3)   # 13
# print(10 - 3)   # 7
# print(10 * 3)   # 30
# print(10 / 3)   # 3.3333333333333335
# print(10 // 3)  # 3 -> integer
# print(10 % 3)   # 1
# print(10 ** 3)  # 1000
# x = 10
# x = x + 3
# print(x)    # 13
# x += 3
# print(x)    # 16
# x -= 3
# print(x)    # 13

# Operator Precedence -------------------------------------

# x = 10 + 3 * 2
# print(x)

# Order of Operations
# parenthesis
# exponentiation 2 ** 3
# multiplication or division
# addition or subtraction

# x = 10 + 3 * 2 ** 2
# print(x)  # 22

# x = (2 + 3) * 10 - 3
# print(x) # 47


# Math Functions -------------------------------------

# x = 2.9
# print(round(x)) # 3
# print(abs(-2.9))    # 2.9 -> always return positive number


# import math

# print(math.ceil(2.9))   # 3
# print(math.floor(2.9))   # 2