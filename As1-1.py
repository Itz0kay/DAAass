

# Program to display the Fibonacci sequence up to n-th term
print("How many terms?")
nterms = int(input())
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
# generate fibonacci sequence


else: 
    print("Fibonacci sequence:")
    while count < nterms:
       print(n1) 
       nth = n1 + n2
# update values
       n1 = n2
       n2 = nth
       count += 1
'''
print("how many terms")
n=int(input())
n1,n2=0,1
c=0
if(n<=0):
    print("enter positive")
elif(n==1):
    print("sequence")
    print(n1)
else:
    print("fibonacii sequence")
    while(c<=n):
        print(n1)
        tmp=n1+n2
        n1=n2
        n2=tmp 
        c+=1        
       
'''     