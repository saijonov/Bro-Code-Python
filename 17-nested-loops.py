# count to 9 3 times
# for x in range(3):
#     print(" ")
#     for x in range(1, 10):
#         print(x, end="")



# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("enter a sybol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()


def draw_hollow_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            # Print '*' for the borders and space for the inside
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("*", end=" ")  # Print star for borders
            else:
                print(" ", end=" ")  # Print space for inside
        print()  # Move to the next line after finishing a row

# Example usage
draw_hollow_rectangle(10, 5)



