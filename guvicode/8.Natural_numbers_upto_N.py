n=int(input("Enter a Number: "))
if(n<0):
    print("Enter a Positive Number!")
else:
    sum=0
    while(n>0):
        sum=sum+n
        n=n-1
        #print(n)
        #print(sum)
print(sum)        

