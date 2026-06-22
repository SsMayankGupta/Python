print("Check for Binary")

string="010001010101111010101"

find=True
for bina in string:
    if bina not in [0,1]:
        find=False
        break
        

if find:
    print("Number is a binary number.")
else:
    print("Number is not a binary number.")

