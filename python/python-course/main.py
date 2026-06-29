# print("Louis Camara")

# name = input("What's your name? ")

# print("Hello " + name)

# Fundamental Data Types
# int # integers
# float # floating point number
# bool
# str
# list
# tuple
# set
# dict

# Classes -> custom types
# SuperCar

# Specialized Data Types
# Modules

# None

# int and float
# print(2 + 4)
# print(2 - 4)
# print(2 * 4)
# print(2 / 4)

# print(type(6))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4)) # 0.5

# print(type(0.00001))
# print(type(5.00001))
# print(type(0))
# print(type(20+1.1))
# print(type(9.9+1.1))
# print(9.9+1.1) # 11.0
# print(2 ** 2)
# print(2 ** 3) # power
# print(2 // 4)
# print(3 // 4)
# print(5 // 4) # gets rounded down to an integer
# print(5 % 4)
# print(6 % 4)
# print(8 % 4)

# math functions
# print(round(3.1))
# print(round(3.9))
# print(abs(-20))

# operator precedence
# print(20 - 3 * 4)
# print((20 - 3) + 2 ** 2)

# ()
# **
# * /
# + -

# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

# print((5 + 4) * 10 / 2) # 45

# print(((5 + 4) * 10) / 2) # 45

# print((5 + 4) * (10 / 2)) # 45

# print(5 + (4 * 10) / 2) # 25

# print(5 + 4 * 10 // 2) # 25

# int
# float
# complex

# print(bin(5))
# print(int('0b101', 2))

# variables

# user_iq = 190
# print(user_iq)
# user_IQ = 191
# print(user_IQ)

# iq = 190
# user_age = iq/4
# a = user_age
# print(a)

# constants
# PI = 3.14
# PI = 0
# print(PI)

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# iq = 100
# user_age = iq / 5 # iq/5 is an expression and user_age = iq/5, a statement

# augmented assignment operator
# some_value = 5
# some_value = 5 + 2
# some_value = some_value + 2
# some_value += 2
# some_value -= 2
# some_value = some_value * 2
# some_value *= 2

# print(some_value)

# strings
# 'hi hello there'
# "hi hello there 225!"
# print(type("hi hello there 225!"))
# username = 'supercoder'
# password = 'supersecret'
# long_string = '''
# WOW
# 0 0
# ---
# '''

# print(long_string)
# first_name = 'Louis'
# last_name = 'Camara'
# full_name = first_name + ' ' + last_name
# print(full_name)

# string concatenation
# print('hello' + ' Tilou')
# print('hello' + '5')
# print('5' + '5')

# type conversion
# print(str(100))
# print(type(str(100)))
# print(type(int(str(100))))

# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

# escape sequence
# weather = "It's sunny"
# weather1 = "It's \"kind of\" sunny"
# weather2 = "\t It's \"kind of\" sunny"
# weather3 = "\t It's \"kind of\" sunny \n hope you have a good day!"

# print(weather)
# print(weather1)
# print(weather2)
# print(weather3)

# backslash = "\\"
# print(backslash)

# formatted strings

# name = 'Johnny'
# age = 55

# print('Hi ' + name + '. You are ' + str(age) + ' years old.')
# print(f'Hi {name}. You are {age} years old.') # better way
# print('Hi {}. You are {} years old.'.format('Johnny', '55'))
# print('Hi {}. You are {} years old.'.format(name, age))
# print('Hi {new_name}. You are {new_age} years old.'.format(new_name='Sally', new_age=35))

# string indexes

# selfish = '01234567'
#          # 01234567

# print(selfish[0])
# print(selfish[1])
# print(selfish[2])
# print(selfish[3])
# print(selfish[4])
# print(selfish[5])
# print(selfish[6])
# print(selfish[7])
# print(selfish)
# print(selfish[0:2]) # [start:stop] # 01
# print(selfish[0:7]) # 0123456
# print(selfish[0:8]) # 01234567
# print(selfish[0:8:1]) # [start:stop:stepover] # 01234567
# print(selfish[0:8:2]) # [start:stop:stepover] # 0246
# print(selfish[1:]) # 1234567
# print(selfish[:5]) # 01234
# print(selfish[::1]) # 01234567
# print(selfish[-1]) # 7
# print(selfish[-2]) # 6
# print(selfish[-3]) # 5
# print(selfish[::-1]) # 76543210
# print(selfish[::-2]) # 7531

