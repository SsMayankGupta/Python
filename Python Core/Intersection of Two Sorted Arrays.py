print("Intersection of Two Sorted Arrays")

lst1=[1,2,3,4,5,6,7,8]
lst2=[4,5,6,7,8,9,10]
intersection=list()


for itm in lst1:
    if itm in lst2:
        print(str(itm))