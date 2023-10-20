def product_custom(lst, repeat):
    if repeat == 1:
        return [[x] for x in lst]
    res = []
    for item in lst:
        for p in product_custom(lst, repeat - 1):
            res.append([item] + p)
    return res


def permutations_custom(lst, r=None):
    if r is None:
        r = len(lst)
    if r == 0:
        return [[]]
    res = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i + 1:]
        for p in permutations_custom(rest, r - 1):
            res.append([lst[i]] + p)
    return res


input_elements = input("Enter elements separated by space: ").split()
n = int(input("How many elements to use for permutations: "))
repeat = input("Do you want the same element to repeat? (y/n): ")

if repeat.lower() == 'y':
    perm = product_custom(input_elements, n)
else:
    perm = permutations_custom(input_elements, n)

print("Permutations: ", perm)
print("Number of elements in the output list: ", len(perm))

def identify_duplicates(tuple_list):
    sets_list = [set(item) for item in tuple_list]
    unique_sets = {frozenset(item) for item in sets_list}
    new_list = []
    for item in unique_sets:
        if len(item) == 1:
            for t in tuple_list:
                if set(t) == item:
                    new_list.append(t)
                    break
        else:
            new_list.append(tuple(item))
    return new_list

# Example usage

new_list = identify_duplicates(perm)
print("Set method List ( removed same ):", new_list)