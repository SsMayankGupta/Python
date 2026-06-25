import numpy 

num=numpy.random.randint(1,100000)
if num%13==0:
    print(num,"Number is divisible by the 13.")
else:
    print(num,"Number is not divisible by the 13.")