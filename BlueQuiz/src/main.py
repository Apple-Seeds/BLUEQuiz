import glob
import os
import sys

def lineReader(file):
    """ This function takes the data from the CSV file and parses it to get the point totals for each attribute """
    # Setting
    attributes = {
        "leader": 0,
        "service": 0,
        "project": 0,
        "detail": 0,
        "time": 0,
        "political": 0,
        "hype": 0,
        "helpful": 0,
        "party": 0,
        "planner": 0,
        "extroverted": 0,
        "creative": 0,
        "spirit": 0,
        "athletic": 0,
        "academic": 0,
        "mentor": 0,
        "music": 0,
    }
    organizations = {
        "pcab": 0,
        "fees": 0,
        "grc": 0,
        "blucru": 0,
        "activ": 0,
        "series": 0,
        "trad": 0,
        "hurd": 0,
        "council": 0,
        "saa": 0,
        "serve": 0,
        "states": 0,
        "radio": 0,
        "blight": 0,
        "fsl": 0
    }


    # Processing
    skip = 0
    questions = 12
    for line in file.readlines():
        if skip > 3:
            elementList = line.split(',')
            for ele in elementList:
                if ele.__contains__('@'):









def getFile():
    """ This function locates the CSV file with 'BRQ' in it, and pulls from that. """
    fileFound = False
    while not fileFound:
        try:
            filepath = glob.glob('../**/BRQ*')[0]  # Takes the first file with 'BRQ' in the directory.
            fileObj = open(filepath)
            fileFound = True
        except IndexError:
            sys.exit(0)
    return fileObj




if __name__ == '__main__':
    # Run in Background

    # Grab CSV File
    file = getFile()
    lineReader(file)


