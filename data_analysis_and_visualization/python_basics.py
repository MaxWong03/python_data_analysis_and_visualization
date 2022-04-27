from collections import Counter

marriage_ages = [22,25,25,25,30,24,26,24,35] # create a list
value_counts = Counter(marriage_ages) # apply the counter functionality
print(value_counts.most_common()) # output values as a list of tuples

# anonymous function in python
z = lambda x, y: x + y # an anonymous function which takes x and y as input and return x + y
print(z(100,5))