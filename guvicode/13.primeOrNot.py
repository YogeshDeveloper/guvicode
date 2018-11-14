number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("no")
            break
    else:
        print("yes")
#Input 1:
#55 
#Output 1:
#no

#Input 2:
#5
#Output 1:
#yes