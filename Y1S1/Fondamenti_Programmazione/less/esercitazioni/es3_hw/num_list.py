def sum_el(l:list) -> list:
	i:int = 0
	tmp:int = 0

	for el in range(len(l)):
		tmp += l[el]

	return tmp

def min_max(l: list) -> list:
	min_max = []
	i:int = 0
	M:list = l[0]
	m:list = l[0]

	for i in l[1:]:
		if i > M:
			M = i
		if i < m:
			m = i
	
	min_max.append(m)
	min_max.append(M)

	return min_max

def solo_pari(l:list) -> list:
	pari = []
	el:int = 0

	for el in range(len(l)):
		if l[el] % 2 == 0:
			pari.append(l[el])

	return pari

def uno_volte(l:list) -> int:
	counter:int = 0
	for el in range(len(l)):
		if l[el] == 1:
			counter += 1
	
	return counter


l = [3,1,4,1,5,9,2,6,5,3]
#print("somma di tutti i termini della lista: ", sum_el(l))
print(min_max(l))
#print("numeri pari contenuti nella lista: ", solo_pari(l))
#print("volte in cui si ripete 1 nella lista: ", uno_volte(l))
