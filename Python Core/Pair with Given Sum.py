print("Pair with Given Sum")

st=set([1,2,3,4,5,6,8,7,9])
sumP=int(input("Enter the targeted sum : "))


lst=list(st)
for i in range(len(lst)-1):
    if lst[i]+lst[i+1]==sumP:
        print("Targeted pair with given sum is : ",lst[i]," + ",lst[i+1]," = ",sumP)