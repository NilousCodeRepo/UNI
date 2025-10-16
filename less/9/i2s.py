query = input("Sputa una query: ")

body = input("Sputa un body: ")

l = -1
r = 0

current = ""

c = 0

while r < len(body):
    current += body[r]
    if (len(current) < len(query)):
        r += 1
        continue

    if (len(current) != len(query)):
        current = current[1:]
        r += 1
        continue

    c += 1
    r += 1

print(f"Ho trovato: {c}")
    
