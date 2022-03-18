import os, sys
import smtplib, ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from process_qualtrics import allocator

def emailUser(email, colleges, five, results, times):
    """ This function handles the email that sends the top five clubs """
    # Compile Message
    before = time.time()
    # Beginning
    message = MIMEMultipart("alternative")
    message["Subject"] = email['subject']
    message["From"] = email['sender']
    message["To"] = email['receiver']
    textFile = getFile('../data/result/text_intro.txt')
    htmlFile = getFile('../data/result/html_intro.txt')
    text = ''
    html = ''
    for line in textFile:
        text += line
    textFile.close()
    for line in htmlFile:
        html =+ line
    htmlFile.close()
    # Middle
    for x in range(5):
        if five[x+1] == "council":
            text += """
            """ + results[five[x+1]][1] + """
                Purpose: """ + results[five[x+1]][2] + """
            """
            html += '''
            <tr>
                <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <img src="''' + results[five[x+1]][0] + '''" style="width: 100%; max-width: 600px; border-radius: 15px 15px 0px 0px;">
                </td>
            </tr>
            <tr>
                <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px; border-radius: 0px 0px 15px 15px;">
                    <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + results[five[x+1]][1] + '''</h1>
                    <p style="text-align: left;"><b>Purpose: </b>''' + results[five[x+1]][2] + '''</p>
            '''
            while colleges: # While there's still colleges in the list
                curCol = colleges.pop(0)
                text += results[five[x+1]][curCol * 3] + ": " + results[five[x+1]][(curCol * 3) + 2] + "\n"
                html += '''<p style="text-align: left; margin: 0 0 10px;"><b>''' + results[five[x+1]][curCol * 3] + '''</b><a href="''' + results[five[x+1]][(curCol * 3) + 1] + results[five[x+1]][(curCol * 3) + 2] + '''"> ''' + results[five[x+1]][(curCol * 3) + 2] + '''</a></p>'''
            html += """
                           </td>
                       </tr>"""
        elif five[x+1] == "fsl":
            text += """
            """ + results[five[x+1]][1] + """
                Purpose: """ + results[five[x+1]][2] + """
                """ + results[five[x+1]][3] + results[five[x+1]][4] + """
                """ + results[five[x+1]][5] + results[five[x+1]][6] + """
            """
            html += '''
            <tr>
                <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <img src="''' + results[five[x+1]][0] + '''" alt="TestImage" style="width: 100%; max-width: 600px; border-radius: 15px 15px 0px 0px;">
                </td>
            </tr>
            <tr>
                <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px; border-radius: 0px 0px 15px 15px;">
                    <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + results[five[x+1]][1] + '''</h1>
                    <p style="text-align: left;"><b>Purpose: </b>''' + results[five[x+1]][2] + '''</p>
                    <p style="text-align: left; margin: 0 0 10px;"><b>''' + results[five[x+1]][3] + '''</b><a href="''' + results[five[x+1]][4] + '''">''' + results[five[x+1]][4] + '''</a></p>
                    <p style="text-align: left; margin: 0 0 10px;"><b>''' + results[five[x+1]][5] + '''</b><a href="''' + results[five[x+1]][6] + '''">''' + results[five[x+1]][6] + '''</a></p>
                </td>
            </tr> 
            '''
        else:
            text += """
                """ + results[five[x+1]][1] + """
                Purpose: """ + results[five[x+1]][2] + """
                """ + results[five[x+1]][3] + results[five[x+1]][4] + """
                """
            html += '''
                <tr>
                    <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
                </tr>
                <tr>
                    <td>
                        <img src="''' + results[five[x+1]][0] + '''" style="width: 100%; max-width: 600px; border-radius: 15px 15px 0px 0px;">
                    </td>
                </tr>
                <tr>
                    <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px; border-radius: 0px 0px 15px 15px;">
                        <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + results[five[x+1]][1] + '''</h1>
                        <p style="text-align: left;"><b>Purpose: </b>''' + results[five[x+1]][2] + '''</p>
                        <p style="text-align: left; margin: 0 0 10px;"><b>''' + results[five[x+1]][3] + '''</b><a href="''' + results[five[x+1]][4] + '''">''' + results[five[x+1]][4] + '''</a></p>
                    </td>
                </tr> 
                '''
    # End
    html += """
                        <tr>
                            <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
        """
    pPart = MIMEText(text, "plain")
    hPart = MIMEText(html, "html")
    message.attach(pPart)
    message.attach(hPart)
    # Sendoff
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email['sender'], email['password'])
        server.sendmail(email['sender'], email['receiver'], message.as_string())
        print("Email Sent to: " + email['receiver'])
        after = time.time()
        times.append(after - before)
        print(f"---Line Strip took: {times[0]:.3f} seconds to run.")
        print(f"---Processing took: {times[1]:.3f} seconds to run.")
        print(f"---User Email took: {times[2]:.3f} seconds to run.")

def pull(path, five):
    """ This function opens a given CSV file and processes it into workable data. """
    info = {}
    file = getFile(path)
    for line in file:
        line = line.strip('\n')
        lineData = line.split('"""')
        for el in range(len(lineData)):
            if el != 2 and el != 3:
                lineData[el] = lineData[el].strip(',')
        if lineData[0] == five:
            lineData.pop(0)
            info[five] = lineData
    file.close()
    return info


def getResults(five):
    """ This function takes the top five results and points the 'pull' function to the correct csv, returning a dictionary of important club info. """
    # Setup
    results = {}
    # Academic
    general = ['pcab', 'fees', 'saa', 'council', 'nscsc']
    medical = ['therapy', 'amsa', 'cadvaer', 'hosa', 'neuro', 'dental', 'pmed', 'physass', 'spmed', 'diet']
    humanities = ['anthro', 'milpsych', 'globcom', 'colstud', 'natstud', 'mun', 'prssa']
    business = ['finance', 'sport', 'nsls']
    etc = ['aspire', 'ram']
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


def lineProcessor(file):
    """ The primary function of the program. Ingests CSV, parses information, sends it to processors, and emails the user with the results. """
    # Setup
    email = {
        'sender': "bluequizinvolvement@gmail.com",
        'password': "wdB!PGbV*GhG&23y",
        'subject': "BLUE Quiz Involvement Survey Results!"
    }
    times = []

    # Processing
    skipHeadings = 0
    for line in file:
        if skipHeadings > 2:
            # Ripping
            before = time.time()
            quizResponses = []
            line = line.strip('\n')
            elementList = line.split(',')
            for el in range(len(elementList)):
                if el == 0 or el > 5:  # Only take needed information
                    if len(elementList[el]) == 0:  # Unseen Values
                        quizResponses.append(0)
                    else:
                        if el < 7:
                            quizResponses.append(elementList[el])
                        else:
                            quizResponses.append(int(elementList[el]))
            after = time.time()
            times.append(after - before)
            # ID Logging
            log = open('../data/response_id.txt', 'w')
            log.write(quizResponses.pop(0))
            log.close()
            # Allocating
            before = time.time()
            topFive = allocator(quizResponses)
            colleges = topFive.pop(0) # Grab college list from resulting list
            after = time.time()
            times.append(after - before)
            # # Emailing
            email['receiver'] = quizResponses.pop(0) # Grab email
            results = getResults(topFive)
            emailUser(email, colleges, topFive, results, times)
        else:
            skipHeadings += 1


def getFile(path):
    """Retrieve a file (usually a .CSV but not always) and pull from that. """
    try:
        file = open(path)
    except FileNotFoundError:
        print("Error: '" + path + "' was not able to be located.")
        sys.exit(1)
    return file


if __name__ == '__main__':
    # File Processing
    filepath = '../data/Blue Quiz V2.csv'
    fileObj = getFile(filepath)
    lineProcessor(fileObj)
    fileObj.close()
    # os.remove(filepath)
    print("Run Complete!")