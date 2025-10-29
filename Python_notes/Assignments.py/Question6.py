
def multiplication_table(number, upto=10):
    for i in range(1, upto + 1):
        print(f"{number} × {i} = {number * i}", end = ' ')

multiplication_table(7)
print()
multiplication_table(3, 5)