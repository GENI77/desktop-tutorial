from typing import List, Dict, Tuple, Set


# data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
#                   "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
#
#
#
#
#
#
# calculate_structure_sum()
# result = calculate_structure_sum(data_structure)
# print(result)

def calculate_structure_sum(*args):
    structure_sum = 0
    if isinstance(data_structure, int):
        structure_sum += data_structure
    elif isinstance(data_structure, dict):
        structure_sum += sum(data_structure.values())
    elif isinstance(data_structure, tuple):
        structure_sum += len(data_structure)
    elif isinstance(data_structure, list):
        structure_sum += len(data_structure)
    elif isinstance(data_structure, str):
        structure_sum += len(data_structure)
    for i in data_structure:
        return structure_sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
