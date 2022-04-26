'''
For
  - contain iterable using enumerate()
'''

names = ['tyler', 'karen', 'jill']

for i, name in enumerate(names):
    print("Index: {0}".format(i))
    print("Value: {0}".format(name))

'''
List comprehensions
  - Combining List and loops
'''

range(1, 6)  # creates [1,2,3,4,5]
numbers_gt_5 = [x for x in range(1, 15) if x > 5]
nums_plus_one = [x + 1 for x in range(5)]

'''
Sort
  - .sort() for basic sort
  - sorted for advance sort
'''

my_list = [2, 10, 1, -5 22]
my_list_sorted_abs = sorted(my_list, key=abs, reverse=True)

'''
zip
  - Combining two lists into a list of tuples 
  - Breaking a tuple into two lists

  zip returns a generator, so we have to wrap it in list() to print it
'''

# Combining two lists into a tuple
list_1 = [1,2,3]
list_2 = ['x', 'y', 'z']
zip(list_1, list_2)

# Brekaing a tuple into two lists
pairs = [('x', 1), ('y', 2), ('z', 3)]
letters, numers = zip(*pairs)