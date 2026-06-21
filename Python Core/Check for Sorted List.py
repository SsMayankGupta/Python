print("Check for Sorted List")

lst=list([1,2,3,5])
# lst = [1, 3, 2, 4]
# lst=list([1,2,3,5,2,3,4,8,4,5,6,7,1,23,23,54,98,23,56,10,29])
sz=len(lst)
st=False



for i in range(0,sz):
    for j in range(i,sz):
        if(lst[i]>lst[j]):
            print("List is not sorted")
            st=True
            break
        else:
            st=False
    if st:
        break

if st:
    print("List is not sorted.")
else:
    print("List is sorted.")



# .2
issorted=False
for i in range(0,sz-1):
    if lst[i]>lst[i+1]:
        print("List is not sorted.") 
        issorted=True

if(issorted==False):
    print("List is sorted.")
