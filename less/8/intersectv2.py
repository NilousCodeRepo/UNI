def intersect(a: list, b: list) -> list:
	return [el
			for el in a
				if el in b
			]#list comprehension


a = [1,2,3]
b = [3,4,5]
print(intersect(a,b))
