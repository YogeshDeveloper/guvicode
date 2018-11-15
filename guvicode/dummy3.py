a=55
b=59
for i in range(a,b+1):
    if(i>1):
        for j in range(2,i):
            print(i%j==0)