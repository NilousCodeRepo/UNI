nums = []
while True:	
	num = input("inserire numeri: ")
	if num.lower() == "stop":
		break
	nums.append(num)

set_val = set(nums)

print(sorted(set_val))
