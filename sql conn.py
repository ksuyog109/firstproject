# select * from mcqquestions where qtypeid=1 and dtypeid=1 order by rand() limit 8;
# select * from mcqquestions where qtypeid=1 and dtypeid=2 order by rand() limit 8;
# select * from mcqquestions where qtypeid=1 and dtypeid=3 order by rand() limit 8;

import MySQLdb
import json
db=MySQLdb.connect(host="localhost",user="root",db="mcqmodule")
c=db.cursor()
ans=[]
correct=[]

c.execute("select * from mcqquestionsfinal where qtypeid=1 and dtypeid=1 order by rand() limit 8")

score=0
res=c.fetchall()
row_headers=[x[0] for x in c.description]
#print(row_headers)
#js=json.dumps(res,sort_keys=True, indent=4, separators=(',', ': '),)
jsondata=[]

for i,row in enumerate(res):
    jsondata.append(dict(zip(row_headers, row)))
    print("Qe."+str(i+1),row[3]," \n1. ",row[4]," \n2. ",row[5],"\n3. ",row[6]," \n4. ",row[7])
    #print(row[8])
    ans.append(input("answer"))
    #print(ans)
    if(int(ans[i])==int(row[8])):
        correct.append('\033[4m' + 'True'+'\033[0m')
        score+=1
    else: correct.append("False")
print(jsondata)
c.execute("select * from mcqquestions where qtypeid=1 and dtypeid=2 order by rand() limit 8")

res=c.fetchall()
for i,row in enumerate(res):
    print("Qm."+str(i+1+8),row[3]," \n1. ",row[4]," \n2. ",row[5],"\n3. ",row[6]," \n4. ",row[7])
    #print(row[8])
    ans.append(input("answer"))
    #print(ans)
    if(int(ans[i+8])==int(row[8])):
        correct.append('\033[4m' + 'True'+'\033[0m')
        score += 1
    else:
        correct.append("False")
c.execute("select * from mcqquestions where qtypeid=1 and dtypeid=3 order by rand() limit 4")

res=c.fetchall()
for i,row in enumerate(res):
    print("Qh."+str(i+17),row[3]," \n1. ",row[4]," \n2. ",row[5],"\n3. ",row[6]," \n4. ",row[7])
    #print(row[8])
    ans.append(input("answer"))
    #print(ans)
    if(int(ans[i+16])==int(row[8])):
        correct.append('\033[4m' + 'True'+'\033[0m')
        score += 1
    else:
        correct.append("'''False'''")
        #score-=0.25
print("======================================================\nscore is:"+str(score))
for i,val in enumerate(ans):
    print("Q."+str(i+1),val," ",correct[i])