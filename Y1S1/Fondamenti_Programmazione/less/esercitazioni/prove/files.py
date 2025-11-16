#scrivi nel file almeno una parola
def write_file(file_path:str):
	with open(file_path, encoding = 'utf8',mode = "at") as f:
		string:str = input("inserire stringa da inserire nel file: ")
		f.write(string)



def notalpha(text: str) -> set[str]:
	char = set(text)
	
	return {
						c
						for c in char
							if not c.isalpha()
					}

def rimpiazza_con_spazi(text:str, notalpha: set[str]) -> str:
	
	for char in notalpha:
		text = text.replace(char, ' ')
	
	return text


#leggi un file e torna tutte le istanze di parole con "a" in una lista
def read_file(file_path:str) -> list:
	lista:list = []
	l_final: list = []

	with open(file_path, encoding = 'utf8',mode = "rt") as f:
		text:str = f.read()
		text = text.lower()
		
		nonalfa = notalpha(text)
		
		text =rimpiazza_con_spazi(text, nonalfa)	
		text = text.split()

		lista.append(text)
		for el in lista:
			for c in el:
				if 'a' in c:
						l_final.append(c)
	return l_final


fp:str = input("inserire nome del file che si vuole aprire: ")
write_file(fp)

print("lista di parole che hannno 'a' all'interno: ",read_file(fp))
