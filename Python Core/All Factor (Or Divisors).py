import numpy

num=numpy.random.randint(1,1000)
st=set()

for i in range(2,num+1):
    if num%i==0:
        st.add(i)

print(num,st)