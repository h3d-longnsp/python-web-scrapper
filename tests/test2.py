list_of_tuples = [(1, 2), (None, None), (8, 9)]
filtered_list = [tpl for tpl in list_of_tuples if not any(x is None for x in tpl)]


print(filtered_list)