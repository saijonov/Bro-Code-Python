# def hello(greeting, title, first_name, last_name):
#     print(f"{greeting} {title} {first_name} {last_name}")

# hello(first_name = "Said", greeting="Hello", title = "Mr", last_name = "Dadajanov")

# for x in range(1,11):
#     print(x, end=" ")

# print("1", "2", "3", sep="-")

def get_phone(country_code, area_code, first, last):
    return f"+{country_code}({area_code}){first}-{last}"
phone_num = get_phone(country_code=+1, area_code=989, first=456, last=9653)
print(phone_num)