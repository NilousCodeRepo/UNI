def set_ops(set1: set([int]), set2: set([int])):
	print(set1 | set2)#unione
	print(set1 & set2)#intersezione
	print(set1 - set2)#differenza
	print(set1 ^ set2)#differenza simmetrica

set1, set2 = {1,2,3,4,5},{4,5,6,7,8}
set_ops(set1,set2);
