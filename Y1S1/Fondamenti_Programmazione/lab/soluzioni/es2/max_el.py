# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: list[int]) -> int: 
    M:int = 0

    for i in range(len(elements)):
        if M < elements[i]:
            M = elements[i]
    return M

l: list = [3,2,1]
print(max_element(l))
