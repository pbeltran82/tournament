#!/usr/bin/env python
# author: Pedro Beltran
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()	
    cursor = DB.cursor()
    cursor.execute("delete from matches;")	
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()	
    cursor = DB.cursor()
    cursor.execute("delete from player;")	
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()	
    cursor = DB.cursor()
    cursor.execute("select count(*) from player;")
    values = cursor.fetchall()
    DB.commit()
    DB.close()	
    return values[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()	
    cursor = DB.cursor()
    cursor.execute("insert into player values(%s);",(name,))	
    cursor.execute("select max(id) from player;")
    id = cursor.fetchall()[0][0]
    cursor.execute("insert into matches values({0},0,0)".format(id))
    DB.commit()
    DB.close()
	
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()	
    cursor = DB.cursor()
    cursor.execute("select player.id, player.name, matches.wins, matches.matches from player join matches on player.id = matches.id order by wins desc;")
    value = cursor.fetchall()	
    DB.commit()
    DB.close()
    return value	

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()	
    cursor = DB.cursor()
    queryWin = "UPDATE matches set wins = wins + 1, matches = matches + 1 WHERE id = {0}".format(winner)
    queryLos = "UPDATE matches set wins = wins + 0, matches = matches + 1 WHERE id = {0}".format(loser)	
    cursor.execute(queryWin)
    cursor.execute(queryLos)	
    DB.commit()
    DB.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    count = 0
    pairings = []
    pairing = []
    for i in standings:
        if(count%2 == 0):
            pairing += [i[0], i[1]]    
        else:
            pairing += [i[0], i[1]]
            pairings.append(tuple(pairing))
            pairing = []    
        count = count + 1
    return pairings

