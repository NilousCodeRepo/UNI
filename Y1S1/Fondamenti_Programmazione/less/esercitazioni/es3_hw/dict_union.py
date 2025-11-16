def dict_union(d1:dict, d2:dict)-> dict:
	result = {}

	for key, value in dict1.items():
		if key in dict2:
			result[key] = value + dict2[key]
		else:
			result[key] = value

	for key, value in dict2.items():
		if key not in dict1:
			result[key] = value

		return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(dict_union(dict1,dict2));
