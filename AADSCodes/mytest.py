from General import RevWFI, NewAdjMatrix
from WFI import WFI

G = {'a': {'a': 0, 'b': 2, 'c': 0, 'd': 0},
    'b': {'a': 0, 'b': 0, 'c': 3, 'd': -1},
    'c': {'a': -1, 'b': 0, 'c': 0, 'd': 7},
    'd': {'a': 3, 'b': 0, 'c': 0, 'd': 0}}


def WFI(G):
    D=G
    P=NewAdjMatrix(G)
    for u in G:
        for v in G:
            if D[u][v]: P[u][v]=u
            if u!=v and D[u][v]==0:
                D[u][v]=sys.maxsize
    for k in G:
        for i in G:
            for j in G:
                if D[i][k]+D[k][j]<D[i][j]:
                    D[i][j]=D[i][k]+D[k][j]
                    P[i][j]=P[k][j]
    return (D,P)

print('***')
print(RevWFI(P,'a','d'))