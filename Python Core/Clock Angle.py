import numpy

hours=numpy.random.randint(1,12)
minutes=numpy.random.randint(1,60)

print("Angle made by clock hannds is : ",abs((11/2)*minutes-30*hours),"Degree")