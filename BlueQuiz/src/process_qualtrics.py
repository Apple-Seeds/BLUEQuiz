import random


def generateFive(subcats, attribs, specvals):
    """ This function takes the point totals and determines the top five clubs. """
    # Setup
    clubNames = {
        'general': ['pcab', 'fees', 'saa', 'council', 'nscsc', 'aspire'],
        'medical': ['therapy', 'amsa', 'cadvaer', 'hosa', 'neuro', 'dental', 'pmed', 'physass', 'spmed', 'diet',
                    'milpsych'],
        'humanities': ['anthro', 'globcom', 'colstud', 'natstud', 'mun', 'prssa'],
        'business': ['finance', 'sport', 'nsls'],
        'athletic': ['hurd', 'canyon', 'archery', 'yoga', 'trail'],
        'arts': ['radio', 'blight', 'series', 'film', 'irish', 'bigband', 'cswing'],
        'lifestyle': ['blucru', 'activity', 'trad', 'fsl', 'game', 'paint', 'tennis', 'spike', 'ram'],
        'dei': ['girl', 'nami', 'ostem', 'scandi', 'tagalog', 'transfer'],
        'spiritual': ['lds', 'colchrist', 'fellow', 'goldcity', 'varsity', 'navi', 'newman', 'ratio', 'inter', 'ssa'],
        'kindness': ['serve', 'rotaract', 'cares', 'bestbud', 'gdays'],
        'political': ['grc', 'dems', 'ydsa', 'surf']
    }
    clubPoints = {}
    for el in clubNames:
        for name in clubNames[el]:
            clubPoints[name] = random.randrange(1, 4)

    # # Assign Points
    # # -- General --
    # clubPoints['pcab'] = (attribs['leader'] + attribs['project'] + attribs['serve'])
    # if specvals[10] == 2:
    #     clubPoints['pcab'] += 2
    # clubPoints['fees'] = (attribs['detail'] + attribs['time'] + attribs['political'])
    # if specvals[10] == 1:
    #     clubPoints['fees'] += 2
    # clubPoints['saa'] = (attribs['extroverted'] + attribs['mentor'] + attribs['aggie'])
    # if specvals[10] == 4:
    #     clubPoints['saa'] += 2
    # clubPoints['council'] = (attribs['serve'] + attribs['detail'] + attribs['smart'] + len(specvals[0]))
    # if specvals[10] == 3:
    #     clubPoints['council'] += 2
    # clubPoints['nscsc'] = (attribs['leader'] + attribs['mentor'] + attribs['charisma'])
    # clubPoints['aspire'] = (attribs['project'] + attribs['detail'] + attribs['outdoors'])
    # if 3 in specvals[0]:
    #     clubPoints['aspire'] += 3
    # else:
    #     clubPoints['aspire'] -= 2

    # # -- Medical --
    # clubPoints['therapy'] = (attribs['serve'] + attribs['hardwork'] + attribs['active'])
    # if specvals[14] == 1 or specvals[14] == 2:
    #     clubPoints['therapy'] += 3
    # clubPoints['amsa'] = (attribs['leader'] + attribs['team'] + attribs['mentor'])
    # clubPoints['cadaver'] = (attribs['detail'] + attribs['smart'] + specvals[12])
    # if specvals[14] == 8:
    #     clubPoints['cadaver'] += 3
    # clubPoints['hosa'] = (attribs['leader'] + attribs['team'] + subcats['medical'])
    # clubPoints['neuro'] = (attribs['detail'] + attribs['smart'])
    # if specvals[14] == 4:
    #     clubPoints['neuro'] += 3
    # clubPoints['dental'] = (attribs['detail'] + attribs['extroverted'] + specvals[11])
    # if specvals[14] == 5:
    #     clubPoints['dentist'] += 3
    # clubPoints['pmed'] = (attribs[''] + attribs[''] + subcats['medical'])
    # clubPoints['physass'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['spmed'] = (attribs['cultured'] + attribs[''] + subcats['medical'])
    # clubPoints['diet'] = (attribs[''] + attribs[''] + attribs[''])
    # if specvals[14] == 10:
    #     clubPoints['diet'] += 3
    # clubPoints['milpsych'] = (attribs['serve'] + attribs[''] + attribs[''] + specvals[13])
    # if specvals[14] != 12:
    #     clubPoints['amsa'] += 3
    #     clubPoints['hosa'] += 3
    #     clubPoints['pmed'] += 3

    # # -- Humanities --
    # clubPoints['anthro'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['glocom'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['colstud'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['natstud'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['mun'] = (attribs[''] + attribs[''] + attribs[''])
    # if specvals[15] == 2:
    #     clubPoints['mun'] + 2
    # clubPoints['prssa'] = (attribs[''] + attribs[''] + attribs[''])

    # # -- Business --
    # clubPoints['finance'] = (attribs[''] + attribs[''] + attribs[''] + specvals[16])
    # clubPoints['sport'] = (attribs['active'] + attribs[''] + attribs[''])
    # clubPoints['nsls'] = (attribs['leader'] + attribs[''] + attribs[''])

    # # -- Athletic --
    # clubPoints['hurd'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['canyon'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['archery'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['yoga'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['trail'] = (attribs[''] + attribs[''] + attribs[''])

    # # -- Arts --
    # clubPoints['radio'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['blight'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['series'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['film'] = (attribs[''] + attribs[''] + attribs[''] + specvals[1])
    # clubPoints['irish'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['bigband'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['cswing'] = (attribs[''] + attribs[''] + attribs[''])
    # if specvals[15] == 4:
    #     clubPoints['irish'] += 2
    #     clubPoints['bigband'] += 2
    #     clubPoints['cswing'] += 2

    # # -- Lifestyle --
    # clubPoints['blucru'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['activity'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['trad'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['fsl'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['game'] = (attribs[''] + attribs[''] + attribs[''])
    # if specvals[2] == 1:
    #     clubPoints['game'] += 4
    # clubPoints['paint'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['tennis'] = (attribs[''] + attribs[''] + attribs[''])
    # if specvals[2] == 2:
    #     clubPoints['tennis'] += 4
    # clubPoints['spike'] = (attribs[''] + attribs[''] + attribs[''])
    # if specvals[2] == 3
    #     clubPoints['spike'] += 4
    # clubPoints['ram'] = (attribs[''] + attribs[''] + attribs[''])
    # if 6 in specvals[0]:
    #     clubPoints['ram'] += 2

    # # -- DEI --
    # clubPoints['girl'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['nami'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['ostem'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['scandi'] = (attribs[''] + attribs[''] + attribs[''] + specvals[5])
    # clubPoints['tagalog'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['transfer'] = (attribs[''] + attribs[''] + attribs[''] + specvals[4])

    # # -- Spiritual --
    # clubPoints['lds'] = (attribs[''] + attribs[''] + attribs[''] + specvals[6])
    # clubPoints['colchrist'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['fellow'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['goldcity'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['varsity'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['navi'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['newman'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['ratio'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['inter'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['ssa'] = (attribs[''] + attribs[''] + attribs[''])

    # # -- Kindness --
    # clubPoints['serve'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['rotaract'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['cares'] = (attribs[''] + attribs[''] + attribs[''])
    # clubPoints['bestbud'] = (attribs[''] + attribs[''] + attribs[''] + specvals[7])
    # clubPoints['gdays'] = (attribs[''] + attribs[''] + attribs[''])

    # # -- Political --
    # clubPoints['grc'] = (attribs['political'] + attribs['serve'] + specvals[9])
    # clubPoints['dems'] = (attribs['political'] + attribs['team']  + specvals[8])
    # clubPoints['ydsa'] = (attribs['political'] + attribs['discuss'] + specvals[8])
    # clubPoints['surf'] = (attribs['political'] + attribs['mentor'] + specvals[9])

    # # -- Random --
    # for key in clubPoints:
    #     for val in key:
    #         val += random.randrange(1, 4)

    # Sort
    topCats = sorted(subcats.items(), key=lambda k: k[1], reverse=True)
    topClubs = sorted(clubPoints.items(), key=lambda k: k[1], reverse=True)

    # Results
    five = []
    for x in range(5):
        # Get subcat
        if x < 1:
            picks = clubNames[topCats[0]]  # Does the top subcat twice
        else:
            picks = clubNames[topCats.pop(0)]
        # Get club
        for y in topClubs:
            if y in picks:
                five.append(y)
                topClubs.remove(y)
                break
    return five


