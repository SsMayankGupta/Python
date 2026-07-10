import numpy

features=""
testdata=list()
trainingData=list()

with open("C:/Users/acer/OneDrive/Desktop/Machine learning Engineer/Machine Learning Projects/Instagram_Post_Analytics.csv","r") as file:
    features=(file.readline()).split(",")
    for i in range(2):
        testdata+=list((file.readline()).split(","))
    for i in range(2):
        trainingData+=list((file.readline()).split(","))

print(features)
print(testdata)
print(trainingData)
  