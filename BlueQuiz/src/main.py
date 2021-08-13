import glob
import os, sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def emailUser(info):
    """ This function handles the email that sends the top three organizations """
    # Setup
    sender = "acollegeemailfororganization@gmail.com"  # Undetermined as of yet
    receiver = info[0]
    password = ""  # Undetermined as of yet
    message = MIMEMultipart("alternative")
    orgs = {
        "pcab": ["""
            President's Cabinet
            Purpose: Work on initiatives set by the USUSA President. It’s function/form is different from year-to-year, but for our purposes PCab is focused on:
            \t 1. Enhancing equity on USU campuses
            \t 2. Increasing access to involvement opportunities
            \t 3. Amplifying student voices
            \t 4. Promoting & fundraising for scholarship opportunities that incentivize service & leadership.
            Application Link:
            """,
                 """
            <p><b>President's Cabinet</b><br>
                <b>Purpose:</b> Work on initiatives set by the USUSA President. It’s function/form is different from year-to-year, but for our purposes PCab is focused on:
                <ol>
                <li>Enhancing equity on USU campuses</li>
                <li>Increasing access to involvement opportunities</li>
                <li>Amplifying student voices</li>
                <li>Promoting & fundraising for scholarship opportunities that incentivize service & leadership.</li>
                </ol>
                <b>Application Link:</b> 
            """],

        "fees": ["""
            Student Fee Board
            Purpose: Advisory board to the University President to decide on student fees. Receives presentations, discusses, reviews, & votes on whether or not to recommend a change in student fees.
            Application Link:
            """,
                 """
            <p><b>Student Fee Board</b><br>
                <b>Purpose:</b> Advisory board to the University President to decide on student fees. Receives presentations, discusses, reviews, & votes on whether or not to recommend a change in student fees.<br>
                <b>Application Link:</b> 
            """],

        "grc": ["""
            Government Relations Council (GRC)
            Purpose: Advocate for student interest to state & local officials & raise awareness of civic issues on campus. Plans Gripe Night, Voter Registration, & Aggie Ice Cream Day on the Hill
            Application Link:
            """,
                """
            <p><b>Government Relations Council (GRC)</b><br>
                <b>Purpose:</b> Advocate for student interest to state & local officials & raise awareness of civic issues on campus. Plans Gripe Night, Voter Registration, & Aggie Ice Cream Day on the Hill<br>
                <b>Application Link:</b> 
            """],

        "blucru": ["""
            Blue Crew
            Purpose: Assist in the marketing of events & helps set up/take down for events
            Application Link:
            """,
                   """
            <p><b>Blue Crew</b><br>
                <b>Purpose:</b> Assist in the marketing of events & helps set up/take down for events<br>
                <b>Application Link:</b> 
            """],

        "activity": ["""
            Activities Committee
            Purpose: Plans & executes The Howl, Mardi Gras, & End of Year Bash
            Application Link:
            """,
                     """
            <p><b>Activities Committee</b><br>
                <b>Purpose:</b> Plans & executes The Howl, Mardi Gras, & End of Year Bash<br>
                <b>Application Link:</b> 
            """],

        "series": ["""
            Series Committee
            Purpose: Plans & executes regular/recurring events that are generally more artistic like PoBev & Moonlight & Music
            Application Link:
            """,
                   """
            <p><b>Series Committee</b><br>
                <b>Purpose:</b> Plans & executes regular/recurring events that are generally more artistic like PoBev & Moonlight & Music<br>
                <b>Application Link:</b> 
            """],

        "trad": ["""
            Traditions Committee
            Purpose: Plans & executes Homecoming week, Mr.USU, Sweater Swap, & High Stakes Bingo
            Application Link:
            """,
                 """
            <p><b>Traditions Committee</b><br>
                <b>Purpose:</b> Plans & executes Homecoming week, Mr.USU, Sweater Swap, & High Stakes Bingo<br>
                <b>Application Link:</b> 
            """],

        "hurd": ["""
            HURD Committee
            Purpose: Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports
            Application Link:
            """,
                 """
            <p><b>HURD Committee</b><br>
                <b>Purpose:</b> Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports<br>
                <b>Application Link:</b> 
            """],

        "council": ["""
            College Councils
            Purpose: Advocate for student interests to their college’s administration (deans & department heads), plan & execute service projects & college specific events. Each college has its own week filled with events.
            """,
                    """
            <p><b>College Councils</b><br>
                <b>Purpose:</b> Advocate for student interests to their college’s administration (deans & department heads), plan & execute service projects & college specific events. Each college has its own week filled with events.<br>
            """],

        "saa": ["""
            Student Alumni Association
            Purpose: Create lifelong aggies. Focuses on donors and guest speakers. Engage alumni. Plan & execute initiatives to connect students with alumni. Also, True Aggie Night, Miss USU, and A-Day.
            Application Link:
            """,
                """
            <p><b>Student Alumni Association</b><br>
                <b>Purpose:</b> Create lifelong aggies. Focuses on donors and guest speakers. Engage alumni. Plan & execute initiatives to connect students with alumni. Also, True Aggie Night, Miss USU, and A-Day.<br>
                <b>Application Link:</b> 
            """],

        "serve": ["""
            Service Center Programs
            Purpose: Some of the programs run out of the center are SNAC, gleaning, best buddies, Special Olympics, Athletics United, etc.
            Application Link:
            """,
                  """
            <p><b>Service Center</b><br>
                <b>Purpose:</b> Some of the programs run out of the center are SNAC, gleaning, best buddies, Special Olympics, Athletics United, etc.<br>
                <b>Application Link:</b> 
            """],

        "states": ["""
            Statesman
            Purpose: Student news. Gives students an opportunity to write
            Application Link:
            """,
                   """
            <p><b>Statesman</b><br>
                <b>Purpose:</b> Student news. Gives students an opportunity to write<br>
                <b>Application Link:</b> 
            """],

        "radio": ["""
            Aggie Radio
            Purpose: Provides students with opportunities to DJ, create radio talk shows, podcasts, & plan/coordinate events (mainly concerts)
            Application Link:
            """,
                  """
            <p><b>Aggie Radio</b><br>
                <b>Purpose:</b> Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports<br>
                <b>Application Link:</b> 
            """],

        "blight": ["""
            Blue Light
            Purpose: Meet content creation needs for clients, primarily USUSA
            Application Link:
            """,
                   """
            <p><b>Blue Light</b><br>
                <b>Purpose:</b> Meet content creation needs for clients, primarily USUSA<br>
                <b>Application Link:</b> 
            """],

        "fsl": ["""
            Fraternity & Sorority Life
            Purpose: Advance personal development through community service, philanthropic fundraising, & activities.
            Application Link:
            """,
                """
            <p><b>Fraternity & Sorority Life</b><br>
                <b>Purpose:</b> Advance personal development through community service, philanthropic fundraising, & activities.<br>
                <b>Application Link:</b> 
            """]
    }
    councils = {
        1: ["", "<b>Arts Application: </b> <a href=""></a><br>"],
        2: ["", "<b>Agriculture Application: </b><a href=""></a><br>"],
        3: ["", "<b>Engineering Application: </b><a href=""></a><br>"],
        4: ["", "<b>Humanities & Social Sciences Application: </b><a href=""></a><br>"],
        5: ["", "<b>Science Application: </b><a href=""></a><br>"],
        6: ["", "<b>Education Application: </b><a href=""></a><br>"],
        7: ["", "<b>Huntsman Application: </b><a href=""></a><br>"],
        8: ["", "<b>Natural Resources Application: </b><a href=""></a><br>"],
    }

    # Compile Message
    message["Subject"] = "Blue Quiz Involvement Survey Results"
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
        <html>
            <body>
                <img src="https://math.usu.edu/ldp/galleries/.private_ldp/a68540/production/master/c3bc1389-5787-4101-92d0-91c4fde8df13.jpg" alt="Drone view of Old Main">
                <h3>“The only way you can taste life is with involvement.” <em>Sadhguru</em></h3>
                <p>Thank you for filling out our survey. You are a great match for the following three committees. Our goal here at USU is to cultivate an environment of development and growth and we need your help. Every single student can make a difference in our community and help others feel welcomed and heard, and it starts with involvement. Check out the options listed below or browse for other opportunities listed on our website. We can’t wait to hear your perspectives and ideas and together change our school for the better.</p>
        """
    for x in range(3):
        text += orgs[info[x+1]][0]
        html += orgs[info[x+1]][1]
        if info[x+1] == "council":
            x = 4
            while x <= len(info):
                text += councils[x][0]
                html += councils[x][1]
                x += 1
    html += """
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
    attributes["planner"] += 3
    attributes["project"] += 3
    attributes["detail"] += 3

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
    if data[1] < 9:
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
        impInfo.append(orgsList[x][0])
    if data[1] < 9:
        for el in colleges:
            impInfo.append(el)
    return impInfo


def lineProcessor(file):
    """ This function takes the data from the CSV file, rips out the necessary info, and processes it """
    # Setup
    skip = 0

    # Processing
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
    """ This function locates the CSV file with 'BRQ' in it, and pulls from that. """
    try:
        path = glob.glob('../**/BRQ*')[0]  # Takes the first file with 'BRQ' in the directory.
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