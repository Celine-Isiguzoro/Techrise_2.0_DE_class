'''1. Write a code to do the following: the code takes in two numbers A and B. 
It then subtracts B from A if A is greater than B with the message"A-B='A-B' " 
where 'A-B' is the difference of A and B. If B is greater than A.,
it then subtracts A from B and gives the message"B-A='B-A'" 
where 'B-A' the the difference between B and A. 
When both conditions are  negative, the program should give the corresponding message.'''

a = int(input('Enter A: '))
b = int(input('Enter B: '))
if a > b:
    print(f'A - B = {a-b}')
elif b > a:
    print(f'A - B = {b-a}')
else:
    print('A and B are equal')

'''2. Write a code to take in a string of any lenght.
if there are spaces between words, they are removed.
non alphabetical characters are also removed.
if the index of a particular alphabet is even, the program converts it to a capital letter 
and if the index number is odd, it is converted to a small letter.
The resulting string is then printed out. Note: Do not use any list when writing the code'''
str1 = str(input('Enter input: '))
resulting_string = ''
string_index = 0
for x in str1:
    if x.isalpha(): # Eliminates spaces and non- alphabetical characters
        if string_index % 2 == 0: # To check if it's even
            resulting_string += x.upper() # the result is converted to capital letter if it's even
        else:
            resulting_string += x.lower()
        string_index += 1
print(resulting_string)

'''3. Okoro and sons company recently advertised vacancies.
The number of applicants are much and have to be pruned down while the successfull applicants are to be fixed in
the following departments: Engineering, Admin, Customer Care and Security based on certain criteria. 
The company has a policy of not employing people that are not up to 18 years. 
Any man not up to 25 years old is placed in Customer care department. 
Any woman below 31 years is also placed in the Customer care department. 
Any man below 45 years old is posted to the Engineering department.
The rest of the women are posted to the Admin department.
The rest of the men are recruited as security men. 
All successful applicants should not exceed 50 years of age. 
write a code to place all the personnel in their various departments accordingly immediately they make their 
application(if they are eligible)'''
'''
Departments in the company:
Engineering
Admin
Customer care
Security
'''
# This excludes people below 18 and above 50 automatically
age = int(input('Enter your age: '))
if age < 18 or age > 50:
    print('You are not eligible')
    exit()

# This converts all gender inputs to lower case
gender = input('What is your gender: ').lower()

# Males above 18 and below 25 are kept in the customer care department
if gender == 'male' and age >= 18 and age < 25:
    print('You are in the customer care department')

# Females below 31 are kept in the customer care department
elif gender == 'female' and age < 31:
    print('You are in the customer care department')

# Males between the ages of 25 and 45 are kept in engineering department
elif gender == 'male' and age>= 25 and age < 45:
    print('You are in the engineering department')

# Females between the ages of 31 and 50 are kept in the admin department
elif gender == 'female' and age >= 31 and age <= 50:
    print('You are in the admin department')

# Males between the ages of 45 and 50 are kept in the security department
elif gender == 'male' and age >= 45 and age <= 50:
    print('You are in the security department')
