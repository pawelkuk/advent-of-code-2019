from functools import reduce
import operator
from pprint import pprint
from typing import List


def get_number_of_orbits(node: 'Node') -> int:
    n_of_orbits = 0
    while node.parent:
        n_of_orbits += 1
        node = node.parent
    return n_of_orbits


class Node:
    def __init__(self,
                 val: str,
                 parent=None,
                 children: List['Node'] = None):
        self.val = val
        self.parent = parent
        self.children = children if children else []

    def __repr__(self) -> str:
        parent = self.parent if self.parent else None
        return (f'Node(val="{self.val}", '
                f'parent={repr(parent)},'
                f'children={repr(len(self.children))})')


with open('input6.txt', mode='r') as f:
    data_str = f.readlines()

# data_str = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']  # noqa
data = list(map(lambda x: x.strip().split(')'), data_str))
all_obj = dict.fromkeys(reduce(operator.add, data))

for k in all_obj.keys():
    all_obj[k] = Node(k)

for orbited, orbits in data:
    is_being_orbited_around = all_obj[orbited]
    orbits_around = all_obj[orbits]

    is_being_orbited_around.children.append(orbits_around)
    orbits_around.parent = is_being_orbited_around

tree = all_obj['COM']
sum_ = 0
for node in all_obj.values():
    sum_ += get_number_of_orbits(node)

pprint(sum_)
