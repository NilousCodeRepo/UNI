def check_pwd() -> bool:
    al = "abcdefghijklmnopqrstuvwxyz"
    pwd = input("inserire password: ")
    if len(pwd) >= 6 and len(pwd) <= 16:
        elif pwd in al:
	         
	else:
		if len(pwd) < 6:
			print("ERRORE: password troppo corta")
		if len(pwd) > 16:
			print("ERRORE: password troppo lunga")
	return True

check_pwd()
