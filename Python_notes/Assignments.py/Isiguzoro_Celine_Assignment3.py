'''1. 
Using the concept of for loop, do a multiplication table from 1 - 12 i.s over the range of 1, 13'''
'''rg = range(1, 13)
for num in rg:
    for i in rg:
        print(f'{num} * {i} = {num * i}')'''
multiply = range (1, 13)
for i in multiply:
    for j in multiply:
        product = j * i
        print(f'{i} * {j} = {product}, ')

'''2. 
Using the concept of while loop, write the code for a password checker. 
The code will initialize a password and allow the user to input a password into the system, 
while the user's password does not match the already initialized one after three attempts, the user will receive a message to try again later
but if the user's password matches the initialized password before the maximum attempt is exhausted, the user receives a login successful message'''

'''attempt_count = 0
correct_password = 12345

while attempt_count < 3:
    user_input = input('Enter Password: ').lower()

    if user_input == correct_password:
        print('Login successful!')
        break
    else:
        attempt_count += 1
        if attempt_count < 3:
            print('Try again.')
        else:
            print('Too many attempts, exiting...')'''