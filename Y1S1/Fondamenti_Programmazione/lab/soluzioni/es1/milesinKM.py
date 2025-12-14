q = bool(input("convertire mph in km(0) o viceversa(1)?"))

if q == 0:
    q2 = float(input("inserire numero di mph da convertire: "))
    print(f"{q2*1.61}")
    
elif q == 1:
    q3 = float(input("inserire numero di km da convertire:"))
    print(f"km =  {q3/1.61}")
else:
    print("inserire valore corretto")
