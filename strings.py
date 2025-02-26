# Variables
##a = 10  # int or Integer
# Datatypes
# the type of value that is being stored in a variable.
'''
1. Primitive -> already comes defined by language
    1. number -> Integer (int), Float (float), Complex (complex)
    2. string -> str   # start from here
    3. squence -> List, Tuple
    4. Map -> Dictionary
    5. Byte -> Bytes, BytesArray, MemoryView
    6. Sets -> Set, Frozenset
2. Non-Primitive (User defined datatype)
'''
# we can use python type() to confirm a varaible datatype
##print(type(a))


myname = "i love python"
print(myname[-1]) # indexing

## String Slicing
print(myname[2:6])  # str[start:end(n-1)]

print(myname[::2])  # str[start:end:step]

##myname[0] = "we"
##print(myname) # error i.e. string are immutable, once assigned then can't be changed

# Squence -> a variable can multiple values with zero based index.
# List
languages = ["html","css","js","python","framework"]
print(languages)

print(type(languages))

languages[-1] = "Django"  # list are mutable i.e. can reassigned multiple times as needed
print(languages)

## List slicing
print(languages[::2])

## string reverse
data = "banana"
print(data[::-1])

# Tuples
skills = ("softskills","hardskills") 
print(skills)

print(type(skills))

##skills[1] = "special skills" # error i.e. tuples cannot reassigned because they are immutable
##print(skills)

