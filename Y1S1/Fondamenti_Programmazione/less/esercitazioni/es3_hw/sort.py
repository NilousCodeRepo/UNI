nomi = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print("nomi in ordine alfabetico: ", nomi)

print("nomi in ordine di lunghezza: ", sorted( nomi, key = lambda s: len(nomi) ))

print("nomi in ordine di lunghezza inversa: ", sorted( nomi, key = lambda s: len(s),
																							 reverse=True) )

