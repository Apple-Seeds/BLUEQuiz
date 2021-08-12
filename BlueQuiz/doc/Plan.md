# 'Blue Quiz' Committee Calculator

## Explanation
So the President's Cabinet has put together a committee to create this personality quiz that'll provide students with a select number of organizations that they can join to get more involved on campus. There's much that goes into a project such as this, obviously, but this chunk specifically is the program that'll be taking student responses and processing them so that they can get proper results. Ideally, this would be able to be expanded in the future to include clubs, so the approach should be simple enough to:

1. Be expandable to include more organizations and other venues as time passes
2. Give each organization a decently fair chance of being selected via student responses
3. As simple as I can get it. :)


## Approach
So about a week ago at the time of writing this I was bored and work and honestly a little *stressed* so I wrote up a step-by-step list of everything this program needs to do in order to run properly. It's very likely this may change, but as of right now here's the basic recipe for this program to function:

1. Run Consistently
2. Check if there's file in the directory that starts with 'BQR' *(Blue Quiz Response)*
3. Open the BQR file and use a while loop to run through each line
4. For each line,
	- Set the blank dictionaries. One holds the attributes/interests, the other holds the organizations
	- Split the line on its comments and put the information into an array
	- Go through every answer and input the point equivalents into a dictionary of all the attributes and interests
	- Have another dictionary of committees, and have each one pull the points for its respective attributes and interests
	- Return the three committees with the highest point totals
	- Send an email with that information
5. Delete the file when all the lines have been run through

Now, obviously, there's a lot there. I'll break down my thoughts on each of those goals as best as I can, so anyone reading this in the future has a better idea of how I intend to achieve the goal, and also so I can think through what I'm doing.

### Number 1
So I had a few ideas on how to go about this goal. I need this program to check if there's a file relatively often so it'll run around the time it gets put in the directory. The way I plan to do this is, I assume we'll be using a Windows computer, by using the Task Scheduler. Every five or ten minutes I'll have the program run this through the `python.exe`, and then in the code I'll have a function that checks for the filename with the 'BRQ' prefix on it. If it's there, then great! Pull that and start processing. If not, then just exit the program and don't worry about it until the next run. This seems to be the best solution in my mind for getting this program up and running. Considering the file checking is the first thing the program does, it should be a very quick and easy process just to run it through Python every so often. I'd consider setting the interval to be every half hour which is when the files get exported, but I think having it run every five minutes is best because if the timing gets off it'll stick check every often. If somehow the housing for the program gets turned off, I'm not really sure how it'll work with the exports, but if it does and a bunch of files begin to pile up, every five minutes the program will run and pull one of the files. Seems like a decent plan.

