import glob
import os, sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def emailUser(info):
    """ This function handles the email that sends the top three organizations """
    # Setup
    sender = ""  # Undetermined as of yet
    receiver = info[0]
    password = ""  # Undetermined as of yet
    message = MIMEMultipart("alternative")
    orgs = {
        "pcab": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                 "President's Cabinet",
                 "Work on initiatives set by the USUSA President. It’s function/form is different from year-to-year, but for our purposes PCab is focused on:",
                 ""],
        "fees": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                 "Student Fee Board",
                 "Advisory board to the University President to decide on student fees. Receives presentations, discusses, reviews, & votes on whether or not to recommend a change in student fees.",
                 ""],
        "grc": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                "Government Relations Council (GRC)",
                "Advocate for student interest to state & local officials & raise awareness of civic issues on campus. Plans Gripe Night, Voter Registration, & Aggie Ice Cream Day on the Hill",
                ""],
        "blucru": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                   "Blue Crew",
                   "Assist in the marketing of events & helps set up/take down for events",
                   ""],
        "activity": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                     "Activities Committee",
                     "Plans & executes The Howl, Mardi Gras, & End of Year Bash",
                     ""],
        "series": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                   "Series Committee",
                   "Plans & executes regular/recurring events that are generally more artistic like PoBev & Moonlight & Music",
                   ""],
        "trad": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                 "Traditions Committee",
                 "Plans & executes Homecoming week, Mr.USU, Sweater Swap, & High Stakes Bingo",
                 ""],
        "hurd": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                 "HURD Committee",
                 "Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports",
                 ""],
        "council": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                    "College Councils",
                    "Advocate for student interests to their college’s administration (deans & department heads), plan & execute service projects & college specific events. Each college has its own week filled with events.",
                    ""],
        "saa": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                "Student Alumni Association",
                "Create lifelong aggies. Focuses on donors and guest speakers. Engage alumni. Plan & execute initiatives to connect students with alumni. Also, True Aggie Night, Miss USU, and A-Day.",
                ""],
        "serve": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                  "Service Center Programs",
                  "Some of the programs run out of the center are SNAC, gleaning, best buddies, Special Olympics, Athletics United, etc.",
                  ""],
        "states": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                   "Statesman",
                   "Student news. Gives students an opportunity to write",
                   ""],
        "radio": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                  "Aggie Radio",
                  "Provides students with opportunities to DJ, create radio talk shows, podcasts, & plan/coordinate events (mainly concerts)",
                  ""],
        "blight": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                   "Blue Light",
                   "Meet content creation needs for clients, primarily USUSA",
                   ""],
        "fsl": ["http://labs.jensimmons.com/2016/examples/images/testscreen-large.jpg",
                "Fraternity & Sorority Life",
                "Advance personal development through community service, philanthropic fundraising, & activities.",
                ""]
    }
    councils = {
        1: ["Arts Application:", ""],
        2: ["Agriculture Application:", ""],
        3: ["Engineering Application:", ""],
        4: ["Humanities & Social Sciences Application:", ""],
        5: ["Science Application:", ""],
        6: ["Education Application:", ""],
        7: ["Huntsman Application:", ""],
        8: ["Natural Resources Application:", ""],
    }

    # Compile Message
    message["Subject"] = "Blue Quiz Involvement Survey Results!"
    message["From"] = sender
    message["To"] = receiver
    text = """\
        “The only way you can taste life is with involvement.” Sadhguru
        Thank you for filling out our survey. You are a great match for the following three committees. Our goal here 
        at USU is to cultivate an environment of development and growth and we need your help. Every single student 
        can make a difference in our community and help others feel welcomed and heard, and it starts with 
        involvement. Check out the options listed below or browse for other opportunities listed on our website. We 
        can’t wait to hear your perspectives and ideas and together change our school for the better. """
    html = """\
        <!DOCTYPE html>
        <html>
            <head>
                <style type="text/css" media="screen">
                    img {
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                        width: 100%;
                        max-width: 900px;
                        height:  auto;
                        object-fit: contain;
                        align-content: center;
                    }
                    h1{
                        font-family:sans-serif;
                        text-align: center;
                    }
                    p{
                        font-family: Georgia, serif;
                        text-align: center;
                        font-size: 12pt;
                    }
                    table{
                        background-color: #0F2439;
                        border-spacing: 0;
                        border-collapse: collapse;
                        table-layout: fixed;
                        margin: 0;
                    }
                    td{
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                    }
                    ol{
                        font-family: Georgia, serif;
                        font-size: 12pt;
                    }
                </style>
            </head>
            <body>
                <div style="background-color: #0F2439; backface-visibility: 75%;" >
                    <img src="https://www.usu.edu/admissions/images/USU_Get_Involved.jpg" alt="Students playing pool">
                </div>
                <div style="background-color:#eee; padding:8px; word-wrap: break-word;">
                    <h1 style="font-family:garamond; text-align:center;">"The only way you can taste life is with involvement.” - <em>Sadhguru</em></h1>
                    <p style="font-family:garamond; font-size: 16pt;">Thank you for filling out our survey. You are a great match for the following three committees. Our goal here at USU is to cultivate an environment of development and growth and we need your help. Every single student can make a difference in our community and help others feel welcomed and heard, and it starts with involvement. Check out the options listed below or browse for other opportunities listed on <a href="https://www.usu.edu/involvement/"?>our website</a>. <br>We can’t wait to hear your perspectives and ideas and together change our school for the better. </p>
                </div>
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                    <tbody>
        """
    for x in range(3):
        if info[x+1] == "council":
            text += """
            """ + orgs[info[x+1]][1] + """
                Purpose: """ + orgs[info[x+1]][2] + """
            """
            html += '''
            <tr>
                <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <img src="''' + orgs[info[x+1]][0] + '''" style="width: 100%; max-width: 600px;">
                </td>
            </tr>
            <tr>
                <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px;">
                    <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + orgs[info[x+1]][1] + '''</h1>
                    <p style="text-align: left;"><b>Purpose: </b>''' + orgs[info[x+1]][2] + '''</p>
            '''
            x = 4
            while x < len(info):
                text += councils[info[x]][0] + ": " + councils[info[x]][1] + "\n"
                html += '''<p style="text-align: left; margin: 0 0 10px;"><b>''' + councils[info[x]][0] + '''</b><a href="''' + councils[info[x]][1] + '''"> ''' + councils[info[x]][1] + '''</a></p>'''
                x += 1
            html += """
                           </td>
                       </tr>"""
        elif info[x+1] == "pcab":
            text += """
            """ + orgs[info[x+1]][1] + """
            Purpose: """ + orgs[info[x+1]][2] + """
            \t 1. Enhancing equity on USU campuses
            \t 2. Increasing access to involvement opportunities
            \t 3. Amplifying student voices
            \t 4. Promoting & fundraising for scholarship opportunities that incentivize service & leadership.
            Application Link: """ + orgs[info[x+1]][3] + """
            """
            html += '''
            <tr>
                <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
            </tr>
            <tr>
                <td>
                    <img src="''' + orgs[info[x+1]][0] + '''" alt="TestImage" style="width: 100%; max-width: 600px;">
                </td>
            </tr>
            <tr>
                <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px;">
                    <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + orgs[info[x+1]][1] + '''</h1>
                    <p style="text-align: left;"><b>Purpose: </b>''' + orgs[info[x+1]][2] + '''</p>
                    <ol>
                        <li>Enhancing equity on USU campuses</li>
                        <li>Increasing access to involvement opportunities</li>
                        <li>Amplifying student voices</li>
                        <li>Promoting & fundraising for scholarship opportunities that incentivize service & leadership.</li>
                    </ol>
                    <p style="text-align: left; margin: 0 0 10px;"><b>Application Link: </b>''' + orgs[info[x+1]][3] + '''</p>
                </td>
            </tr> 
            '''
        else:
            text += """
                """ + orgs[info[x+1]][1] + """
                Purpose: """ + orgs[info[x+1]][2] + """
                Application Link: """ + orgs[info[x+1]][3] + """
                """
            html += '''
                <tr>
                    <td aria-hidden="true" height="40" style="font-size: 0px; line-height: 0px;">&nbsp;</td>
                </tr>
                <tr>
                    <td>
                        <img src="''' + orgs[info[x+1]][0] + '''" style="width: 100%; max-width: 600px;">
                    </td>
                </tr>
                <tr>
                    <td style="padding: 10px 20px 20px 20px; font-family:sans-serif; background-color: #eee; width: 100%; max-width: 560px;">
                        <h1 style="margin: 0 0 10px; text-align: left; font-family:Georgia, serif;">''' + orgs[info[x+1]][1] + '''</h1>
                        <p style="text-align: left;"><b>Purpose: </b>''' + orgs[info[x+1]][2] + '''</p>
                        <p style="text-align: left; margin: 0 0 10px;"><b>Application Link: </b>''' + orgs[info[x+1]][3] + '''</p>
                    </td>
                </tr> 
                '''
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
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        print("Email Sent!")


