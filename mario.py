from cs50 import get_int

height = 0

while True:
    height = get_int("Height: ")
    if height > 1 and height < 9:
        break

width = 1
spaces = height - width

for i in range(0, height, 1):
    for j in range(1, (spaces + 1), 1):
        print(" ", end = '')
        
    for z in range (1, (width + 1), 1):
        print("#", end = '')
        
    for s in range (0, 2, 1):
        print(" ", end = '')
        
    for h in range(1, (width + 1), 1):
        print("#", end = '')
    
    print("\n")   
    width += 1
    spaces -= 1