print("Check for Subset")

st=set([1,2,3,4,5,6,7])
print(type(st))
print((st))

sub_st=set([1,2,3,10])

issubset=True
for itm in sub_st:
    if itm not in st:
        issubset=False
        break


if issubset:
    print("sub_st is a subset of the st set")
else:
    print("sub_st is not a subset of the st set")