def factorial(n):
    if(n==1):
        return n
    else:
        return n * factorial(n-1)

def main():
    x = int(input("enter the number for the factorial to be calculated : "))
    result = factorial(x)
    print(result)
