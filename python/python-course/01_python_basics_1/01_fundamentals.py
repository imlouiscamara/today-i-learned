print("louis camara")

name = input("what's your name? ")

print("hello " + name)


# fundamental data types
int # integers
float # floating point number
bool
str
list
tuple
set
dict

# custom types
# classes (def)

# specialized data types
# modules
None


# int and float
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)

print(type(6))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4)) # 0.5

print(type(0.00001))
print(type(5.00001))
print(type(0))
print(type(20+1.1))
print(type(9.9+1.1))

print(9.9+1.1) # 11.0

print(2 ** 2)
print(2 ** 3) # power

print(2 // 4)
print(3 // 4)
print(5 // 4) # gets rounded down to an integer

print(5 % 4)
print(6 % 4)
print(8 % 4) # modulo


# math functions
print(round(3.1))
print(round(3.9))
print(abs(-20))


# operator precedence
print(20 - 3 * 4)
print((20 - 3) + 2 ** 2)
# here's the order:
# ()
# **
# * /
# + -


# EXERCISE
# guess the output of each answer before you click RUN
# try to write down your answer before and see how you do... keep it mind i made it a little tricky for you :)

print((5 + 4) * 10 / 2) # 45

print(((5 + 4) * 10) / 2) # 45

print((5 + 4) * (10 / 2)) # 45

print(5 + (4 * 10) / 2) # 25

print(5 + 4 * 10 // 2) # 25


print(bin(5))
print(int('0b101', 2))


# variables
user_iq = 190
print(user_iq)
user_IQ = 191
print(user_IQ)

iq = 190
user_age = iq / 4
a = user_age
print(a)


# constants
PI = 3.14
PI = 0
print(PI)

a,b,c = 1,2,3
print(a)
print(b)
print(c)

iq = 100
user_age = iq/5 # iq/5 is an expression and user_age = iq/5, a statement


# augmented assignment operator
some_value = 5
some_value = 5 + 2
some_value = some_value + 2
some_value += 2
some_value -= 2
some_value = some_value * 2
some_value *= 2
print(some_value)