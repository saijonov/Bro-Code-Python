unit = input("Is that temperature in C or F? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    result = (temp*9/5)+32
    print(result)
elif unit == "F":
    result=(temp-32)+5/9
    print(result)
else:
    print("Invalid")