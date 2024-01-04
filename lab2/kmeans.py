#!/bin/env python3

import csv
import random
import math
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

def distance(p1, p2):
    # TODO: scrivete metrica tra P1 e P2
    # Euclidean distance between P1 and P2
    print(p1)
    print(p2)
    dx = int(p1["age"]) - int(p2["age"])
    dy = int(p1["bank"]) - int(p2["bank"])
    return math.sqrt(dx * dx + dy * dy)

def average(ps):
    # TODO: scrivere funzione media
    # Calculate the average of points in ps
    n = len(ps)
    if n == 0:
        return {"age": 0, "bank": 0}
    else:
        sum_x = sum(float(data[i]["age"]) for i in ps)
        sum_y = sum(float(data[i]["bank"]) for i in ps)
        return {"age": sum_x / n, "bank": sum_y / n}

if __name__ == "__main__":

    data = []
    columns = ["age", "bank"]
    df = pd.read_csv("../data_creation/Anondata.csv", usecols=columns)
    for d in df.to_dict(orient="records"):
        data.append(d)
    N = len(data)
    K = 3 # K = 0 -> rosso | K = 1 -> verde | K = 2 -> blue
    # [0,1,2,3,4,5,6,7,8,9,10,...]
    # 2, 5, 9

    centroids = random.sample(data, k = K) # k centroidi
    clusters = [-1 for _ in range(N)] # clusters[i] = j <- il punto i è contenuto nel cluster j
    old_clusters = []

    while clusters != old_clusters:
    
        old_clusters = clusters[::] # copio i cluster

        for i in range(N):
            # quale è il centroide più vicino del punto i-esimo
            distances = [distance(data[i], centroids[j]) for j in range(K)]
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
        
    x = [data[i]["age"] for i in range(N)]
    y = [data[i]["bank"] for i in range(N)] 
    colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
    C = np.array([colors[clusters[i]] for i in range(N)]) # assegna il color in base al cluster di appartenenza
    
    print(clusters)
    plt.scatter(x, y, c=C/255.0) 
    plt.show() 