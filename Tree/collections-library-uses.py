from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap, UserDict, UserList, UserString

# 1. Counter: Count the occurrences of elements in an iterable.
my_list = ['a', 'b', 'c', 'a', 'b', 'a']
print(Counter(my_list))  # Output: Counter({'a': 3, 'b': 2, 'c': 1})

# 2. defaultdict: Dictionary with default value for missing keys.
d = defaultdict(int)
d['key1'] = 1
print(d['key2'])  # Output: 0 (default value for int)

# 3. OrderedDict: Dictionary that retains the order of insertion.
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 4. deque: Double-ended queue for fast adding and removing from both ends.
d = deque([1, 2, 3, 4, 5])
d.append(6)  # Adds 6 at the end
d.appendleft(0)  # Adds 0 at the beginning
print(d)  # Output: deque([0, 1, 2, 3, 4, 5, 6])

# 5. namedtuple: Create tuple-like objects with named fields.
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0], p[1])  # Output: 11 22
print(p.x, p.y)  # Output: 11 22

# 6. ChainMap: Combine multiple mappings into a single unit.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_dict = ChainMap(dict1, dict2)
print(combined_dict['c'])  # Output: 4

# 7. UserDict: Wrapper around dictionary objects for easier dict subclassing.
class MyDict(UserDict):
    def popitem(self):
        if self.data:
            return self.data.popitem()
        else:
            raise KeyError('dictionary is empty')

# 8. UserList: Wrapper around list objects for easier list subclassing.
class MyList(UserList):
    def remove_duplicates(self):
        return list(set(self.data))

# 9. UserString: Wrapper around string objects for easier string subclassing.
class MyString(UserString):
    def reverse(self):
        return self.data[::-1]

# 10. defaultdict with list: Use a list as the default factory.
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['a'].append(3)
print(d)  # Output: defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2]})
