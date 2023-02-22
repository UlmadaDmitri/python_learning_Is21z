list = ["Apple", 7, 1, 9, "Plum", "Lemon", 0]
sorted_list = sorted(list, key=lambda x: (isinstance(x, str), x))
print(sorted_list)
