from functools import reduce
import operator
from typing import List, Tuple


def get_number_of_orbits(node: "Node") -> int:
    n_of_orbits = 0
    while node.parent:
        n_of_orbits += 1
        node = node.parent
    return n_of_orbits


def get_distance(
    origin: "Node", destination: "Node", came_from: "Node" = None
) -> Tuple[int, bool]:
    all_ = (
        origin.children[:]
        if origin.parent is None
        else [origin.parent, *origin.children]
    )
    if destination in all_:
        return 1, True
    else:
        for node in all_:
            if node != came_from:
                dist, status = get_distance(node, destination, origin)
                if status is True:
                    return dist + 1, True
    return -1, False


class Node:
    def __init__(self, val: str, parent=None, children: List["Node"] = None):
        self.val = val
        self.parent = parent
        self.children = children if children else []

    def __repr__(self) -> str:
        parent = self.parent if self.parent else None
        return (
            f'Node(val="{self.val}", '
            f"parent={repr(parent)},"
            f"children={repr(len(self.children))})"
        )

    def __eq__(self, other) -> bool:
        res = True if self is other else False
        return res


if __name__ == "__main__":
    with open("input6.txt", mode="r") as f:
        data_str = f.readlines()

    # data_str = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']  # noqa
    data = list(map(lambda x: x.strip().split(")"), data_str))
    all_obj = dict.fromkeys(reduce(operator.add, data))

    for k in all_obj.keys():
        all_obj[k] = Node(k)

    for orbited, orbits in data:
        is_being_orbited_around = all_obj[orbited]
        orbits_around = all_obj[orbits]

        is_being_orbited_around.children.append(orbits_around)
        orbits_around.parent = is_being_orbited_around

    tree = all_obj["COM"]
    sum_ = 0
    for node in all_obj.values():
        sum_ += get_number_of_orbits(node)

    YOU = all_obj["YOU"]
    SAN = all_obj["SAN"]
    # breakpoint()
    dist, status = get_distance(YOU, SAN, SAN)
    print(dist, status)
