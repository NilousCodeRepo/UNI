n:int = int(input("inserire n: "))
m:int = int(input("inserire m: "))

r1 = n/m
r2 = n//m
r3 = n%m

print("divisione normale: ", r1, type(r1))
print("divisione intera: ",r2, type(r2))
print("divisione con resto: ", r3, type(r3))

