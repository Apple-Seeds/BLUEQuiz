import random


def generateThree(subcats, attribs, names, points):
    """ This function takes the point totals and determines the top three clubs. """
    

    # Assign Points
    

    # Sort
    topCats = sorted(subcats.items(), key=lambda k: k[1], reverse=True)
    topClubs = sorted(points.items(), key=lambda k: k[1], reverse=True)

    # Results
    three = []
    for x in range(3):
        # Get subcat
        if x < 1:
            picks = names[topCats[0]]  # Does the top subcat twice
        else:
            picks = names[topCats.pop(0)]
        # Get club
        for y in topClubs:
            if y in picks:
                three.append(y)
                topClubs.remove(y)
                break
    return three


def allocator(data):
    """ This function takes the orderly list of data and sorts all of the points and whatnot. """
    # Club Setup
    clubNames = {
        'general': ['pcab', 'fees', 'council', 'saa', 'nscsc', 'ento', 'aspire'],
        'medical': ['therapy', 'amsa', 'cadvaer', 'hosa', 'neuro', 'dental', 'pmed', 'nami', 'physass', 'span', 'diet', 'milpsych', 'mcat', 'mftsa'],
        'business': ['algo', 'sport', 'nsls', 'bit'],

        'athletic': ['hurd', 'canyon', 'archery', 'yoga', 'trail', 'volley'],
        'arts': ['radio', 'blight', 'series', 'film',  'bigband', 'cswing', 'star', 'thea'],
        'lifestyle': ['blucru', 'activity', 'trad', 'fsl', 'game', 'paint', 'tennis', 'spike', 'pickle', 'skate', 'aikido', 'snow', 'ram'],

        'dei': ['girl', 'ostem', 'transfer', 'story', ' women'],
        'international': ['globcom', 'natstud', 'scandi', 'tagalog', 'russia'],
        'studies': ['anthro', 'colstud', 'mun', 'prssa', 'phil', 'nsslha'],

        'spiritual': ['lds', 'fellow', 'newman', 'inter', 'ssa', 'christ'],
        'kindness': ['serve', 'rotaract', 'cares', 'bestbud', 'gdays', 'smile'],
        'political': ['grc', 'party', 'repo']
    }
    clubPoints = {}
    for el in clubNames:
        for name in clubNames[el]:
            clubPoints[name] = random.randrange(1, 4)

    # Data Setup
    data.pop(0)  # Unnecessary email data
    results = []
    subcats = {
    	#-Academic-
        'general': 0,
        'medical': 0,
        'business': 0,
        #-Recreation-
        'athletic': 0,
        'arts': 0,
        'lifestyle': 0,
        #-DEI-
        'dei': 0,
        'international': 0,
        'studies': 0,
        #-Service-
        'spiritual': 0,
        'kindness': 0,
        'political': 0
    }
    attribs = {

    }

    # College Collection
    """ This just a short list of numbers corresponding to whatever colleges they're a part of. """
    colleges = []
    for x in range(11):
        if data.pop(0) > 0:
            colleges.append(x + 1)

    # Point Allocation ----------------------------------
    specialPackage = [] # The 'Special Package' is for data that is relevant only to a specific club.
    specialPackage.append(colleges)

    # ----------Intro Questions-----------
    # Q2: --------------------------------
    because = []
    for x in range(5):
        if data.pop(0) > 0:
            because.append(x + 1)
    if 1 in because:
        subcats['athletic'] += 2
        subcats['arts'] += 2
        subcats['lifestyle'] += 3
        subcats['dei'] += 2
        subcats['international'] += 2
        subcats['studies'] += 2
        attribs['extrovert'] += 3
        attribs['aggie'] += 2
        attribs['team'] += 1
    elif 2 in because:
        subcats['dei'] += 2
        subcats['international'] += 2
        subcats['studies'] += 2
        subcats['spiritual'] += 2
        subcats['kindness'] += 3
        subcats['political'] += 2
        attribs['caring'] += 2
        attribs['mentor'] += 2
        attribs['leader'] += 1
    elif 3 in because:
    	subcats['general'] += 2
        subcats['medical'] += 2
        subcats['business'] += 3
        attribs['leader'] += 2
        attribs['team'] += 2
        attribs['extrovert'] += 1
    elif 4 in because:
        subcats['general'] += 2
        subcats['medical'] += 2
        subcats['business'] += 2
        subcats['dei'] += 3
        subcats['international'] += 3
        subcats['studies'] += 2
        attribs['devout'] += 2
        attribs['caring'] += 3
        attribs['reflect'] += 2
    elif 5 in because:
    	subcats['athletic'] += 2
        subcats['arts'] += 2
        subcats['lifestyle'] += 3
        subcats['spiritual'] += 2
        subcats['kindness'] += 2
        subcats['political'] += 2
        attribs['lax'] += 2
        attribs['extrovert'] += 1
        attribs['outdoors'] += 2
    # Q3: --------------------------------
    subcats['general'] += data[0]
    subcats['medical'] += data[0]
    subcats['business'] += data[0]
    attribs['detailed'] += data[0] + 1
    attribs['smart'] += data[0]
    attribs['lax'] -= data[0]
    # Q4: --------------------------------
    subcats['athletic'] += data[1] + 1
    subcats['arts'] += data[1] - 1
    subcats['lifestyle'] += data[1]
    attribs['aggie'] += data[1] + 1
    attribs['extrovert'] += data[1]
    attribs['team'] += data[1] - 1
    # Q5: --------------------------------
    subcats['spiritual'] += data[2]
    subcats['kindness'] += data[2] + 1
    subcats['political'] += data[2]
    attribs['caring'] += data[2]
    attribs['reflect'] += data[2]
    attribs['leader'] += data[2]
    # ---------Academic Questions---------
    # Q6: -------------------------------- (Kind of a hard question to come up with attribs for. :/)
    subcats['medical'] -= data[3]
    attribs['dirty'] += data[3] - 1
    attribs['caring'] -= 1
    attribs['detailed'] += 1
    # Q7: --------------------------------
    subcats['general'] += data[4]
    subcats['business'] += data[4]
    attribs['team'] += data[4] + 1
    attribs['detailed'] += data[4]
    attribs['leader'] += data[4]
    # Q8: --------------------------------
    subcats['business'] += data[5] + 1
    attribs['work'] += data[5]
    attribs['leader'] += data[5]
    attribs['team'] += data[5]
    # Q9: --------------------------------
    subcats['medical'] += data[6]
    attribs['detailed'] += data[6]
    attribs['outdoors'] += data[6]
    attribs['reflect'] += data[6] - 1
    # Q10: -------------------------------
    subcats['general'] += data[7]
    attribs['leader'] += data[7]
    attribs['work'] += data[7]
    attribs['detailed'] += data[7]
    # ---------General Questions----------
    # Q11: -------------------------------
    subcats['general'] += data[8]
    clubPoints['pcab'] += data[8]
    clubPoints['fees'] += data[8]
    clubPoints['nscsc'] += data[8]
    attribs['detailed'] += data[8]
    attribs['work'] += data[8]
    # Q12: -------------------------------
    subcats['general'] += data[9]
    clubPoints['pcab'] += data[9]
    clubPoints['fees'] += data[9]
    clubPoints['council'] += data[9]
    attribs['aggie'] += data[9]
    attribs['caring'] += data[9]
    # Q13: -------------------------------
    subcats['general'] += data[10]
    clubPoints['saa'] += data[10] + 1
    attribs['aggie'] += data[10] + 1
    attribs['extrovert'] += data[10]
    # Q14: -------------------------------
    if data[11] == 1:
        subcats['general'] += 2
        clubPoints['ento'] += 5
        attribs['caring'] += 2
        attribs['reflect'] += 1
    elif data[11] == 2:
        subcats['general'] += 1
        clubPoints['ento'] += 3
        attribs['work'] += 2
        attribs['dirty'] += 1
    elif data[11] == 3:
        subcats['general'] += 1
        clubPoints['ento'] += 1
        attribs['lax'] += 2
        attribs['dirty'] += 2
    elif data[11] == 4:
        subcats['general'] -= 1
        clubPoints['ento'] -= 10
        attribs['detailed'] += 1
        attribs['dirty'] -= 2
    # Q15: -------------------------------
    subcats['general'] += data[12]
    clubPoints['aspire'] += data[12] + 2
    attribs['smart'] += data[12] + 2
    attribs['excited'] += data[12]
    # ---------Medical Questions----------
    # Q16: -------------------------------
    subcats['medical'] += data[13]
    clubPoints['cadvaer'] += data[13]
    clubPoints['neuro'] += data[13]
    clubPoints['dental'] += data[13]
    clubPoints['mcat'] += data[13]
    clubPoints['pmed'] += data[13]
    attribs['detailed'] += data[13]
    attribs['dirty'] += data[13]
    attribs['work'] += data[13]
    # Q17: -------------------------------
    subcats['medical'] += data[14]
    clubPoints['milpsych'] += data[14]
    clubPoints['mftsa'] += data[14]
    clubPoints['nami'] += data[14]
    clubPoints['therapy'] 
    # Q18: -------------------------------
    # ---------Business Questions---------
    # Q19: -------------------------------
    # Q20: -------------------------------
    # --------Recreation Questions--------
    # Q21: -------------------------------
    # Q22: -------------------------------
    # Q23: -------------------------------
    # ---------Athletic Questions---------
    # Q24: -------------------------------
    # Q25: -------------------------------
    # Q26: -------------------------------
    # -----------Arts Questions-----------
    # Q27: -------------------------------
    # Q28: -------------------------------
    # Q28: -------------------------------
    # Q29: -------------------------------
    # ---------Lifestyle Questions--------
    # Q30: -------------------------------
    # Q31: -------------------------------
    # Q32: -------------------------------
    # Q33: -------------------------------
    # Q34: -------------------------------
    # --------Humanities Questions--------
    # Q35: -------------------------------
    # Q36: -------------------------------
    # Q37: -------------------------------
    # Q38: -------------------------------
    # ---------Diversity Questions--------
    # Q39: -------------------------------
    # Q40: -------------------------------
    # Q41: -------------------------------
    # -------International Questions------
    # Q42: -------------------------------
    # Q43: -------------------------------
    # Q44: -------------------------------
    # Q45: -------------------------------
    # ----------Studies Questions---------
    # Q46: -------------------------------
    # Q47: -------------------------------
    # Q48: -------------------------------
    # Q49: -------------------------------
    # ----------Service Questions---------
    # Q50: -------------------------------
    # Q51: -------------------------------
    # Q52: -------------------------------
    # Q53: -------------------------------
    # ---------Spiritual Questions--------
    # Q54: -------------------------------
    # Q55: -------------------------------
    # Q56: -------------------------------
    # ---------Kindness Questions---------
    # Q57: -------------------------------
    # Q58: -------------------------------
    # ---------Political Questions--------
    # Q59: -------------------------------
    # Q60: -------------------------------
    # Q61: -------------------------------
    # END ----------------------------------------------
    # Results
    return colleges + generateThree(subcats, attribs, clubNames, clubPoints)
