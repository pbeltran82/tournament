# tournament
How to run the tournament project

Note: I'm running my project on Windows 7 with Python 2
and Vagrant VM using postgreSQL. 

1. Go to your directory where you have PostgreSQL set up using the Git Bash Command line prompt. 
2. Clone this project using this url https://github.com/pbeltran82/tournament.git
3. Now, start up vagrant by typing "vagrant up"
4. Followed by typing, "vagrant ssh" to login in. 
5. Once logged in, type "psql"
6. Type "\i tournament.sql" to load the database and tables
7. Type "\q"
7. Finally type the following to run the tournament program: "python tournament_test.py"
