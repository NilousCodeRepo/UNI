# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.

def max_element(elements: list[int]) -> int: 
#	M:int = 0
#
#    for i in range(len(elements)):
#        if M < elements[i]:
#            M = elements[i]
##    return M
#	return [M:=i for i in elements if M < i]
	if len(elements) == 1:
		return elements[0]

	return max(elements[0], max_element(elements[1:]))


l: list = [2,3,1]
print(max_element(l))
