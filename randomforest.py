import numpy as np
from sklearn.ensemble import RandomForestClassifier,forest

X = [[0,1,1,0,0,0,0,0,1,0,0,0,0], [1,0,0,1,0,0,1,0,0,0,1,0,0],[1,0,0,1,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1],[1,0,0,1,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,0,0,0,1,0,0],[0,1,0,0,0,1,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
Y = ['Assembly Line Work','Attorney','Author(Non-Fiction)','Author(Fiction)','Bank Teller','Book-keeper','Budget Director','Cashier','Caterer','Clergy','Computer Programmer','Construction Work']
