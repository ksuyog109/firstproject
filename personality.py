import MySQLdb
from flask import Flask,render_template
from flask_restful import reqparse
import socket
app = Flask(__name__)
db=MySQLdb.connect(host="localhost",user="root",db="mcqmodule")
c=db.cursor()
#c.execute("select * from personality order by rand()")
c.execute("select * from personality")
res=c.fetchall()
ans=[]
eiscore1=[]
tfscore4=[]
jpscore2=[]
snscore3=[]
print("========================================================\nAnswer -3 for disagree 3 for agree give in range -3 to 3\n========================================================")
for i,row in enumerate(res):
    print (i+1,"\t",row[1])
    #print(row)
    #ans.append(input("answer"))
    ans.append(-2)
    if (int(ans[i]) ==-3):
        ans[i]=-10
    elif (int(ans[i]) ==-2):
        ans[i]=-6
    elif (int(ans[i]) ==-1):
        ans[i]=-3
    elif (int(ans[i]) ==0):
        ans[i]=0
    elif (int(ans[i]) == 1):
        ans[i] = 3
    elif (int(ans[i]) ==2):
        ans[i]=6
    elif (int(ans[i]) ==3):
        ans[i]=10
    else:
        print("error")
    ans[i]=int(row[3])*ans[i]
    if(int(row[2])==1):
        eiscore1.append(ans[i])
        print("eiscore ",ans[i])
    elif(int(row[2])==2):
        jpscore2.append(ans[i])
        print("jpscore ", ans[i])
    elif(int(row[2])==3):
        snscore3.append(ans[i])
        print("snscore ", ans[i])
    elif(int(row[2])==4):
        tfscore4.append(ans[i])
        print("tfscore ", ans[i])
print(sum(eiscore1),"\n",sum(jpscore2),"\n",sum(snscore3),"\n",sum(tfscore4))
if(sum(eiscore1)>=0):
    print("introvert")
elif(sum(eiscore1)<0):
    print("extrovert")
if (sum(jpscore2) >= 0):
    print("p")
elif (sum(eiscore1) < 0):
    print("j")
if (sum(snscore3) >= 0):
    print("n")
elif (sum(snscore3) < 0):
    print("s")
if (sum(tfscore4) >= 0):
    print("f")
elif (sum(tfscore4) < 0):
    print("t")


