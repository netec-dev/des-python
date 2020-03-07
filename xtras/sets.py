# 5.4. Sets
# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

# Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

# Here is a brief demonstration:

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# show that duplicates have been removed
print(basket) # {'orange', 'banana', 'pear', 'apple'}
# fast membership testing
'orange' in basket # True
'crabgrass' in basket # False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

# unique letters in a
print(a) # {'a', 'r', 'b', 'c', 'd'}
# letters in a but not in b
print(a - b) # {'r', 'd', 'b'}
# letters in a or b or both
print(a | b) # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# letters in both a and b
print(a & b) # {'a', 'c'}
# letters in a or b but not both
print(a ^ b) # {'r', 'd', 'b', 'm', 'z', 'l'}

# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # {'r', 'd'}