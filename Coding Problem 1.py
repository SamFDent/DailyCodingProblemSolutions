'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
numbers = [10,15,3,7]
x = len(numbers)
foundnumind = 0

for num in numbers:
	if foundnumind == 1:
		break
	else:
		loop = 0
	while loop < x:
		if foundnumind == 1:
			break
		elif num + numbers[loop] == 17:
			print('Target Number Found! ' + str(num) + ' and ' + str(numbers[loop]) = ' make 17')
			foundnumind = 1
			break
		else:
			loop = loop + 1

print('End of processing')
