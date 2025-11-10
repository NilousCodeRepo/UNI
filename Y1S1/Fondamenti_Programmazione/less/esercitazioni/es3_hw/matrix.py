def matrix_3x3(l: list[list])-> list:
	diag:list = []

	for i in range(len(l)):
		el:list = l[i][i]#perchè si fa 00 11 22
													 #che sono proprio le posizioni giuste
		diag.append(el)

	return diag

l = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_3x3(l))
