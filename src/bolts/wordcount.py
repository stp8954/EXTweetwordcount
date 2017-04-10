from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
        self.dbcur = self.conn.cursor()

    def process(self, tup):
        word = tup.values[0]
        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.

        # Increment the local count
        self.counts[word] += 1

        # call stored procedure to increment word count
        self.dbcur.callproc("add_word", [word, 1])
        self.conn.commit()
        
        self.emit([word, self.counts[word]])

        self.log('%s: %d' % (word, self.counts[word]))

    def cleanup(self):
        self.dbcur.close()
        self.conn.close()
