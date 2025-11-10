def dict_string(s:str) -> dict:
	d:dict = {}
	counter:int = 0
	
	for el in s:
		d[el] = counter
		counter+=1

	return d 

s = "ciao"
print(dict_string(s))
