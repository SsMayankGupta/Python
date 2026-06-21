question="Search in a List"
print(question)
question=""


lst=list([1,2,7,9,3,5,2,8,3,5,6,8,90,34,342,76,45])
tar=input("Enter targeted value : ")


# .1
if(tar in lst):
    print("Targeted item : "+tar+" Exists in the list.")
else:
    print("Does't exists.")
    print('Does\'t exists.')


# .2
exists=False
for item in lst:
    if item==tar:
        print("Targeted item : "+tar+" Exists in the list.")
        exists=True
        break
    else:
        exists=False

if exists==False:
    print('Does\'t exists.')
    