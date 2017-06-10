def fibo(n):
    a = 0
    b = 1
    sum = 0
    series =[]
    series.append(a)
    series.append(b)
    while(sum < n):
        sum = a + b
        series.append(sum)
        a = b
        b = sum
    print(series)


limit = int(input("enter the number till where u want your fib series : "))
fibo(limit)

