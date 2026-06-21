print('Reverse List')

# .1
lst=list(['mayank','kajal','bindu','shyam','suman','arpit','tanu','vansh','aradhya'])
lst.reverse()
print(lst)


# .2
lstL=len(lst)
mid=0
if lstL%2==0:
    mid=int(lstL/2)
else:
    mid=int((lstL+1)/2)

for i in range(0,mid):
    temp=lst[i]
    lst[i]=lst[lstL-i-1]
    lst[lstL-i-1]=temp

print(lst)