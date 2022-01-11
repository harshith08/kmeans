__author__ = "Harshith Pasumarthi"
__email__ = "harshithsunny6@gmail.com"


import pandas as pd
import numpy as np
import random as rd
from distance import euclidieanDistance
import matplotlib.pyplot as plt

class kMeans:

    '''
    This is the constuctor with the current labels and centers
    '''
    def __init__(self):
       self.labels = []
       self.final_centers = []

    '''
    This function is used to find the labels of the corresponding data points
    '''
    def meanCalculation(self,centers,k,data):
        self.labels = []
        for i in range(len(data)):
            temp_dist = []
            for j in range(k):
                distance = euclidieanDistance(data[i],centers[j])
                temp_dist.append(distance)
            min_dist = temp_dist.index(min(temp_dist))
            self.labels.append(min_dist)
        return self.labels

    '''
    This ifunction is used to update the center location based on the labels
    '''
    def centerCalculation(self,centers,data):
        self.final_centers = []
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

    '''
    This function is used to check the cost fucntion of the updated centers
    '''
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

    '''
    This function is used to generate random integers for the initial cluster centers
    '''
    def randomIntegers(self,k,rows):
        rand_array = rd.sample(rows,k=k)
        return rand_array
    
    '''
    This function is used to evaluate the numerator part of the dunn index formula where it is defined
    as the distance between the two farthest data points with a cluster or called as cluster diameter
    '''
    def clusterDiameter(self,k,data):
        denominator = []
        # Outer loop runs for number clusters
        for c in range(k):
            maximum = 0
            distance = 0
            temp=[]
           
            # This loop is to compare the points with their corresponding centers and appending them to a temporary variable
            for n in range(len(self.labels)):
                if self.labels[n] == c:
                    temp.append(data[n])
            # calculate the distances and finding the maximum distance between two points in a cluster
            for i in range(len(temp)):
                for j in range(i+1,len(temp)):
                    distance = np.sqrt(np.sum(np.square(temp[i]-temp[j])))
                    if distance > maximum:
                        maximum = distance
            denominator.append(maximum)
        bottom_result = max(denominator)          
        return bottom_result

    '''
    This function is used to evaluate the denominator part of the dunn index formula where it is defined
    as the distance between the two nearest data points of any two different cluster or called as 
    cluster distance
    '''
    def clusterDistance(self,k,data):
        numerator=[]
        # two loops that runs for all combinations of clusters
        for l in range(k-1):
            # random initial minimum value
            minimum=10
            for m in range(l+1,k):
                # initialized two temporary list array to store the values of data points that belong to different clusters
                temp1=[]
                temp2=[]
                for n in range(len(self.labels)):
                    if self.labels[n] == l:
                        temp1.append(data[n])
                    elif self.labels[n] == m:
                        temp2.append(data[n])
                # Calculating the distance between the points and computing minimum distance
                for x in range(len(temp1)):
                    for y in range(len(temp2)):
                        distance = (np.sqrt(np.sum(np.square(temp1[x]-temp2[y]))))
                        if distance < minimum:
                            minimum=distance
                numerator.append(minimum)
        uppper_result = min(numerator)
        return uppper_result

    '''
    This function has the 3D plot 
    '''
    def graphPlotting(self,centers,data,k):  
        x = [x[0] for x in centers]
        y = [x[1] for x in centers]
        z = [x[2] for x in centers]

        # creating and plotting figure
        fig = plt.figure(figsize = (10, 7))
        ax = plt.axes(projection ="3d")
        ax.scatter(data[:,0],data[:,1],data[:,2], c=self.labels, cmap='viridis')
        # naming in plot values       
        ax.scatter3D(x, y, z, color = "red",marker='x',s=200,alpha=1.0)
        name1 = "plot for k = "+str(k)
        plt.title(name1)
        ax.set_xlabel("Age")
        ax.set_ylabel("Annual Income")
        ax.set_zlabel("Spending Score")
        name2 = "KMeans"+str(k)+".png"
        plt.savefig(name2)
        plt.clf()

'''
This is the main method
'''
if __name__ == "__main__":
    
    dunn_values = []
    no_of_clusters = []

    # csv reading
    df = pd.read_csv("Mall_Customers.csv")

    # here for the columns i delected the unwanted ones you can change these as per your wish
    col = []
    for i in range(len(df.columns)):
        col.append(str(df.columns[i]))
    data = np.array(df[col])
    for i in range(len(data[0])):
        if type(data[0][i]) == str:
            col.pop(i)
    col.pop(0)

    # converting the data into an numpy array
    data = np.array(df[col])
    # number of rows in the csv file
    rows = [i for i in range(len(data))]
    
    # object created for the class "KMeans"
    ob1 = kMeans()

    # this for loop spans k values from 2 to 10 
    for k in range(2,11):
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
        
        epochs = 0
        
        # you can execute this program for wither of the conditions below

        # while abs(J_new - J_old) >= 0.01:
        while epochs < 300:
            labels = ob1.meanCalculation(updated_centers,k,data)
            updated_centers = ob1.centerCalculation(updated_centers,data)
            J_old = J_new
            J_new = ob1.costFunction(updated_centers,data)
            epochs+=1
        up = ob1.clusterDistance(k,data)
        down = ob1.clusterDiameter(k,data)
        dunn_values.append(up/down)
        no_of_clusters.append(k)
        
        ob1.graphPlotting(updated_centers,data,k)
        
    # this is thhe elbow plot to decide the best k value
    plt.plot(no_of_clusters,dunn_values)
    plt.title("Elbow Graph ")
    plt.xlabel("Number of Clusters k")
    plt.ylabel("Dunn Index") 
    plt.savefig("Dunn Index.png")
    plt.clf()
    print("successful")
