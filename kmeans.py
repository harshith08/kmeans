import pandas as pd
import numpy as np
import random as rd
from distance import euclidieanDistance
class kMeans:
    def __init__(self):
       self.labels = []
       self.final_centers = []
    def meanCalculation(self,centers,k,data):
        for i in range(len(data)):
            temp_dist = []
            for j in range(k):
                distance = euclidieanDistance(data[i],centers[j])
                temp_dist.append(distance)
            min_dist = temp_dist.index(min(temp_dist))
            self.labels.append(min_dist)
        return self.labels
    def centerCalculation(self,centers,data):
        for i in range(len(centers)):
            addition = 0
            counter = 0
            for j in range(len(self.labels)):
                if self.labels[j] == i:
                    addition +=  data[j]
                    counter +=1
            mean = addition/counter
            self.final_centers.append(mean)
        return self.final_centers

    def costFunction(self,centers,data):
        J = 0
        for i in range(len(centers)):
            addition = 0
            for j in range(len(self.labels)):
                if self.labels[j]==i:
                    dist = np.square(euclidieanDistance(centers[i],data[j]))
                    addition += dist
            J += addition
        return J
    def randomIntegers(self,k,rows):
        rand_array = rd.sample(rows,k=k)
        return rand_array
    def another(self):
        print(self.tot)
        
if __name__ == "__main__":
    k=2
    df = pd.read_csv("Mall_Customers.csv")
    col = []
    for i in range(len(df.columns)):
        col.append(str(df.columns[i]))
    data = np.array(df[col])
    for i in range(len(data[0])):
        if type(data[0][i]) == str:
            col.pop(i)
    data = np.array(df[col])
    
    rows = [i for i in range(len(data))]
    
    ob1 = kMeans()
    rand_array = ob1.randomIntegers(k,rows)
    
    initial_centers = []
    for i in range(k):
        temp1 = data[rand_array[i]]
        temp1 = temp1 - 0.8
        initial_centers.append(temp1)
    labels = ob1.meanCalculation(initial_centers,k,data)
    J_old = ob1.costFunction(initial_centers,data)
    updated_centers = ob1.centerCalculation(initial_centers,data)
    J_new = ob1.costFunction(updated_centers,data)
    print("old J =",J_old,"\n\n","new J = ",J_new)

 
