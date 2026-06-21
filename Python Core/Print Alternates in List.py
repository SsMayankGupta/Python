print("Print Alternates in List")

lst=list([12,"mayank",18,"30,000","male",28.88,23.3e10,{"Mayank","Rahul"},("Abhishek","Kumar Jatin"),{"name":"Mayank","age":18}])
print(lst[::2]) #Here c1:c2:c3 c1 & c2 defines the range of slicing and c3 tells about the gap between to indexs in list

print(lst[0:5:3]) # this always includes first element in it