#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

url = 'https://app.c2cschools.com/?controller=viewScores&amp;format=html&amp;showHeader=0&amp;showStartTime=0&amp;showLeagueDivision=1&amp;sortLeagueDivision=0&amp;colorKey=00A0FF&amp;sanctioningGroupId=CC68EC897D112875354FC6DD7B43BB6F&amp;activityId=0FD0BEEAA74711E0B6DD000C2932D1AD&amp;activityLevelId=FC83F4AC87B440C2BA95D69E3B03C23F&amp;gender=female&amp;startDate=2018-11-05&amp;endDate=2018-12-31&amp;divId=c2c_scores' # Replace with the URL of your webpage
#url = 'http://10.7.50.35/scores.html'
r = requests.get(url)
data=r.text
soup = BeautifulSoup(data, "lxml")

tro=soup.find_all(attrs={'row odd','row even'})
for game in tro:
    gametext=game.text
    breakout=gametext.splitlines()
    if breakout[8] == '-':
        continue
    if breakout[5].startswith('AHSAA') and breakout[14].startswith('AHSAA'):
        hometeam=breakout[2].replace(',','')
        homediv=breakout[5]
        homescore=breakout[8]
        awayteam=breakout[11].replace(',','')
        awaydiv=breakout[14]
        awayscore=breakout[17]
        output=awayteam+','+awayscore+','+hometeam+','+homescore
        print output.strip()

