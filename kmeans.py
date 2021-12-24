import pandas as pd
import numpy as np
from distance import euclidieanDistance
class kMeans:
    def __init__(self,name,age):
        self.x = name
        self.y = age
    def calculation(self, value):
        self.tot = value
        notvalue=8
        print(self.tot,",",notvalue)
    def another(self):
        print(self.tot)
    if __name__ == "__main__":
        df = pd.read_csv("Mall_Customers.csv")
        
ob1 = kMeans("Harshith",23)

