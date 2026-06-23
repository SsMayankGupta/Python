def fact(num):
    if num==1 or num==0:
        return 1
    return num*fact(num-1)

print("Binomial coeffi. of 10C2: ",fact(10)/fact(2)*fact(8))
print("Binomial coeffi. of 10C10: ",fact(10)/fact(10)*fact(0))

