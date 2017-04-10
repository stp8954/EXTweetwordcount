# Steps to run application:

1.	Clone the repository “EXTweetwordcount” 
		git clone https://github.com/stp8954/EXTweetwordcount.git
		git pull origin exercise2

2.	Check whether PostgreSQL is up and running:
		ps auxw | grep postgres

3.	If not, change your current path to /data directory
		cd /data

4.	And start Postgres
		start_postgres.sh

5.	CD to EXTweetwordcount

6.	Make runapp.sh executable
		Chmod 755 ./runapp.sh

7.	Run script “runapp.sh”.This runs the storm topology for 120 seconds.
		If you see this in the cmd window

			WARNING: You're currently running as root; probably by accident.
			Press control-C to abort or Enter to continue as root.
			Set LEIN_ROOT to disable this warning.

		Press ENTER
8.	To view list of all words in the DB, “finalresults.py” script can be run “python finalresults.py”

9.	To view list of a specific word in the DB, “finalresults.py” script can be run “python finalresults.py wordname”

10.	To create histogram of words with counts in a given range histogram.py script can be used. “python histogram.py 5,15”
