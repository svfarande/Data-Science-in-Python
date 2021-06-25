# Chapter Three - Built-In Data Structures, Functions, and Files

# Tuples -
nested_tup = (4, 5, 6), 1, 2, 3, (7, 8)
print(nested_tup)  # ((4, 5, 6), 1, 2, 3, (7, 8))

# immutable
tup = tuple(['foo', [1, 2], True])
# tup[2] = False    # TypeError: 'tuple' object does not support item assignment
tup[1].append(3)    # as list is mutable
print(tup)  # ('foo', [1, 2, 3], True)

# Multiplying a tuple by an integer, as with lists, has the effect of concatenating together
# that many copies of the tuple:
# Note that the objects themselves are not copied, only the references to them.
tupx3 = tup * 3
print(tupx3)  # ('foo', [1, 2, 3], True, 'foo', [1, 2, 3], True, 'foo', [1, 2, 3], True)

# unpacking nested tuples -
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
print(d)  # 7

# swapping of variables is easy now -
e, f = 1, 3
print(e, f)     # 1 3
f, e = e, f
print(e, f)     # 3 1

# advanced tuple unpacking -
tup = 1, 2, 3, 4, 5
v1, v2, *rest = tup     # or v1, v2, *_ = tup
print(v1, v2)   # 1 2
print(rest)     # [3, 4, 5]     # note this is list
print(type(rest))      # <class 'list'>

# List -

# insert is computationally expensive compared with append, because references to subsequent
# elements have to be shifted internally to make room for the new element. If you need to insert
# elements at both the beginning and end of a sequence, you may wish to explore collections.deque,
# a double-ended queue, for this purpose.

# Checking whether a list contains a value is a lot slower than doing so with dicts and
# sets (to be introduced shortly), as Python makes a linear scan across the values of the
# list, whereas it can check the others (based on hash tables) in constant time.

# Note that list concatenation by addition is a comparatively expensive operation since
# a new list must be created and the objects copied over. Using extend to append elements
# to an existing list, especially if you are building up a large list, is usually preferable.

# sort has a few options that will occasionally come in handy. One is the ability to pass
# a secondary sort key—that is, a function that produces a value to use to sort the
# objects.

b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
print(b)    # ['He', 'saw', 'six', 'small', 'foxes']

# Binary search and maintaining a sorted list -
# The built-in bisect module implements binary search and insertion into a sorted list.
# bisect.bisect finds the location where an element should be inserted to keep it sorted,
# while bisect.insort actually inserts the element into that location
import bisect
c = [1, 2, 2, 2, 3, 4, 7]
print(bisect.bisect(c, 2))  # 4
print(bisect.bisect(c, 5))  # 6
bisect.insort(c, 6)     # insertion
print(c)    # [1, 2, 2, 2, 3, 4, 6, 7]
# The bisect module functions do not check whether the list is sorted, as doing so would be
# computationally expensive. Thus, using them with an unsorted list will succeed without error but
# may lead to incorrect results.

seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[3:6] = [6, 3]
print(seq)  # [7, 2, 3, 6, 3, 0, 1]
print(seq[-4:])     # [6, 3, 0, 1]
print(seq[-6:-2])   # [2, 3, 6, 3]
print(seq[::-1])    # [1, 0, 3, 6, 3, 2, 7] # Reversing it cleverly

# enumerate
some_list = ['foo', 'bar', 'baz']
print(list(enumerate(some_list)))   # [(0, 'foo'), (1, 'bar'), (2, 'baz')]
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)  # {'foo': 0, 'bar': 1, 'baz': 2

# zip
# A very common use of zip is simultaneously iterating over multiple sequences, possibly also
# combined with enumerate. zip can take an arbitrary number of sequences, and the number of elements
# it produces is determined by the shortest sequence
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))      # 0: foo, one\n1: bar, two\n2: baz, three


# Set -

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

# union -
print(a.union(b))   # {1, 2, 3, 4, 5, 6, 7, 8}
print(a | b)    # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection -
print(a.intersection(b))    # {3, 4, 5}
print(a & b)    # {3, 4, 5}

# Python set operations
'''
Function 						Alternative syntax 		Description

a.add(x) 						N/A 					Add element x to the set a

a.clear() 						N/A 					Reset the set a to an empty state, discarding 
                                                        all of its elements

a.remove(x) 					N/A 					Remove element x from the set a

a.pop() 						N/A 					Remove an arbitrary element from the set a,
														raising KeyError if the set is empty

a.union(b) 						a | b 					All of the unique elements in a and b

a.update(b) 					a |= b 					Set the contents of a to be the union of the 
														elements in a and b

a.intersection(b) 				a & b 					All of the elements in both a and b

a.intersection_update(b) 		a &= b 					Set the contents of a to be the intersection of 
														the elements in a and b

a.difference(b) 				a - b 					The elements in a that are not in b

a.difference_update(b) 			a -= b 					Set a to the elements in a that are not in b

a.symmetric_difference(b) 		a ^ b 					All of the elements in either a or b but not both

a.symmetric_difference_update(b)a ^= b 					Set a to contain the elements in either a or b but
														not both

a.issubset(b) 					N/A 					True if the elements of a are all contained in b

a.issuperset(b) 				N/A 					True if the elements of b are all contained in a

a.isdisjoint(b) 				N/A 					True if a and b have no elements in common
'''

# Unordered Collections of Unique Elements and that doesn't support operations like
# indexing or slicing -
a = {'s', 'f'}
# print(a[0])   # TypeError: 'set' object is not subscriptable