### Number 2 
Unfortunately, Qualtrics is a pain and won't let me export after each response, and only lets me export at *minimum* once a day at a specific time. Thankfully, each survey can have up to fifty automations, so I'm just going to put *forty-eight* of them on there that export every thirty minutes. It *also* has the fun issue where responses collected within an hour of an export aren't counted until the next, so unfortunately people are just gonna have to wait an hour or so for their responses to be sent through one of my, again, *forty-eight* automations. I'm not looking forward to putting those all on there. [This](https://www.qualtrics.com/support/survey-platform/data-and-analysis-module/data/download-data/response-export-automations/#SetupExport) is the support page on how to do all that.

But, I digress. The second goal of the program is, once those exports get thrown into some directory, it needs to read it and open it up. I do know how to do the reading files part, that isn't difficult. The only issue I see arising here *(besides the aforementioned problem of not knowing where this program is going to be put)* is getting the specific file name. The Qualtrics exports tack on a date and time at the end of the file, making it difficult for me to know the exact file name. Thankfully, Qualtrics *also* lets me add a prefix to the filename. This is where I can use something from the '[glob](https://docs.python.org/3/library/glob.html)' library, which will let me specifically target if a file with that prefix exists. [This](https://stackoverflow.com/questions/21746750/check-and-wait-until-a-file-exists-to-read-it) stack overflow page and [this](https://www.guru99.com/python-check-if-file-exists.html) python tutorial page might provide some help in this endeavor as well.

### Number 3
This is just opening the file and running a loop through each line. Nothing special. The only thing I'll have to pay attention to is that the first three lines are just unhelpful tags, and the responses I'm looking for aren't until the end of the existing lines, since Qualtrics in it's *ever* helpful nature, has decided to give me such useful information such as the time they took to finish the quiz and, of course, their *latitude and longitude*. Thanks Qualtrics! Very cool! 

Thankfully, that shouldn't be too difficult to do. The lines are separated by newlines and it's a CSV with a specific structure, so it won't be to bad to get over to that part of the line. Just one loop to cut out the first three lines *(I think I can read them in a certain way as well. I'll have to look.)*, followed by a nested loop that for every subsequent line, skips over a bunch of commas, and then begins reading in the points. Something like that. If I get stuck, I think I do something similar in the 'Big Data Processing' program I have, so I can take a look at that.

### Number 4
This should hopefully be pretty self explanatory. Do all the stuff mentioned in a big loop. Nothing fancy.

As for worries, the only 'known unknown' I've got to deal with here is that last one about sending the committees through an email. This will likely not be too difficult once I get the housing for this program figured out, but I do have [this](https://docs.python.org/3/library/email.examples.html) documentation and [this](https://realpython.com/python-send-email/) tutorial page to help me out when that time eventually comes. Past that, there's nothing in this program I really feel I *don't* already know how to do. 

### Number 5
Just deleting a file here. That's just a `os.remove(filename)` command. Whoopee.

And that's it! That's the program, ideally. Again, subject to change as I actually build the thing, but at the moment that seems to cover everything.


## Pseudocode
### Main
	If the namespace is the main function,
		# File Processing
		Set a variable to hold the filepath, which is returned from 'getFile()'
		Set a the file object by opening up the file at the filepath
		Call 'lineProcessor()' and send it the file object
		Close the file
		Delete the file

### GetFile
	getFile() is defined
		""" This function locates the CSV file with 'BRQ' in it, and pulls from that. """
		Attempt to do the following:
			-Set the file path string using the 'glob' library.
		If it returns an IndexError:
			-Exit the program
		Return the file path

### LineProcessor
	lineProcessor() is defined, and given the exported CSV file
		""" This function takes the data from the CSV file, rips out the necessary info, and processes it """
		# Setup
		Set a skip variable that'll be used to ignore the first three lines of the CSV
		Set an empty list that'll hold all the quiz information

		# Processing
		For each line in the file,
			-If we've skipped past the first three lines,
				## Ripping
				--Strip the newlines out
				--Create a list with each element in the file split on the commas
				--For each element index in the range of that list,
					---If the index is at or beyond the email line (index 17 or greater),
						----Add the element at that index to the quiz information list
				## Allocating
				--Set the important info list to be equal to 'allocator()', which has the quiz info list sent to it
				## Reporting
				--Call 'emailUser()' and send it the important info list.
			-Otherwise,
				--Increment the skip variable by one

### Allocator
	allocator() is defined, and given the orderly list of quiz data
		""" This function takes the orderly list of data and sorts all of the points and whatnot. """
		# Setup
		Set the attribute dictionary
		Set the dictionary with all the different organizations
		For each item in the orderly list of data, 
			-Starting with index 1,
				--Convert the element at that index into an integer

		# Council Formatting
		''' Due to the college major question allowing multiple choices, that heavily screws up the indexes. This is to remedy that. '''
		Set a 'difference' variable that takes the length of the orderly list and subtracts it by the amount of questions.
		Set a blank list for the colleges they selected
		If that difference variable is greater than zero,
			Increment with a 'for' loop the value of the difference variable,
				Add the popped return of Index 2 to the college list
		Add the value of Index 1 to the college list, but DO NOT REMOVE IT

		# Point Allocation
		''' If future questions are added, just add the lines here '''
		Index 3: 
			-Add points to 'project', 'detail',
		Index 4: 
			-Add points to 'political'
		Index 5: 
			-If 1 is the answer,
				--Add points to 'hype' and 'party' and 'athletic'
		Index 6: 
			-Add points to 'helpful' and 'academic' and 'detail' and 'project'
		Index 7: 
			-=== to be added ===
		Index 8:
			-If 1 is the answer,
				--Add points to 'hype' and 'athletic' and 'spirit'
			-If 2 is the answer,
				--Add points to 'creative'
			-If 3 is the answer,
				--Add points to 'party' and 'music' and 'extroverted'
			-If 4 is the answer,
				--Add points to 'academic' and 'mentor'
		Index 9:
			-If 1 is the answer,
				--===not sure what to add to here===
			-If 2 is the answer,
				--Add points to 'helpful' and 'spirit' and 'service'
			-If 3 is the answer,
				--Add points to 'mentor' and 'extroverted' and 'leader'
			-If 4 is the answer,
				--Add points to 'political' and 'leader'
			-If 5 is the answer,
				--Add points to 'detail' and 'leader'
			-If 6 is the answer,
				--Add points to 'extroverted'
		Index 10:
			-Add points to 'planner', project', 'detail'

		# Processing
		''' If future organizations are added, add the lines here. Add them to the dictionary as well. '''
		PCab:
			-Add points from 'leader', 'service', 'project', and 'political'
		Fees:
			-Add points from 'detail' and 'time'
		GRC:
			-Add points from 'political' and 'academic'
		BlueCrew:
			-Add points from 'service', 'hype', and 'helpful'
		Activities:
			-Add points from 'party', 'planner', and 'extroverted'
		Series:
			-Add points from 'extroverted', 'creative', and 'music'
		Traditions:
			-Add points from 'helpful', 'planner', 'extroverted', and 'spirit'
		HURD:
			-Add points from 'hype', 'extroverted', and 'athletic'
		Council:
			-If their college score is less than 9,
				--Add points from 'service', 'planner', and 'academic'
				--Add a small bump since they know the college their major is in. 
		SAA:
			-Add points from 'helpful', 'extroverted', and 'spirit'
		Service:
			-Add points from 'service', 'helpful', and 'mentor'
		Statesman:
			-Add points from 'creative' and 'mentor'
		Radio:
			-Add points from 'creative' and 'music'
		B-Light:
			-Add points from 'detail' and 'creative'
		FSL:
			-Add points from 'service', 'hype', and 'parties'

		# Reporting
		Add the email into the important info list
		Sort the organization dictionary by the highest value in descending order
		For the first three keys in that dictionary,
			-Add each one of them to the important info list
		If their college score is less than 9,
			-For each element in the college list,
			 --Add that element's number to the end of the important info list
		Return the important info list

### EmailUser
	emailUser() is defined, and given the list of important info
		""" This function handles the email that sends the top three organizations """
		# Setup
		Set the sending email
		Set the recipient email, which is the first element in the important info list
		Set the sending password
		Set the main message to be a MIMEMultipart Alternative 
		Set a dictionary with each committee and its little blurb in plain text and HTML
		Set a college council dictionary with the link to each committee's signup websites

		# Compile Message
		Set the message subject
		Set the message "From" the sending quiz address
		Set the message "To" the recipient email
		Set a 'text' string with just the introduction
		Set the 'html' string with just the introduction
		For each element in the plain dictionary,
			-If the current element's key is equal to one of the three committees in the important info list,
				--Add its plain text blurb to the 'text' string
				--Add its HTML blurb to the 'html' string
				--If the current element is the college council,
					---For every element in the important info list beyond Index 3,
						----Add its college council link to the end of the 'text' string
						----Add its college council link to the end of the 'html' string
		Turn the 'text' string into a MIMEText object
		Turn the 'html' string into a MIMEText object
		Attach the plain text object to the main message
		Attach the html object to the main message

		# Sendoff
		Set the context to be the default context
		With the SMTP library, given the server address, the port, and the context,
			-Login to the server
			-Send the email to the sender and give it the sending email, the recipient email, and the created message

## Python Code
### Main
	if __name__ == '__main__':
		# File Processing
		filepath = getFile()
		fileObj = open(filepath)
		lineProcessor(fileObj)
		fileObj.close()
		os.remove(filepath)

### GetFile
	def getFile():
		""" This function locates the CSV file with 'BRQ' in it, and pulls from that. """
		try:
			filepath = glob.glob('../**/BRQ*')[0]  # Takes the first file with 'BRQ' in the directory.
		except IndexError:
			sys.exit(1)
		return filepath

### LineProcessor
	def lineProcessor(file):
		""" This function takes the data from the CSV file, rips out the necessary info, and processes it """
		# Setup
		skip = 0
		quizResponses = []

		# Processing
		for line in file:
			if skip > 3:
				## Ripping
				line = line.strip('\n')
				elementList = line.split(',')
				for el in range(elementList):
					if el >= 17:
						quizResponses.append(elementList[el])
				## Allocating
				importantInfo = allocator(quizResponses)
				## Reporting
				emailUser(importantInfo)
			else:
				skip += 1

### Allocator
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
		for x in range(data):
			if x > 0:
				data[x] = int(data[x])

		# Council Formatting
		''' The college major question (Q1) allows multiple choices, and that heavily screws up the indexes. This is to remedy that. '''
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
		elif data[9] == 2:
			attributes["helpful"] += 3
			attributes["spirit"] += 3
			attributes["service"] += 3
		elif data[9] == 3:
			--Add points to 'mentor' and 'extroverted' and 'leader'
			attributes["mentor"] += 3
			attributes["extroverted"] += 3
			attributes["leader"] += 3
		elif data[9] == 4:
			--Add points to 'political' and 'leader'
			attributes["political"] += 3
			attributes["leader"] += 3
		elif data[9] == 5:
			attributes["detail"] += 3
			attributes["leader"] += 3
		elif data[9] == 6
			attributes["extroverted"] += 3
		# Q10: --------------------------------
		attributes["planner"] += 3
		attributes["project"] += 3
		attributes["detail"] += 3

		# Processing
		''' If future organizations are added, add the lines here. Add them to the dictionary as well. '''
		orgs["pcab"] = (attributes["leader"] + attributes["service"] + attributes["project"] + attributes["political"])
		orgs["fees"] = (attributes["detail"] + attributes["time"])
		orgs["grc"] = (attributes[political] + attributes["academic"])
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
		orgs["fsl"] = (attributes["service"] + attributes["hype"] + attributes["parties"])

		# Reporting
		impInfo = [data[0]]
		orgs = sorted(orgs.items(), key=lambda x:x[1], reverse=true)
		orgList = orgs.keys()
		for x in range(3):
			impInfo.append(orgList[x])
		if data[1] < 9:
			for el in colleges:
				impInfo.append(el)
		return impInfo

### EmailUser
	def emailUser(info):
		""" This function handles the email that sends the top three organizations """
		# Setup
		sender = ""   # Undetermined as of yet
		receiver = info[1]
		password = "" # Undetermined as of yet
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

	        "grc": """
			Government Relations Council (GRC)
			Purpose: Advocate for student interest to state & local officials & raise awareness of civic issues on campus. Plans Gripe Night, Voter Registration, & Aggie Ice Cream Day on the Hill
			Application Link:
			""",
			"""
			<p><b>Government Relations Council (GRC)</b><br>
				<b>Purpose:</b> Advocate for student interest to state & local officials & raise awareness of civic issues on campus. Plans Gripe Night, Voter Registration, & Aggie Ice Cream Day on the Hill<br>
				<b>Application Link:</b> 
			"""],

	        "blucru": """
			Blue Crew
			Purpose: Assist in the marketing of events & helps set up/take down for events
			Application Link:
			""",
			"""
			<p><b>Blue Crew</b><br>
				<b>Purpose:</b> Assist in the marketing of events & helps set up/take down for events<br>
				<b>Application Link:</b> 
			"""],

	        "activity": """
			Activities Committee
			Purpose: Plans & executes The Howl, Mardi Gras, & End of Year Bash
			Application Link:
			""",
			"""
			<p><b>Activities Committee</b><br>
				<b>Purpose:</b> Plans & executes The Howl, Mardi Gras, & End of Year Bash<br>
				<b>Application Link:</b> 
			"""],

	        "series": """
	        Series Committee
			Purpose: Plans & executes regular/recurring events that are generally more artistic like PoBev & Moonlight & Music
			Application Link:
			""",
			"""
			<p><b>Series Committee</b><br>
				<b>Purpose:</b> Plans & executes regular/recurring events that are generally more artistic like PoBev & Moonlight & Music<br>
				<b>Application Link:</b> 
			"""],

	        "trad": """
	        Traditions Committee
			Purpose: Plans & executes Homecoming week, Mr.USU, Sweater Swap, & High Stakes Bingo
			Application Link:
			""",
			"""
			<p><b>Traditions Committee</b><br>
				<b>Purpose:</b> Plans & executes Homecoming week, Mr.USU, Sweater Swap, & High Stakes Bingo<br>
				<b>Application Link:</b> 
			"""],

	        "hurd": """
	        HURD Committee
			Purpose: Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports
			Application Link:
			""",
			"""
			<p><b>HURD Committee</b><br>
				<b>Purpose:</b> Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports<br>
				<b>Application Link:</b> 
			"""],

	        "council": """
	        College Councils
			Purpose: Advocate for student interests to their college’s administration (deans & department heads), plan & execute service projects & college specific events. Each college has its own week filled with events.
			""",
			"""
			<p><b>College Councils</b><br>
				<b>Purpose:</b> Advocate for student interests to their college’s administration (deans & department heads), plan & execute service projects & college specific events. Each college has its own week filled with events.<br>
			"""],

	        "saa": """
	        Student Alumni Association
			Purpose: Create lifelong aggies. Focuses on donors and guest speakers. Engage alumni. Plan & execute initiatives to connect students with alumni. Also, True Aggie Night, Miss USU, and A-Day.
			Application Link:
			""",
			"""
			<p><b>Student Alumni Association</b><br>
				<b>Purpose:</b> Create lifelong aggies. Focuses on donors and guest speakers. Engage alumni. Plan & execute initiatives to connect students with alumni. Also, True Aggie Night, Miss USU, and A-Day.<br>
				<b>Application Link:</b> 
			"""],

	        "serve": """
	        Service Center Programs
			Purpose: Some of the programs run out of the center are SNAC, gleaning, best buddies, Special Olympics, Athletics United, etc.
			Application Link:
			""",
			"""
			<p><b>Service Center</b><br>
				<b>Purpose:</b> Some of the programs run out of the center are SNAC, gleaning, best buddies, Special Olympics, Athletics United, etc.<br>
				<b>Application Link:</b> 
			"""],

	        "states": """
	        Statesman
			Purpose: Student news. Gives students an opportunity to write
			Application Link:
			""",
			"""
			<p><b>Statesman</b><br>
				<b>Purpose:</b> Student news. Gives students an opportunity to write<br>
				<b>Application Link:</b> 
			"""],

	        "radio": """
	        Aggie Radio
			Purpose: Provides students with opportunities to DJ, create radio talk shows, podcasts, & plan/coordinate events (mainly concerts)
			Application Link:
			""",
			"""
			<p><b>Aggie Radio</b><br>
				<b>Purpose:</b> Spread awareness & excitement around USU athletics, plan events & initiatives that increases attendance at games, promotes HURD Premium, & focuses on supporting women’s sports<br>
				<b>Application Link:</b> 
			"""],

	        "blight": """
	        Blue Light
			Purpose: Meet content creation needs for clients, primarily USUSA
			Application Link:
			""",
			"""
			<p><b>Blue Light</b><br>
				<b>Purpose:</b> Meet content creation needs for clients, primarily USUSA<br>
				<b>Application Link:</b> 
			"""],

	        "fsl": """
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
			1: ["","<b>Arts Application: </b> <a href=""></a><br>"],
			2: ["","<b>Agriculture Application: </b><a href=""></a><br>"],
			3: ["","<b>Engineering Application: </b><a href=""></a><br>"],
			4: ["","<b>Humanities & Social Sciences Application: </b><a href=""></a><br>"],
			5: ["","<b>Science Application: </b><a href=""></a><br>"],
			6: ["","<b>Education Application: </b><a href=""></a><br>"],
			7: ["","<b>Huntsman Application: </b><a href=""></a><br>"],
			8: ["","<b>Natural Resources Application: </b><a href=""></a><br>"],
		}

		# Compile Message
		message["Subject"] = "Blue Quiz Involvement Survey Results"
		message["From"] = sender
		message["To"] = receiver
		text = """\
		“The only way you can taste life is with involvement.” Sadhguru

		Thank you for filling out our survey. You are a great match for the following three committees. Our goal here at USU is to cultivate an environment of development and growth and we need your help. Every single student can make a difference in our community and help others feel welcomed and heard, and it starts with involvement. Check out the options listed below or browse for other opportunities listed on our website. We can’t wait to hear your perspectives and ideas and together change our school for the better. 
		"""
		html = """\
		<html>
			<body>
				<img src="https://math.usu.edu/ldp/galleries/.private_ldp/a68540/production/master/c3bc1389-5787-4101-92d0-91c4fde8df13.jpg" alt="Drone view of Old Main">
				<h3>“The only way you can taste life is with involvement.” <em>Sadhguru</em></h3><br>
				<p>Thank you for filling out our survey. You are a great match for the following three committees. Our goal here at USU is to cultivate an environment of development and growth and we need your help. Every single student can make a difference in our community and help others feel welcomed and heard, and it starts with involvement. Check out the options listed below or browse for other opportunities listed on our website. We can’t wait to hear your perspectives and ideas and together change our school for the better.</p>
		"""
		for el in orgs:
			if el in info:
				text += el[0]
				html += el[1]
				if el == "council":
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
		with smtplib.SMTP_SSL("", 465, context=context) as server:
			server.login(sender, password)
			server.sendmail(sender, receiver, message.as_string())


## Implementation 


## Testing