from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

X = [[0, 1,1,0,0,0,0,0,1,0,0,0,0], [1, 0,0,1,0,0,1,0,0,0,1,0,0],[1, 0,0,1,0,0,0,0,0,0,1,0,0],[0, 0,0,0,0,0,0,0,0,0,0,1,0],[0, 0,0,0,0,0,1,0,0,0,1,0,0],[0, 0,0,0,0,0,0,0,0,0,0,0,1],[1, 0,0,1,0,1,1,0,0,0,0,0,0],[1, 0,0,0,0,1,0,0,0,0,1,0,0],[0, 0,1,0,0,1,0,0,0,0,1,0,0],[0, 1,0,0,0,1,0,1,0,0,0,0,0],[0, 1,1,0,0,0,0,1,0,0,0,0,0],[0, 0,0,0,0,0,0,0,0,0,0,0,0]]
Y = ['Assembly Line Work','Attorney','Author(Non-Fiction)','Author(Fiction)','Bank Teller','Book-keeper','Budget Director','Cashier','Caterer','Clergy','Computer Programmer','Construction Work']
ed=euclidean_distances(X,[[0, 0,0,0,0,0,0,1,0,0,0,0,1]])
'''
firmin=np.argmin(ed)
ed[firmin]=99
smin=np.argmin(ed)
ed[smin]=99
tmin=np.argmin(ed)
ed[tmin]=99
forthmin=np.argmin(ed)
ed[forthmin]=99
fivemin=np.argmin(ed)
ed[fivemin]=99
print(firmin,smin,tmin,forthmin,fivemin)
'''
#print(Y[firmin],Y[smin],Y[tmin],Y[forthmin],Y[fivemin])
print(ed)
minindex=[]
minval=[]
flag=[]
tmp=list(ed)
for i in range(0,5):
    ind=np.argmin(tmp)
    minindex.append(ind)
    val=tmp[ind]
    print(minindex)
    minval.append(val)
    print(minval)
    tmp[ind]=999
    if (i>0):
        if(minval[i-1]==minval[i]):
            flag.append(1)
        else:
            flag.append(0)
    else:
        flag.append(0)

print(minval)
print(flag)
rec=0

proba=['very high', 'very high','high','high','medium']
for i in range(0,5):

    print(Y[minindex[i]],proba[rec])
    if (flag[i] == 0):
        rec = rec + 1