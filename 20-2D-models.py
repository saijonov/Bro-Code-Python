# fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
# vegetables = ['carrot', 'broccoli', 'spinach', 'pepper', 'tomato']
# meats = ['chicken', 'beef', 'pork', 'lamb', 'turkey']

# groceries = [fruits, vegetables, meats]

# print(groceries[0][0])

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()