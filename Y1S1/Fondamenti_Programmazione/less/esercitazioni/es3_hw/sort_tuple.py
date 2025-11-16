studenti = [('Alice', 85), ('Bob', 92), ('Charlie', 85), ('Diana', 78)]

s = sorted(studenti, key = lambda x: (-x[1],x[0]))#-t[1] < 0 che per ordine
																									#crescente viene ordinato bene
s1 = sorted(s)#lo metto in ordine alfabetico
print(s)
