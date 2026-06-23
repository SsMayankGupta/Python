import numpy

num=numpy.random.randint(1,100)

mxprime=2
prime_find=False
for i in range(2,num):
    if num%i==0:
        j=2
        isprime=True
        while(j<i):
            if i%j==0:
                isprime=False
            j+=1
        if isprime and mxprime<i:
            prime_find=True
            mxprime=i

if prime_find:
    print(num,"Maximum prime factor is : ",mxprime)
else:
    print(num,"No prime factor exists for this number.")
    
            