# Creazione di un dizionario vuoto
voti = {}

# Ciclo per raccogliere i voti
while True:
    nome = input("Inserisci il nome dello studente (o 'fine' per terminare): ")
    if nome.lower() == "fine":
        break

    voto_input = input("Inserisci il voto (1-10): ")
    
    # Controllo che il voto sia un numero e compreso tra 1 e 10
    try:
        voto = int(voto_input)
        if 1 <= voto <= 10:
            voti[nome] = voto #aggiungo valore voto a chiave nome
        else:
            print("Il voto deve essere tra 1 e 10. Riprova.")
    except ValueError:
        print("Per favore, inserisci un numero valido.")

# Calcolo e stampa dei risultati
studenti_sufficienti = sum(1 for voto in voti.values() if voto >= 6)

print(f"\nNumero di studenti con voto ≥ 6: {studenti_sufficienti}")
print("\nTabella dei nomi e voti:")
print("Nome\tVoto")
for key, value in voti.items():
    print(f"{key}\t{value}")

