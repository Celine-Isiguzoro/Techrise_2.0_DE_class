def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

def print_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

print("Right Triangle:")
print_right_triangle(4)
print("\nPyramid:")
print_pyramid(3)
print("\nNumber Pyramid:")
print_number_pyramid(3)s