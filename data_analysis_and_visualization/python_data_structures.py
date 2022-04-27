# Lists in Python
# Lists are ordered, changeable, and allow for duplicates

# Slicing
p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# p2 will be [1,2,3,4,5] because [0:5] implies starting from 0th index of p1 and stop at 5th index
p2 = p1[0:5]
# same as #p2, different synatax
p3 = p1[:5]

# List operations
depths = [1, 5, 3, 6, 4, 7, 10, 12]

first_5_depths = depths[:5]
print('depths[:5]:', first_5_depths)
print('sum():', sum(depths))
print('max():', max(depths))
# return last element
print('depths[-1]:', depths[-1])
# return end of list starting from second to the end 
print('depths[-2:]:', depths[-2:])
# return 2nd, 3rd, and 4th elements
print(depths[2:5])
# commands that check if a value is contained in the list
print('num in list:', 22 in depths)
print('num in list:', 1 in depths)
# append
depths.append(44)
print('list.append:', depths)
#extend
depths.extend([100,200])
print('list.extend(list):', depths)
#modify
depths[4] = 100
print('list[i]:', depths)
depths.insert(5,1000)
print('list.insert(index, value):', depths)

'''
Generators:
  - Objects you can loop over like a list
  - Don't store the entire list in memory
  - Return the next value in the list only when asked > memory efficient
'''

'''
Dictionaries
  - Hold key-value pairs
  - Each key is unique, and assoicated with a value
  - Key-value pairs are unordered and changeable
'''
my_dict = {"age": 22, "birth_year": 1999, "name": "jack", "siblings": ["jill", "jen"]}
# check key
print('key in dict:', 'age' in my_dict)
# get value for key
print('dict.get(key):', my_dict.get('age'))
print('dict.get(key, value if absent):', my_dict.get('company', 1))
# return all key
print('dict.keys():',my_dict.keys())
# return all values
print('dict.values():', my_dict.values())
# return all key value pair
print('dict.items():', my_dict.items())

# defaultdict
from collections import defaultdict
my_default_dict = defaultdict(int) # make a default dictionary
my_default_dict['age'] = 22 # adding a key-value pair
print(my_default_dict['company']) # printing the value of the key "company"

'''
Sets
  - Unordered collection of unique elements
  - Allows for union, intersection, and difference operation
'''
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(1) #Note that the set only contains a single "1" value
print(my_set)

my_set2 = set()
my_set2.add(1)
my_set2.add(2)
my_set2.add(3)
my_set2.add(4)

print(my_set2)

#Prints the overlap
print('intersection:', my_set.intersection(my_set2))

#Prints the combination
print('union:', my_set.union(my_set2))

#prints the difference
print('difference:', my_set.difference(my_set2))

