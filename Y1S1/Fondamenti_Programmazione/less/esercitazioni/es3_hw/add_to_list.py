def add_to_list(lista: list) -> list:
	new_lista = []

	index:int = 0
	value:int = 0
	
	lista.append(11)
	lista.insert(index, value)
	
	for i in range(len(lista)):
		if lista[i] != 5:
			new_lista.append(lista[i])
	
	return new_lista


l = [1,2,3,4,6,5,7,8,9,10]
returned_list = add_to_list(l)

print(returned_list)
print("lunghezza lista:",len(returned_list))
# devo fare così altrimenti len() mi restituisce la lunghezza della lista l
# ma a me serve new_lista, quindi il valore ritornato da f() che è una copia
# della lista originale, quindi fare len(l) non ha senso, in quanto io modifico
# la copia non l'originale.
