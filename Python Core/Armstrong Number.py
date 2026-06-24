import math


for num in range(1,20000):
    stnum=str(num)
    nnum=0
    for x in stnum:
        nnum+=(int(x))*(int(x))*(int(x))

    if nnum==num:
        print(num,"Entered number is armstrong number.")
    else:
        print(num,"Entered number is not a armstrong nummber.")