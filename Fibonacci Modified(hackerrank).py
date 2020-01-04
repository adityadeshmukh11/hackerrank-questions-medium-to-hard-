a,b,n=map(int,input().strip().split(" "))
l=[]
#print(l)
def fibo(a,b,n):
    if (n < 1): 
        return 0
    for i in range(0, n): 
        l.append(b) 
        next1 = a + (b**2 )
        a = b 
        b = next1
    
z=(fibo(a,b,n))
print(l[-2])


