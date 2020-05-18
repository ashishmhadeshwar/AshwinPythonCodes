#This is a program to find the Fibonacci sequence
a=0
b=1
for _ in range(1,11):
    c=a+b
    print(c)
    a=b
    b=c
