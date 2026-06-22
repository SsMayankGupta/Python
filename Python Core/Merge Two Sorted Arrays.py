import bisect

print("Merge Two Sorted Arrays")

lst1=[1,2,3,4,5,6,7,8]
lst2=[4,5,6,7,8,9,10]

for itm in lst2:
    bisect.insort_left(lst1,itm)
    
print(lst1)

# if avoiding duplicates
l_s=list(set(lst1))
print(l_s)

