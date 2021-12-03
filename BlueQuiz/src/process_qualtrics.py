def generateResults(subcats, attribs):
    """ This function takes the point totals and determines the top five clubs. """
    # Setup
    clubNames = {
        'general': ['pcab', 'fees', 'saa', 'council', 'nscsc'],
        'medical': ['therapy', 'amsa', 'cadvaer', 'hosa', 'neuro', 'dental', 'pmed', 'physass', 'spmed', 'diet'],
        'humanities': ['anthro', 'milpsych', 'globcom', 'colstud', 'natstud', 'mun', 'prssa'],
        'business': ['finance', 'sport', 'nsls'],
        'etc': ['aspire', 'ram'],
        'athletic': ['hurd', 'canyon', 'archery', 'yoga', 'trail'],
        'arts': ['radio', 'blight', 'series', 'film', 'irish', 'bigband', 'cswing'],
        'lifestyle': ['blucru', 'activity', 'trad', 'fsl', 'game', 'paint', 'tennis', 'spike'],
        'dei': ['girl', 'nami', 'ostem', 'scandi', 'tagalog', 'transfer'],
        'spiritual': ['lds', 'colchrist', 'fellow', 'goldcity', 'varsity', 'navi', 'newman', 'ratio', 'inter', 'ssa'],
        'kindness': ['serve', 'rotaract', 'cares', 'bestbud', 'gdays'],
        'political': ['dems', 'ydsa', 'surf']
    }
    clubPoints = {}
    for el in clubNames:
        for name in clubNames[el]:
            clubPoints[name] = 0

    # Assign Points
    clubPoints['pcab'] =
    clubPoints['fees'] = 
    clubPoints['saa'] = 
    clubPoints['council'] = 
    clubPoints['nscsc'] =
    clubPoints['therapy'] =
    clubPoints['amsa'] =
    clubPoints['cadaver'] =
    clubPoints['hosa'] =
    clubPoints['neuro'] =
    clubPoints['dental'] =
    clubPoints['pmed'] =
    clubPoints['physass'] =
    clubPoints['spmed'] =
    clubPoints['diet'] =
    clubPoints['anthro'] =
    clubPoints['milpsych'] =
    clubPoints['glocom'] =
    clubPoints['colstud'] =
    clubPoints['natstud'] =
    clubPoints['mun'] =
    clubPoints['prssa'] =
    clubPoints['finance'] =
    clubPoints['sport'] =
    clubPoints['nsls'] =
    clubPoints['aspire'] =
    clubPoints['ram'] =
    clubPoints['hurd'] = 
    clubPoints['canyon'] =
    clubPoints['archery'] =
    clubPoints['yoga'] =
    clubPoints['trail'] =
    clubPoints['radio'] = 
    clubPoints['blight'] =
    clubPoints['series'] =
    clubPoints['film'] =
    clubPoints['irish'] = 
    clubPoints['bigband'] = 
    clubPoints['cswing'] = 
    clubPoints['blucru'] = 
    clubPoints['activity'] =
    clubPoints['trad'] = 
    clubPoints['fsl'] = 
    clubPoints['game'] =
    clubPoints['paint'] =
    clubPoints['tennis'] =
    clubPoints['spike'] =
    clubPoints['girl'] =
    clubPoints['nami'] =
    clubPoints['ostem'] =
    clubPoints['scandi'] =
    clubPoints['tagalog'] =
    clubPoints['transfer'] =
    clubPoints['lds'] =
    clubPoints['colchrist'] =
    clubPoints['fellow'] =
    clubPoints['goldcity'] =
    clubPoints['varsity'] =
    clubPoints['navi'] =
    clubPoints['newman'] =
    clubPoints['ratio'] =
    clubPoints['inter'] =
    clubPoints['ssa'] =
    clubPoints['serve'] =
    clubPoints['rotaract'] =
    clubPoints['cares'] =
    clubPoints['bestbud'] =
    clubPoints['gdays'] =
    clubPoints['dems'] =
    clubPoints['ydsa'] =
    clubPoints['surf'] =

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
            picks = clubNames[topCats[0]] # Does the top subcat twice
        else:
            picks = clubNames[topCats.pop(0)]
        # Get Club
        for y in topClubs:
            if y in picks:
                five.append(y)
                topClubs.remove(y)
                break;
    return five

def allocator(data):
    """ This function takes the orderly list of data and sorts all of the points and whatnot. """
    # Setup
    data.pop(0) # Unnecessary email data
    results = []
    subcats = {
        'general': 0,
        'medical': 0,
        'humanities': 0,
        'business': 0,
        'etc': 0,
        'athletic': 0,
        'arts': 0,
        'lifestyle': 0,
        'dei': 0,
        'spiritual': 0,
        'kindness': 0,
        'political': 0
    }
    attribs = {
        'leader': 0,
        'helpful': 0,
        'project': 0,
        'detail': 0,
        'political': 0,
        'aggie': 0,
        'planner': 0,
        'extroverted': 0,
        'creative': 0,
        'spirit': 0,
        'athletic': 0,
        'academic': 0,
    }

    # College Collection
    colleges = []
    for x in range(10):
        if (data.pop(0) > 0)
            colleges.append(x+1)

    # Point Allocation
    # Q2: --------------------------------
    because = []
    for x in range(5):
        if (data.pop(0) > 0)
            because.append(x+1)
    if 1 in because:
        subcats['athletic'] += 2
        subcats['arts'] += 2
        subcats['lifestyle'] += 3
        attribs['extroverted'] += 3
        attribs['leader'] += 2
    elif 2 in because:
        subcats['spiritual'] += 2
        subcats['kindness'] += 3
        subcats['political'] += 2
        attribs['helpful'] += 3
        attribs['leader'] += 2
    elif 3 in because:

    # Results
    return colleges + generateResults(subcats, attribs)