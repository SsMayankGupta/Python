import numpy

num=numpy.random.randint(1,1000)
lst=list()
num_it_self_prime=True

for i in range(2,num):
    if num%i==0:
        j=2
        isprime=True
        while(j<i):
            if i%j==0:
                isprime=False
                break
            j+=1
        if isprime:
            lst.append(i)
        num_it_self_prime=False


if num_it_self_prime:
    print(num," is it self prime number.")
else:
    print(num," The list all prime factors of number is : ",lst)
