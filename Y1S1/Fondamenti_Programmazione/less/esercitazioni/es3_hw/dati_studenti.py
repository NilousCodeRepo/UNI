def media(lista_voti:list[tuple()]) -> dict:
	lv_dict: dict = dict(lista_voti)
	lv_list: list = list(lv_dict.values())
	
	for key,grade in lv_dict.items():
		avg = sum(grade) / len(grade)
		lv_dict[key] = avg
	
	return lv_dict

def elabora_dati(dati):
	m:dict = media(dati)
	
	print("studenti in ordine di voto decrescente: ", ordine)
	print("studenti con voto >= di 9: ", almeno_9)


studenti = [
	("Alice", [8, 7, 9, 6]),
	("Bob", [9, 8, 10, 7]),
	("Charlie", [6, 5, 7, 8]),
	("Diana", [10, 9, 9, 8])
]

risultati = elabora_dati(studenti)
print(risultati)
