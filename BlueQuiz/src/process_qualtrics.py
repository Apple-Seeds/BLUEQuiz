import random


def generateThree(subcats, attribs, names, points):
    """ This function takes the point totals and determines the top three clubs. """

    # Assign Points
        # -- General --
    points['pcab'] = (subcats['general'] + attribs['leader'] + attribs['team'] + attribs['aggie'])
    points['fees'] = (subcats['general'] + attribs['detailed'] + attribs['discuss'] + attribs['helpful'])
    points['council'] = (subcats['general'] + attribs['team'] + attribs['detailed'] + attribs['work'])
    points['saa'] = (subcats['general'] + attribs['aggie'] + attribs['mentor'] + attribs['hype'])
    points['nscsc'] = (subcats['general'] + attribs['detailed'] + attribs['work'] + attribs['smart'])
    points['ento'] = (subcats['general'] + attribs['messy'] + attribs['outdoors'] + attribs['caring'])
    points['aspire'] = (subcats['general'] + attribs['detailed'] + attribs['excited'] + attribs['smart'])

    # -- Medical --
    points['therapy'] = (subcats['medical'] + attribs['active'] + attribs['caring'] + attribs['helpful'])
    points['amsa'] = (subcats['medical'] + attribs['leader'] + attribs['helpful'] + attribs['team']) 
    points['cadaver'] = (subcats['medical'] + attribs['messy'] + attribs['detailed'] + attribs['excited'])
    points['hosa'] = (subcats['medical'] + attribs['leader'] + attribs['smart'] + attribs['mentor'])
    points['neuro'] = (subcats['medical'] + attribs['smart'] + attribs['detailed'] + attribs['work'])
    points['dental'] = (subcats['medical'] + attribs['smart'] + attribs['messy'] + attribs['detailed'])
    points['pmed'] = (subcats['medical'] + attribs['detailed'] + attribs['work'] + attribs['mentor'])
    points['nami'] = (subcats['medical'] + attribs['caring'] + attribs['mentor'] + attribs['discuss'])
    points['physass'] = (subcats['medical'] + attribs['helpful'] + attribs['work'] + attribs['caring'])
    points['span'] = (subcats['medical'] + subcats['dei'] + attribs['excited'] + attribs['helpful'])
    points['diet'] = (subcats['medical'] + attribs['active'] + attribs['outdoors'] + attribs['mentor'])
    points['milpsych'] = (subcats['medical'] + attribs['caring'] + attribs['smart'] + attribs['discuss'])
    points['mcat'] = (subcats['medical'] + attribs['smart'] + attribs['work'] + attribs['detailed'])
    points['mftsa'] = (subcats['medical'] + attribs['caring'] + attribs['mentor'] + attribs['discuss'])

    # -- Business --
    points['algo'] = (subcats['business'] + attribs['smart'] + attribs['detailed'] + attribs['hype'])
    points['sport'] = (subcats['business'] + attribs['hype'] + attribs['leader'] + attribs['mentor'])
    points['nsls'] = (subcats['business'] + attribs['leader'] + attribs['work'] + attribs['extrovert'])
    points['bit'] = (subcats['business'] + attribs['smart'] + attribs['detailed'] + attribs['hype'])

    # -- Athletic --
    points['hurd'] = (subcats['athletic'] + attribs['aggie'] + attribs['extrovert'] + attribs['hype'])
    points['canyon'] = (subcats['athletic'] + attribs['outdoors'] + attribs['active'] + attribs['messy'])
    points['archery'] = (subcats['athletic'] + attribs['active'] + attribs['detailed'] + attribs['outdoors'])
    points['yoga'] = (subcats['athletic'] + attribs['lax'] + attribs['introspective'] + attribs['creative'])
    points['trail'] = (subcats['athletic'] + attribs['outdoors'] + attribs['active'] + attribs['messy'])
    points['volley'] = (subcats['athletic'] + attribs['team'] + attribs['active'] + attribs['hype'])

    # -- Arts --
    points['radio'] = (subcats['arts'] + attribs['discuss'] + attribs['creative'] + attribs['excited'])
    points['blight'] = (subcats['arts'] + attribs['creative'] + attribs['detailed'] + attribs['work'])
    points['series'] = (subcats['arts'] + attribs['creative'] + attribs['aggie'] + attribs['excited'])
    points['film'] = (subcats['arts'] + attribs['creative'] + attribs['lax'] + attribs['discuss'])
    points['bigband'] = (subcats['arts'] + attribs['active'] + attribs['extrovert'] + attribs['hype'])
    points['cswing'] = (subcats['arts'] + attribs['active'] + attribs['extrovert'] + attribs['devout'])
    points['star'] = (subcats['arts'] + attribs['creative'] + attribs['lax'] + attribs['devout'])
    points['thea'] = (subcats['arts'] + attribs['extrovert'] + attribs['creative'] + attribs['introspective'])

    # -- Lifestyle --
    points['blucru'] = (subcats['lifestyle'] + attribs['aggie'] + attribs['work'] + attribs['outdoors'])
    points['activity'] = (subcats['lifestyle'] + attribs['extrovert'] + attribs['aggie'] + attribs['hype'])
    points['trad'] = (subcats['lifestyle'] + attribs['excited'] + attribs['aggie'] + attribs['creative'])
    points['fsl'] = (subcats['lifestyle'] + attribs['extrovert'] + attribs['team'] + attribs['hype'])
    points['game'] = (subcats['lifestyle'] + attribs['lax'] + attribs['team'] + attribs['detailed'])
    points['paint'] = (subcats['lifestyle'] + attribs['team'] + attribs['messy'] + attribs['active'])
    points['tennis'] = (subcats['lifestyle'] + attribs['active'] + attribs['detailed'] + attribs['lax'])
    points['spike'] = (subcats['lifestyle'] + attribs['messy'] + attribs['extrovert'] + attribs['outdoors'])
    points['pickle'] = (subcats['lifestyle'] + attribs['lax'] + attribs['outdoors'] + attribs['extrovert'])
    points['skate'] = (subcats['lifestyle'] + attribs['active'] + attribs['excited'] + attribs['lax'])
    points['aikido'] = (subcats['lifestyle'] + attribs['active'] + attribs['work'] + attribs['messy'])
    points['snow'] = (subcats['lifestyle'] + attribs['active'] + attribs['outdoors'] + attribs['messy'])
    points['ram'] = (subcats['lifestyle'] + attribs['outdoors'] + attribs['leader'] + attribs['helpful'])

    # -- DEI --
    points['girl'] = (subcats['dei'] + attribs['discuss'] + attribs['introspective'] + attribs['extrovert'])
    points['ostem'] = (subcats['dei'] + attribs['smart'] + attribs['work'] + attribs['devout'])
    points['transfer'] = (subcats['dei'] + attribs['aggie'] + attribs['extrovert'] + attribs['excited'])
    points['story'] = (subcats['dei'] + attribs['excited'] + attribs['caring'] + attribs['introspective'])
    points['women'] = (subcats['dei'] + attribs['smart'] + attribs['work'] + attribs['devout'])

    # -- International --
    points['globcom'] = (subcats['international'] + attribs['discuss'] + attribs['detailed'] + attribs['leader'])
    points['natstud'] = (subcats['international'] + attribs['smart'] + attribs['excited'] + attribs['smart'])
    points['scandi'] = (subcats['international'] + attribs['excited'] + attribs['outdoors'] + attribs['lax'])
    points['tagalog'] = (subcats['international'] + attribs['smart'] + attribs['excited'] + attribs['lax'])
    points['russia'] = (subcats['international'] + attribs['discuss'] + attribs['excited'] + attribs['lax'])
    points['irish'] = (subcats['international'] + attribs['active'] + attribs['excited'] + attribs['extrovert'])

    # -- Studies --
    points['anthro'] = (subcats['studies'] + attribs['introspective'] + attribs['mentor'] + attribs['messy'])
    points['colstud'] = (subcats['studies'] + attribs['introspective'] + attribs['discuss'] + attribs['discuss'])
    points['mun'] = (subcats['studies'] + attribs['leader'] + attribs['discuss'] + attribs['caring'])
    points['prssa'] = (subcats['studies'] + attribs['leader'] + attribs['team'] + attribs['extrovert'])
    points['phil'] = (subcats['studies'] + attribs['introspective'] + attribs['discuss'] + attribs['excited'])
    points['nsslha'] = (subcats['studies'] + attribs['helpful'] + attribs['work'] + attribs['mentor'])

    # -- Spiritual --
    points['lds'] = (subcats['spiritual'] + attribs['devout'] + attribs['team'] + attribs['caring'])
    points['fellow'] = (subcats['spiritual'] + attribs['devout'] + attribs['active'] + attribs['hype'])
    points['newman'] = (subcats['spiritual'] + attribs['introspective'] + attribs['team'] + attribs['devout'])
    points['inter'] = (subcats['spiritual'] + attribs['excited'] + attribs['introspective'] + attribs['discuss'])
    points['ssa'] = ((30 - subcats['spiritual']) + attribs['introspective'] + attribs['lax'] + attribs['discuss'])
    points['christ'] = (subcats['spiritual'] + attribs['devout'] + attribs['discuss'] + attribs['introspective'])

    # -- Kindness --
    points['serve'] = (subcats['kindness'] + attribs['helpful'] + attribs['team'] + attribs['aggie'])
    points['rotaract'] = (subcats['kindness'] + attribs['helpful'] + attribs['leader'] + attribs['caring'])
    points['cares'] = (subcats['kindness'] + attribs['caring'] + attribs['aggie'] + attribs['helpful'])
    points['bestbud'] = (subcats['kindness'] + attribs['caring'] + attribs['mentor'] + attribs['aggie'])
    points['gdays'] = (subcats['kindness'] + attribs['helpful'] + attribs['messy'] + attribs['team'])
    points['smile'] = (subcats['kindness'] + attribs['caring'] + attribs['helpful'] + attribs['lax'])

    # -- Political --
    points['grc'] = (subcats['political'] + attribs['leader'] + attribs['discuss'] + attribs['work'])
    points['party'] = (subcats['political'] + attribs['discuss'] + attribs['introspective'] + attribs['team'])
    points['repo'] = (subcats['political'] + attribs['devout'] + attribs['introspective'] + attribs['caring'])

    # Sort
    topCats = sorted(subcats.items(), key=lambda k: k[1], reverse=True)
    topClubs = sorted(points.items(), key=lambda k: k[1], reverse=True)

    # Results
    three = []
    for x in range(3):
        # Get subcat
        picks = names[topCats[x][0]]
        # Get club
        for y in topClubs:
            if y[0] in picks:
                three.append(y[0])
                topClubs.remove(y)
                break
    return three


