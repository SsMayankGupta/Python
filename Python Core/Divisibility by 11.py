import numpy

num=numpy.random.randint(1,100)
# num=1331
if num%11==0:
    print(num,"Number is divisible by 11.")
else:
    print(num,"Number is not divisible by 11.")


# .2
es=os=0
nums=str(num)
for i in range(len(nums)):
    if i%2==0:
        es+=int(nums[i])
    else:
        os+=int(nums[i])

if (abs(es-os))%11==0:
    print(num,"Number is divisible by 11.")
else:
    print(num,"Number is not divisible by 11.")