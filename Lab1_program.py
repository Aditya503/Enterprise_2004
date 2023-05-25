
# Determining if a number is Prime or not:

num = int(input("Enter a positive integer: "))
if(num<2):
    print(num," is not a Prime Number")
for i in range(2,int(num/2)+1):
        # if number is divisible by any number between 2 and n/2 , it's not a prime number
    if(num % i==0):
        print(num," is not a Prime Number")
        break
    else: 
        print(num," is a Prime Number")
        break
         
