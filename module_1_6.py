my_dict = {"Lena": 2005, "Katya": 2001, "Kirill": 2010}
print(my_dict)
print(my_dict.get("Lena")), print(my_dict.get("Lera", "Такого ключа нет "))
my_dict["Ira"] = 1996
my_dict["Vasya"] = 1990
print(my_dict)
del my_dict["Vasya"]
print(my_dict)
my_set = {1, 2, 3, 4, 5, 6, 2, 3, 4, 5, "Nais", True, (1, 2, 3, 4)}
my_set.add(14)
my_set.add(13)
print(my_set)
my_set.remove(14)
print(my_set)
