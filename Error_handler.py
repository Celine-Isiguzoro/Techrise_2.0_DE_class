# Retirement age calculator
# worker_age = input('Enter worker age: ').strip()
# if worker_age.isdigit():
#     retirement_age = age + 33
#     print(retirement_age)

# else:
#     print('type in figure')
try: 
    worker_age = input('Enter worker age: ').strip()
    if not worker_age.isdigit():
        raise ValueError ('Enter age in figure')
    age = int(worker_age)
    if not 18 <= age <= 25:
        raise ValueError ('Worker\'s age must be between 18 and 25')
except ValueError as e:
    print(f'Enter correct information: {e}')
else:
    retirement_age = age + 35
    print(f'You will retire at age {retirement_age} years old.')
finally:
    print('🙌')