persone = [
	{'nome': 'Alice', 'eta': 25},
	{'nome': 'Bob', 'eta': 30},
	{'nome': 'Charlie', 'eta': 20}
]
persone.sort(key = lambda d: d['eta'])
print(persone)
