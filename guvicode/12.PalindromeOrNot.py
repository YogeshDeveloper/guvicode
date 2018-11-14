n = int(input("Enter the number: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    #print("dig ",dig)
    rev=rev*10+dig
    #print("rev ",rev)
    n=n//10
    #print("n ",n)
if(temp==rev):
    print("yes")
else:
    print("no")
