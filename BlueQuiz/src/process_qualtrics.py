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
            clubPoints[name] = 0

    # Assign Points
    # -Manual-
    clubPoints['pcab'] = (attribs['leader'] + attribs['team'] + attribs['project'])
    clubPoints['fees'] = (attribs['detail'] - attribs['busybee'] + subcats['political'])
    clubPoints['saa'] = (attribs['aggie'] + attribs['serve'] + attribs['extroverted'])
    clubPoints['council'] = (attribs['serve'] + attribs['extroverted'] + (len(specvals[0]) * 2))
    clubPoints['nscsc'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['therapy'] = (attribs['serve'] + attribs[''] + attribs[''])
    clubPoints['amsa'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['cadaver'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['hosa'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['neuro'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['dental'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['pmed'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['physass'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['spmed'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['diet'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['anthro'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['milpsych'] = (attribs['serve'] + attribs[''] + attribs[''])
    clubPoints['glocom'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['colstud'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['natstud'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['mun'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['prssa'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['finance'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['sport'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['nsls'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['aspire'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['ram'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['hurd'] = (subcats['athletic'] + attribs['aggie'] + attribs['hype'])
    clubPoints['canyon'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['archery'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['yoga'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['trail'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['radio'] = (subcats['arts'] + attribs['music'] + attribs['charisma'])
    clubPoints['blight'] = (attribs['detail'] + subcats['arts'] + subcats['business'])
    clubPoints['series'] = (subcats['arts'] + attribs['extroverted'] + attribs['aggie'])
    clubPoints['film'] = (subcats['arts'] + attribs['cozy'] + attribs['discuss'])
    clubPoints['irish'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['bigband'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['cswing'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['blucru'] = (attribs['serve'] + attribs['aggie'] + subcats['business'])
    clubPoints['activity'] = (attribs['hype'] + attribs['aggie'] + attribs['detail'])
    clubPoints['trad'] = (attribs['charisma'] + attribs['aggie'] + attribs['extroverted'])
    clubPoints['fsl'] = (attribs['extroverted'] + attribs['hype'] + attribs['serve'])
    clubPoints['game'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['paint'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['tennis'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['spike'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['girl'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['nami'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['ostem'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['scandi'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['tagalog'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['transfer'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['lds'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['colchrist'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['fellow'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['goldcity'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['varsity'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['navi'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['newman'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['ratio'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['inter'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['ssa'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['serve'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['rotaract'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['cares'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['bestbud'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['gdays'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['grc'] = (subcats['political'] + subcats['academic'] + attribs['stugov'])
    clubPoints['dems'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['ydsa'] = (attribs[''] + attribs[''] + attribs[''])
    clubPoints['surf'] = (attribs[''] + attribs[''] + attribs[''])
    # -Random-
    for key in clubPoints:
        key += random.randrange(1, 4)

    # Sort
    subcats = sorted(subcats.items(), key=lambda k: k[1], reverse=True)
    topCats = subcats.keys()
    clubPoints = sorted(clubPoints.items(), key=lambda k: k[1], reverse=True)
    topClubs = clubPoints.keys()

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
        'general': 0,
        'medical': 0,
        'humanities': 0,
        'business': 0,
        'athletic': 0,
        'arts': 0,
        'lifestyle': 0,
        'dei': 0,
        'spiritual': 0,
        'kindness': 0,
        'political': 0
    }
    attribs = {
        "leader": 0,
        "charisma": 0,
        "hardwork": 0,
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
    }

    # College Collection
    colleges = []
    for x in range(10):
        if data.pop(0) > 0:
            colleges.append(x + 1)

    # Point Allocation ----------------------------------
    specialPackage = [] # The 'Special Package' is for data that is relevant only to a specific club.
    specialPackage.append(colleges)
    # ----------Intro Questions----------
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
        attribs['extroverted'] += 3
        attribs['charisma'] += 2
    elif 2 in because:
        subcats['spiritual'] += 2
        subcats['kindness'] += 3
        subcats['political'] += 2
        subcats['dei'] += 2
        attribs['serve'] += 3
        attribs['hardwork'] += 2
    elif 3 in because:
        subcats['general'] += 2
        subcats['medical'] += 2
        subcats['business'] += 3
        subcats['political'] += 2
        attribs['charisma'] += 2
        attribs['leader'] += 2
    elif 4 in because:
        subcats['spiritual'] += 2
        subcats['kindness'] += 2
        subcats['general'] += 2
        subcats['humanities'] += 2
        subcats['business'] += 2
        attribs['hardwork'] += 2
        attribs['leader'] += 2
    elif 5 in because:
        subcats['lifestyle'] += 2
        subcats['athletic'] += 2
        subcats['kindness'] += 2
        subcats['athletic'] += 2
        attribs['time'] += 2
        attribs['cozy'] += 2
    # Q3: --------------------------------
    subcats['general'] += data[0]
    subcats['medical'] += data[0]
    subcats['humanities'] += data[0]
    subcats['business'] += data[0]
    subcats['kindness'] += data[0] - 1
    subcats['political'] += data[0] - 1
    attribs['smart'] += data[0]
    attribs['detail'] += data[0]
    attribs['project'] += data[0]
    # Q4: --------------------------------
    subcats['athletic'] += data[1] + 1
    subcats['lifestyle'] += data[1]
    attribs['extroverted'] += data[1]
    attribs['hype'] += data[1]
    attribs['aggie'] += data[1]
    attribs['active'] += data[1]
    # Q5: --------------------------------
    subcats['dei'] += data[2]
    subcats['spiritual'] += data[2]
    subcats['kindness'] += data[2]
    subcats['political'] += data[2]
    attribs['leader'] += data[2]
    attribs['serve'] += data[2]
    attribs['hardwork'] += data[2]
    # -----------REC Questions-----------
    # Q6: --------------------------------
    if data[3] == 1:
        subcats['athletic'] += 3
        attribs['active'] += 3
        attribs['aggie'] += 3
    elif data[3] == 2:
        subcats['lifestyle'] += 3
        attribs['extroverted'] += 2
        attribs['music'] += 2
    elif data[3] == 3:
        subcats['arts'] += 3
        attribs['creative'] += 3
        attribs['cozy'] += 2
        specialPackage.append(3)
    elif data[3] == 4:
        subcats['arts'] += 4
        attribs['creative'] += 3
        attribs['detail'] += 2
    elif data[3] == 5:
        subcats['lifestyle'] += 3
        attribs['cozy'] += 3
        attribs['time'] += 2
    # Q7: --------------------------------
    subcats['athletic'] += data[4]
    attribs['aggie'] += 2
    attribs['active'] += data[4]
    attribs['hardwork'] += data[4]
    attribs['outdoors'] += data[4]
    # Q8: --------------------------------
    if data[5] == 1:
        subcats['art'] += 3
        attribs['creative'] += 3
        attribs['detail'] += 2
    elif data[5] == 2:
        subcats['lifestyle'] += 3
        attribs['extroverted'] += 3
        attribs['discuss'] += 2
    elif data[5] == 3:
        subcats['lifestyle'] += 2
        subcats['arts'] += 2
        attribs['music'] += 3
    elif data[5] == 4:
        subcats['athletic'] += 2
        attribs['cozy'] += 2
        attribs['active'] += 2
    # ---------Athletic Questions---------
    # Q9: --------------------------------
    subcats['athletic'] += data[6]
    attribs['active'] += data[6]
    attribs['outdoors'] += data[6] + 1
    # Q10: --------------------------------
    subcats['athletic'] += data[7]
    attribs['active'] += data[7]
    attribs['hardwork'] += data[7] - 1
    # -----------Artsy Questions-----------
    # Q11: --------------------------------
    subcats['arts'] += data[8]
    attribs['active'] += data[8]
    attribs['dance'] += data[8] + 1
    attribs['extroverted'] += data[8] - 1
    # Q12: --------------------------------
    subcats['arts'] += data[9]
    attribs['extroverted'] += data[9] + 1
    attribs['dance'] += data[9]
    attribs['hype'] += data[9] + 1
    # Q13: --------------------------------
    subcats['arts'] += data[10]
    attribs['creative'] += data[10] + 1
    attribs['music'] += data[10] - 1
    attribs['detail'] += data[10]
    # ---------Lifestyle Questions---------
    # Q14: --------------------------------
    subcats['lifestyle'] += data[11]
    attribs['extroverted'] += data[11]
    attribs['team'] += data[11]
    # Q15: --------------------------------
    subcats['lifestyle'] += 2
    if data[12] in [1, 2, 3, 4]:
        specialPackage.append(data[12])
    elif data[12] == 6:
        attribs['extroverted'] -= 2
        attribs['active'] -= 1
        subcats['lifestyle'] -= 3
    # Q16: --------------------------------
    attribs['detail'] += data[13]
    attribs['smart'] += data[13]
    # Q17: --------------------------------
    attribs['active'] += data[14] - 1
    attribs['outdoors'] += data[14] + 1
    specialPackage.append(data[14])
    # ------------DEI Questions------------
    # Q18: --------------------------------
    subcats['dei'] += data[15]
    attribs['serve'] += data[15]
    attribs['political'] += data[15] - 1
    # Q19: --------------------------------
    specialPackage.append(data[16])
    attribs['aggie'] += data[16] - 1
    # Q20: --------------------------------
    subcats['dei'] += 1
    specialPackage.append(data[17])
    # Q21: --------------------------------
    subcats['dei'] += data[18]
    attribs['cultured'] += data[18]
    # ----------Service Questions----------
    # Q22: --------------------------------
    subcats['spiritual'] += data[19]
    attribs['faith'] += data[19] + 1
    # Q23: --------------------------------
    subcats['political'] += data[20]
    attribs['political'] += data[20]
    attribs['leader'] += data[20] - 1
    # Q24: --------------------------------
    subcats['serve'] += 3
    if data[21] == 1:
        attribs['extroverted'] -= 1
        attribs['team'] -= 1
        attribs['serve'] += 2
    elif data[21] == 2:
        attribs['team'] += 2
        attribs['extroverted'] += 1
        attribs['serve'] += 2
    elif data[21] == 3:
        attribs['team'] += 2
        attribs['extroverted'] += 2
        attribs['leader'] += 1
        attribs['serve'] += 1
    elif data[21] == 4:
        subcats['serve'] -= 4
        attribs['serve'] -= 2
    # ----------Spirit Questions----------
    # Q25: --------------------------------
    specialPackage.append(data[22])
    subcats['spiritual'] += data[22]
    attribs['faith'] += data[22] - 1
    # Q26: --------------------------------
    subcats['spiritual'] += data[23]
    attribs['faith'] += data[23] + 2
    attribs['cultured'] += data[23]
    attribs['discuss'] += data[23] - 1
    # Q27: --------------------------------
    subcats['spiritual'] += data[24]
    attribs['discuss'] += data[24] + 2
    attribs['faith'] += data[24]
    attribs['extroverted'] += data[24] - 1
    # Q28: --------------------------------
    subcats['spiritual'] += data[25]
    specialPackage.append(data[25])
    attribs['faith'] += data[25] - 1
    # -----------Kind Questions-----------     (needs some work)
    # Q29: --------------------------------
    specialPackage.append(data[26])
    subcats['kindness'] += data[26]
    attribs['mentor'] += data[26]
    attribs['serve'] += data[26] + 1
    # Q30: --------------------------------
    subcats['kindness'] += data[27]
    attribs['serve'] += data[27] + 1
    # Q31: --------------------------------
    subcats['kindness'] += data[28]
    attribs['serve'] += data[28] + 1
    attribs['leader'] += data[28] - 1
    # ----------Politic Questions----------    (needs some work)
    # Q32: --------------------------------
    specialPackage.append(data[29])
    subcats['political'] += data[29]
    # Q33: --------------------------------
    specialPackage.append(data[30])
    subcats['political'] += data[30]
    # ---------Academic Questions----------
    # Q34: --------------------------------
    subcats['medical'] -= data[31]
    # Q35: --------------------------------
    subcats['general'] += data[32]
    subcats['business'] += data[32]
    attribs['team'] += data[32]
    attribs['leader'] += data[32] - 1
    attribs['project'] += data[32] - 1
    # Q36: --------------------------------
    subcats['general'] -= data[33]
    subcats['medical'] -= data[33]
    attribs['smart'] += data[33]
    attribs['hardwork'] -= data[33]
    attribs['detail'] -= data[33]
    # Q37: --------------------------------
    subcats['humanities'] += data[34] + 1
    subcats['business'] += data[34]
    # Q38: --------------------------------
    subcats['general'] += data[35]
    subcats['humanities'] += data[35]
    subcats['political'] += data[35] -1
    attribs['political'] += data[35]
    attribs['detail'] += data[35]
    # Q39: --------------------------------
    subcats['business'] += data[36] + 1
    attribs['leader'] += data[36]
    attribs['charisma'] += data[36] - 1
    attribs['hardwork'] += data[36]
    # ---------General Questions----------
    # Q40: --------------------------------
    if data[37] != 5:
        subcats['general'] += 2
        specialPackage.append(data[37])
    else:
        subcats['general'] -= 2
    # Q41: --------------------------------
    subcats['general'] += data[38]
    attribs['smart'] += data[38]
    attribs['hardwork'] += data[38]
    # Q42: --------------------------------
    subcats['general'] += data[39]
    attribs['leader'] += data[39]
    attribs['aggie'] += data[39] - 1
    attribs['serve'] += data[39] - 1
    # Q43: --------------------------------
    subcats['general'] += data[40]
    subcats['athletic'] += data[40] - 1
    attribs['aggie'] += data[40] + 1
    attribs['mentor'] += data[40]
    attribs['hype'] += data[40] - 1
    # ---------Medical Questions----------
    # Q44: --------------------------------
    specialPackage.append(data[41])
    subcats['medical'] += data[41]
    subcats['detail'] += data[41] - 1
    # Q45: --------------------------------
    specialPackage.append(data[42])
    subcats['medical'] += data[42]
    subcats['hardwork'] += data[42]
    subcats['serve'] += data[42] - 1
    # Q46: --------------------------------
    specialPackage.append(data[43])
    subcats['medical'] += data[43]
    subcats['serve'] += data[43]
    # Q47: --------------------------------
    subcats['medical'] += 3
    if data[44] != 12 or data[44] != 0:
        specialPackage.append(data[44])      
    else:
        subcats['medical'] -= 3
    # ---------Medical Questions----------
    # Q48: --------------------------------
    subcats['humanities'] += data[45]
    attribs['cultured'] += data[45] + 1
    attribs['discuss'] += data[45] - 1
    # Q49: --------------------------------
    if data[46] != 5 or data[46] != 0:
        specialPackage.append(data[46])
        subcats['humanities'] += 2
        if data[46] == 4:
            attribs['dance'] += 3
        elif data[46] == 3:
            attribs['music'] += 3
        elif data[46] == 2:
            attribs['charisma'] += 2
    else:
        subcats['humanities'] -= 2
    # Q50: --------------------------------
    subcats['humanities'] -= data[47]
    attribs['cultured'] -= data[47]
    attribs['political'] -= data[47] + 1
    attribs['discuss'] -= data[47] + 1
    # ---------Business Questions----------
    # Q51: --------------------------------
    subcats['business'] += data[48]
    attribs['leader'] += data[48] + 1
    attribs['charisma'] += data[48] - 1
    attribs['team'] += data[48]
    # Q52: --------------------------------
    specialPackage.append(data[49])
    subcats['business'] += data[49] - 1
    attribs['detail'] += data[49] - 1
    # END ----------------------------------------------

    # Results
    return colleges + generateFive(subcats, attribs, specialPackage)
