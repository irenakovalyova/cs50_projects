from cs50 import get_int

height = 0

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

width = 1
spaces = height - width

for i in range(0, height, 1):
    print(" " * spaces, end="")  # Adding white spaces before dashes
    print("#" * width, end="")  # Adding first set of dashes
    print(" " * 2, end="")  # Adding white spaces between the two sets of dashes
    print("#" * width)  # Adding the second set of dashes
    width += 1
    spaces -= 1
