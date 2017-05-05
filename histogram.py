import sys
import psycopg2

try:
  lower,upper = sys.argv[1].split(",")    
except IndexError:
       print ("Invalid number of parameters: Needs 2 parameters ")
       sys.exit()
except ValueError:
       print( "Invalid number of parameters: Needs 2 parameters ")
       sys.exit()


conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
querystr = cur.mogrify("select * from tweetwordcount where count >= %s and count <= %s ORDER by count DESC;", (lower,upper))
cur.execute(querystr)
data = cur.fetchall()
words = {r[0]:r[1] for r in data}

for index in sorted(words):
  print("%s: %s" % (index, words[index]))   