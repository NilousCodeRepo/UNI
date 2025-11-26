"""
Prende una lista di tuple (nome, [lista_voti]) e restituisce:
DONE - Dizionario con nome -> media voti
DONE - Lista studenti ordinata per media decrescente
DONE - Set degli studenti che hanno almeno un voto >= 9
- Statistiche globali (media classe, voto max, voto min)
"""

def media(lista_voti:list[tuple()]) -> dict:
	lv_dict: dict = dict(lista_voti)#necessario per creare la lista dei voti
	
	for key,grade in lv_dict.items():
		avg = sum(grade) / len(grade)
		lv_dict[key] = avg

	return lv_dict


def elabora_dati(dati):
	m:dict = media(dati)
	rev_sort_m = list(reversed(sorted(m.keys())))
	s: list = []

	print("studenti con media in ordine decrescente:", rev_sort_m)
	
	for key,value in m.items():
		if value >= 9:
			s.append(key)
		
	print("studenti con voto >= di 9: ", s)

def global_stats(studenti) -> dict:	
	stats: dict = {}#chiave nome, valore = tupla(voto M, voto m)
	stats.update(studenti)

	for key,value in stats.items():		
		for i in list(value):
			M = max(value)	
		for i in list(value):
			m = min(value)
	
		t_voto: tuple = (M,m)

		stats[key] = t_voto

	return stats

studenti = [
	("Alice", [8, 7, 9, 6]),
	("Bob", [9, 8, 10, 7]),
	("Charlie", [6, 5, 7, 8]),
	("Diana", [10, 9, 9, 8])
]

risultati = elabora_dati(studenti)
print(risultati)
print(global_stats(studenti))
