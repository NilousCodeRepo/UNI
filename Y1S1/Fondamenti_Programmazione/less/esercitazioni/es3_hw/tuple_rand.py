import random

def rand_gen() -> list[tuple([int ,int])]:

	return [(x := random.randint(0,100), 
					 y := random.randint(0,100)) 
					 for _ in range(5)]


def tuple_rand() -> list:
	t_list: list[tuple([int, int])] = rand_gen()
	t_list.sort()
	
	print(t_list)	
	
	distance:tuple([int, int]) = t_list[0]

	return distance

print("distanza minima dall'origine: ", tuple_rand())
