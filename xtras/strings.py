# https://docs.python.org/3/tutorial/introduction.html#strings
# 3.1.2. Strings
# Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. \ can be used to escape quotes:
# single quotes
print('spam eggs') # 'spam eggs'
# use \' to escape the single quote...
print('doesn\'t') # "doesn't"
# ...or use double quotes instead
print("doesn't") # "doesn't"
print('"Yes," they said.') # '"Yes," they said.'
print("\"Yes,\" they said.") # '"Yes," they said.'
print('"Isn\'t," they said.') # '"Isn\'t," they said.'

#In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:
print('"Isn\'t," they said.') # '"Isn\'t," they said.'
print('"Isn\'t," they said.') # "Isn't," they said.
s = 'First line.\nSecond line.'  # \n means newline
# without print(), \n is included in the output
print(s) # 'First line.\nSecond line.'
# with print(), \n produces a new line
print(s)  
# First line.
# Second line.

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

# here \n means newline!
print('C:\some\name')  
# C:\some
# ame

# note the r before the quote
print(r'C:\some\name')   # C:\some\name

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# produces the following output (note that the initial newline is not included):

# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# Strings can be concatenated (glued together) with the + operator, and repeated with *:

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium') # 'unununium'

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('Py' 'thon') # 'Python'

# This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text) # 'Put several strings within parentheses to have them joined together.'

# This only works with two literals though, not with variables or expressions:
prefix = 'Py'
# can't concatenate a variable and a string literal
#prefix 'thon' 
#  File "<stdin>", line 1
#    prefix 'thon'
#                ^
#SyntaxError: invalid syntax

#print(('un' * 3) 'ium')
#  File "<stdin>", line 1
#    ('un' * 3) 'ium'
#                   ^
#SyntaxError: invalid syntax
# If you want to concatenate variables or a variable and a literal, use +:
prefix = "Py"
print(prefix + 'thon') # 'Python'
# Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

word = 'Python'
# character in position 0
print(word[0]) # 'P'
# character in position 5
print(word[5]) # 'n'

# Indices may also be negative numbers, to start counting from the right:
# last character
print(word[-1]) # 'n' 
# second-last character
print(word[-2]) # 'o'
print(word[-6]) # 'P'

# Note that since -0 is the same as 0, negative indices start from -1.

# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
# characters from position 0 (included) to 2 (excluded)
print(word[0:2]) # 'Py'
# characters from position 2 (included) to 5 (excluded)
print(word[2:5]) # 'tho'

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

print(word[:2] + word[2:]) # 'Python'
print(word[:4] + word[4:]) # 'Python'

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

# character from the beginning to position 2 (excluded)
print(word[:2]) # 'Py'
# characters from position 4 (included) to the end
print(word[4:]) # 'on'
# characters from the second-last (included) to the end
print(word[-2:]) # 'on'

# One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
#
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
# The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

# For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

# Attempting to use an index that is too large will result in an error:

# the word only has 6 characters
#print(word[42])  
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range

# However, out of range slice indexes are handled gracefully when used for slicing:

print(word[4:42]) # 'on'
print(word[42:]) # ''

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

#word[0] = 'J'
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

#word[2:] = 'py'
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

#If you need a different string, you should create a new one:

print('J' + word[1:]) # 'Jython'
print(word[:2] + 'py') # 'Pypy'

# The built-in function len() returns the length of a string:

s = 'supercalifragilisticexpialidocious'
print(len(s)) # 34