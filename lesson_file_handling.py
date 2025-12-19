import os

# To know the directory being worked on
# current_working_dir = os.getcwd()
# print(current_working_dir)

# To check for file extension
# direct = r"C:\Users\LENOVO\Desktop\Python_tutorials\assignment_trial.py"
# dee = direct.replace("\\", "/")
# if os.path.exists(dee):
#     print("Found")
# else:
#     print("Not Found")

# To create a directory
# os.mkdir("New directory")
# print("Successful") 

# To list the contents of a directory
# os.listdir("c:/Users/LENOVO/Desktop/Python_tutorials/lesson_file_handling.py")
# print("Successful")

# To list out the items in a folder
# items_dir = os.listdir(os.getcwd())
# for i in items_dir: # To list one after the other
#     print(i)
# print(items_dir) # Printing the items in a list

# To change directory
# os.chdir(r"C:\Users\LENOVO\Desktop\Python_tutorials\new_directory")

# To read a file using with open
# with open ("lesson_file_handling.py", "r") as file:
#     content = file.read()
# print(content)

# To read a line in a file
# with open ("lesson_file_handling.py", "r") as file:
#     lines  = file.readlines()
#     print(lines[0:3]) # To slice lines for printing
    # for line in lines:
    #     print(lines[2:5], end= "")

# with open("leson_file_handling.txt", "w") as f:
#     f.write("Cyril is still not a nice person, he has never bought me biscuit since day one")
#     print("Successfully replaced")

# Writing in a file in lines
# lines = ["Cyril has always shouted at me\n", "He is always hiding his pen\n", "He is hairy like chimpanze"]
# with open("leson_file_handling.txt", "w") as file:
#     file.writelines(lines)
#     print("Success")

# Append to a file already created
# lines = ["\n He is tall sha but I'm taller\n", "He is always threatening me as well"]
# with open("leson_file_handling.txt", "a") as file:
#     file.writelines(lines)
#     print("I'm trying abeg")

# Using flush
#with open("example.txt", "w+") as nf:
    #nf.write("My younger brother will be signing out soon and my family members are sewing clothes for the event")
    # Flush ensures that it is written in a disk(ROM 256ssd) and not in memory(RAM)
    # nf.flush()
    # Python moves the file from RAM to ROM so that it will be given a location using the seek method
    # The location doesn't change in the ROM 
    # nf.seek(1, 0) # Move the pointer to that point and read from there
    # To read the next few chracters
    # data = nf.read(8)
    # nf.seek(3, 0)
    # nf.write("baby")
    # data = nf.read(30)
    # print(f"Data read before replacement")

# To change the name of the current directory
# current_name = "example.txt"
# new_name = "changed.txt"
# os.rename(current_name, new_name)
# print(f"{new_name}")

# # To delete a directory
# os.remove("changed.txt")
# print("file has been deleted")

# # To open a new file and write
# with open("csv_handler.py", "w") as file:
#     file.write("# CSV management") 

# Create a function to collect data (user details) from user and store it as textfile while incorporating error handling
# data = []
# def user_details():
#     try:
#         with open("user_details.txt", "w") as txt:
#             Name = input("Enter your name: ").title()
#             if not Name.isalpha():
#                 raise ValueError ("Enter letters not digits")
#             Age = int(input("Enter your age: "))
#             if Age < 16:
#                 raise ValueError ("You are not qualified")
#             Fav_colour = input("Enter your favourite colour: ")
#             if not Fav_colour.isalpha():
#                 raise ValueError ("enter letters not digits")
#     except FileNotFoundError:
#             print("File not found")
#     except ValueError as e:
#             print("Enter correct data")
#     finally:
#             print("Successful")
# user_details()

# with open("user_details.txt", "w") as file:
#     data1 = "User_ID, Name, Age, Colour"
#     file.write(data1)
# print("Success")

