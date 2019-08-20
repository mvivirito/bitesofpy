from datetime import datetime
from datetime import timedelta
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()



# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    #   get rid of that pesky T
    x = line.replace('T', ' ')
    #string dates are now in this format: 2014-07-03 23:24:31
    match = re.search(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', x)

    #convert to datetime objects
    date = datetime.strptime(match.group(0), '%Y-%m-%d %H:%M:%S' )
    return(date)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdownlist = []
    for x in loglines:
        if (x.find(SHUTDOWN_EVENT) != -1):
            item = convert_to_datetime(x)
            shutdownlist.append(item)
    timebetween = (shutdownlist[1] - shutdownlist[0])
    return(timebetween)





