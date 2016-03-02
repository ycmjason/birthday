import datetime

BIRTH_YEAR=1995
BIRTH_MONTH=5
BIRTH_DAY=5

def isFriday(date):
    FRIDAY=5
    return date.isoweekday()==FRIDAY

EXPECTED_LIFE=90
for year in range(1995, 1995+EXPECTED_LIFE):
    date=datetime.datetime(year, BIRTH_MONTH, BIRTH_DAY)
    if(isFriday(date)):
        print "%d: It's friday on your %d(th) birthday!" % (year, year-BIRTH_YEAR)
        if(year%10 == 5):
            print "(this is special as the year ends with 5)"

print "------- now let's see how often is it for 5th May, ___5 AND it's a Friday! -----"
for year in range(1005, 1995+EXPECTED_LIFE, 10):
    date=datetime.datetime(year, BIRTH_MONTH, BIRTH_DAY)
    if(isFriday(date)):
        print "it was friday on 5/5/%d!" % (year)
