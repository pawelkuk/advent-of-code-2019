def calc_fuel(mass: int) -> int:
    fuel: int = mass // 3 - 2 
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)

with open('input.txt', mode='r') as f:
    data_str = f.readlines()
data = map(int, data_str)

out = sum(calc_fuel(x) for x in data)
print(out)