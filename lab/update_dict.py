def update_dict():
    d = {}
    lista_chiavi = ["federighi", "coglione", "ciupe", "nigga"]
    valore = 1
    for i in lista_chiavi:
        d[i] = valore
        valore += 1
    print(d)

update_dict()
