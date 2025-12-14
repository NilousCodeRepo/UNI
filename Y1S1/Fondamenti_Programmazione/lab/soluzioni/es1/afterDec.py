#s = "38293829441.2241"
#counter = 0
#
#for el in s:
#	if el.isnumeric():
#		counter += 1
#	else:
#		print(s[counter:])

def func(s):
	if not s:
		return s

	if s[0] == ".":
		return s[0:]

	return func(s[1:])#uso la ricorsione per ridurre la string

s = "38293829441.2241"
print(func(s))
