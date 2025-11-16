def area_rect(w, h=None) -> int | float:
	area:int = int()
	if h == None:
		print("altezza non presente")
		exit
	else:
		area = w*h
	return area

print(area_rect(1,2))
