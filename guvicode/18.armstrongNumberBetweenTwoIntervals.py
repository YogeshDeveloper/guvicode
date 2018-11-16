a=int(input('Enter the starting interval: '))
b=int(input('Enter the ending interval: '))

#if(a>1 and b>1):


for i in range(a,b+1):
    #print(i)
    order =len(str(i))
    temp=i
    s=0
    while (temp>0):
            digit = temp%10
            s=s+digit**order
            temp=temp//10
    if(temp==s):
            print(temp) 
        