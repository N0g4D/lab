#!/bin/python3

'''
G is graph with

vertices degrees = [1,1,1,2,2,2,2,5,5,5,7,7,7,7,7,7,7]

counts(degree == 1) = 3
counts(degree == 2) = 4
counts(degree == 5) = 3
counts(degree == 7) = 8

G is 3-degree anonymous graph (min(counts))
'''

def check(G, k, l):
    '''
    G = (V, E) the graph to check
    k = number of vertices
    l = number of common neighbors

    check if the graph G is (k,l) anonymous
    '''
    '''
    check if the (k,l)-anonymous weakly definition is true for v \in V
 
    '''
    V, E = G

    '''
    E = [
        (1,3),
        (5,2),
        (1,2),
        (1,7),
        ...
    ]
    '''
    neighbors = {
        v: set() for v in V
    }

    # for each edge (u,v) add them to the set of neighbors
    for (u, v) in E:
        neighbors[v].add(u)
        neighbors[u].add(v)

    #for v in V:
    #    print(f"N({v}) = ", neighbors[v])

    # check the definition of all the vertices in V
    for v in V:
        #print("CHECKING", v)
        counts = 0
        # count the number of vertices that shares at least l neighbors
        for w in V:
            if w == v: # skip if i'm checking the same node
                continue
            # count common neighbors between v, w

            '''
                neighbors[v] = {1,2,3,4,8}
                neighbors[w] = {4,6,8,9}
                intersection = {4,8}
            '''
            common_neighbors = len(neighbors[v].intersection(neighbors[w]))
            #print("\t", f"COMMON NEIGHBOURS({v}, {w}) =", common_neighbors, "SET =", neighbors[v].intersection(neighbors[w]))
            if common_neighbors >= l:
                counts += 1
            # add 1 to counts if common neighbors >= l

        # graph is not (k,l)-anonymous
        # because for node v there are not at least k different
        # vertices with at least l common neighbors
        #print("\t", "COMMON NEIGHBOURS = ", counts)
        if counts < k:
            return False

    return True # pass all the checks


'''
    G = (V,E)
    G' = (V, E = (E', E'')) where E'' = set of fake new edges and E' = set of true edges


'''
def checkStrongly(G, k, l):
    # TODO: check if the graph is (k,l)-anonymous in the strong definition
    '''
    to do this copy the function check
    in the common_neighbors set consider only the edges in the original graph G and not G'
    i.e. vertices connected by an edge in E' and not in E''
    '''
    pass

V = [1,2,3,4,5,6,7,8,9,10]

E = [
    (1,2),
    (1,3),
    (2,3),
    (3,5),
    (4,7),
    (5,7),
    (5,8),
    (6,8),
    (7,8),
    (8,9),
    (8,10)
]

G = (V, E)

print(f"G is ({1},{1})-anonymous", check(G, 1, 1))
print(f"G is ({2},{1})-anonymous", check(G, 2, 1))
print(f"G is ({3},{1})-anonymous", check(G, 3, 1))
print(f"G is ({4},{1})-anonymous", check(G, 4, 1))
print(f"G is ({5},{1})-anonymous", check(G, 5, 1))
print(f"G is ({5},{1})-anonymous", check(G, 6, 1))


'''
if G is (k,l) anonymous then is also (1, l)-anonymoius, ..., (k-1, anonymous)
'''

V = [1,2,3,4,5,6,7] 
# (1,2,3,4,5) is a clique of N = 5 and x = 6 and y = 7
# u = 3


E = [
    (1,2),
    (1,3),
    (1,4),
    (1,5),
    (2,1),
    (2,3),
    (2,4),
    (2,5),
    (3,1),
    (3,2),
    (3,4),
    (3,5),
    (4,1),
    (4,2),
    (4,3),
    (4,5),
    (5,1),
    (5,2),
    (5,3),
    (5,4),
    (6,7), # x - y edge
    (3,6), # u - x edge
    (3,7) # u - y edge
    
]

'''
    (1,6),
    (2,6),
    (3,6),
    (4,6),
    (5,6),
    (1,7),
    (2,7),
    (3,7),
    (4,7),
    (5,7),
'''

G = (V, E)

# k = 5
print("")
print("")
print(f"G is ({1},{1})-anonymous", check(G, 1, 1))
print(f"G is ({2},{1})-anonymous", check(G, 2, 1))
print(f"G is ({3},{1})-anonymous", check(G, 3, 1))
print(f"G is ({4},{1})-anonymous", check(G, 4, 1))
print(f"G is ({5},{1})-anonymous", check(G, 5, 1))
print(f"G is ({6},{1})-anonymous", check(G, 6, 1))
print(f"G is ({7},{1})-anonymous", check(G, 7, 1))