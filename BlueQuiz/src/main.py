import os, sys
import smtplib, ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from process_qualtrics import allocator


def emailUser(email, colleges, three, results):
    """ This function compiles the email that sends the top three clubs """
    # Beginning
    message = MIMEMultipart("alternative")
    message["Subject"] = email['subject']
    message["From"] = email['sender']
    message["To"] = email['receiver']
    textFile = getFile('../data/result/text_intro.txt')
    htmlFile = getFile('../data/result/html_intro.html')
    text = ''
    html = ''
    for line in textFile:
        text += line
    textFile.close()
    for line in htmlFile:
        html += line
    htmlFile.close()

    # Middle
    for x in range(3):
        if three[x] == "council":
            text += """
            """ + results[three[x]][1] + """
                Purpose: """ + results[three[x]][2] + """
            """
            html += '''
            <tr>
                <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <img src="''' + results[three[x]][0] + '''" style="width: 100%; max-width: 600px; border-radius: 15px 15px 0px 0px;">
                </td>
            </tr>
            <tr>
                <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px; border-radius: 0px 0px 15px 15px;">
                    <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + \
                    results[three[x]][1] + '''</h1>
                    <p style="text-align: left;"><b>Purpose: </b>''' + results[three[x]][2] + '''</p>
            '''
            while colleges:  # While there's still colleges in the list
                curCol = colleges.pop(0)
                text += results[three[x]][curCol * 3] + ": " + results[three[x]][(curCol * 3) + 2] + "\n"
                html += '''<p style="text-align: left; margin: 0 0 10px;"><b>''' + results[three[x]][
                    curCol * 3] + '''</b><a href="''' + results[three[x]][(curCol * 3) + 1] + results[three[x]][
                            (curCol * 3) + 2] + '''"> ''' + results[three[x]][(curCol * 3) + 2] + '''</a></p>'''
            html += """
                           </td>
                       </tr>"""
        elif three[x] == "fsl":
            text += """
            """ + results[three[x]][1] + """
                Purpose: """ + results[three[x]][2] + """
                """ + results[three[x]][3] + results[three[x]][4] + """
                """ + results[three[x]][5] + results[three[x]][6] + """
            """
            html += '''
            <tr>
                <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <img src="''' + results[three[x]][0] + '''" alt="TestImage" style="width: 100%; max-width: 600px; border-radius: 15px 15px 0px 0px;">
                </td>
            </tr>
            <tr>
                <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px; border-radius: 0px 0px 15px 15px;">
                    <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + \
                    results[three[x]][1] + '''</h1>
                    <p style="text-align: left;"><b>Purpose: </b>''' + results[three[x]][2] + '''</p>
                    <p style="text-align: left; margin: 0 0 10px;"><b>''' + results[three[x]][
                        3] + '''</b><a href="''' + results[three[x]][4] + '''">''' + results[three[x]][4] + '''</a></p>
                    <p style="text-align: left; margin: 0 0 10px;"><b>''' + results[three[x]][
                        5] + '''</b><a href="''' + results[three[x]][6] + '''">''' + results[three[x]][6] + '''</a></p>
                </td>
            </tr> 
            '''
        elif three[x] == "christ" or three[x] == "party" or three[x] == "repo":
            text += """
                """ + results[three[x]][1] + """
                Purpose: """ + results[three[x]][2]
            i = 3
            while three[x][i] != "END":
                text += results[three[x]][i] + results[three[x]][i + 1] + """ """
                i += 2
            html += '''
                <tr>
                    <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
                </tr>
                <tr>
                    <td>
                        <img src="''' + results[three[x]][0] + '''" style="width: 100%; max-width: 600px; border-radius: 15px 15px 0px 0px;">
                    </td>
                </tr>
                <tr>
                    <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px; border-radius: 0px 0px 15px 15px;">
                        <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + \
                    results[three[x]][1] + '''</h1>
                        <p style="text-align: left;"><b>Purpose: </b>''' + results[three[x]][2] + '''</p>'''
            i = 3
            while three[x][i] != "END":
                html += '''<p style="text-align: left; margin: 0 0 10px;"><b>''' + results[three[x]][
                    i] + '''</b><a href="''' + results[three[x]][i + 1] + '''">''' + results[three[x]][
                            4] + '''</a></p>'''
                i += 2
            html += '''
                    </td>
                </tr> 
                '''
        else:
            text += """
                """ + results[three[x]][1] + """
                Purpose: """ + results[three[x]][2] + """
                """ + results[three[x]][3] + results[three[x]][4] + """
                """
            html += '''
                <tr>
                    <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
                </tr>
                <tr>
                    <td>
                        <img src="''' + results[three[x]][0] + '''" style="width: 100%; max-width: 600px; border-radius: 15px 15px 0px 0px;">
                    </td>
                </tr>
                <tr>
                    <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px; border-radius: 0px 0px 15px 15px;">
                        <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + \
                    results[three[x]][1] + '''</h1>
                        <p style="text-align: left;"><b>Purpose: </b>''' + results[three[x]][2] + '''</p>
                        <p style="text-align: left; margin: 0 0 10px;"><b>''' + results[three[x]][
                        3] + '''</b><a href="''' + results[three[x]][4] + '''">''' + results[three[x]][4] + '''</a></p>
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

    # Sendoff!
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email['sender'], email['password'])
        server.sendmail(email['sender'], email['receiver'], message.as_string())
        print("Email Sent to: " + email['receiver'])


