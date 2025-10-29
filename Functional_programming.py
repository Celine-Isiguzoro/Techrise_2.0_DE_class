# def greet():
#     greet = 'Hello'
#     return greet
# y = greet()
# print(y) # The instruction given to python

# def multiplication(n, m = 2): # function takes two parameters n and m
#     '''This is for multiplication'''
#     return n + m

# multiplication(3) #'' 

# n = 3
# m = 4
# multiplication(n, m) # takes arguments

# def people_names(names):
#     '''This is for naming people'''
#     return names 

# names = 'hope'
# people_names(names)

# def fruits(fruit1, fruit2):
#     return (f' I like {fruit1}. But i love {fruit2}')

# def add(n, m):
#     return n + m
# y = add(6,2)
# print(y)

# # To calc for discounted_price
# def discount(price, percentage):
#     d = price * (percentage/100)
#     discounted_price = price - (price * (percentage/100))
#     return discounted_price # Local function can't be called out
# z = discount(345, 23)
# print(z)

# def add(*args):
#     total = sum(args)
#     return total
# y = add(4,5,6)
# print(y)

# def user_profile(**details):
#     profile = {}
#     for key, value in details.items(): 
#         profile[key]= value
#     return profile

# user = user_profile(name = 'cyril')
# print(user)

# def get_age(Name):
#     '''This function gets the user's age'''
#     user_age = input('How old are you? ') # gets the user age
#     return f'{Name}, you are {user_age} years old'

def subtraction(a,b,c=7):
    difference = (a-b) - c
    return difference

x = subtraction(3,2)
print(x)