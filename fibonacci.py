def recursion(n):
    if n <= 1:
        return n
    else :
        return (recursion(n-1) + recursion(n-2))


# how many integers do you want in your fibonacci series
def main():
    a=[]
    number=int(input("give us the number of outputs you want"))
    if number<= 0:
        print("invalid input")
    else:
        for i in range(number):
            print(i)
            a.append(recursion(i))
            #print(recursion(i))
        print(a)
        
if __name__ == "__main__" : main()
