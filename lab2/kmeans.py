#!/bin/env python3

import csv
import random
import math
import matplotlib.pyplot as plt 
import numpy as np

def distance(p1, p2):
    # TODO: scrivete metrica tra P1 e P2
    # Euclidean distance between P1 and P2
    dx = float(p1["x"]) - float(p2["x"])
    dy = float(p1["y"]) - float(p2["y"])
    dz = float(p1["z"]) - float(p2["z"])
    return math.sqrt(dx * dx + dy * dy + dz * dz)

def average(ps):
    # TODO: scrivere funzione media
    '''
        (x, y, z)
        {
            x: media degli x
            y: media degli y
            z: media degli z  
        } 
    '''
    # Calculate the average of points in ps
    n = len(ps)
    if n == 0:
        return {"x": 0, "y": 0, "z": 0}
    else:
        sum_x = sum(float(points[i]["x"]) for i in ps)
        sum_y = sum(float(points[i]["y"]) for i in ps)
        sum_z = sum(float(points[i]["z"]) for i in ps)
        return {"x": sum_x / n, "y": sum_y / n, "z": sum_z / n}

if __name__ == "__main__":

    points = []

    with open("points.csv", "r") as f:
        for point in csv.DictReader(f):
            points.append(point)

    N = len(points)
    K = 3 # K = 0 -> rosso | K = 1 -> verde | K = 2 -> blue
    # [0,1,2,3,4,5,6,7,8,9,10,...]
    # 2, 5, 9

    centroids = random.sample(points, k = K) # k centroidi
    clusters = [-1 for _ in range(N)] # clusters[i] = j <- il punto i è contenuto nel cluster j
    old_clusters = []

    while clusters != old_clusters:
    
        old_clusters = clusters[::] # copio i cluster

        for i in range(N):
            # quale è il centroide più vicino del punto i-esimo
            distances = [distance(points[i], centroids[j]) for j in range(K)]
            '''
            centro un array lungo K
            dove distances[i] = distance tra punto-esimo e tutti i centroidi attuali
            '''
            clusters[i] = distances.index(min(distances)) #  prendimi l'indice dell'elemento minimo

        # Per ogni singolo cluster, aggiorno il centroide
        for i in range(K):
            # array che contiene tutti i punti che hanno come cluster di appartenenza
            # il cluster i-esimo
            points_in_clusters = [j for j in range(N) if clusters[j] == i] # filtra usando list comprehension
            # points_in_clusters = filter(lambda x: x == i, clusters)               # filtra usando filter
            centroids[i] = average(points_in_clusters)
        
    x = [points[i]["x"] for i in range(N)]
    y = [points[i]["y"] for i in range(N)] 
    colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
    C = np.array([colors[clusters[i]] for i in range(N)]) # assegna il color in base al cluster di appartenenza
    
    print(clusters)
    plt.scatter(x, y, c=C/255.0) 
    plt.show() 