numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

is_even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", is_even)

squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared_numbers)

greater_than_50 = list(filter(lambda x: x > 50, squared_numbers))
print("Greater than 50:", greater_than_50) 