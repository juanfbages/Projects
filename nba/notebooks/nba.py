import requests
import csv

def getData(metric = 'Base', season = '2014-15'):
    url = 'http://stats.nba.com/stats/leaguedashteamstats?' + \
          'Conference=&' + \
          'DateFrom=&' + \
          'DateTo=&' + \
          'Division=&' + \
          'GameScope=&' + \
          'GameSegment=&' + \
          'LastNGames=0&' + \
          'LeagueID=00&' + \
          'Location=&' + \
          'MeasureType=' + metric + '&' + \
          'Month=0&' + \
          'OpponentTeamID=0&' + \
          'Outcome=&' + \
          'PORound=0&' + \
          'PaceAdjust=N&' + \
          'PerMode=PerGame&' + \
          'Period=0&' + \
          'PlayerExperience=&' + \
          'PlayerPosition=&' + \
          'PlusMinus=N&' + \
          'Rank=N&' + \
          'Season=' + season + '&' + \
          'SeasonSegment=&' + \
          'SeasonType=Regular+Season&' + \
          'ShotClockRange=&' + \
          'StarterBench=&' + \
          'TeamID=0&' + \
          'VsConference=&' + \
          'VsDivision='

    response = requests.get(url)

    # Parse API Response

    results = response.json()['resultSets']
    headers = results[0]['headers']
    stats = results[0]['rowSet'] 
    stats.insert(0, headers)

    return stats