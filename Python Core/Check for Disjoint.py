print("Check for Disjoint")

f_st=set([1,2,3,4])
s_set=set([4,5,6,7])

isdisjoint=True
for itm in f_st:
    if itm in s_set:
        isdisjoint=False
        break

if isdisjoint:
    print("Both sets are Disjoint sets.")
else:
    print("Both sets are not Disjoint sets.")