# import csv
# with open("user_dtails.csv", "w") as csv_file:
#     data1 = "User_ID, Name, Age, Colour\n"
#     data2 = "1, Mark, 78, Blue\n"
#     data3 = "2, Alice, 25, Green"
#     csv_file.write(data1)
#     csv_file.write(data2)
#     csv_file.write(data3)
# print("Success")

# Passing a list in a csv file
# data = [
#         ["User_ID","Name", "Age", "Colour"],
#         [1, "Mark", 78, "Blue"],
#         [2, "Alice", 21, "Purple"],
#         [3, "Cyril", 27, "Brown"],
#         [4, "Amaka", 32, "Red"],
#         [5, "Zeph", 30, "Blue"],
#         [6, "Jonah", 34, "Black"]]
# with open("user_details.csv", "w", newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(data)
# print("Success")

# To read
# import csv
# with open("user_details.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     #First row is usually the header
#     headers = next(reader)
#     print(f"Columns: {headers}") # Print the headers
#     #for row in reader: #iterate through each row
#     for row in reader:
#         user_id = row[0]
#         name = row[1]
#         age = row[2]
#         colour = row[3]
#         print(f"User: {user_id}:My name is {name}, and I am {age} years old and I love {colour}")

# # Writing to a csv file with DictWriter
# users = [{"User_ID": 1,
#           "name": "Ezra",
#           "email": "ezranehmiah@gmail.com",
#           "signup_date": "2025-09-29",
#           "status": "Active"},
#           {"User_ID": 2,
#            "name": "Cyril",
#            "email": "ehiemerecyril@gmail.com",
#            "signup_date":"2025-09-29",
#             "status": "not active"},
#             {"User_ID": 3,
#            "name": "Chikodi",
#            "email": "ehiemerechikodi@gmail.com",
#            "signup_date":"2025-09-29",
#             "status": "active"}]
# with open("user_details.csv", "w", newline="") as file:
#     # fieldnames_ = ["User_ID", "name", "email", "signup_date", "status"] # All the keys in the dict
#     writer = csv.DictWriter(file, fieldnames= ["User_ID", "name", "email", "signup_date", "status"])
#     writer.writeheader()
#     writer.writerows(users)
# print("csv created with DictWriter")

# # To read a dict
# with open("user_details.csv", "r") as file:
#     reader = csv.DictReader(file)
#     print("-" * 40)
#     # Each row is now a dictionary
#     for row in reader:
#         # print(row)
#         print(f"User: {row["User_ID"]}")
#         print(f"Name: {row["name"]}")
#         print(f"Email: {row["email"]}")
#         print(f"Status: {row["status"]}")
#         print(f"Signup_date: {row["signup_date"]}")
#         print("-" * 40)

# import json
# data = {"User_ID": 1,
#           "name": "Ezra",
#           "email": "ezranehmiah@gmail.com",
#           "signup_date": "2025-09-29",
#           "status": "Active"}
# with open("data.json", "w") as file:
#     x = json.dump(data, file, indent=4)
#     print("JSON file created")
#     print(type(x))

# thislist = ["apple", "banana", "cherry", "Pineapple"]
# thislist[1:2] = ["blackcurrant", "watermelon", "Udara", "Plum"]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "pineapple"]
# list2 = []
# for x in thislist:
#     if "a" in x.lower:
#         print(thislist)

# newlist = [x if x != "banana" else "orange" for x in thislist]
# print("orange" for x in newlist)

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(name = "Buddy", animal = "dog")


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = {"mango", "pineapple", "papaya"}
# tropical.extend(thislist)
# print(tropical)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# with open ("numpy.py", "w") as file:
#     file.write("Numpy")
# print("Successful")
# import os
# os.rename("numpy.py", "numpy_class.py")
# print("success")

# with open("pandas_class.py", "w") as pandasfile:
#     pandasfile.write("Pandas Class")

# with open("cpn_assessment.py", "w") as file:
#     file.write("CPN")

# with open("visualization.py", "w") as visual:
#     visual.write("import matplotlib")

# os.mkdir("Visualization_dir")

with open("isiguzoro_assg7.py", "w") as file:
    file.write("import matplotlib")
