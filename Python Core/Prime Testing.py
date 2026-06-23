import numpy


def prime():
    num=numpy.random.randint(1,100000)
    i=2
    isprime=True
    while(i<=num):
        if i!=num and num%i==0:
            isprime=False
            break
        i+=1

    if isprime:
        print(num,"Number is prime number.")
    else:
        print(num,"Number is not prime number.")

for i in range(100):
    prime()

# I have used a loop here for just enjoyment with my computer
# Here i done a big mistake that was not incresing the i and i was thinking why my laptop is getting to hot