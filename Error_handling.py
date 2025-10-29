# Key error
'''dict1 = {'name': 'hope', 'place': 'aba'}
print(dict1['hope'])'''

# FileNotFound error
'''file = open('Data_set.txt')
print(file)'''

# AttributeError
# int1 = 10
# int1.append(5)
# print(int1)

# Try and Except using ZeroDivision error
# try:
#     value = int(input('Enter a number: '))
#     result = 100/value
#     print(result)
# except ValueError:
#        print('You must enter a valid number')
# except ZeroDivisionError:
#     print('Invalid number')
# finally:
#     print('😒')

# Open user form
# try:
#     user_data = open('data.txt','r')
#     content = f.read()
# except FileNotFoundError:
#     print('File not found')
# finally:
#     print('Closing file...')

# Collection of even numbers
# even_number = []
# try:
#     number = input('Enter the number: ').strip()
#     if not number.isdigit():
#         raise ValueError ('Not digit')
#     no = int(number)
#     if no < 2:
#         raise ValueError ('Number is less than 2')
# except ValueError as e:
#     print(f'Enter even number: {e}')
# else:
#     if no % 2 == 0:
#         even_number.append(number)
#         print(even_number)
#     else:
#         print('not even')
class ZeroError(Exception):
    '''This is the error raised if the number is zero'''
    pass
even_number = []
while True: # To allow the list to keep growing
    try:
        number = input('Enter the number: ').strip()
        if not number.isdigit():
            raise ValueError ('Not digit')
        no = int(number)
        if no == 0:
            raise ZeroError ('Number is zero')
        if no < 2:
            raise ValueError ('Number is less than 2')
    except ZeroError as z:
        print(f'Number must be greater than 0{z}')
    except ValueError as e:  # Runs when there's error
        print(f'Enter even number: {e}')
    else: # Runs when there's no error
        if no % 2 == 0:
            no = int(number)
            even_number.append(no)
            print(even_number)
        else:
            print('not even')
    finally:
        print('You can stop now')
        

        