def allocator(data):
    """ This function takes the orderly list of data and sorts all of the points and whatnot. """
    # Club Setup
    clubNames = {
        'general': ['pcab', 'fees', 'council', 'saa', 'nscsc', 'ento', 'aspire'],
        'medical': ['therapy', 'amsa', 'cadvaer', 'hosa', 'neuro', 'dental', 'pmed', 'nami', 'physass', 'span', 'diet',
                    'milpsych', 'mcat', 'mftsa'],
        'business': ['algo', 'sport', 'nsls', 'bit'],

        'athletic': ['hurd', 'canyon', 'archery', 'yoga', 'trail', 'volley'],
        'arts': ['radio', 'blight', 'series', 'states', 'film', 'bigband', 'cswing', 'star', 'thea'],
        'lifestyle': ['blucru', 'activity', 'trad', 'fsl', 'game', 'paint', 'tennis', 'spike', 'pickle', 'skate',
                      'aikido', 'snow', 'ram'],

        'dei': ['girl', 'ostem', 'transfer', 'story', 'women'],
        'international': ['globcom', 'natstud', 'scandi', 'tagalog', 'russia', 'irish'],
        'studies': ['anthro', 'colstud', 'mun', 'prssa', 'phil', 'nsslha'],

        'spiritual': ['lds', 'fellow', 'newman', 'inter', 'ssa', 'christ'],
        'kindness': ['serve', 'rotaract', 'cares', 'bestbud', 'gdays', 'smile'],
        'political': ['grc', 'party', 'repo']
    }
    clubPoints = {}
    for el in clubNames:
        for name in clubNames[el]:
            clubPoints[name] = random.randrange(1, 9)

    # Data Setup
    email = [data.pop(0)]
    results = []
    subcats = {
        # -Academic-
        'general': 0,
        'medical': 0,
        'business': 0,
        # -Recreation-
        'athletic': 0,
        'arts': 0,
        'lifestyle': 0,
        # -DEI-
        'dei': 0,
        'international': 0,
        'studies': 0,
        # -Service-
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
        'introspective': 0,
        'discuss': 0,
        'lax': 0,
        'outdoors': 0,
        'active': 0,
        'detailed': 0,
        'work': 0,
        'messy': 0,
        'smart': 0,
        'excited': 0,
        'creative': 0,
        'helpful': 0,
        'hype': 0
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
        subcats['athletic'] += 4
        subcats['arts'] += 4
        subcats['lifestyle'] += 3
        subcats['dei'] += 4
        subcats['international'] += 4
        subcats['studies'] += 4
        attribs['extrovert'] += 5
        attribs['aggie'] += 4
        attribs['team'] += 3
        attribs['excited'] += 4
    if 2 in because:
        subcats['dei'] += 4
        subcats['international'] += 4
        subcats['studies'] += 4
        subcats['spiritual'] += 4
        subcats['kindness'] += 5
        subcats['political'] += 4
        attribs['helpful'] += 4
        attribs['mentor'] += 4
        attribs['leader'] += 3
    if 3 in because:
        subcats['general'] += 4
        subcats['medical'] += 4
        subcats['business'] += 5
        attribs['leader'] += 4
        attribs['team'] += 4
        attribs['hype'] += 3
    if 4 in because:
        subcats['general'] += 4
        subcats['medical'] += 4
        subcats['business'] += 4
        subcats['dei'] += 5
        subcats['international'] += 5
        subcats['studies'] += 4
        attribs['devout'] += 3
        attribs['caring'] += 4
        attribs['introspective'] += 2
    if 5 in because:
        subcats['athletic'] += 4
        subcats['arts'] += 4
        subcats['lifestyle'] += 5
        subcats['spiritual'] += 4
        subcats['kindness'] += 4
        subcats['political'] += 4
        attribs['lax'] += 4
        attribs['outdoors'] += 4
        attribs['messy'] += 2
    # Q3: --------------------------------
    subcats['general'] += data[0]
    subcats['medical'] += data[0]
    subcats['business'] += data[0]
    attribs['detailed'] += data[0] * 1.5
    attribs['smart'] += data[0]
    attribs['lax'] -= data[0]
    # Q4: --------------------------------
    subcats['athletic'] += data[1] * 1.5
    subcats['arts'] += data[1] * 0.5
    subcats['lifestyle'] += data[1]
    attribs['aggie'] += data[1] * 1.5
    attribs['extrovert'] += data[1]
    attribs['team'] += data[1] * 0.5
    # Q5: --------------------------------
    subcats['spiritual'] += data[2]
    subcats['kindness'] += data[2] * 1.5
    subcats['political'] += data[2]
    attribs['caring'] += data[2]
    attribs['introspective'] += data[2]
    attribs['leader'] += data[2]
    # ---------Academic Questions---------
    # Q6: -------------------------------- (Kind of a hard question to come up with attribs for. :/)
    subcats['medical'] -= data[3]
    attribs['messy'] += data[3] * 0.5
    attribs['helpful'] -= 1
    attribs['detailed'] += 1
    # Q7: --------------------------------
    subcats['general'] += data[4]
    subcats['business'] += data[4]
    attribs['team'] += data[4] * 1.5
    attribs['detailed'] += data[4]
    attribs['discuss'] += data[4]
    # Q8: --------------------------------
    subcats['business'] += data[5] * 1.5
    attribs['work'] += data[5]
    attribs['leader'] += data[5]
    attribs['team'] += data[5]
    # Q9: --------------------------------
    subcats['medical'] += data[6]
    attribs['detailed'] += data[6]
    attribs['outdoors'] += data[6]
    attribs['introspective'] += data[6] * 0.5
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
    attribs['helpful'] += data[9]
    # Q13: -------------------------------
    subcats['general'] += data[10]
    clubPoints['saa'] += data[10] * 1.5
    attribs['aggie'] += data[10] * 1.5
    attribs['hype'] += data[10] * 0.5
    # Q14: -------------------------------
    if data[11] == 1:
        subcats['general'] += 3
        clubPoints['ento'] += 7
        attribs['caring'] += 3
        attribs['messy'] -= 1
    elif data[11] == 2:
        subcats['general'] += 2
        clubPoints['ento'] += 4
        attribs['work'] += 3
        attribs['messy'] += 2
    elif data[11] == 3:
        subcats['general'] += 2
        clubPoints['ento'] += 2
        attribs['lax'] += 3
        attribs['messy'] += 3
    elif data[11] == 4:
        subcats['general'] -= 2
        clubPoints['ento'] -= 11
        attribs['helpful'] += 2
        attribs['messy'] -= 3
    # Q15: -------------------------------
    subcats['general'] += data[12]
    clubPoints['aspire'] += data[12] * 2
    attribs['smart'] += data[12] * 2
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
    attribs['messy'] += data[13]
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
    attribs['leader'] += data[16] * 1.5
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
        attribs['hype'] += 2
    elif data[18] == 2:
        subcats['lifestyle'] += 3
        attribs['extrovert'] += 4
        attribs['lax'] += 3
        attribs['hype'] += 2
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
    attribs['messy'] += data[19] - 1
    attribs['aggie'] += data[19] * 0.5
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
        attribs['hype'] += 2
    elif data[20] == 4:
        subcats['athletic'] += 3
        attribs['lax'] += 1
        attribs['active'] += 2
    elif data[20] == 5:
        subcats['athletic'] += 3
        attribs['outdoors'] += 4
        attribs['lax'] += 1
    elif data[20] == 6:
        subcats['athletic'] -= 1
        subcats['arts'] -= 1
        subcats['lifestyle'] -= 1
    # ---------Athletic Questions---------
    # Q24: -------------------------------
    subcats['athletic'] += data[21]
    clubPoints['canyon'] += data[21]
    clubPoints['trail'] += data[21]
    attribs['outdoors'] += data[21] * 1.5
    attribs['messy'] += data[21] * 0.5
    # Q25: -------------------------------
    subcats['athletic'] += data[22]
    clubPoints['hurd'] += data[22] * 1.5
    attribs['aggie'] += data[22] * 1.5
    attribs['hype'] += data[22]
    # Q26: -------------------------------
    subcats['athletic'] += data[23]
    clubPoints['spike'] += data[23]
    clubPoints['volley'] += data[23]
    clubPoints['archery'] += 4 - data[23]
    clubPoints['yoga'] += 4 - data[23]
    attribs['messy'] += data[23] * 0.5
    attribs['active'] += data[23] * 1.5
    # -----------Arts Questions-----------
    # Q27: -------------------------------
    subcats['arts'] += data[24]
    clubPoints['thea'] += data[24] * 1.5
    attribs['creative'] += data[24]
    attribs['extrovert'] += data[24] * 0.5
    # Q28: -------------------------------
    if data[25] == 1:
        subcats['arts'] += 3
        clubPoints['states'] += 3
        clubPoints['radio'] += 3
        attribs['detailed'] += 2
        attribs['creative'] += 2
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
        attribs['introspective'] += 1
    elif data[25] == 5:
        subcats['arts'] += 3
        clubPoints['bigband'] += 4
        clubPoints['cswing'] += 4
        attribs['active'] += 3
        attribs['hype'] += 2
    elif data[25] == 6:
        subcats['arts'] -= 2
        attribs['lax'] += 3
    # Q29: -------------------------------
    subcats['arts'] += data[26]
    clubPoints['film'] += data[26]
    clubPoints['star'] += data[26] * 0.5
    attribs['creative'] += data[26] * 0.5
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
    clubPoints['snow'] += data[28] * 1.5
    attribs['outdoors'] += data[28] * 0.5
    attribs['active'] += data[28]
    # Q32: -------------------------------
    subcats['lifestyle'] += data[29]
    clubPoints['aikido'] += data[29]
    clubPoints['paint'] += data[29]
    attribs['active'] += data[29] * 1.5
    attribs['lax'] -= data[29] * 0.5
    # Q33: -------------------------------
    subcats['lifestyle'] += data[30]
    clubPoints['skate'] += data[30] * 1.5
    attribs['outdoors'] += data[30] * 0.5
    attribs['active'] += data[30] * 0.5
    # Q34: -------------------------------
    subcats['lifestyle'] += data[31]
    clubPoints['blucru'] += data[31]
    clubPoints['activity'] += data[31]
    clubPoints['trad'] += data[31]
    clubPoints['fsl'] += data[31]
    attribs['aggie'] += data[31]
    attribs['hype'] += data[31]
    # --------Humanities Questions--------
    # Q35: -------------------------------
    subcats['dei'] += data[32]
    subcats['international'] += data[32]
    attribs['discuss'] += data[32]
    attribs['excited'] += data[32] * 0.5
    # Q36: -------------------------------
    subcats['dei'] += data[33] * 1.5
    subcats['political'] += data[33]  # (not technically in this category, but it felt good to add here)
    attribs['helpful'] += data[33]
    attribs['excited'] += data[33]
    attribs['leader'] += data[33] * 0.5
    # Q37: -------------------------------
    subcats['studies'] += data[34]
    attribs['lax'] += data[34] * 0.5
    attribs['smart'] -= data[34] * 0.5
    # Q38: -------------------------------
    subcats['international'] += data[35]
    subcats['studies'] += data[35]
    attribs['discuss'] += data[35]
    attribs['excited'] += data[35]
    attribs['extrovert'] += data[35]
    # ---------Diversity Questions--------
    # Q39: ------------------------------- (this one is weird since it should primarily just be transfer students, but I don't want to figure out how to make it *only* transfer students right now.)
    subcats['dei'] += data[36] * 0.5
    clubPoints['transfer'] += data[36] * 0.5
    attribs['aggie'] += data[36]
    attribs['excited'] += data[36] * 0.5
    if data[36] > 2:
        clubPoints['transfer'] += data[36] * 2
    else:
        clubPoints['transfer'] -= 30 # they absolutely should not get this unless they're a transfer student
    # Q40: -------------------------------
    subcats['dei'] += data[37]
    clubPoints['girl'] += data[37]
    clubPoints['story'] += data[37]
    attribs['excited'] += data[37]
    attribs['discuss'] += data[37]
    # Q41: -------------------------------
    subcats['dei'] += data[38]
    clubPoints['ostem'] += data[38]
    clubPoints['women'] += data[38]
    attribs['aggie'] += data[38] * 0.5
    attribs['work'] += data[38]
    if data[38] > 2:
        clubPoints['ostem'] += 5
        clubPoints['women'] += 5
    # -------International Questions------
    # Q42: -------------------------------
    subcats['international'] += data[39]
    clubPoints['globcom'] += data[39]
    clubPoints['natstud'] += data[39]
    attribs['smart'] += data[39]
    attribs['excited'] += data[39]
    # Q43: -------------------------------
    subcats['international'] += data[40]
    clubPoints['irish'] += data[40] * 1.5
    attribs['excited'] += data[40]
    # Q44: -------------------------------
    subcats['international'] += data[41]
    clubPoints['scandi'] += data[41]
    clubPoints['russia'] += data[41]
    attribs['outdoors'] += data[41] * 0.5
    attribs['excited'] += data[41]
    # Q45: -------------------------------
    subcats['international'] += data[42]
    clubPoints['tagalog'] += data[42] * 1.5
    attribs['smart'] += data[42]
    attribs['work'] += data[42] * 0.5
    # ----------Studies Questions---------
    # Q46: -------------------------------
    subcats['studies'] += data[43]
    clubPoints['anthro'] += data[43]
    attribs['smart'] += data[43]
    attribs['discuss'] += data[43]
    # Q47: -------------------------------
    subcats['studies'] += data[44]
    clubPoints['mun'] += data[44]
    clubPoints['prssa'] += data[44]
    attribs['helpful'] += data[44] * 0.5
    attribs['leader'] += data[44] * 0.5
    # Q48: -------------------------------
    subcats['studies'] += data[45]
    clubPoints['colstud'] += data[45]
    clubPoints['phil'] += data[45]
    attribs['introspective'] += data[45]
    attribs['discuss'] += data[45]
    # Q49: -------------------------------
    subcats['studies'] += data[46]
    clubPoints['nsslha'] += data[46]
    attribs['helpful'] += data[46]
    attribs['mentor'] += data[46]
    # ----------Service Questions---------
    # Q50: -------------------------------
    subcats['spiritual'] += data[47] * 1.5
    attribs['devout'] += data[47]
    attribs['introspective'] += data[47]
    attribs['caring'] += data[47] * 0.5
    # Q51: -------------------------------
    subcats['political'] += data[48]
    attribs['smart'] += data[48]
    attribs['detailed'] += data[48]
    attribs['discuss'] += data[48]
    # Q52: -------------------------------
    if data[49] == 1:
        subcats['kindness'] += 3
        attribs['extrovert'] -= 2
        attribs['helpful'] += 2
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
        attribs['helpful'] -= 2
        attribs['team'] -= 1
    # Q53: -------------------------------
    for x in range(7):
        choice = (7 - data.pop(50))+1
        if x == 1:
            subcats['spiritual'] += choice
            attribs['devout'] += choice
            attribs['introspective'] += choice * 0.5
        elif x == 2:
            subcats['political'] += choice
            attribs['discuss'] += choice
            attribs['devout'] += choice * 0.5
        elif x == 3:
            subcats['general'] += choice
            subcats['medical'] += choice
            subcats['business'] += choice
            attribs['smart'] += choice
            attribs['work'] += choice
            attribs['mentor'] += choice
        elif x == 4:
            subcats['medical'] += choice
            attribs['outdoors'] += choice
            attribs['active'] += choice
        elif x == 5:
            subcats['lifestyle'] += choice
            subcats['kindness'] += choice
            subcats['dei'] += choice * 0.5
            attribs['extrovert'] += choice
            attribs['caring'] += choice
        elif x == 6:
            subcats['athletic'] += choice
            subcats['general'] += choice * 0.5
            attribs['aggie'] += choice * 1.5
            attribs['mentor'] += choice * 0.5
        elif x == 7:
            subcats['dei'] += choice
            subcats['international'] += choice
            subcats['spiritual'] += choice
            attribs['introspective'] += choice
            attribs['devout'] += choice * 0.5
    # ---------Spiritual Questions--------
    # Q54: -------------------------------
    if data[50] == 1:
        subcats['spiritual'] += 3
        clubPoints['lds'] += 15
        attribs['devout'] += 3
        attribs['extrovert'] += 2
    elif data[50] == 2:
        subcats['spiritual'] += 3
        clubPoints['christ'] += 15
        attribs['devout'] += 3
        attribs['introspective'] += 2
    elif data[50] == 3:
        subcats['spiritual'] += 3
        clubPoints['newman'] += 15
        attribs['devout'] += 3
        attribs['team'] += 2
    elif data[50] == 4:
        subcats['spiritual'] += 1
        clubPoints['ssa'] += 15
        attribs['devout'] -= 1
        attribs['discuss'] += 3
    elif data[50] == 5:
        subcats['spiritual'] += 3
        clubPoints['inter'] += 5
        attribs['introspective'] += 2
    elif data[50] == 6:
        subcats['spiritual'] -= 3
        clubPoints['inter'] -= 3
        attribs['excited'] -= 1
    # Q55: -------------------------------
    subcats['spiritual'] += data[51]
    attribs['devout'] += (data[51] / 2)
    attribs['introspective'] += (data[51] / 2)
    # Q56: -------------------------------
    clubPoints['inter'] += data[52] + 1
    attribs['discuss'] += data[52] + 1
    attribs['introspective'] += data[52]
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
        attribs['introspective'] += 2
    if 2 in service:
        subcats['kindness'] += 3
        clubPoints['bestbud'] += 3
        attribs['caring'] += 3
        attribs['mentor'] += 2
    if 3 in service:
        subcats['kindness'] += 3
        clubPoints['smile'] += 3
        attribs['caring'] += 3
        attribs['active'] += 1
    if 4 in service:
        subcats['kindness'] += 3
        clubPoints['rotaract'] += 3
        clubPoints['gdays'] += 3
        attribs['caring'] += 3
        attribs['excited'] += 1
    # Q59: -------------------------------
    subcats['kindness'] += data[54]
    clubPoints['rotaract'] += data[54] * 0.5
    clubPoints['cares'] += data[54]
    clubPoints['serve'] += data[54]
    attribs['caring'] += data[54] * 0.5
    attribs['aggie'] += data[54] * 0.5
    attribs['leader'] += data[54]
    # ---------Political Questions--------
    # Q60: -------------------------------
    subcats['political'] += data[55]
    clubPoints['party'] += data[55]
    attribs['discuss'] += data[55]
    attribs['caring'] += data[55] * 0.5
    attribs['devout'] += data[55]
    # Q61: -------------------------------
    subcats['political'] += data[56]
    clubPoints['grc'] += data[56] * 1.5
    attribs['discuss'] += data[56]
    attribs['leader'] += data[56]
    attribs['work'] += data[56] * 0.5
    # Q62: -------------------------------
    subcats['political'] += data[57]
    clubPoints['repo'] += data[57] * 1.5
    attribs['devout'] += data[57]
    attribs['discuss'] += data[57]
    attribs['caring'] += data[57] * 0.5
    # END ----------------------------------------------
    # Results
    return colleges + email + generateThree(subcats, attribs, clubNames, clubPoints)
