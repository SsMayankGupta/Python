print("Check for Sorted Array")

lst=[1,2,3,1,3,4,5,6,77,6,5,4,23]
lst2=lst.copy()

# .1
if lst==lst2.sort():
    print("Array is sorted array.")
else:
    print("Array is not sorted array.")

# .2
issorted=False
for i in range(len(lst)):
    if lst[i]>lst[i+1]:
        print("List is not sorted.")
        issorted=True
        break
if issorted==False:
    print("List is sorted list")


# .3
