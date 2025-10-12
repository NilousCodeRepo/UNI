def replace_substring(string: str, find: str, replace) -> str:
	if find in string:
		for index in range(len(string)):
			if string[index] in find:
				string = string[:index] + replace + string[index+1:] 
	else:
		print(f"there is no {find} in {string}")
	
	print(string)

replace_substring("ciao come va?", "ci", "o")
