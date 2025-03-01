# Datatypes
# the type of value that is being stored in a variable.
'''
1. Primitive -> already comes defined by language
    1. number -> Integer (int), Float (float), Complex (complex)
    2. string -> str   # start from here
    3. squence -> List, Tuple, Range
    4. Map -> Dictionary
    5. Byte -> Bytes, BytesArray, MemoryView
    6. Sets -> Set, Frozenset
    7. Boolean -> bool -> Truth (True) or Falsy( False)
2. Non-Primitive (User defined datatype)
'''

# Range
items = range(10) # range(end) i.e. n-1
print(list(items))

item2 = range(5,20) #range(start,end)
print(tuple(item2))

item3 = list(range(1,20,2)) # range(start,end,step)
print(item3)

#Map -> Dictionary -> 
dict1 = {"key1":"item 1","key2":"item 2","key2":"item 3"}
print(type(dict1))
print(dict1)
print(dict1["key2"]) # key2 is the key of "item 3"

# Sets -> collection of unique and non-indexed
item = {1,1,1,2,3,4}
print(item)

#print(item[3]) # error : sets can't be subscritable

# Frozenset
mylistdata = [1,1,1,2,3,4]
item = frozenset(mylistdata)
print(item)


# Boolean -> True or False

print(bool(0)) # only zero is false and other are True

print(bool("")) # only blank string is false and others are True

print(bool([])) # only blank list is false and others are True
print(bool(())) # only blank tuple is false and others are True
print(bool({})) # only blank set is false and others are True


# Bytes -> any string whhich has prefix of 'b'
data = b'this is something'
print(type(data))

#memoryview
data2 = memoryview(data)
print(data2)

# bytearray
data3 = bytearray(data2)

print(data3)

data3 = bytearray(b'A')
print(data3[0])


## ASCII -> American Standart Code for Information Interchange
letter = 'a' # 97
print(ord(letter))


number = 65 # 'A'
print(chr(number))

print("a cool emoji",chr(128512))

