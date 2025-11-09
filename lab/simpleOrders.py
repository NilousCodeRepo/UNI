menu = {"pizza":8, "pasta":7, "insalata":5}
tot = 0
while True:
	scelta = input("inserire piatto, digita 'stop' per uscire:")
	if scelta.lower() == "stop":
		break

	if scelta in menu.keys():
		tot += (int(menu.get(scelta)))
	else:
		while True:
			print("""piatto non esistente.
Inserisci nuovo piatto(enter). Per uscire digita 'stop':""")
			s = input()
			if s.lower() == "stop":
				break	
			else:
				key = input("inserire nuovo piatto: ")
				value = input("inserire prezzo del nuovo piatto: ")
				new_menu = {key:value}
	menu.update(new_menu)	

print(f"totale da pagare: {tot}")
