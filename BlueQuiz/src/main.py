import glob
import os, sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def emailUser(info):
    """ This function handles the email that sends the top three organizations """
    # Setup
    sender = "bluequizinvolvement@gmail.com"
    receiver = info[0]
    password = "wdB!PGbV*GhG&23y"
    message = MIMEMultipart("alternative")
    orgs = {
        "pcab": ["https://usustatesman.com/wp-content/uploads/2021/04/webp.net-resizeimage-19.jpg",
                 "President's Cabinet",
                 "Work on initiatives set by the USUSA President. It’s function/form is different from year-to-year, but for our purposes PCab is focused on:",
                 "Application Link: ",
                 "https://usu.co1.qualtrics.com/jfe/form/SV_0vssECtz4E3oGii"],
        "fees": ["https://usustatesman.com/wp-content/uploads/2021/01/webp.net-resizeimage-8-1050x709.jpg",
                 "Student Fee Board",
                 "Advisory board to the University President and chaired by the USUSA Executive VP. Decides on student fees. Receives presentations, discusses, reviews, & votes on whether or not to recommend a change in student fees. Applications usually open up towards the end of September.",
                 "Website: ",
                 "https://www.usu.edu/student-affairs/student-fees"],
        "grc": ["https://usustatesman.com/wp-content/uploads/2014/09/GRC_VoterRegistration.jpg",
                "Government Relations Council (GRC)",
                "Advocate for student interest to state & local officials & raise awareness of civic issues on campus. Plans Gripe Night, Voter Registration, & Aggie Ice Cream Day on the Hill",
                "Application Link: ",
                "https://usu.co1.qualtrics.com/jfe/form/SV_6AtXnSBck14zsDs"],
        "blucru": ["https://usustatesman.com/wp-content/uploads/2015/12/IMG_6393.jpg",
                   "Blue Crew",
                   "Assist in the marketing of events & helps set up/take down for events",
                   "Application Link: ",
                   "https://usu.co1.qualtrics.com/jfe/form/SV_dh6MakKgwh0WKtU"],
        "activity": ["https://usustatesman.com/wp-content/uploads/2018/10/mh-howl-2016-7-1-1050x500.jpg",
                     "Activities Committee",
                     "Plans & executes The Howl, Mardi Gras, & End of Year Bash",
                     "Application Link: ",
                     "https://usu.co1.qualtrics.com/jfe/form/SV_5tnDz4KcQkIMUTk"],
        "series": ["https://usustatesman.com/wp-content/uploads/2015/10/TM_Pobev.jpg",
                   "Series Committee",
                   "Plans & executes regular/recurring events that are generally more artistic like PoBev and Moonlight & Music",
                   "Application Link: ",
                   "https://usu.co1.qualtrics.com/jfe/form/SV_5tnDz4KcQkIMUTk"],
        "trad": ["https://usustatesman.com/wp-content/uploads/2020/09/img_9338-1-1050x700.jpg",
                 "Traditions Committee",
                 "Plans & executes Homecoming week, Mr.USU, Sweater Swap, & High Stakes Bingo",
                 "Application Link: ",
                 "https://usu.co1.qualtrics.com/jfe/form/SV_5tnDz4KcQkIMUTk"],
        "hurd": ["https://usustatesman.com/wp-content/uploads/2017/10/usuvsunr05-1-1050x700.jpg",
                 "HURD Committee",
                 "Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports",
                 "Application Link: ",
                 "https://usu.co1.qualtrics.com/jfe/form/SV_cSAGzZBiW4065xQ"],
        "council": ["https://usustatesman.com/wp-content/uploads/2019/01/20190109_feeboardmeeting_rimando2-1050x700.jpg",
                    "College Councils",
                    "Advocate for student interests to their college’s administration (deans & department heads), plan & execute service projects & college specific events. Each college has its own week filled with events.",
                    ],
        "saa": ["https://usustatesman.com/wp-content/uploads/2015/10/KT.SAAnetworking.10.8.03.jpg",
                "Student Alumni Association",
                "Create lifelong aggies. Focuses on donors and guest speakers. Engage alumni. Plan & execute initiatives to connect students with alumni. Also, True Aggie Night, Miss USU, and A-Day.",
                "Website: ",
                "https://www.usu.edu/alumni/"],
        "serve": ["https://usustatesman.com/wp-content/uploads/2021/02/snac.jpg",
                  "Service Center Programs",
                  "Some of the programs run out of the center are SNAC, gleaning, best buddies, Special Olympics, Athletics United, etc.",
                  "Website: ",
                  "https://www.usu.edu/servicecenter/index"],
        "states": ["https://i.ibb.co/2vhVDVJ/states.png",
                   "Statesman",
                   "Student news. Gives students an opportunity to write",
                   "Application Link: ",
                   "https://docs.google.com/forms/d/e/1FAIpQLSea_u0ACnO9fcVxBlN19upb2QVO2Qmg2YLPl9SibU6p2q-CgA/viewform"],
        "radio": ["https://usustatesman.com/wp-content/uploads/2013/10/2840326-2159898677.jpg",
                  "Aggie Radio",
                  "Provides students with opportunities to DJ, create radio talk shows, podcasts, & plan/coordinate events (mainly concerts)",
                  "Application Link: ",
                  "https://docs.google.com/forms/d/e/1FAIpQLSea_u0ACnO9fcVxBlN19upb2QVO2Qmg2YLPl9SibU6p2q-CgA/viewform"],
        "blight": ["https://i.ibb.co/mTnCpwH/blight.png",
                   "Blue Light",
                   "Meet content creation needs for clients, primarily USUSA",
                   "Application Link: ",
                   "https://docs.google.com/forms/d/e/1FAIpQLSea_u0ACnO9fcVxBlN19upb2QVO2Qmg2YLPl9SibU6p2q-CgA/viewform"],
        "fsl": ["https://i.ibb.co/xgrX0Lm/fsl.jpg",
                "Fraternity & Sorority Life",
                "Advance personal development through community service, philanthropic fundraising, & activities.",
                "Sorority Link: ",
                "Fraternity Link: ",
                "https://www.usu.edu/involvement/fsl/sorority-recruitment",
                "https://docs.google.com/forms/d/e/1FAIpQLSfoAJLxRYokCNgDpJ-0A4pCIZv7ZLM3bF2Ng8CiYMwRHJrERQ/viewform?usp=send_form"]
    }
    councils = {
        1: ["Arts Contact:", "mailto:", "ccasenator.ususa@usu.edu"],
        2: ["Agriculture Contact:", "mailto:", "caassenator.ususa@usu.edu"],
        3: ["Engineering Application:", "mailto:", "engrsenator.ususa@usu.edu"],
        4: ["Humanities & Social Sciences Application:", "", "https://usu.co1.qualtrics.com/jfe/form/SV_9mh79aPEaFUpE9M"],
        5: ["Science Application:", "", "https://usu.co1.qualtrics.com/jfe/form/SV_9vLBETERRRrJmKy"],
        6: ["Education Application:", "", "https://docs.google.com/forms/d/e/1FAIpQLSdM7-KZXgiu4FgrfTT5OuJiT3oHrpQPPCfiu4m02muxdn1Psw/viewform"],
        7: ["Huntsman Contact:", "mailto:" ,"huntsmansenator.ususa@usu.edu"],
        8: ["Natural Resources Application:", "", "https://usu.co1.qualtrics.com/jfe/form/SV_9mh79aPEaFUpE9M"],
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
                        color:black;
                    }
                    p{
                        font-family: Georgia, serif;
                        text-align: center;
                        font-size: 12pt;
                        color:black;
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
                text += councils[info[x]][0] + ": " + councils[info[x]][2] + "\n"
                html += '''<p style="text-align: left; margin: 0 0 10px;"><b>''' + councils[info[x]][0] + '''</b><a href="''' + councils[info[x]][1] + councils[info[x]][2] + '''"> ''' + councils[info[x]][2] + '''</a></p>'''
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
            """ + orgs[info[x+1]][3] + orgs[info[x+1]][4] + """
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
                    <p style="text-align: left; margin: 0 0 10px;"><b>''' + orgs[info[x+1]][3] + '''</b><a href="''' + orgs[info[x+1]][4] + '''">''' + orgs[info[x+1]][4] + '''</a></p>
                </td>
            </tr> 
            '''
        elif info[x+1] == "fsl":
            text += """
            """ + orgs[info[x+1]][1] + """
                Purpose: """ + orgs[info[x+1]][2] + """
                """ + orgs[info[x+1]][3] + orgs[info[x+1]][5] + """
                """ + orgs[info[x+1]][4] + orgs[info[x+1]][6] + """
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
                    <p style="text-align: left; margin: 0 0 10px;"><b>''' + orgs[info[x+1]][3] + '''</b><a href="''' + orgs[info[x+1]][5] + '''">''' + orgs[info[x+1]][5] + '''</a></p>
                    <p style="text-align: left; margin: 0 0 10px;"><b>''' + orgs[info[x+1]][4] + '''</b><a href="''' + orgs[info[x+1]][6] + '''">''' + orgs[info[x+1]][6] + '''</a></p>
                </td>
            </tr> 
            '''
        else:
            text += """
                """ + orgs[info[x+1]][1] + """
                Purpose: """ + orgs[info[x+1]][2] + """
                """ + orgs[info[x+1]][3] + orgs[info[x+1]][4] + """
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
                        <p style="text-align: left; margin: 0 0 10px;"><b>''' + orgs[info[x+1]][3] + '''</b><a href="''' + orgs[info[x+1]][4] + '''">''' + orgs[info[x+1]][4] + '''</a></p>
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
        print("Email Sent to: " + receiver)


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
        if x > 1:
            data[x] = int(data[x])

    # Council Formatting
    '''The college major question (Q1) allows multiple choices. As of v1.2.0 the way the CSV and program handles this
    information has changed, and now works a little better.'''
    colleges = []
    for x in range(10):
        colleges.append(data.pop(2))

    # Point Allocation
    # Q2: --------------------------------
    if data[2] != -99:
        attributes["project"] += data[2]
        attributes["detail"] += data[2]
        attributes["planner"] += data[2]
    # Q3: --------------------------------
    if data[3] != -99:
        attributes["political"] += data[3]
        orgs["states"] += 2
    # Q4: --------------------------------
    if data[4] == 1:
        attributes["hype"] += 5
        attributes["party"] += 4
        attributes["athletic"] += 4
        attributes["spirit"] += 3
    elif data[4] == 2:
        attributes["time"] += 2
        attributes["mentor"] += 2
        attributes["extroverted"] -= 1
    # Q5: --------------------------------
    if data[5] != -99:
        attributes["helpful"] += data[5]
        attributes["academic"] += data[5]
        attributes["detail"] += data[5]
        attributes["project"] += data[5]
    # Q6: --------------------------------
    if data[6] == 1:
        attributes["hype"] += 3
        attributes["athletic"] += 3
        attributes["spirit"] += 3
    elif data[6] == 2:
        attributes["creative"] += 3
        orgs["blight"] += 2
    elif data[6] == 3:
        attributes["party"] += 3
        attributes["music"] += 3
        attributes["extroverted"] += 3
    elif data[6] == 4:
        attributes["academic"] += 3
        attributes["mentor"] += 3
    # Q7: --------------------------------
    if data[7] == 1:
        attributes["mentor"] += 3
        attributes["extroverted"] += 3
        attributes["leader"] += 3
    elif data[7] == 2:
        attributes["helpful"] += 3
        attributes["spirit"] += 3
        attributes["service"] += 3
    elif data[7] == 3:
        attributes["detail"] += 3
        attributes["leader"] += 3
        attributes["project"] += 3
        orgs["saa"] += 2
    elif data[7] == 4:
        attributes["political"] += 3
        attributes["leader"] += 3
        attributes["time"] += 2
    elif data[7] == 5:
        attributes["extroverted"] += 3
        attributes["leader"] += 3
        attributes["service"] += 3
    # Q8: --------------------------------
    if data[8] != -99:
        attributes["planner"] += data[8]
        attributes["project"] += data[8]
        attributes["detail"] += data[8]
        attributes["time"] -= (data[8]-2)
    # Q9: --------------------------------
    if data[9] == 1:
        attributes["academic"] += 3
        attributes["planner"] += 3
    if data[9] == 2:
        attributes["athletic"] += 3
        attributes["music"] += 2
    if data[9] == 3:
        attributes["spirit"] += 2
        attributes["helpful"] += 2
    if data[9] == 4:
        attributes["athletic"] += 2
        attributes["time"] += 2
    if data[9] == 5:
        attributes["music"] += 3
        attributes["creative"] += 3
    # Q10: --------------------------------
    if data[10] == 1 or data[10] == 3:
        attributes["political"] += 3
        attributes["academic"] += 3
        attributes["planner"] += 3
    elif data[10] == 2:
        attributes["creative"] += 3
        attributes["music"] += 3
        attributes["hype"] += 3

    # Processing
    ''' If future organizations are added, add the lines here. Add them to the dictionary as well. '''
    orgs["pcab"] += (attributes["leader"] + attributes["service"] + attributes["project"] + attributes["political"])
    orgs["fees"] += (attributes["detail"] + attributes["time"])
    orgs["grc"] += (attributes["political"] + attributes["academic"])
    orgs["blucru"] += (attributes["service"] + attributes["hype"] + attributes["helpful"])
    orgs["activity"] += (attributes["party"] + attributes["planner"] + attributes["extroverted"])
    orgs["series"] += (attributes["extroverted"] + attributes["creative"] + attributes["music"])
    orgs["trad"] += (attributes["helpful"] + attributes["planner"] + attributes["extroverted"] + attributes["spirit"])
    orgs["hurd"] += (attributes["hype"] + attributes["extroverted"] + attributes["athletic"])
    orgs["council"] += (attributes["service"] + attributes["planner"] + attributes["academic"] + len(colleges)) # Bump if they know
    orgs["saa"] += (attributes["helpful"] + attributes["extroverted"] + attributes["spirit"])
    orgs["serve"] += (attributes["service"] + attributes["helpful"] + attributes["mentor"] + 2) # Bump due to less q's
    orgs["states"] += (attributes["creative"] + attributes["mentor"])
    orgs["radio"] += (attributes["creative"] + attributes["music"])
    orgs["blight"] += (attributes["detail"] + attributes["creative"])
    orgs["fsl"] += (attributes["service"] + attributes["hype"] + attributes["party"])

    # Reporting
    impInfo = [data[0], data[1]]
    orgsList = sorted(orgs.items(), key=lambda k: k[1], reverse=True)
    for x in range(3):
        if orgsList[x][0] == "council":
            if colleges[8] == 1 or colleges[9] == 1:
                orgsList.pop(x)
        impInfo.append(orgsList[x][0])
    if "council" in impInfo:
        for x in range(len(colleges)):
            if colleges[x] == 1:
                impInfo.append(x+1)
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
            elementList = line.split(',')
            for el in range(len(elementList)):
                if (11 <= el < 31) or el == 0:
                    quizResponses.append(elementList[el])
            ## Allocating
            importantInfo = allocator(quizResponses)
            ## ID Logging
            log = open('../data/response_id.txt', 'w')
            log.write(importantInfo.pop(0))
            log.close()
            ## Reporting
            emailUser(importantInfo)
        else:
            skip += 1


def getFile():
    """ This function locates the CSV file with 'BQR' in it, and pulls from that. """
    try:
        path = glob.glob('../data/Blue Quiz.csv')[0]
    except IndexError:
        print("No File Found")
        sys.exit(1)
    return path


if __name__ == '__main__':
    # File Processing
    filepath = getFile()
    fileObj = open(filepath)
    lineProcessor(fileObj)
    fileObj.close()
    os.remove(filepath)