# Sets are equal if and only if their contents are equal:
print({1, 2, 3} == {3, 2, 1})   # True

# Function -

def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)


# Each function can have positional arguments and keyword arguments. Keyword arguments
# are most commonly used to specify default values or optional arguments. In
# the preceding function, x and y are positional arguments while z is a keyword argument.
# This means that the function can be called in any of these ways:
print(my_function(5, 6, z=0.7))     # 0.06363636363636363
print(my_function(3.14, 7, 3.5))    # 35.49
print(my_function(10, 20))  # 45.0

# The main restriction on function arguments is that the keyword arguments must follow
# the positional arguments (if any). You can specify keyword arguments in any
# order; this frees you from having to remember which order the function arguments
# were specified in and only what their names are.

# It is possible to use keywords for passing positional arguments as well. In the preceding
# example, we could also have written. In some cases this can help with readability.
print(my_function(x=5, y=6, z=7))   # 77
print(my_function(y=6, z=7, x=5))   # 77


# Assigning variables outside of the function’s scope is possible, but those variables must be declared as global via the global keyword when using inside some function


# Currying: Partial Argument Application -
# Currying is computer science jargon (named after the mathematician Haskell Curry)
# that means deriving new functions from existing ones by partial argument application.
def add_numbers(x, y):
    return x + y


def add_five(y):
    add_numbers(5, y)


# OR
# add_five = lambda y: add_numbers(5, y)
# now here y is said to be curried

# OR we can use partial from functools
from functools import partial

add_five = partial(add_numbers, 5)


# Generators -
def cube(n):
    print("Cube of no. from 1 to {0}".format(n))
    for i in range(1, n + 1):
        yield i, i ** 3


print(dict(cube(5)))    # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# Generator Comprehension -
print(dict(((i, i ** 3) for i in range(1, 6))))     # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

import itertools

# The standard library itertools module has a collection of generators for many common
# data algorithms.

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, lambda x: x[0]):
    print(letter, list(names))
'''
A ['Alan', 'Adam']
W ['Wes', 'Will']
A ['Albert']
S ['Steven']
'''

'''Some useful itertools functions
Function                    Description

combinations(iterable, k)   Generates a sequence of all possible k-tuples of elements in the 
                            iterable, ignoring order and without replacement 
                            (see also the companion function combinations_with_replacement)

permutations(iterable, k)   Generates a sequence of all possible k-tuples of elements in the 
                            iterable, respecting order
                            
groupby(iterable[,keyfunc]) Generates (key, sub-iterator) for each unique key

product(*iterables, repeat=1) Generates the Cartesian product of the input iterables as tuples
                              , similar to a nested for loop
'''

# File IO & OS -

# to get an EOL(End of Line)-free list -
# lines = [x.rstrip() for x in open(path)]
# tell() give current position of file handle

import sys

print(sys.getdefaultencoding())  # utf-8

'''Python file modes
Mode    Description
r       Read-only mode
w       Write-only mode; creates a new file (erasing the data for any file with the same name)
x       Write-only mode; creates a new file, but fails if the file path already exists
a       Append to existing file (create the file if it does not already exist)
r+      Read and write
b       Add to mode for binary files (i.e., 'rb' or 'wb')
t       Text mode for files (automatically decoding bytes to Unicode). This is the default if not 
        specified. Add t to other modes to use this (i.e., 'rt' or 'xt')
'''

# Bytes and Unicode with Files
# Create file and insert below data using code below -
data = ['Sueña el rico en su riqueza,\n',
        'que más cuidados le ofrece;\n',
        'sueña el pobre que padece\n',
        'su miseria y su pobreza;\n',
        'sueña el que a medrar empieza,\n',
        'sueña el que afana y pretende,\n',
        'sueña el que agravia y ofende,\n',
        'y en el mundo, en conclusión,\n',
        'todos sueñan lo que son,\n',
        'aunque ninguno lo entiende.\n']
with open('segismundo.txt', 'w+') as f:
    f.writelines(data)
    f.seek(0)
    check = f.readlines()
    # print(check)

# The default behavior for Python files (whether readable or writable) is text mode,
# which means that you intend to work with Python strings (i.e., Unicode). This contrasts
# with binary mode, which you can obtain by appending b onto the file mode

with open('segismundo.txt') as f:
    chars = f.read(10)
    print(chars)        # Sueña el r

# UTF-8 is a variable-length Unicode encoding, so when I requested some number of
# characters from the file, Python reads enough bytes (which could be as few as 10 or as
# many as 40 bytes) from the file to decode that many characters.

with open('segismundo.txt', 'rb') as f:
    chars = f.read(10)
    print(chars)        # b'Sue\xf1a el r'
    print(chars.decode('latin-1'))         # Sueña el r

# Sueña = Sue\xc3\xb1a 
# [(Postion - Character) -> 0 - 'S', 1 - 'u', 2 - 'e', 3 - '\xc3', 4 - '\xb1', 5 - 'a']

# A character such as 'ñ' is represented using 2 hexadecimal characters in UTF-8 (\xc3\xb1). Then
# make sure while decoding such character you read both the byte else reading data only till 3rd index # it will give you below error -
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 3: unexpected end of data

# Also beware using seek when opening files in any mode other than binary. If the file position
# falls in the middle of the bytes defining a Unicode character, then subsequent
# reads will result in an error:
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte
# Lets say you keep your seek on 4th index of 'Sueña' then it will give you that error.