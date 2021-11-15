from cs50 import get_int

height = 0

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

width = 1
spaces = height - width

for i in range(0, height, 1):
    print(" " * spaces, end="")
    print("#" * width, end="")
    print(" " * 2, end="")
    print("#" * width)
    width += 1
    spaces -= 1
