import MySQLdb

db=MySQLdb.connect(host="localhost",user="root",db="mcqmodule")
c=db.cursor()