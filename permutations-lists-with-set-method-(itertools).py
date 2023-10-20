from itertools import product, permutations


input_elements = input("Enter elements separated by space: ").split()
n = int(input("How many elements to use for permutations: "))
repeat = input("Do you want the same element to repeat? (y/n): ")

if repeat.lower() == 'y':
    perm = list(product(input_elements, repeat=n))
else:
    perm = list(permutations(input_elements, n))

print("Permutations: ", perm)
print("Number of elements in the output list: ", len(perm))

print('__________________________________________\n')
print('considering tuples as sets ((a,b)=(b,a))')
print('__________________________________________')
# Example usage
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
