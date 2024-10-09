# name = input("Enter your full name: ")
# number = input("enter your phone number: ")
# result = len(name)
# result = name.find(" ")
# result = name.rfind("a")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = number.replace("-", " ")
# print(result)

# print(help(str))

username = input("Enter a username: ")

if username.find(" ") != -1 or not username.isalpha() or len(username) >= 12:
    print("Nope")
else:
    print("Yes")
