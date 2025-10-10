import random
segreto = random.randint(1,20)
for i in range(1,5):
	scelta = int(input("scegliere un numero da 1 a 20: "))
	if scelta >= segreto: 
		print("alto")
	if scelta <= segreto: 
		print("basso")
	if scelta == segreto:
		print("hai vinto")
		break