# selfish = '01234567'

# selfish = 100
# selfish[0] = '8' # error
# selfish = selfish + '8'

# print(selfish)

# str()
# int()
# print()
# len()
# print(len('hello'))
# greet = 'hello'
# print(greet[:])
# print(greet[0:len(greet)])
# .format

# quote = 'to be or not to be'

# print(quote.upper())
# print(quote.capitalize())
# print(quote.lower())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))

# print(quote)

# quote2 = quote.replace('be', 'me')
# print(quote2)

#booleans
# bool
# True
# False

# name = 'tilou'
# is_cool = False

# is_cool = True

# print(bool(0))
# print(bool(1))
# print(bool('True'))
# print(bool(''))

# name = 'Louis Camara'
# age = 20
# relationship_status = 'single'

# relationship_status = 'it\'s complicated'

# print(relationship_status)

# exercise type conversion
# birth_year = input('what year were you born?')
# print(type(birth_year))
# age = 2026 - int(birth_year)

# print(f'your age is: {age}')


# birth_year = input('what year were you born?')
# print(type(birth_year))
# age = 2026 - float(birth_year)

# print(f'your age is: {age}')


# birth_year = input('what year were you born?')
# print(type(birth_year))
# age = 2026 - bool(birth_year)

# print(f'your age is: {age}')

# a = 'Andrei'
# is_cool = False #is cool flag

# is_cool = True

# print(bool('True'))

# exercise password checker

# username = input('what is your username? ')
# password = input('what is your password? ')

# password_length = len(password)
# hidden_password = '*' * password_length

# print(f'{username}, your password, {hidden_password}, is {password_length} characters long.')

# list

# li = [1,2,3,4,5]
# li2 = ['a', 'b', 'c']
# li3 = [1,2.5,'a', True]

# amazon_cart = ['notebooks', 'sunglasses']
# print(amazon_cart[0])
# print(amazon_cart[1])
# print(amazon_cart[2])

# data structure

# list slicing
# amazon_cart = [
#     'notebooks',
#     'sunglasses',
#     'toys',
#     'grapes'
# ]
# print(amazon_cart[0:2])
# print(amazon_cart[0::2])

# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[1:3]
# new_cart = amazon_cart
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# new_cart2 = amazon_cart[0:3]
# print(new_cart)
# print(new_cart2)
# print(amazon_cart)

# matrix
# matrix = [
#     [1,2,3],
#     [2,4,6],
#     [7,8,9]
#     ]

# matrix_x = [
#     [1,5,1],
#     [0,1,0],
#     [1,0,1]
# ]

# print(matrix[0][1])

# list methods
# basket = [1,2,3,4,5]
# print(len(basket))

#adding
# basket.append(100)
# basket.insert(5, 100)
# new_list = basket.extend([100])
# basket.extend([100])
# print(basket)
# print(new_list) #returns None

#removing
# basket.pop() #index
# basket.pop()
# basket.pop(0)
# basket.remove() #value
# new_list = basket.pop(4)
# new_list = basket.clear()
# print(basket)
# print(new_list)

# basket = ['a','x','b','c','d','e','d']

# print(basket.index('d', 0, 4))
# print('d' in basket)
# print('x' in basket)
# print('i' in 'hi my name is ian')
# print(basket.count('d'))
# basket.sort()
# new_basket = basket[:]
# new_basket = basket.copy()
# new_basket.sort()
# basket.reverse()
# print(basket)
# print(len(basket))
# print(new_basket)
# print(sorted(basket))
# print(basket[::-1])
# print(basket)

# print(list(range(1,100)))
# print(list(range(100)))
# print(list(range(101)))

# sentence = ' '
# new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])

# print(sentence)
# print(new_sentence)

# list unpacking
# a,b,c = [1,2,3]
# a,b,c, *other = [1,2,3,4,5,6,7,8,9]
# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# a,b,c = 1,2,3

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# None
# weapons = None
# print(weapons)

# Dictionary
# dictionary = {'a': 1,'b': 2,'x': 3}
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}
my_list = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
    },
    {
    'a': [4,5,6],
    'b': 'hello',
    'x': True
    }
]

print(dictionary)
print(dictionary['a'])
print(dictionary['a'][1])
print(dictionary['b'])
print(dictionary['x'])
print(my_list[0]['a'][2])