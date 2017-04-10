import sys
import psycopg2

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv)!=2:
  cur.execute("select word,count from tweetwordcount")
  result = cur.fetchall()
  print sorted(result,key = lambda x:x[1])
  conn.commit()
  conn.close()

else:
  param1 = sys.argv[1]
  querystr = cur.mogrify("select * from tweetwordcount where word = %s;",(str(param1),))
  cur.execute(querystr)
  data = cur.fetchall()
  #print data
  print("total number of occurences of %s: %s" %(data[0][0],data[0][1]) )
  conn.commit()
  conn.close()
 