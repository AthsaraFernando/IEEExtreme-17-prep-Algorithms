from itertools import count, cycle, permutations, combinations, chain, zip_longest, product, combinations_with_replacement, groupby

# 1. Infinite Iterators
# count(start, step) creates an infinite iterator starting from 'start' and incrementing by 'step'
for i in count(5, 2):
    if i > 20:
        break
    print(i, end=' ')  # Prints the numbers from 5 with a step of 2 until it reaches 20
print("\n")

# cycle(iterable) creates an infinite iterator cycling through elements of 'iterable'
iterable = [1, 2, 3]
for i in cycle(iterable):
    if i > 5:
        break
    print(i, end=' ')  # Prints the elements of the list [1, 2, 3] in a cycle until it reaches 5
print("\n")

# 2. Finite Iterators
# permutations(iterable, r) returns all possible r-length tuples of elements from 'iterable'
items = ['a', 'b', 'c']
perm = permutations(items, 2)
print(list(perm))  # Prints all the possible 2-length permutations of the elements in the list ['a', 'b', 'c']
print("\n")

# combinations(iterable, r) returns all possible r-length combinations of elements from 'iterable'
comb = combinations(items, 2)
print(list(comb))  # Prints all the possible 2-length combinations of the elements in the list ['a', 'b', 'c']
print("\n")

# 3. Combining Iterators
# chain(*iterables) chains multiple iterables together into one sequence
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = chain(list1, list2)
print(list(combined))  # Prints the combined list of [1, 2, 3, 'a', 'b', 'c']
print("\n")

# zip_longest(*iterables, fillvalue) zips multiple iterables together, filling missing values with 'fillvalue'
a = [1, 2, 3]
b = ['a', 'b']
zipped = zip_longest(a, b, fillvalue='*')
print(list(zipped))  # Zips the lists a and b together, filling missing values with '*'
print("\n")

# 4. Iterators on Iterators
# product(*iterables, repeat) returns the Cartesian product of the input iterables
iter1 = [1, 2]
iter2 = ['a', 'b']
prod = product(iter1, iter2)
print(list(prod))  # Prints the Cartesian product of the lists [1, 2] and ['a', 'b']
print("\n")

# combinations_with_replacement(iterable, r) returns r-length combinations with repeated elements
items = ['a', 'b', 'c']
comb_wr = combinations_with_replacement(items, 2)
print(list(comb_wr))  # Prints all the possible 2-length combinations with repeated elements from the list ['a', 'b', 'c']
print("\n")

# 5. Grouping Data
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('c', 5)]
grouped_data = groupby(data, key=lambda x: x[0])
for key, group in grouped_data:
    print(key, list(group))  # Groups the data by the first element of each tuple
