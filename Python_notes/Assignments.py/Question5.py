counter = 0

def increment_counter():
    global counter
    counter += 1
    

    
def get_counter():
    return counter

def reset_counter():
    global counter
    counter = 0

for _ in range(5):
    increment_counter()

print(get_counter())

reset_counter()

print(get_counter())