import sys

alist = []

n = int(input())
for _ in range(n):
   command, *attr = input().split()
   if(command == "print"):
      print(alist)
   else:
      getattr(alist, command)(*(int(x) for x in attr))
