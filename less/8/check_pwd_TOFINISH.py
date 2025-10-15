# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.

def check_pwd() -> bool:
	pwd = input("inserire password: ")
	if len(pwd) >= 6 and len(pwd) <= 16:
		pass
	else:
		if len(pwd) < 6:
			print("ERRORE: password troppo corta")
		if len(pwd) > 16:
			print("ERRORE: password troppo lunga")

	return True

check_pwd()

