def split_string(string: str, characters: str = '') -> list[str]:
	list(string)
	new_string = []
	for index in range(len((string))):
		if characters in string:
			new_string[i] = string[:index] 
			

#print(string.split("o")) desired output:['cia', ' c', 'me va?']

split_string("ciao come va?", "o")
