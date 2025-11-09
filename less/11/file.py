with open("prova.txt",mode= "a" ,encoding="utf8") as A:
    A.write("ciao")
    print("ciao da print", file = A)
