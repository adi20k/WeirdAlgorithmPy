n=int(3)
arr=[]
check=True
while check:
	if (n%2)==0:
	    n= int(n/2)
	    arr.append(n)
	    #print(n)
	else:
	    n=n*3+1
	    arr.append(n)
	    #print(n)
	if(n==1):
	    check=False
print( *arr)
