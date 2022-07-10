n=int(input())
for i in range(n):
	a=int(input())
	b=list(map(int,input().split()))
	b.sort()
	odd=0
	for i in b:
		if i%2!=0:
			odd+=1
	if b[0]==1:
		print('CHEF')
	elif odd%2==0:
		print('CHEFINA')
	else:
		print('CHEF')