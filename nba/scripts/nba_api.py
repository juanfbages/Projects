import requests
import csv

def main():
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
          'MeasureType=Base&' + \
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
          'Season=2014-15&' + \
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

    # Write to csv

    filename = 'stats.csv'
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(stats)

    # Print API request parameters

    print(response.json()['parameters'])

if __name__ == '__main__':
    main()
