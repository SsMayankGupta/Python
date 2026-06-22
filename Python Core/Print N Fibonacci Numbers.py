print("Print N Fibonacci Numbers")

n=int(input("Enter a number : "))
t0=0
t1=1
for i in range(n):
    print(t0)
    temp=t0
    t0=t1
    t1=temp+t1
