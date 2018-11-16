#Find factorial of given n number
n=int(input("Enter the number: "))
s=1
if(n>1):
    for i in range(1,n+1):
        s=s*i
print(s)
#Input
#5
#Output
#120