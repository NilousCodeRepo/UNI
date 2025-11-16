def stats(l: list[int]) -> tuple([int, int]):
	media:int = 0
	d = len(l)

	for i in range(len(l)):
		media += l[i]
	media = media / d

	M = max(l)
	m = min(l)
	l[0] = media
	l[1] = M
	l[2] = m
	
	limited_t:tuple() = tuple(l[:3])

	return limited_t

l:list[int] = [3,2,1] 
print(stats(l))
