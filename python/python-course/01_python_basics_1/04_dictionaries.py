# dictionary
dictionary = {'a': 1,'b': 2,'x': 3}

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
print(my_list)
print(my_list[0]['a'][2])


dictionary = {
    'weapons': [1,2,3],
    'greeting': 'hello',
    'is_Magic': True
}

dictionary = {
    123: [1,2,3],
    '123': [1,2,3],
    '123': 'hello', # overwrite
    True: 'hello',
    # [100]: True, # impossible
    '[100]': True
}

# [0] = # impossible

print(dictionary[123])
print(dictionary['123'])
print(dictionary[True])
print(dictionary['[100]'])


user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user['basket'])
print(user['age'])
print(user.get('age', 55))


user2 = dict(name='JohnJohn')
print(user2)


print('i' in 'hi')

print('basket' in user)
print('size' in user)

print('hello' in user.keys())
print('age' in user.keys())

print('age' in user.values())
print('hello' in user.values())

print(user.clear())
print(user.items())


user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

user2 = user.copy()
print(user)
print(user.clear())
print(user2)


user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.pop('greet'))
print(user.popitem())
print(user.update({'age': 55}))
print(user.update({'ages': 55}))
print(user)