# [start:end:step]

credit_number = input("Enter card numbers: ")
# print(credit_number[0]) 
# print(credit_number[0:4:2])

only_numbers = credit_number.replace("-", "")
only_number = only_numbers.replace(" ", "")

last_digits = only_number[12:]
print(f"XXXX-XXXX-XXXX-{last_digits}")