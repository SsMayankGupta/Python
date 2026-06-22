print("Check for Palindrome")

string="Hi This is Mayank gupta"
# string="HHssHH"


if string==string[::-1]:
    print("String is a palindrom string.")
else:
    print("not a palindrom string.")


# .2 
i=0
strlen=len(string)
if strlen%2==0:
    strlenH=int(strlen/2)
else:
    strlenH=int((strlen+1)/2)

ispalimdrom=True
for i in range(strlenH):
    if string[i]!=string[strlen-i-1]:
        ispalimdrom=False

if ispalimdrom:
    print("String is a palimdrom string.")
else:
    print("String is not a palimdrom string.")
    