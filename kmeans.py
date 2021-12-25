import pandas as pd
import numpy as np
import random as rd
from distance import euclidieanDistance
class kMeans:
    def __init__(self):
       pass
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
        rows = [i for i in range(len(data))]
        result = randomIntegers(k,rows)
        print(result)
ob1 = kMeans()

