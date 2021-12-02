import os, sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def emailUser(sender, password, results):
    # Compile Message
    # Beginning
    receiver = info[0]
    message = MIMEMultipart("alternative")
    message["Subject"] = "Blue Quiz Involvement Survey Results!"
    message["From"] = sender
    message["To"] = receiver
    textFile = getFile('../data/result/text_intro.txt')
    htmlFile = getFile('../data/result/html_intro.txt')
    for line in textFile:
        text += line
    textFile.close()
    for line in htmlFile:
        html =+ line
    htmlFile.close()
    # Middle


def pull(path, five):
    info = {}
    file = open('../data/clubdata/academic/general.csv')
    for line in file:
        line = line.strip('\n')
        lineData = line.split(',')
        if lineData[0] == five:
            lineData.pop(0)
            info[five] = lineData
    file.close()
    return info


def getResults(five):
    # Setup
    results = {}
    # Academic
    general = ['pcab', 'fees', 'saa', 'council', 'nscsc']
    medical = ['therapy', 'amsa', 'cadvaer', 'hosa', 'neuro', 'dental', 'pmed', 'physass', 'spmed', 'diet']
    humanities = ['anthro', 'milpsych', 'globcom', 'colstud', 'natstud', 'mun', 'prssa']
    business = ['finance', 'sport', 'nsls']
    etc = ['aspire', 'ram', 'terra']
    # Recreation
    athletic = ['hurd', 'canyon', 'archery', 'yoga', 'trail']
    arts = ['radio', 'blight', 'series', 'film', 'irish', 'bigband', 'cswing']
    lifestyle = ['blucru', 'activity', 'trad', 'fsl', 'game', 'paint', 'tennis', 'spike']
    # DEI
    dei = ['girl', 'nami', 'ostem', 'scandi', 'tagalog', 'transfer']
    # Service
    spiritual = ['lds', 'colchrist', 'fellow', 'goldcity', 'varsity', 'navi', 'newman', 'ratio', 'inter', 'ssa']
    kindness = ['serve', 'rotaract', 'cares', 'bestbud', 'gdays']
    political = ['dems', 'ydsa', 'surf']

    # Search
    for org in five:
        if org in general:
            path = '../data/clubdata/academic/general.csv'
            results.update(pull(path, five))
        elif org in medical:
            path = '../data/clubdata/academic/medical.csv'
            results.update(pull(path, five))
        elif org in humanities:
            path = '../data/clubdata/academic/humanities.csv'
            results.update(pull(path, five))
        elif org in business:
            path = '../data/clubdata/academic/business.csv'
            results.update(pull(path, five))
        elif org in etc:
            path = '../data/clubdata/academic/etc.csv'
            results.update(pull(path, five))
        elif org in athletic:
            path = '../data/clubdata/recreation/athletic.csv'
            results.update(pull(path, five))
        elif org in arts:
            path = '../data/clubdata/recreation/arts.csv'
            results.update(pull(path, five))
        elif org in lifestyle:
            path = '../data/clubdata/recreation/lifestyle.csv'
            results.update(pull(path, five))
        elif org in dei:
            path = '../data/clubdata/dei/dei.csv'
            results.update(pull(path, five))
        elif org in spiritual:
            path = '../data/clubdata/service/spiritual.csv'
            results.update(pull(path, five))
        elif org in kindness:
            path = '../data/clubdata/service/kindness.csv'
            results.update(pull(path, five))
        elif org in political:
            path = '../data/clubdata/service/political.csv'
            results.update(pull(path, five))
    return results


def allocator(data):


def lineProcessor(file):
    """ This function takes the data from the CSV file, rips out the necessary info, and sends it up for processing. """
    # Setup
    email = "bluequizinvolvement@gmail.com"
    password = "wdB!PGbV*GhG&23y"

    # Processing
    skipHeadings = 0
    for line in file:
        if skipHeadings > 2:
            # Ripping
            quizResponses = []
            line = line.strip('\n')
            elementList = line.split(',')
            for el in range(len(elementList)):
                if el == 0 or el > 5:  # Only take needed information
                    if len(elementList[el]) == 0:  # Unseen Values
                        quizResponses.append('0')
                    else:
                        quizResponses.append(elementList[el])
            for data in range(len(quizResponses)):
                if data != 0 and data != 1:
                    quizResponses[data] = int(quizResponses[data])
            # Allocating
            topFive = allocator(quizResponses)
            # ID Logging
            log = open('../data/response_id.txt', 'w')
            log.write(importantInfo.pop(0))
            log.close()
            # Emailing
            results = getResults(topFive)
            emailUser(email, password, results)
        else:
            skipHeadings += 1


def getFile(path):
    """ This function locates the CSV file and pulls from that. """
    try:
        file = open(path)
    except FileNotFoundError:
        print("No File Found")
        sys.exit(1)
    return file


if __name__ == '__main__':
    # File Processing
    filepath = '../data/Blue Quiz V2.csv'
    fileObj = getFile(filepath)
    lineProcessor(fileObj)
    fileObj.close()
    os.remove(filepath)
