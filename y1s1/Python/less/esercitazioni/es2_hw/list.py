lista = ["a", "b", "c"]
quanti = 2
for index in range(quanti):
    lista.append(input("Frutto da aggiungere:\t"))

for (index, el) in enumerate(lista):#enum fornisce  una tupla formata dagli indici e dagli elementi della lista
    print(f"{el} all'indice {index+1}")
    
