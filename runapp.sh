#! /bin/bash

#drop db
dropdb -U postgres Tcount
#create db
createdb -U postgres Tcount
# create tables and stored proc
psql -d Tcount -U postgres -f setupdb.sql
#run topology for 2 minutes
sparse run -t 120