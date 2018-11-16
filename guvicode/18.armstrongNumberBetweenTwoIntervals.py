#Find the armstrong number between two intervals
a=int(input())
b=int(input())
for num in range(a,b+1):
    s=0
    #print(num)
    order=len(str(num))
    temp=num
    while temp > 0:
        digit = temp % 10
        s += digit ** order
        temp //= 10
        if num == s:
            print(num)    
            
#Input
#150
#160
#Output
#153