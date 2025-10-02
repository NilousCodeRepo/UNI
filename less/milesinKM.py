print("convertire mph in km(0) o viceversa(1)?")
q = bool(input())    
if q == 0:
    print("inserire numero di mph da convertire: ")
    q2 = float(input())
    print(f"{q2*1.61}")
    
elif q == 1:
    print("inserire numero di km da convertire: ")
    q3 = float(input())
    print(f"km =  {q3/1.61}")
else:
    print("inserire valore corretto")
