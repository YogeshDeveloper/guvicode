n=int(input("Enter the number: "))
order =len(str(n))
s=0

while (n>1):
    digit = n%10
    s=s+digit**order
    n=n//10
if(n==s):
    print("yes")
else:
    print("no")    
    #Input 1 
    #371
    #Output 1
    #yes 
#Input 2
#45
#Output 2
#No