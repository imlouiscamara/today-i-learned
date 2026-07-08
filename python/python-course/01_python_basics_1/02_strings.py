# strings
'hi hello there'
"hi hello there 225!"
print(type("hi hello there 225!"))

username = 'supercoder'
password = 'supersecret'

long_string = '''
              WOW
              0 0
              ---
              '''
print(long_string)

first_name = 'louis'
last_name = 'camara'
full_name = first_name + ' ' + last_name
print(full_name)


# string concatenation
print('hello' + ' tilou')
print('hello' + '5')
print('5' + '5')


# type conversion
print(str(100))
print(type(str(100)))
print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)


# escape sequence
weather = "It's sunny"
weather1 = "It's \"kind of\" sunny"
weather2 = "\t It's \"kind of\" sunny"
weather3 = "\t It's \"kind of\" sunny \n hope you have a good day!"

print(weather)
print(weather1)
print(weather2)
print(weather3)

backslash = "\\"
print(backslash)


# formatted strings
name = 'Johnny'
age = 55

print('Hi ' + name + '. You are ' + str(age) + ' years old.')
print(f'Hi {name}. You are {age} years old.') # best way
print('Hi {}. You are {} years old.'.format('Johnny', '55'))
print('Hi {}. You are {} years old.'.format(name, age))
print('Hi {new_name}. You are {new_age} years old.'.format(new_name='Sally', new_age=35))


# string indexes
selfish = '01234567'
         # 01234567

print(selfish[0])
print(selfish[1])
print(selfish[2])
print(selfish[3])
print(selfish[4])
print(selfish[5])
print(selfish[6])
print(selfish[7])
print(selfish)
print(selfish[0:2]) # [start:stop] # 01
print(selfish[0:7]) # 0123456
print(selfish[0:8]) # 01234567
print(selfish[0:8:1]) # [start:stop:stepover] # 01234567
print(selfish[0:8:2]) # [start:stop:stepover] # 0246
print(selfish[1:]) # 1234567
print(selfish[:5]) # 01234
print(selfish[::1]) # 01234567
print(selfish[-1]) # 7
print(selfish[-2]) # 6
print(selfish[-3]) # 5
print(selfish[::-1]) # 76543210
print(selfish[::-2]) # 7531

selfish = '100'
# selfish[0] = '8' # impossible
selfish = selfish + '8'

print(selfish)


str()
int()
print()
len()

print(len('hello'))
greet = 'hello'
print(greet[:])
print(greet[0:len(greet)])


# .format

quote = 'to be or not to be'

print(quote.upper()) # TO BE OR NOT TO BE
print(quote.capitalize()) # To be or not to be
print(quote.lower()) # to be or not to be
print(quote.find('be')) # 3
print(quote.replace('be', 'me')) # to me or not to me

print(quote)

quote2 = quote.replace('be', 'me')
print(quote2)


# booleans
bool
True
False

name = 'tilou'
is_cool = False
is_cool = True

print(bool(0))
print(bool(1))
print(bool('True'))
print(bool(''))


name = 'Louis Camara'
age = 20

relationship_status = 'single'
relationship_status = 'it\'s complicated'

print(relationship_status)


# exercise type conversion
birth_year = input('what year were you born?')
print(type(birth_year))
age = 2026 - int(birth_year)

print(f'your age is: {age}')

birth_year = input('what year were you born?')
print(type(birth_year))
age = 2026 - float(birth_year)

print(f'your age is: {age}')

birth_year = input('what year were you born?')
print(type(birth_year))
age = 2026 - bool(birth_year)

print(f'your age is: {age}')


a = 'Andrei'

is_cool = False #is cool flag
is_cool = True

print(bool('True'))


# exercise password checker
username = input('what is your username? ')
password = input('what is your password? ')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password, {hidden_password}, is {password_length} characters long.')