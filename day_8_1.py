with open('input8.txt', mode='r') as f:
    data_str = f.readline().strip()

width = 25
height = 6

img_size = width * height
n_of_layers = int(len(data_str)/(width*height))

result_image = ''

for n_pixel in range(img_size):
    layer = 0
    while True:
        if data_str[layer*img_size + n_pixel] == '2':
            layer += 1
        else:
            result_image += data_str[layer*img_size + n_pixel]
            break

print(len(result_image))
print(result_image)

for i in range(height):
    print(result_image[ (i*width) : (width*(i+1)) ])  # noqa

for i in range(height):
    tmp = ''
    for j in range(width):
        tmp += ' ' if result_image[i * width + j] == '0' else '*'
    print(tmp)
