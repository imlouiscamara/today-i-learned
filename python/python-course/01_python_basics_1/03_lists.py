# list

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2.5,'a', True]

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])
# print(amazon_cart[2]) # invalid


# data structure

# list slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0:2])
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[1:3]
print(amazon_cart)
print(new_cart)

new_cart = amazon_cart
amazon_cart[0] = 'desktop'
print(amazon_cart)
print(new_cart)

new_cart = amazon_cart[:]
new_cart[0] = 'gum'
new_cart2 = amazon_cart[0:3]
print(new_cart)
print(new_cart2)
print(amazon_cart)


# matrix
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
    ]

matrix_x = [
    [1,5,1],
    [0,1,0],
    [1,0,1]
]

print(matrix[0][1])
print(matrix_x[0][1])


# list methods
basket = [1,2,3,4,5]
print(len(basket))

# adding
basket.append(100)
basket.insert(5, 99)
new_list = basket.extend([101])
basket.extend([102])
print(basket)
print(new_list) # returns None

# removing
basket.pop()
basket.pop(0) # index

basket.remove(101) # value

new_list = basket.pop(4)
new_list = basket.clear()

print(basket)
print(new_list)


basket = ['a','x','b','c','d','e','d']

# print(basket.index('d', 0, 4))
print(basket.index('d', 0, len(basket)))

print('d' in basket)
print('x' in basket)
print('y' in basket)

print('i' in 'hi my name is ian')

print(basket.count('d'))

basket.sort()

new_basket = basket.copy()
new_basket = basket[:]
new_basket.sort()
basket.reverse()

print(basket)
print(len(basket))
print(new_basket)
print(sorted(basket))
print(basket[::-1])


print(list(range(1,100)))
print(list(range(100)))
print(list(range(101)))


sentence = ' '
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])

print(sentence)
print(new_sentence)


# list unpacking
a,b,c = [1,2,3]
a,b,c, *other = [1,2,3,4,5,6,7,8,9]
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
a,b,c = 1,2,3

print(a)
print(b)
print(c)
print(other)
print(d)

None
weapons = None
print(weapons)