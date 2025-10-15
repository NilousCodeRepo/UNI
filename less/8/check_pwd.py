def check_pwd(pwd: str) -> bool:
	pwd = input("inserire password: ")
	if len(pwd) >= 6 and <= 16:
		
	else:
		if len(pwd) < 6:
			print("ERRORE: password troppo corta")
		if len(pwd) > 16:
			print("ERRORE: password troppo lunga")
	
