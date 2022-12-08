#!/usr/bin/python3

# Begin imports
import calendar
import datetime
import json
import requests
import time

from iso8601 import parse_date
from pydub import AudioSegment
from pydub.playback import play
# Finish imports

# Begin constants
API_URL = "http://api.aladhan.com/v1/timingsByCity/:date_or_timestamp"
# Finish constants

# Begin functions
def getPrayerTimes():
    date = datetime.datetime.today().strftime('%m-%d-%Y')

'''
    calculation_data = {
        'date_or_timestamp': date,
        'city': ,
        'country': ,
        'state': ,
        'method': ,
        'school': ,
        'iso8601': 'true'
    }
'''

    file = open("log.txt", "a")
    file.write("Refreshed prayer times at " + str(datetime.datetime.today()) + "\n")
    file.close()

    response = requests.get(API_URL, params=calculation_data)
    return response.json()

def createPrayerTimesList(timesDict):
    timesList = []

    timesOuter = timesDict['data']
    timesInner = timesOuter['timings']
    for item in timesInner.items():
        if item[0] == 'Dhuhr' or item[0] == 'Asr' or item[0] == 'Maghrib' or item[0] == 'Isha':
            parsed = parse_date(item[1])
            timetuple = parsed.timetuple()
            timesList.append(calendar.timegm(timetuple))
    return timesList


def athan(timesList):
    while True:
        currentTime = int(time.time() - 25200)
        isha = timesList[-1]

        for i in timesList:
            if currentTime == i:
                file = open("log.txt", "a")
                file.write("Played athan at " + str(datetime.datetime.today()) + "\n")
                file.close()

                athan = AudioSegment.from_mp3('athan.mp3')
                play(athan)
                time.sleep(1)
            if currentTime > (isha + 120):
                return
            else:
                time.sleep(.1)

def setRefreshTime(prayerTimes):
    dhuhr = prayerTimes[0]
    return (dhuhr + 85800)

# End functions

prayerTimes = createPrayerTimesList(getPrayerTimes())
refreshTime = setRefreshTime(prayerTimes)

while True:
    if int(time.time() - 25200) >= refreshTime:
        prayerTimes = createPrayerTimesList(getPrayerTimes())
        refreshTime = setRefreshTime(prayerTimes)
        print('Refreshed prayer times at ' + str(datetime.datetime.now()))

    athan(prayerTimes)
