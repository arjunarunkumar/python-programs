
    
    

def prime(n):
    if(n > 1):
        for i in range(2,n):
            if(n%i == 0):
                print(n, " is not a prime number")
                print(i, "times ", n//i , "is ",n)
                break
        else:
            print(n,"is a prime number")
        
    else:
        print(n,"is not a prime number")
    
x="yes"
while(x=="yes" or x == "y"):
    n= int(input("enter the number to check prime or not"))
    prime(n)
    x=input("do you wanna go again")
