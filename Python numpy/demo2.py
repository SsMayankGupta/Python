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

# print(features)
# print(testdata)
# print(trainingData)


import pandas as pd

df = pd.read_csv("C:/Users/acer/OneDrive/Desktop/Machine learning Engineer/Machine Learning Projects/Instagram_Post_Analytics.csv")

# print("Features (columns):", df.columns.tolist())
likes=df[df.columns[3]].tolist();

print("std",(numpy.array(likes)+1).std())
print("avg",(numpy.array(likes)+10).mean())
print("max",numpy.array(likes).max())
print("min",numpy.array(likes).min())
print("sum",numpy.array(likes).sum())
print("sum",len(numpy.array(likes)))
# print(numpy.array(likes).std())
# print(likes)
# print("First column:", df[df.columns[0]].tolist())
# print("Second column:", df[df.columns[1]].tolist())

  