# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(8,6,9,6,5,4,8))

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(8,6,9,6,5,4,8))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Said", "Gani", "Dadajanov")
        


## KWARGS

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# print_address(street ="123 Fake City", city="Detroit", state="MI", zip="54321")

# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key, end=" ")

# print_address(street ="123 Fake City", city="Detroit", state="MI", zip="54321")





## args kwargs togther

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end=", ")

# shipping_label("Mr.", "Said", "Dadajanov",
#                street="123 fake street",
#                city="detroit",
#                zip="85632")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('zip')}")

shipping_label("Mr.", "Said", "Dadajanov",
               street="123 fake street",
               apt = '456',
               city="detroit",
               zip="85632")