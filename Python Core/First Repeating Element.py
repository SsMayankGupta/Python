print("First Repeating Element")

lst=list([1,2,3,4,5,6,3,4,5,6,7,8])

idx=1
for itm in lst:
    if itm in lst[idx:-1]:
        print("First element in the list that repeats is : "+str(itm))
        break
    idx+=1