
lst=list([2,34,1,2,3,4,543,45,3,45,6,74,3,45,6,7,12])
print(max(lst))
print(min(lst))

# .2
# sorting


# .3
mn=mx=lst[0]
for x in lst:
    if mn>x:
        mn=x
    elif mx<x:
        mx=x

print("Minimumm value is : ",mn,"Maximuum value is :",mx)