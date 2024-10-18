# dictionary is a collection of key and value

capitals = {"USA": "Washington D.C.",
            "India":"New Dehli",
            "Russia": "Moscow",
            "China":"Beijing"}

# print(dir(capitals))

# print(capitals.get("USA"))

# capitals.update({"USA": "Florida"})
# print(capitals.get("USA"))

# capitals.pop("China")
# print(capitals)

# keys = capitals.keys()
# values = capitals.values()

# print(keys)
# print(values)

# for key in keys:
#     print(key)

items = capitals.items()
# print(items)
for key, value in capitals.items():
    print(f"{key}:{value}")