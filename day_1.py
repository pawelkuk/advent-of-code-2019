import math

with open('input.txt', mode='r') as f:
    data_str = f.readlines()
data = map(int, data_str)
out = sum(x // 3 - 2 for x in data)
print(out)
# import ipdb; ipdb.set_trace()