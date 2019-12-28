with open("input8.txt", mode="r") as f:
    data_str = f.readline().strip()

width = 25
height = 6

n_of_pixels = width * height
n_of_layers = int(len(data_str) / (width * height))

min_zeros = 10000000
result = 0
for i in range(n_of_pixels):
    layer = data_str[(n_of_layers * i) : (n_of_layers * i + n_of_pixels)]
    zeros = layer.count("0")
    min_zeros = min(min_zeros, zeros)
    if min_zeros == zeros:
        result = layer.count("2") * layer.count("1")

print(min_zeros)
print(result)
