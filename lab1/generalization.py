import csv
import pandas as pd

class Tree:

    data = []
    level = 0
    parent = {}

    def __init__(self, l):
        self.level = l

    def connect(self, n, p):
        self.parent[n] = p # definisco il parent di un nodo

    def generalize(self, n):
        return self.parent[n] # restituisco il parent (valore più generale di n)

age = Tree(4)
zip = Tree(5)

with open("age.csv", "r") as f:
    for row in csv.DictReader(f):
        L0 = int(row["L0"])
        L1 = int(row["L1"])
        L2 = int(row["L2"])
        L3 = int(row["L3"])
        L4 = int(row["L4"])
        age.connect(L0, L1)
        age.connect(L1, L2)
        age.connect(L2, L3)
        age.connect(L3, L4)

with open("zip.csv", "r") as f:
    for row in csv.DictReader(f):
        L0 = int(row["L0"])
        L1 = int(row["L1"])
        L2 = int(row["L2"])
        L3 = int(row["L3"])
        L4 = int(row["L4"])
        L5 = int(row["L5"])
        zip.connect(L0, L1)
        zip.connect(L1, L2)
        zip.connect(L2, L3)
        zip.connect(L3, L4)
        zip.connect(L4, L5)

D = []
attrs = ["name","surname","age","zip","bank","disease"]

EI = ["name", "surname"] # tokenizzarli
QI = ["age", "zip"]      # generalizzarli o sopprimerli
SD = ["bank", "disease"] # lasciarli invariati

'''
0
1
2
3
0
1
2
3
4

0 -> 2
1 -> 2
3 -> 2
4 -> 1
'''

freq = { qi: {} for qi in QI }
#print(freq)

with open("../data_creation/data.csv", "r") as f:
    for row in csv.DictReader(f):
        D.append(row)

# Tokenizzazione su EI
for attr in EI:
    for row in D:
        row[attr] = row[attr][0] # prendo solo la prima lettera


# Generalizzare i QI
gens = []
for attr in QI:
    for row in D:
        val = int(row[attr])
        if val not in freq[attr].keys():
            freq[attr][val] = 0

        freq[attr][val] += 1
    # Calcolo le freq dell'attr in D
    #maxVal = max(freq[attr].items)
    #minVal = min(freq[attr].items)

    # Generalizzo
    gens.append(pd.cut(list(freq[attr].values()), bins=4, labels=[1,2,3,4]))

print(gens[0][0])


for i,attr in enumerate(QI):
    for j,row in enumerate(D):
        for _ in range(gens[i][j]):
            if(attr == "age"):
                D[j][attr] = age.generalize(int(D[j][attr]))
            else:
                D[j][attr] = zip.generalize(int(D[j][attr]))
            ## genVal = age.generalize(freq[attr][row])
    
#print("AGE: "+str(freq["age"]))
#print("Generalized AGE: "+str(freq["age"]))
#print("ZIP: "+str(freq["zip"]))

#print(D)