def pull(path, three):
    """ This function opens a given CSV file and processes it into workable data. """
    info = {}
    file = getFile(path)
    for line in file:
        # Get line of data
        line = line.strip('\n')
        lineData = line.split('"""')
        # Check if it's the right line
        if lineData[1] in three:
            # Clean out garbage
            index = 0
            while index < len(lineData):
                if len(lineData[index]) < 2:
                    lineData.pop(index)
                index += 1
            for el in range(len(lineData)):
                if el != 2 and el != 3:
                    lineData[el] = lineData[el].strip(',')
            # Add information to info
            info[lineData[0]] = lineData[1:]
    file.close()
    return info


def getResults(three):
    """ This function takes the top three results and points the 'pull' function to the correct csv, returning a dictionary of important club info. """
    # Setup
    results = {}
    # Academic
    general = ['pcab', 'fees', 'council', 'saa', 'nscsc', 'ento', 'aspire']
    medical = ['therapy', 'amsa', 'cadvaer', 'hosa', 'neuro', 'dental', 'pmed', 'nami', 'physass', 'span', 'diet',
               'milpsych', 'mcat', 'mftsa']
    business = ['algo', 'sport', 'nsls', 'bit']
    # Recreation
    athletic = ['hurd', 'canyon', 'archery', 'yoga', 'trail', 'volley']
    arts = ['radio', 'blight', 'series', 'states', 'film', 'bigband', 'cswing', 'star', 'thea']
    lifestyle = ['blucru', 'activity', 'trad', 'fsl', 'game', 'paint', 'tennis', 'spike', 'pickle', 'skate', 'aikido',
                 'snow', 'ram']
    # Humanities
    dei = ['girl', 'ostem', 'transfer', 'story', ' women']
    international = ['globcom', 'natstud', 'scandi', 'tagalog', 'russia', 'irish']
    studies = ['anthro', 'colstud', 'mun', 'prssa', 'phil', 'nsslha']
    # Service
    spiritual = ['lds', 'fellow', 'newman', 'inter', 'ssa', 'christ']
    kindness = ['serve', 'rotaract', 'cares', 'bestbud', 'gdays', 'smile']
    political = ['grc', 'party', 'repo']

    # Search
    for org in three:
        if org in general:
            path = '../data/clubdata/academic/general.csv'
            results.update(pull(path, three))
        elif org in medical:
            path = '../data/clubdata/academic/medical.csv'
            results.update(pull(path, three))
        elif org in business:
            path = '../data/clubdata/academic/business.csv'
            results.update(pull(path, three))
        elif org in athletic:
            path = '../data/clubdata/recreation/athletic.csv'
            results.update(pull(path, three))
        elif org in arts:
            path = '../data/clubdata/recreation/arts.csv'
            results.update(pull(path, three))
        elif org in lifestyle:
            path = '../data/clubdata/recreation/lifestyle.csv'
            results.update(pull(path, three))
        elif org in dei:
            path = '../data/clubdata/humanities/dei.csv'
            results.update(pull(path, three))
        elif org in international:
            path = '../data/clubdata/humanities/international.csv'
            results.update(pull(path, three))
        elif org in studies:
            path = '../data/clubdata/humanities/studies.csv'
            results.update(pull(path, three))
        elif org in spiritual:
            path = '../data/clubdata/service/spiritual.csv'
            results.update(pull(path, three))
        elif org in kindness:
            path = '../data/clubdata/service/kindness.csv'
            results.update(pull(path, three))
        elif org in political:
            path = '../data/clubdata/service/political.csv'
            results.update(pull(path, three))
    return results


def lineProcessor(file):
    """ The primary function of the program. Ingests CSV, parses information, sends it to processors, and emails the user with the results. """
    # Setup
    email = {
        'sender': "bluequizinvolvement@gmail.com",
        'password': "wwjjcwvylkigvyli",
        'subject': "Aggie BLUE Quiz Involvement Survey Results!"
    }

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
                        quizResponses.append(0)
                    else:
                        if el < 7:  # Non-Integer Data
                            quizResponses.append(elementList[el])
                        else:  # Integer Data
                            quizResponses.append(int(elementList[el]))
            # ID Logging
            """ This saves the Response ID so future pulls can start from the correct spot. """
            log = open('../data/response_id.txt', 'w')
            log.write(quizResponses.pop(0))
            log.close()
            # Allocating
            """ This sends the data to the allocator, which counts up the points and picks the top three clubs. """
            topThree = allocator(quizResponses)
            colleges = []
            index = 0
            while index < len(topThree):
                if isinstance(topThree[index], int):
                    colleges.append(topThree.pop(0))  # Grab college list from resulting list
                else:
                    index += 1
            # Emailing
            """ This collects all the data and sends it to the emailing function to be sent out. """
            email['receiver'] = topThree.pop(0)  # Grab email
            results = getResults(topThree)
            emailUser(email, colleges, topThree, results)
        else:
            skipHeadings += 1


def getFile(path):
    """Retrieve a file. That's about it. """
    try:
        file = open(path, encoding="utf8")
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
    os.remove(filepath)
    print("Run Complete!")
