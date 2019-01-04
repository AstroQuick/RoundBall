#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import mysql.connector

#url = 'https://app.c2cschools.com/?controller=viewScores&amp;format=html&amp;showHeader=0&amp;showStartTime=0&amp;showLeagueDivision=1&amp;sortLeagueDivision=0&amp;colorKey=00A0FF&amp;sanctioningGroupId=CC68EC897D112875354FC6DD7B43BB6F&amp;activityId=0FD0BEEAA74711E0B6DD000C2932D1AD&amp;activityLevelId=FC83F4AC87B440C2BA95D69E3B03C23F&amp;gender=female&amp;startDate=2018-11-05&amp;endDate=2018-11-10&amp;divId=c2c_scores' # Replace with the URL of your webpage
url = 'http://10.7.50.35/scores.html'
r = requests.get(url)
data=r.text
soup = BeautifulSoup(data, "lxml")

mydb=mysql.connector.connect(host="localhost",user="rbeckman",passwd="Qw01moty!",database="ratings")
mycursor=mydb.cursor()
sqlCheckTeam=("select TeamName from Teams where TeamName = %s")
sqlGetTeamID=("select idTeams from Teams where TeamName = %s")
sqlInsertTeam=("insert into Teams (TeamName, TeamClass, TeamArea) values (%s, %s, %s)")
sqlInsertGame=("insert into Games (HomeTeamId, HomeScore, AwayTeamId, AwayScore) values(%s, %s, %s, %s)")


tro=soup.find_all(attrs={'row odd','row even'})
for game in tro:
    breakout=game.text.splitlines()
    if breakout[8] == '-':
        continue
    if breakout[5].startswith('AHSAA') and breakout[14].startswith('AHSAA'):
        hometeam=breakout[2].replace(',','')
        homeclass=breakout[5][13]
        homearea=breakout[5][41:43]
        homescore=breakout[8]
        awayteam=breakout[11].replace(',','')
        awayclass=breakout[14][13]
        awayarea=breakout[14][41:43]
        awayscore=breakout[17]
#        output=awayteam+','+awayscore+','+hometeam+','+homescore
#        print output.strip()
        mycursor.execute(sqlCheckTeam, [hometeam])
        myresult=mycursor.fetchall()
        if (len(myresult)==0):
            if (homearea.isalpha()):
                homearea=('99')
            mycursor.execute(sqlInsertTeam, (hometeam, homeclass, homearea))
            mydb.commit()
            hometeamid=mycursor.lastrowid
        else:
            mycursor.execute(sqlGetTeamID, [hometeam])
            result=mycursor.fetchall()
            for row in result:
                hometeamid=row[0]
        mycursor.execute(sqlCheckTeam, [awayteam])
        myresult=mycursor.fetchall()
        if (len(myresult)==0):
            if (awayarea.isalpha()):
                awayarea=('99')
            mycursor.execute(sqlInsertTeam, (awayteam, awayclass, awayarea))
            mydb.commit()
            awayteamid=mycursor.lastrowid
        else:
            mycursor.execute(sqlGetTeamID, [awayteam])
            result=mycursor.fetchall()
            for row in result:
                awayteamid=row[0]
        mycursor.execute(sqlInsertGame, (hometeamid, homescore, awayteamid, awayscore))
        mydb.commit()
mycursor.close()
mydb.close()
