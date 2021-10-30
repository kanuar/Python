''' disarium number checker
a number is said to be a disarium number if it is 
equal to the sum of the digits raised to the power of their respective 
position  in the number 
eg 
175 is a disarium number because
1^1 + 7^2 + 5^3 is 175
ie 1+49+125 =175

another example is 89 
8+81= 89
8^1 + 9^2 =89


added another function with overloading called disarium generator which will generate 
disarium numbers from 10 - n 
and returns none if there isnt any disarium number in the range mentioned
the second generator ie the ranged disarium (overloaded version of the normal generator)
generates disarium numbers in the range a to b
'''

def checker(n):
	c=n 
	s=0
	ct=1
	while c!=0:
		d=c%10
		s+=d**ct
		ct+=1
		c//=10
		pass
	if s==n :
		return True
	else : 
		return False
	pass

def generator(n):
	l=[]
	for i in range(10,n+1):
		if checker(i):
			l.append(i)
	else: 
		if l==[]:
			return None
	return l

def generator(a,b):
	l=[]
	for i in range(a,b+1):
		if checker(i):
			l.append(i)
	else:
		if l==[]:
			return None
			pass

	return l