def allocator(data):
    """ This function takes the orderly list of data and sorts all of the points and whatnot. """
    # Setup
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
    orgs = {
        "pcab": 0,
        "fees": 0,
        "grc": 0,
        "blucru": 0,
        "activity": 0,
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
    for x in range(len(data)):
        if x > 0:
            data[x] = int(data[x])

    # Council Formatting
    '''The college major question (Q1) allows multiple choices, and that heavily screws up the indexes. This is to 
    remedy that. '''
    questions = 12  # Change for the set amount of questions there should be for the quiz.
    diff = len(data) - questions
    colleges = []
    if diff > 0:
        for x in range(diff):
            colleges.append(data.pop(2))
    colleges.append(data[1])

    # Point Allocation
    ''' If future questions are added, just add the lines here '''
    # Q3: --------------------------------
    attributes["project"] += data[3]
    attributes["detail"] += data[3]
    # Q4: --------------------------------
    attributes["political"] += data[4]
    # Q5: --------------------------------
    if data[5] == 1:
        attributes["hype"] += data[5]
        attributes["party"] += data[5]
        attributes["athletic"] += data[5]
    # Q6: --------------------------------
    attributes["helpful"] += data[6]
    attributes["academic"] += data[6]
    attributes["detail"] += data[6]
    attributes["project"] += data[6]
    # Q7: === to be added ===
    # Q8: --------------------------------
    if data[8] == 1:
        attributes["hype"] += 3
        attributes["athletic"] += 3
        attributes["spirit"] += 3
    elif data[8] == 2:
        attributes["creative"] += 3
    elif data[8] == 3:
        attributes["party"] += 3
        attributes["music"] += 3
        attributes["extroverted"] += 3
    elif data[8] == 4:
        attributes["academic"] += 3
        attributes["mentor"] += 3
    # Q9: --------------------------------
    if data[9] == 1:
        # ===not sure what to add to here===
        attributes["political"] += 1
    elif data[9] == 2:
        attributes["helpful"] += 3
        attributes["spirit"] += 3
        attributes["service"] += 3
    elif data[9] == 3:
        attributes["mentor"] += 3
        attributes["extroverted"] += 3
        attributes["leader"] += 3
    elif data[9] == 4:
        attributes["political"] += 3
        attributes["leader"] += 3
    elif data[9] == 5:
        attributes["detail"] += 3
        attributes["leader"] += 3
    elif data[9] == 6:
        attributes["extroverted"] += 3
    # Q10: --------------------------------
    attributes["planner"] += data[10]
    attributes["project"] += data[10]
    attributes["detail"] += data[10]

    # Processing
    ''' If future organizations are added, add the lines here. Add them to the dictionary as well. '''
    orgs["pcab"] = (attributes["leader"] + attributes["service"] + attributes["project"] + attributes["political"])
    orgs["fees"] = (attributes["detail"] + attributes["time"])
    orgs["grc"] = (attributes["political"] + attributes["academic"])
    orgs["blucru"] = (attributes["service"] + attributes["hype"] + attributes["helpful"])
    orgs["activity"] = (attributes["party"] + attributes["planner"] + attributes["extroverted"])
    orgs["series"] = (attributes["extroverted"] + attributes["creative"] + attributes["music"])
    orgs["trad"] = (attributes["helpful"] + attributes["planner"] + attributes["extroverted"] + attributes["spirit"])
    orgs["hurd"] = (attributes["hype"] + attributes["extroverted"] + attributes["athletic"])
    orgs["council"] = (attributes["service"] + attributes["planner"] + attributes["academic"] + 2)
    orgs["saa"] = (attributes["helpful"] + attributes["extroverted"] + attributes["spirit"])
    orgs["serve"] = (attributes["service"] + attributes["helpful"] + attributes["mentor"])
    orgs["states"] = (attributes["creative"] + attributes["mentor"])
    orgs["radio"] = (attributes["creative"] + attributes["music"])
    orgs["blight"] = (attributes["detail"] + attributes["creative"])
    orgs["fsl"] = (attributes["service"] + attributes["hype"] + attributes["party"])

    # Reporting
    impInfo = [data[0]]
    orgsList = sorted(orgs.items(), key=lambda k: k[1], reverse=True)
    for x in range(3):
        if orgsList[x][0] == "council" and (9 or 10 in colleges):
            orgsList.pop(x)
        impInfo.append(orgsList[x][0])
    if data[1] < 9:
        for el in colleges:
            impInfo.append(el)
    return impInfo


def lineProcessor(file):
    """ This function takes the data from the CSV file, rips out the necessary info, and processes it """
    # Processing
    skip = 0
    for line in file:
        if skip > 2:
            ## Ripping
            quizResponses = []
            line = line.strip('\n')
            line = line.replace('"', "")
            elementList = line.split(',')
            for el in range(len(elementList)):
                if el >= 17:
                    quizResponses.append(elementList[el])
            ## Allocating
            importantInfo = allocator(quizResponses)
            ## Reporting
            emailUser(importantInfo)
        else:
            skip += 1


def getFile():
    """ This function locates the CSV file with 'BQR' in it, and pulls from that. """
    try:
        path = glob.glob('../**/BQR*')[0]  # Takes the first file with 'BQR' in the directory.
    except IndexError:
        sys.exit(1)
    return path


if __name__ == '__main__':
    # File Processing
    filepath = getFile()
    fileObj = open(filepath)
    lineProcessor(fileObj)
    fileObj.close()
    os.remove(filepath)