def allocator(data):
    """ This function takes the orderly list of data and sorts all of the points and whatnot. """
    # Setup
    data.pop(0)  # Unnecessary email data
    results = []
    subcats = {
    	#-Academic-
        'general': 0,
        'medical': 0,
        'humanities': 0,
        'business': 0,
        #-Recreation-
        'athletic': 0,
        'arts': 0,
        'lifestyle': 0,
        #-DEI-
        'dei': 0,
        #-Service-
        'spiritual': 0,
        'kindness': 0,
        'political': 0
    }
    attribs = {
        "leader": 0,
        "charisma": 0,
        "hardwork": 0,
        "team": 0,
        "project": 0,
        "detail": 0,
        "time": 0,
        "aggie": 0,
        "hype": 0,
        "extroverted": 0,
        "mentor": 0,
        "music": 0,
        "discuss": 0,
        "cozy": 0,
        "smart": 0,
        "active": 0,
        "creative": 0,
        "faith": 0,
        "serve": 0,
        "political": 0,
        "outdoors": 0,
        "dance": 0,
        "cultured": 0,
    }

    # College Collection
    colleges = []
    for x in range(10):
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
        subcats['general'] += 2
        subcats['lifestyle'] += 3
        subcats['dei'] += 2
        subcats['kindness'] += 2
    elif 2 in because:
        subcats['medical'] += 2
        subcats['kindness'] += 3
        subcats['political'] += 2
        subcats['dei'] += 2
    elif 3 in because:
    	subcats['general'] += 2
        subcats['lifestyle'] += 2
        subcats['business'] += 3
        subcats['political'] += 2
    elif 4 in because:
        subcats['humanities'] += 2
        subcats['arts'] += 2
        subcats['dei'] += 2
        subcats['spiritual'] += 2
    elif 5 in because:
    	subcats['general'] += 1
        subcats['lifestyle'] += 2
        subcats['athletic'] += 2
        subcats['arts'] += 2
    # Q3: --------------------------------
    subcats['general'] += data[0]
    subcats['medical'] += data[0]
    subcats['humanities'] += data[0]
    subcats['business'] += data[0]
    # Q4: --------------------------------
    subcats['athletic'] += data[1] + 1
    subcats['lifestyle'] += data[1]
    # Q5: --------------------------------
    subcats['dei'] += data[2]
    subcats['spiritual'] += data[2]
    subcats['kindness'] += data[2]
    subcats['political'] += data[2]
    subcats['arts'] += data[2] - 1

    # -----------REC Questions-----------
    # Q6: --------------------------------
    if data[3] == 1:
        subcats['athletic'] += 4
    elif data[3] == 2:
        subcats['lifestyle'] += 3
    elif data[3] == 3:
        subcats['arts'] += 3
        specialPackage.append(3)
    elif data[3] == 4:
        subcats['arts'] += 4
    elif data[3] == 5:
        subcats['lifestyle'] += 3
    # Q7: --------------------------------
    subcats['athletic'] += data[4]
    # Q8: --------------------------------
    if data[5] == 1:
        subcats['art'] += 3
    elif data[5] == 2:
        subcats['lifestyle'] += 3
    elif data[5] == 3:
        subcats['lifestyle'] += 2
        subcats['arts'] += 2
    elif data[5] == 4:
        subcats['athletic'] += 2
    # ---------Athletic Questions---------
    # Q9: --------------------------------
    subcats['athletic'] += data[6]
    # Q10: --------------------------------
    subcats['athletic'] += data[7]
    # -----------Artsy Questions-----------
    # Q11: --------------------------------
    subcats['arts'] += data[8]
    # Q12: --------------------------------
    subcats['arts'] += data[9]
    # Q13: --------------------------------
    subcats['arts'] += data[10]
    # ---------Lifestyle Questions---------
    # Q14: --------------------------------
    subcats['lifestyle'] += data[11]
    # Q15: --------------------------------
    subcats['lifestyle'] += 2
    if data[12] in [1, 2, 3]:
        specialPackage.append(data[12])
    elif data[12] == 4:

    elif data[12] == 5:
        subcats['lifestyle'] -= 3
    # Q16: --------------------------------
    subcats['lifestyle'] += data[13]

    # Q17: --------------------------------
    subcats['lifestyle'] += data[14] - 1
    subcats['athletic'] += data[14] - 1

    specialPackage.append(data[14])
    # ------------DEI Questions------------
    # Q18: --------------------------------
    subcats['dei'] += data[15]

    # Q19: --------------------------------
    subcats['dei'] += 1
    specialPackage.append(data[16])

    # Q20: --------------------------------
    subcats['dei'] += 1
    specialPackage.append(data[17])
    # Q21: --------------------------------
    subcats['dei'] += data[18]

    # ----------Service Questions----------
    # Q22: --------------------------------
    subcats['spiritual'] += data[19]

    # Q23: --------------------------------
    subcats['political'] += data[20]

    # Q24: --------------------------------
    subcats['kindness'] += 3
    if data[21] == 1:

    elif data[21] == 2:

    elif data[21] == 3:

    elif data[21] == 4:

    # ----------Spirit Questions----------
    # Q25: --------------------------------
    specialPackage.append(data[22])
    subcats['spiritual'] += data[22]

    # Q26: --------------------------------
    subcats['spiritual'] += data[23]

    # Q27: --------------------------------
    subcats['spiritual'] += data[24]

    # Q28: --------------------------------
    subcats['spiritual'] += data[25]
    specialPackage.append(data[25])
    # -----------Kind Questions-----------     (needs some work)
    # Q29: --------------------------------
    specialPackage.append(data[26])
    subcats['kindness'] += data[26]

    # Q30: --------------------------------
    subcats['kindness'] += data[28]

    # ----------Politic Questions----------    (needs some work)
    # Q31: --------------------------------
    specialPackage.append(data[29])
    subcats['political'] += data[29]
    # Q32: --------------------------------
    specialPackage.append(data[30])
    subcats['political'] += data[30]
    # ---------Academic Questions----------
    # Q33: --------------------------------
    subcats['medical'] -= data[31]
    # Q34: --------------------------------
    subcats['general'] += data[32]
    subcats['business'] += data[32]
    # Q35: --------------------------------
    subcats['general'] -= data[33]
    subcats['medical'] -= data[33]

    # Q36: --------------------------------
    subcats['humanities'] += data[34] + 1
    subcats['business'] += data[34]
    # Q37: --------------------------------
    subcats['general'] += data[35]
    subcats['humanities'] += data[35]
    subcats['political'] += data[35] -1
    # Q38: --------------------------------
    subcats['business'] += data[36] + 1
    # ---------General Questions----------
    # Q39: --------------------------------
    if data[37] != 5:
        subcats['general'] += 2
        specialPackage.append(data[37])
    else:
        subcats['general'] -= 2
    # Q40: --------------------------------
    subcats['general'] += data[38]
    # Q41: --------------------------------
    subcats['general'] += data[39]
    # Q42: --------------------------------
    subcats['general'] += data[40]
    subcats['athletic'] += data[40] - 1
    # ---------Medical Questions----------
    # Q43: --------------------------------
    specialPackage.append(data[41])
    subcats['medical'] += data[41]
    # Q44: --------------------------------
    specialPackage.append(data[42])
    subcats['medical'] += data[42]
    # Q45: --------------------------------
    specialPackage.append(data[43])
    subcats['medical'] += data[43]
    # Q46: --------------------------------
    subcats['medical'] += 3
    if data[44] != 12 or data[44] != 0:
        specialPackage.append(data[44])      
    else:
        subcats['medical'] -= 3
    # ---------Humanities Questions----------
    # Q47: --------------------------------
    subcats['humanities'] += data[45]
    # Q48: --------------------------------
    if data[46] != 5 or data[46] != 0:
        specialPackage.append(data[46])
        subcats['humanities'] += 2
        if data[46] == 4:

        elif data[46] == 3:

        elif data[46] == 2:

    else:
        subcats['humanities'] -= 2
    # Q49: --------------------------------   (needs full code reworking, see quiz question)
    subcats['humanities'] -= data[47]

    # ---------Business Questions----------
    # Q50: --------------------------------
    subcats['business'] += data[48]

    # Q51: --------------------------------
    specialPackage.append(data[49])
    subcats['business'] += data[49] - 1
    # END ----------------------------------------------

    # Results
    return colleges + generateFive(subcats, attribs, specialPackage)
