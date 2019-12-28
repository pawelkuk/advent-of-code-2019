from typing import List
from collections import deque
from typing import Deque, Tuple
from itertools import permutations

BI_OPERATIONS = {1: lambda x, y: x + y, 2: lambda x, y: x * y}

UNARY_OPERATIONS = [3, 4]

JUMP_OPERATIONS = [5, 6, 7, 8]


def parse_instruction(instr: int) -> Tuple[Tuple[int, ...], int]:
    padded_instr = "0" * (5 - len(str(instr))) + str(instr)
    # str of the form ABCDE
    DE = int(padded_instr[-2:])
    C = int(padded_instr[2])
    B = int(padded_instr[1])
    A = int(padded_instr[0])
    return (C, B, A), DE


def compute(x: List[int], inputs: Deque[int]) -> Tuple[int, List[int]]:
    idx = 0
    returns = []
    while x[idx] != 99 and idx < len(x):
        modes, operation = parse_instruction(x[idx])
        if operation in BI_OPERATIONS:
            arg_0 = x[idx + 1] if modes[0] else x[x[idx + 1]]
            arg_1 = x[idx + 2] if modes[1] else x[x[idx + 2]]
            if modes[2] == 0:
                x[x[idx + 3]] = BI_OPERATIONS[operation](arg_0, arg_1)
            elif modes[2] == 1:
                x[idx + 3] = BI_OPERATIONS[operation](arg_0, arg_1)
            idx += 4
            continue
        elif operation in UNARY_OPERATIONS:
            if operation == 3:
                if modes[0] == 0:
                    x[x[idx + 1]] = inputs.popleft()
                elif modes[0] == 1:
                    x[idx + 1] = inputs.popleft()
            if operation == 4:
                returns.append(x[idx + 1] if modes[0] else x[x[idx + 1]])
            idx += 2
        elif operation in JUMP_OPERATIONS:
            # breakpoint()
            arg_0 = x[idx + 1] if modes[0] else x[x[idx + 1]]
            arg_1 = x[idx + 2] if modes[1] else x[x[idx + 2]]
            arg_2 = idx + 3 if modes[2] else x[idx + 3]
            if operation == 5:
                if arg_0 != 0:
                    idx = arg_1
                else:
                    idx += 3
                continue
            if operation == 6:
                if arg_0 == 0:
                    idx = arg_1
                else:
                    idx += 3
                continue
            if operation == 7:
                x[arg_2] = 1 if arg_0 < arg_1 else 0
                idx += 4
                continue
            if operation == 8:
                x[arg_2] = 1 if arg_0 == arg_1 else 0
                idx += 4
                continue
    return x[0], returns


with open("input7.txt", mode="r") as f:
    data_str = f.readline()
data = list(map(int, data_str.split(",")))

test_1 = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
test_1_comp, out_codes = compute(test_1, deque([8]))
assert out_codes == [1]
test_1_comp, out_codes = compute(test_1, deque([9]))
assert out_codes == [0]

test_2 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
test_2_comp, out_codes = compute(test_2, deque([7]))
assert out_codes == [1]
test_2_comp, out_codes = compute(test_2, deque([8]))
assert out_codes == [0]

test_3 = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
test_2_comp, out_codes = compute(test_3, deque([8]))
assert out_codes == [1]
test_2_comp, out_codes = compute(test_3, deque([7]))
assert out_codes == [0]

test_4 = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
test_2_comp, out_codes = compute(test_4, deque([7]))
assert out_codes == [1]
test_2_comp, out_codes = compute(test_4, deque([8]))
assert out_codes == [0]

test_5 = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
_, out_codes = compute(test_5, deque([0]))
assert out_codes == [0]
_, out_codes = compute(test_5, deque([21]))
assert out_codes == [1]

# input_deque = deque([5])
# result, out_codes = compute(data, input_deque)
# data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]  # noqa
max_ = 0
max_perm = tuple()
for perm in list(permutations(range(5))):
    input_ = 0
    for i in perm:
        _, out_ = compute(data[:], deque([i, input_]))
        input_ = out_[-1]
    max_ = max(max_, input_)
    max_perm = perm if max_ == input_ else max_perm

print(max_)
print(max_perm)
# print(out_codes)
