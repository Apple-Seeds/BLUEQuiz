import random


def generateThree(subcats, attribs, names, points):
    """ This function takes the point totals and determines the top three clubs. """
    
    # Assign Points
    # -- General --
    points['pcab'] = (subcats['general'] + attribs['leader'] + attribs['detailed'])
    points['fees'] = (subcats['general'] + attribs['detailed'] + attribs['discuss'])
    points['council'] = (subcats['general'] + attribs['team'] + attribs['work'])
    points['saa'] = (subcats['general'] + attribs['aggie'] + attribs['mentor'])
    points['nscsc'] = (subcats['general'] + attribs['smart'] + attribs['work'])
    points['ento'] = (subcats['general'] + attribs['dirty'] + attribs['outdoors'])
    points['aspire'] = (subcats['general'] + attribs['smart'] + attribs['excited'])

    # -- Medical --
    points['therapy'] = (subcats['medical'] + attribs['active'] + attribs['caring'])
    points['amsa'] = (subcats['medical'] + attribs['leader'] + attribs['work'])
    points['cadaver'] = (subcats['medical'] + attribs['dirty'] + attribs['detailed'])
    points['hosa'] = (subcats['medical'] + attribs['leader'] + attribs['smart'])
    points['neuro'] = (subcats['medical'] + attribs['smart'] + attribs['detailed'])
    points['dental'] = (subcats['medical'] + attribs['smart'] + attribs['detailed'])
    points['pmed'] = (subcats['medical'] + attribs['detailed'] + attribs['work'])
    points['nami'] = (subcats['medical'] + attribs['caring'] + attribs['mentor'])
    points['physass'] = (subcats['medical'] + attribs['caring'] + attribs['work'])
    points['span'] = (subcats['medical'] + attribs['discuss'] + attribs['caring'] + subcats['dei'])
    points['diet'] = (subcats['medical'] + attribs['active'] + attribs['outdoors'])
    points['milpsych'] = (subcats['medical'] + attribs['caring'] + attribs['smart'])
    points['mcat'] = (subcats['medical'] + attribs['smart'] + attribs['detailed'])
    points['mftsa'] = (subcats['medical'] + attribs['caring'] + attribs['mentor'])

    # -- Business --
    points['algo'] = (subcats['business'] + attribs['smart'] + attribs['detailed'])
    points['sport'] = (subcats['business'] + attribs['active'] + attribs['leader'])
    points['nsls'] = (subcats['business'] + attribs['leader'] + attribs['work'])
    points['bit'] = (subcats['business'] + attribs['smart'] + attribs['detailed'])

    # -- Athletic --
    points['hurd'] = (subcats['athletic'] + attribs['aggie'] + attribs['extrovert'])
    points['canyon'] = (subcats['athletic'] + attribs['outdoors'] + attribs['active'])
    points['archery'] = (subcats['athletic'] + attribs['active'] + attribs['detailed'])
    points['yoga'] = (subcats['athletic'] + attribs['lax'] + attribs['reflect'])
    points['trail'] = (subcats['athletic'] + attribs['outdoors'] + attribs['active'])
    points['volley'] = (subcats['athletic'] + attribs['team'] + attribs['active'])

    # -- Arts --
    points['radio'] = (subcats['arts'] + attribs['discuss'] + attribs['creative'])
    points['blight'] = (subcats['arts'] + attribs['creative'] + attribs['detailed'])
    points['series'] = (subcats['arts'] + attribs['creative'] + attribs['aggie'])
    points['film'] = (subcats['arts'] + attribs['creative'] + attribs['lax'])
    points['bigband'] = (subcats['arts'] + attribs['active'] + attribs['extrovert'])
    points['cswing'] = (subcats['arts'] + attribs['active'] + attribs['extrovert'])
    points['star'] = (subcats['arts'] + attribs['creative'] + attribs['lax'])
    points ['thea'] = (subcats['arts'] + attribs['extrovert'] + attribs['creative'])

    # -- Lifestyle --
    points['blucru'] = (subcats['lifestyle'] + attribs['aggie'] + attribs['work'])
    points['activity'] = (subcats['lifestyle'] + attribs['extrovert'] + attribs['aggie'])
    points['trad'] = (subcats['lifestyle'] + attribs['excited'] + attribs['aggie'])
    points['fsl'] = (subcats['lifestyle'] + attribs['extrovert'] + attribs['team'])
    points['game'] = (subcats['lifestyle'] + attribs['lax'] + attribs['team'])
    points['paint'] = (subcats['lifestyle'] + attribs['active'] + attribs['dirty'])
    points['tennis'] = (subcats['lifestyle'] + attribs['active'] + attribs['detailed'])
    points['spike'] = (subcats['lifestyle'] + attribs['active'] + attribs['extrovert'])
    points['pickle'] = (subcats['lifestyle'] + attribs['active'] + attribs['outdoors'])
    points['skate'] = (subcats['lifestyle'] + attribs['active'] + attribs['excited'])
    points['aikido'] = (subcats['lifestyle'] + attribs['active'] + attribs['work'])
    points['snow'] = (subcats['lifestyle'] + attribs['active'] + attribs['outdoors'])
    points['ram'] = (subcats['lifestyle'] + attribs['outdoors'] + attribs['leader'])

    # -- DEI --
    points['girl'] = (subcats['dei'] + attribs['discuss'] + attribs['reflect'])
    points['ostem'] = (subcats['dei'] + attribs['smart'] + attribs['work'])
    points['transfer'] = (subcats['dei'] + attribs['aggie'] + attribs['extrovert'])
    points['story'] = (subcats['dei'] + attribs['discuss'] + attribs['caring'])
    points['women'] = (subcats['dei'] + attribs['smart'] + attribs['work'])
    
    # -- International --
    points['globcom'] = (subcats['international'] + attribs['discuss'] + attribs['detailed'])
    points['natstud'] = (subcats['international'] + attribs['smart'] + attribs['discuss'])
    points['scandi'] = (subcats['international'] + attribs['discuss'] + attribs['outdoors'])
    points['tagalog'] = (subcats['international'] + attribs['smart'] + attribs['excited'])
    points['russia'] = (subcats['international'] + attribs['discuss'] + attribs['excited'])
    points['irish'] = (subcats['international'] + attribs['active'] + attribs['excited'])

    # -- Studies --
    points['anthro'] = (subcats['studies'] + attribs['reflect'] + attribs['mentor'])
    points['colstud'] = (subcats['studies'] + attribs['reflect'] + attribs['discuss'])
    points['mun'] = (subcats['studies'] + attribs['leader'] + attribs['discuss'])
    points['prssa'] = (subcats['studies'] + attribs['leader'] + attribs['team'])
    points['phil'] = (subcats['studies'] + attribs['reflect'] + attribs['discuss'])
    points['nsslha'] = (subcats['studies'] + attribs['caring'] + attribs['work'])

    # -- Spiritual --
    points['lds'] = (subcats['spiritual'] + attribs['devout'] + attribs['caring'])
    points['fellow'] = (subcats['spiritual'] + attribs['devout'] + attribs['active'])
    points['newman'] = (subcats['spiritual'] + attribs['detailed'] + attribs['team'])
    points['inter'] = (subcats['spiritual'] + attribs['discuss'] + attribs['reflect'])
    points['ssa'] = (subcats['spiritual'] + attribs['reflect'] + attribs['lax'])
    points['christ'] = (subcats['spiritual'] + attribs['devout'] + attribs['discuss'])

    # -- Kindness --
    points['serve'] = (subcats['kindness'] + attribs['caring'] + attribs['team'])
    points['rotaract'] = (subcats['kindness'] + attribs['leader'] + attribs['caring'])
    points['cares'] = (subcats['kindness'] + attribs['caring'] + attribs['aggie'])
    points['bestbud'] = (subcats['kindness'] + attribs['caring'] + attribs['mentor'])
    points['gdays'] = (subcats['kindness'] + attribs['caring'] + attribs['dirty'])
    points['smile'] = (subcats['kindness'] + attribs['caring'] + attribs['mentor'])

    # -- Political --
    points['grc'] = (subcats['political'] + attribs['leader'] + attribs['discuss'])
    points['party'] = (subcats['political'] + attribs['discuss'] + attribs['reflect'])
    points['repo'] = (subcats['political'] + attribs['devout'] + attribs['reflect'])


    # Sort
    topCats = sorted(subcats.items(), key=lambda k: k[1], reverse=True)
    topClubs = sorted(points.items(), key=lambda k: k[1], reverse=True)

    # Results
    three = []
    for x in range(3):
        # Get subcat
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
        'arts': ['radio', 'blight', 'series', 'states', 'film',  'bigband', 'cswing', 'star', 'thea'],
        'lifestyle': ['blucru', 'activity', 'trad', 'fsl', 'game', 'paint', 'tennis', 'spike', 'pickle', 'skate', 'aikido', 'snow', 'ram'],

        'dei': ['girl', 'ostem', 'transfer', 'story', ' women'],
        'international': ['globcom', 'natstud', 'scandi', 'tagalog', 'russia', 'irish'],
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
        'extrovert': 0,
        'aggie': 0,
        'team': 0,
        'caring': 0,
        'mentor': 0,
        'leader': 0,
        'devout': 0,
        'reflect': 0,
        'discuss': 0,
        'lax': 0,
        'outdoors': 0,
        'active': 0,
        'detailed': 0,
        'work': 0,
        'dirty': 0,
        'smart': 0,
        'excited': 0,
        'creative': 0
    }

    # College Collection
    """ This just a short list of numbers corresponding to whatever colleges they're a part of. """
    colleges = []
    for x in range(11):
        if data.pop(0) > 0:
            colleges.append(x + 1)

    # ----------Intro Questions-----------
    # Q2: --------------------------------
    because = []
    for x in range(5):
        if data.pop(0) > 0:
            because.append(x + 1)
    if 1 in because:
        subcats['athletic'] += 3
        subcats['arts'] += 3
        subcats['lifestyle'] += 4
        subcats['dei'] += 3
        subcats['international'] += 3
        subcats['studies'] += 3
        attribs['extrovert'] += 4
        attribs['aggie'] += 3
        attribs['team'] += 2
    elif 2 in because:
        subcats['dei'] += 3
        subcats['international'] += 3
        subcats['studies'] += 3
        subcats['spiritual'] += 3
        subcats['kindness'] += 4
        subcats['political'] += 3
        attribs['caring'] += 3
        attribs['mentor'] += 3
        attribs['leader'] += 2
    elif 3 in because:
        subcats['general'] += 3
        subcats['medical'] += 3
        subcats['business'] += 4
        attribs['leader'] += 3
        attribs['team'] += 3
        attribs['extrovert'] += 2
    elif 4 in because:
        subcats['general'] += 3
        subcats['medical'] += 3
        subcats['business'] += 3
        subcats['dei'] += 4
        subcats['international'] += 4
        subcats['studies'] += 3
        attribs['devout'] += 3
        attribs['caring'] += 4
        attribs['reflect'] += 3
    elif 5 in because:
        subcats['athletic'] += 3
        subcats['arts'] += 3
        subcats['lifestyle'] += 4
        subcats['spiritual'] += 3
        subcats['kindness'] += 3
        subcats['political'] += 3
        attribs['lax'] += 3
        attribs['extrovert'] += 2
        attribs['outdoors'] += 3
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
    attribs['discuss'] += data[4]
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
        subcats['general'] += 3
        clubPoints['ento'] += 6
        attribs['caring'] += 3
        attribs['reflect'] += 1
    elif data[11] == 2:
        subcats['general'] += 2
        clubPoints['ento'] += 4
        attribs['work'] += 3
        attribs['dirty'] += 2
    elif data[11] == 3:
        subcats['general'] += 2
        clubPoints['ento'] += 2
        attribs['lax'] += 3
        attribs['dirty'] += 3
    elif data[11] == 4:
        subcats['general'] -= 2
        clubPoints['ento'] -= 11
        attribs['detailed'] += 2
        attribs['dirty'] -= 3
    # Q15: -------------------------------
    subcats['general'] += data[12]
    clubPoints['aspire'] += data[12] + 2
    attribs['smart'] += data[12] + 2
    attribs['excited'] += data[12]
    if 3 in colleges or 5 in colleges:
        if data[12] > 2:
            clubPoints['aspire'] += 5
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
    clubPoints['therapy'] += 4 - data[14]
    clubPoints['diet'] += 4 - data[14]
    # Q18: -------------------------------
    subcats['medical'] += data[15]
    clubPoints['amsa'] += data[15]
    clubPoints['hosa'] += data[15]
    clubPoints['physass'] += data[15]
    # ---------Business Questions---------
    # Q19: -------------------------------
    subcats['business'] += data[16]
    clubPoints['sport'] += data[16]
    clubPoints['nsls'] += data[16]
    attribs['leader'] += data[16] + 1
    attribs['team'] += data[16]
    # Q20: -------------------------------
    subcats['business'] += data[17]
    clubPoints['algo'] += data[17]
    clubPoints['bit'] += data[17]
    attribs['detailed'] += data[17]
    attribs['smart'] += data[17]
    # --------Recreation Questions--------
    # Q21: -------------------------------
    if data[18] == 1:
        subcats['athletic'] += 3
        subcats['lifestyle'] += 3
        attribs['outdoors'] += 3
        attribs['aggie'] += 4
        attribs['extrovert'] += 2
    elif data[18] == 2:
        subcats['lifestyle'] += 3
        attribs['extrovert'] += 4
        attribs['lax'] += 3
        attribs['caring'] += 2
    elif data[18] == 3:
        subcats['arts'] += 3
        attribs['lax'] += 3
        attribs['creative'] += 3
        attribs['extrovert'] -= 1
    elif data[18] == 4:
        subcats['arts'] += 3
        attribs['detailed'] += 3
        attribs['creative'] += 3
        attribs['lax'] += 1
    elif data[18] == 5:
        subcats['lifestyle'] += 3
        attribs['lax'] += 4
        attribs['outdoors'] += 2
        attribs['work'] -= 1 
    # Q22: -------------------------------
    subcats['athletic'] += data[19]
    attribs['active'] += data[19]
    attribs['dirty'] += data[19] - 1
    attribs['aggie'] += data[19]
    # Q23: -------------------------------
    if data[20] == 1:
        subcats['arts'] += 3
        attribs['detailed'] += 2
        attribs['creative'] += 3
    elif data[20] == 2:
        subcats['lifestyle'] += 3
        attribs['extrovert'] += 3
        attribs['mentor'] += 2
    elif data[20] == 3:
        subcats['arts'] += 3
        attribs['creative'] += 3
        attribs['lax'] += 1
    elif data[20] == 4:
        subcats['athletic'] += 3
        attribs['lax'] += 1
        attribs['active'] += 2
    elif data[20] == 5:
        subcats['athletic'] += 3
        attribs['outdoors'] += 4
        attribs['lax'] += 1
    elif data[20] == 5:
        subcats['athletic'] -= 1
        subcats['arts'] -= 1
        subcats['lifestyle'] -= 1
    # ---------Athletic Questions---------
    # Q24: -------------------------------
    subcats['athletic'] += data[21]
    clubPoints['canyon'] += data[21]
    clubPoints['trail'] += data[21]
    attribs['outdoors'] += data[21] + 1
    attribs['dirty'] += data[21] - 1
    # Q25: -------------------------------
    subcats['athletic'] += data[22]
    clubPoints['hurd'] += data[22] + 1
    attribs['aggie'] += data[22] + 1
    attribs['extrovert'] += data[22] - 1
    # Q26: -------------------------------
    subcats['athletic'] += data[23]
    clubPoints['spike'] += data[23]
    clubPoints['volley'] += data[23]
    clubPoints['archery'] += 4 - data[23]
    clubPoints['yoga'] += 4 - data[23]
    attribs['dirty'] += data[23] - 1
    attribs['active'] += data[23] + 1
    # -----------Arts Questions-----------
    # Q27: -------------------------------
    subcats['arts'] += data[24]
    clubPoints['thea'] += data[24] + 1
    attribs['creative'] += data[24]
    attribs['extrovert'] += data[24] - 1
    # Q28: -------------------------------
    if data[25] == 1:
        subcats['arts'] += 3
        clubPoints['states'] += 3
        clubPoints['radio'] += 3
        attribs['detailed'] += 2
        attribs['reflect'] += 2
    elif data[25] == 2:
        subcats['arts'] += 3
        clubPoints['states'] += 3
        clubPoints['blight'] += 3
        attribs['detailed'] += 2
        attribs['creative'] += 3
    elif data[25] == 3:
        subcats['arts'] += 3
        clubPoints['blight'] += 3
        clubPoints['series'] += 3
        attribs['extrovert'] += 2
        attribs['mentor'] += 2
    elif data[25] == 4:
        subcats['arts'] += 3
        clubPoints['radio'] += 3
        clubPoints['series'] += 3
        attribs['creative'] += 2
        attribs['reflect'] += 1
    elif data[25] == 5:
        subcats['arts'] += 3
        clubPoints['bigband'] += 4
        clubPoints['cswing'] += 4
        attribs['active'] += 3
        attribs['extrovert'] += 2
    elif data[25] == 6:
        subcats['arts'] -= 2
    # Q29: -------------------------------
    subcats['arts'] += data[26]
    clubPoints['film'] += data[26]
    clubPoints['star'] += data[26] - 1
    attribs['creative'] += data[26] - 1
    attribs['lax'] += data[26]
    # ---------Lifestyle Questions--------
    # Q30: -------------------------------
    if data[27] == 1:
        subcats['lifestyle'] += 3
        clubPoints['game'] += 3
        attribs['lax'] += 2
        attribs['smart'] += 2
    elif data[27] == 2:
        subcats['lifestyle'] += 3
        clubPoints['tennis'] += 3
        attribs['active'] += 2
        attribs['outdoors'] -= 1
    elif data[27] == 3:
        subcats['lifestyle'] += 3
        clubPoints['pickle'] += 3
        attribs['active'] += 2
        attribs['team'] += 2
    elif data[27] == 4:
        subcats['lifestyle'] += 2
    elif data[27] == 5:
        subcats['lifestyle'] -= 2
    # Q31: -------------------------------
    subcats['lifestyle'] += data[28]
    clubPoints['snow'] += data[28] + 1
    attribs['outdoors'] += data[28] - 1
    attribs['active'] += data[28]
    # Q32: -------------------------------
    subcats['lifestyle'] += data[29]
    clubPoints['aikido'] += data[29]
    clubPoints['paint'] += data[29]
    attribs['active'] += data[29] - 1
    attribs['lax'] -= data[29] - 1
    # Q33: -------------------------------
    subcats['lifestyle'] += data[30]
    clubPoints['skate'] += data[30] + 1
    attribs['outdoors'] += data[30] - 1
    attribs['active'] += data[30] - 1
    # Q34: -------------------------------
    subcats['lifestyle'] += data[31]
    clubPoints['blucru'] += data[31]
    clubPoints['active'] += data[31]
    clubPoints['trad'] += data[31]
    clubPoints['fsl'] += data[31]
    attribs['aggie'] += data[31]
    attribs['extrovert'] += data[31] - 1
    # --------Humanities Questions--------
    # Q35: -------------------------------
    subcats['dei'] += data[32]
    subcats['international'] += data[32]
    attribs['discuss'] += data[32]
    attribs['reflect'] += data[32]
    attribs['excited'] += data[32] - 1
    # Q36: -------------------------------
    subcats['dei'] += data[33] + 1
    subcats['political'] += data[33] # (not technically in this category, but it felt good to add here)
    attribs['caring'] += data[33]
    attribs['discuss'] += data[33]
    attribs['leader'] += data[33] - 1
    # Q37: -------------------------------
    subcats['studies'] += data[34]
    attribs['lax'] += data[34] - 1
    attribs['reflect'] += data[34]
    attribs['smart'] -= data[34] - 1
    # Q38: -------------------------------
    subcats['international'] += data[35]
    subcats['studies'] += data[35]
    attribs['discuss'] += data[35]
    attribs['excited'] += data[35]
    attribs['extrovert'] += data[35]
    # ---------Diversity Questions--------
    # Q39: -------------------------------
    subcats['dei'] += data[36] - 1
    clubPoints['transfer'] += data[36] + 1
    attribs['aggie'] += data[36]
    attribs['excited'] += data[36] - 1
    if data[36] > 2:
        clubPoints['transfer'] += 3
    # Q40: -------------------------------
    subcats['dei'] += data[37]
    clubPoints['girl'] += data[37]
    clubPoints['story'] += data[37]
    attribs['reflect'] += data[37]
    attribs['discuss'] += data[37]
    # Q41: -------------------------------
    subcats['dei'] += data[38]
    clubPoints['ostem'] += data[38]
    clubPoints['women'] += data[38]
    attribs['aggie'] += data[38] - 1
    attribs['work'] += data[38]
    if data[38] > 2:
        clubPoints['ostem'] += 3
        clubPoints['women'] += 3
    # -------International Questions------
    # Q42: -------------------------------
    subcats['international'] += data[39]
    clubPoints['globcom'] += data[39]
    clubPoints['natstud'] += data[39]
    attribs['smart'] += data[39]
    attribs['discuss'] += data[39]
    # Q43: -------------------------------
    subcats['international'] += data[40]
    clubPoints['irish'] += data[40] + 1
    attribs['excited'] += data[40]
    attribs['extrovert'] += data[40] - 1
    # Q44: -------------------------------
    subcats['international'] += data[41]
    clubPoints['scandi'] += data[41]
    clubPoints['russia'] += data[41]
    attribs['outdoors'] += data[41] - 1
    attribs['excited'] += data[41]
    # Q45: -------------------------------
    subcats['international'] += data[42]
    clubPoints['tagalog'] += data[42] + 1
    attribs['smart'] += data[42]
    attribs['work'] += data[42] - 1
    # ----------Studies Questions---------
    # Q46: -------------------------------
    subcats['studies'] += data[43]
    clubPoints['anthro'] += data[43]
    attribs['smart'] += data[43]
    attribs['reflect'] += data[43]
    # Q47: -------------------------------
    subcats['studies'] += data[44]
    clubPoints['mun'] += data[44]
    clubPoints['prssa'] += data[44]
    attribs['caring'] += data[44] - 1
    attribs['leader'] += data[44] - 1
    # Q48: -------------------------------
    subcats['studies'] += data[45]
    clubPoints['colstud'] += data[45]
    clubPoints['phil'] += data[45]
    attribs['reflect'] += data[45]
    attribs['discuss'] += data[45]
    # Q49: -------------------------------
    subcats['studies'] += data[46]
    clubPoints['nsslha'] += data[46]
    attribs['caring'] += data[46]
    attribs['mentor'] += data[46]
    # ----------Service Questions---------
    # Q50: -------------------------------
    subcats['spiritual'] += data[47] + 1
    attribs['devout'] += data[47]
    attribs['reflect'] += data[47]
    attribs['caring'] += data[47] - 1
    # Q51: -------------------------------
    subcats['political'] += data[48]
    attribs['smart'] += data[48]
    attribs['detailed'] += data[48]
    attribs['discuss'] += data[48]
    # Q52: -------------------------------
    if data[49] == 1:
        subcats['kindness'] += 3
        attribs['extrovert'] -= 2
        attribs['caring'] += 2
    elif data[49] == 2:
        subcats['kindness'] += 3
        attribs['extrovert'] += 1
        attribs['team'] += 1
    elif data[49] == 3:
        subcats['kindness'] += 3
        attribs['team'] += 3
        attribs['leader'] += 1
    elif data[49] == 4:
        subcats['kindness'] -= 3
        attribs['caring'] -= 2
        attribs['team'] -= 1
    # Q53: -------------------------------
    for x in range(7):
        choice = 7 - data.pop(50)
        if x == 0:
            subcats['spiritual'] += choice
            attribs['devout'] += choice
            attribs['reflect'] += choice - 1
        elif x == 1:
            subcats['political'] += choice
            attribs['discuss'] += choice
            attribs['devout'] += choice - 1
        elif x == 2:
            subcats['general'] += choice
            subcats['medical'] += choice
            subcats['business'] += choice
            attribs['smart'] += choice
            attribs['work'] += choice
        elif x == 3:
            subcats['medical'] += choice
            attribs['outdoors'] += choice
            attribs['active'] += choice
        elif x == 4:
            subcats['lifestyle'] += choice
            subcats['kindness'] += choice
            subcats['dei'] += choice - 1
            attribs['extrovert'] += choice
            attribs['caring'] += choice
        elif x == 5:
            subcats['athletic'] += choice
            subcats['general'] += choice - 1
            attribs['aggie'] += choice + 1
            attribs['leader'] += choice - 1
        elif x == 6:
            subcats['dei'] += choice
            subcats['international'] += choice
            subcats['spiritual'] += choice
            attribs['reflect'] += choice
            attribs['devout'] += choice - 1
    # ---------Spiritual Questions--------
    # Q54: -------------------------------
    if data[50] == 1:
        subcats['spiritual'] += 3
        clubPoints['lds'] += 5
        attribs['devout'] += 3
        attribs['extrovert'] += 2
    elif data[50] == 2:
        subcats['spiritual'] += 3
        clubPoints['christ'] += 5
        attribs['devout'] += 3
        attribs['reflect'] += 2
    elif data[50] == 3:
        subcats['spiritual'] += 3
        clubPoints['newman'] += 5
        attribs['devout'] += 3
        attribs['team'] += 2
    elif data[50] == 4:
        subcats['spiritual'] += 1
        clubPoints['saa'] += 6
        attribs['devout'] -= 1
        attribs['discuss'] += 3
    elif data[50] == 5:
        subcats['spiritual'] += 3
        clubPoints['inter'] += 3
        attribs['reflect'] += 2
    # Q55: -------------------------------
    subcats['spiritual'] += data[51]
    attribs['devout'] += (data[51] / 2)
    attribs['reflect'] += (data[51] / 2)
    # Q56: -------------------------------
    clubPoints['inter'] += data[52] + 1
    attribs['discuss'] += data[52] + 1
    attribs['reflect'] += data[52]
    # ---------Kindness Questions---------
    # Q57: -------------------------------
    data[53] = data[53] + 2
    subcats['kindness'] += (data[53] * -1)
    clubPoints['serve'] -= data[53]
    clubPoints['cares'] -= data[53]
    attribs['excited'] -= data[53]
    attribs['caring'] -= data[53]
    # Q58: -------------------------------
    service = []
    for x in range(5):
        if data.pop(54) > 0:
            service.append(x + 1)
    if 1 in service:
        subcats['kindness'] += 3
        clubPoints['cares'] += 3
        attribs['caring'] += 3
        attribs['reflect'] += 2
    elif 2 in service:
        subcats['kindness'] += 3
        clubPoints['bestbud'] += 3
        attribs['caring'] += 3
        attribs['mentor'] += 2
    elif 3 in service:
        subcats['kindness'] += 3
        clubPoints['smile'] += 3
        attribs['caring'] += 3
        attribs['active'] += 1
    elif 4 in service:
        subcats['kindness'] += 3
        clubPoints['rotaract'] += 3
        clubPoints['gdays'] += 3
        attribs['caring'] += 3
        attribs['leader'] += 1
    # Q59: -------------------------------
    subcats['kindness'] += data[54]
    clubPoints['rotaract'] += data[54]
    clubPoints['cares'] += data[54]
    clubPoints['serve'] += data[54]
    attribs['caring'] += data[54] - 1
    attribs['aggie'] += data[54] - 1
    attribs['leader'] += data[54]
    # ---------Political Questions--------
    # Q60: -------------------------------
    subcats['political'] += data[55]
    clubPoints['party'] += data[55]
    attribs['discuss'] += data[55]
    attribs['caring'] += data[55] - 1
    attribs['devout'] += data[55]
    # Q61: -------------------------------
    subcats['political'] += data[56]
    clubPoints['grc'] += data[56] + 1
    attribs['discuss'] += data[56]
    attribs['leader'] += data[56]
    attribs['work'] += data[56] - 1
    # Q62: -------------------------------
    subcats['political'] += data[57]
    clubPoints['repo'] += data[57] + 1
    attribs['devout'] += data[57]
    attribs['discuss'] += data[57]
    attribs['caring'] += data[57] - 1
    # END ----------------------------------------------
    # Results
    return colleges + generateThree(subcats, attribs, clubNames, clubPoints)
