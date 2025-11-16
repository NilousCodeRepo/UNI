def unique_letters(s1:str,s2:str) -> str:
	s3 = set(s1) & set(s2)
	return s3

print(unique_letters("python", "giove"))
