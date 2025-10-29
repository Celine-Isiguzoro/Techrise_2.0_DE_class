'''age = 16
if age  >= 17:
    print('You can vote')
else: 
    print("You can't vote")

student_score = {'Alice':34, 'Hope': 22, 'Amaka': 88}
for name, score in student_score.items():
    print(f'{name} scored {score}')

rg = range(7,0, -1)
for i in rg:
    print(i)
print('fire down')

# Sum of numbers from 1 to 100
rg = range(1,101)
for i in rg:
    for no in rg:
        print(f'{i} + {no} to give {i + no}')'''

# Using range() with list indexing
'''colors = ['red','yellow', 'green']
for i in range(len(colors)):
    print(f'Color {i +1} :{colors[i]}')'''

'''a = int(input('Enter the number, A: '))
b = int(input('Enter the number, B: '))
if a > b:
    print(f'A-B = {a - b}')'''

#list1 = [0, 12, 56, 27, 65, 78, -8, 65,23]
'''for x in list1:
    if x < 0:
        print('negative error')
        continue
    if x > 2:
        print('Eligible')'''

'''list2 = []
for x in list1:
    if x > 0:
        list2.append(x)
    elif x == 0:
        continue
    elif x < 0:
        continue
print(list2)'''

'''list1 = ["abc", 34, True, 40, "male"]
list1[1:4] =  'hat', 'goat'
print(list1)
for i in range(4):
    for j in range(4):
        print('#', end = '')
    print(z)'''


# To find if a number is even
# x = int((input("Enter a number; ")))
# if x % 2== 0:
#     print("It's an even number")
# else:
#     print("It's an odd number")

# To add two numbers that are even
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
if x % 2 == 0 and y % 2 == 0:
    sum = x + y
    print(f'{x} + {y} = {sum}')
elif not x % 2 == 0 and y % 2 == 0:
    print(f'{x} is not even')
else:
    print('Try another number')
