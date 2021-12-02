def generateResults(subcats, attribs):
    """ This function takes the point totals and determines the top five clubs. """

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
    results.append(colleges)

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
        subcats['']


    # Results
    return generateResults(subcats, attribs)