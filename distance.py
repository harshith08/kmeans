import numpy as np


#* This method is used to find the distance between any two points

def euclidieanDistance(point_a,point_b):
    inter_distance = np.sqrt(np.sum(np.square(point_a - point_b)))
    return inter_distance