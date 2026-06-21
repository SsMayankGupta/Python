print('''Largest Element''')

lst=list([2,4,3,90,23,123,49,43,43,23,54,8,79,0,65,46])
mx=lst[0]

for itm in lst:
    if itm > mx:
        mx=itm

print("Lagest element in the list is : "+str(mx))
