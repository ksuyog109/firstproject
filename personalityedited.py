import MySQLdb
from flask import Flask,render_template,flash
from flask_restful import reqparse
import json
import socket
app = Flask(__name__)
parser = reqparse.RequestParser()
eiscore1=[]
tfscore4=[]
jpscore2=[]
snscore3=[]
for i in range(1,61):
    parser.add_argument('que'+str(i))
for i in range(1,231):
    parser.add_argument('aptique'+str(i))

db=MySQLdb.connect(host="localhost",user="root",db="mcqmodule")
c=db.cursor()
c.execute("select * from personalitysorted")
res = c.fetchall()
#print(res)
ip=socket.gethostbyname(socket.gethostname())
ans=[]
realscore=[]
app.secret_key = 'some_secret'

@app.route('/')
def home():
    flash("asas")
    return render_template("SAMDNBHVBASND.htm")
@app.route('/test')
def test():
    return render_template('test.html',res=res,ip=ip)
@app.route('/result',methods=['GET'])
def result():
    args = parser.parse_args()
    #print(args)
    for i,row in enumerate(res):
        ans.append(args['que'+str(i+1)])
        #print(ans)
        #print(str(i) + " " + ans[i])
        #realscore.append(int(row[3]) * ans[i])
        #print(realscore)
        if(row[3]==-1):
            realscore.append(int(ans[i])*-1)
            #print(i,"  negate")
        else:
            realscore.append(int(ans[i]))
        #print(realscore)
        #print(str(i) + " " + ans[i])

        if (int(row[2]) == 1):
            eiscore1.append(realscore[i])
            print("eiscore ", realscore[i])
        elif (int(row[2]) == 2):
            jpscore2.append(realscore[i])
            print("jpscore ", realscore[i])
        elif (int(row[2]) == 3):
            snscore3.append(realscore[i])
            print("snscore ", realscore[i])
        elif (int(row[2]) == 4):
            tfscore4.append(realscore[i])
            print("tfscore ", realscore[i])

    #ans.append(que1)
        #print(ans[i])
    print(sum(eiscore1), "\n", sum(jpscore2), "\n", sum(snscore3), "\n", sum(tfscore4))
    print(eiscore1, "\n", jpscore2, "\n", snscore3, "\n", tfscore4)
    ans.clear()
    realscore.clear()

    var=0
    if (sum(eiscore1) >= 0):
        print("i")
        var=var+1
    elif (sum(eiscore1) < 0):
        print("e")
    if (sum(snscore3) >= 0):
        print("n")
        var=var+2
    elif (sum(snscore3) < 0):
        print("s")
    if (sum(tfscore4) >= 0):
        print("f")
        var = var + 4
    elif (sum(tfscore4) < 0):
        print("t")
    if (sum(jpscore2) >= 0):
        print("p")
        var=var+8
    elif (sum(eiscore1) < 0):
        print("j")

    eiscore1.clear()
    tfscore4.clear()
    jpscore2.clear()
    snscore3.clear()
    print(var)
    #ph no: 9689161414 ram pawle
    if var==0:
        typ='<!DOCTYPE html><html><body><p><b>Your personality type is ESTJ. </b></p></body></html>'
    elif var==1:
        typ='<!DOCTYPE html><html><body><p><b>Your personality type is ISTJ</b></p></body></html>'
    elif var==2:
        typ='<!DOCTYPE html><html><body><p><b>Your personality type is ENTJ</b></p></body></html>'
    elif var==3:
        typ='<!DOCTYPE html><html><body><p><b>Your personality type is INTJ</b></p></body></html>'
    elif var ==4:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ESFJ</b></p></body></html>'
    elif var ==5:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ISFJ</b></p></body></html>'
    elif var==6:
        return render_template('enfj.html')
    elif var==7:
        typ='<!DOCTYPE html><html><body><p><b>Your personality type is INFJ</b></p></body></html>'
    elif var==8:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ESTP</b></p></body></html>'
    elif var == 9:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ISTP</b></p></body></html>'
    elif var == 10:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ENTP</b></p></body></html>'
    elif var == 11:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is INTP</b></p></body></html>'
    elif var == 12:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ESFP</b></p></body></html>'
    elif var == 13:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ISFP</b></p></body></html>'
    elif var == 14:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is ENFP</b></p></body></html>'
    elif var == 15:
        typ = '<!DOCTYPE html><html><body><p><b>Your personality type is INFP</b></p></body></html>'




    return "error"
@app.route('/aptitude')
def apti():
    c.execute("select * from mcqquestionsfinal where qtypeid=1 and dtypeid=1 order by rand() limit 8")
    score = 0
    verbaleasy = c.fetchall()
    d={}
    questioncount=1
    for row in verbaleasy:
        d['que'+str(questioncount)]={'id':str(row[0]),'qtype':row[1],'dtype':row[2],'question':str(row[3]),'opt1':str(row[4]),'opt2':str(row[5]),'opt3':str(row[6]),'opt4':str(row[7]),'correct':str(row[8])}
        questioncount= questioncount+1
    print(d)
    c.execute("select * from mcqquestionsfinal where qtypeid=1 and dtypeid=2 order by rand() limit 8")
    verbalmid=c.fetchall()
    for row in verbalmid:
        d['que'+str(questioncount)]={'id':str(row[0]),'qtype':row[1],'dtype':row[2],'question':str(row[3]),'opt1':str(row[4]),'opt2':str(row[5]),'opt3':str(row[6]),'opt4':str(row[7]),'correct':str(row[8])}
        questioncount= questioncount+1
    c.execute("select * from mcqquestionsfinal where qtypeid=1 and dtypeid=3 order by rand() limit 4")
    verbalhard = c.fetchall()
    for row in verbalhard:
        d['que'+str(questioncount)]={'id':str(row[0]),'qtype':row[1],'dtype':row[2],'question':str(row[3]),'opt1':str(row[4]),'opt2':str(row[5]),'opt3':str(row[6]),'opt4':str(row[7]),'correct':str(row[8])}
        questioncount= questioncount+1
    #print(aptireseasy)

    data=json.dumps(d)
    print(data)

    return render_template()
    return render_template("aptitest.html",ip=ip,aptires=verbaleasy,verbalmid=verbalmid,verbalhard=verbalhard)
@app.route('/aptiresult')
def aptiresult():
    args = parser.parse_args()
    print(args)
    c.execute("select * from mcqquestionsfinal")
    res=c.fetchall()
    scoreverbal=0
    scorelogical=0
    scorequant=0
    for i,row in enumerate(res):
        if (args['aptique' + str(i+1)] != None):
            print('aptique' + str(i+1), args['aptique' + str(i+1)])
            ans=args['aptique' + str(i+1)]
            if(row[1]==1):
                if int(row[8])==int(ans):
                    scoreverbal=scoreverbal+1
            if (row[1] == 2):
                if int(row[8]) == int(ans):
                    scorelogical = scorelogical + 1
            if (row[1] == 3):
                if int(row[8]) == int(ans):
                    scorequant = scorequant + 1

    return "your verbal score is :"+str(scoreverbal)

if __name__ == '__main__':
    app.run(host=ip,debug=True)