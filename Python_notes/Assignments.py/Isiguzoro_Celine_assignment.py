'''import re

def is_palindrome(text):
    cleaned = re.sub(r'[^a-z0-9]', '', str(text).lower())
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text

def check_palindromes(items):
    for item in items:
        if is_palindrome(item):
            print(f"{item} is a palindrome!")
        else:
            print(f"{item} is not a palindrome")

My_list = [
    'mummy',
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon, no melon',
    'some men interpret nine memos',
    'madam'
]

check_palindromes(My_list)
'''
# Second assignment 


import time # Import the time library

list1 = [] # an empty set
while True:
  item = input("Enter item for list1: ")
  list1.append(item)
  done = input("Are you through (yes/no): ").lower()
  if done == "yes":
    break

list2 = []
while True:
  item = input("Enter item for list2: ")
  list2.append(item)
  done = input("Are you through (yes/no): ").lower()
  if done == "yes":
    break

if len(list1) != len(list2):
  print("Length of lists don't match.")
else:
  print("Lengths match. Proceeding", end="")
  for _ in range(3):
    time.sleep(1)
    print(".", end="")
  print()
  
  my_dictionary = dict(zip(list1, list2))
  print("The result of the dictionary is:", my_dictionary)


