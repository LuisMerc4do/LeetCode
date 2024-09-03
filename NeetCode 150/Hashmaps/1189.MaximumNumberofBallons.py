def maxNumberOfBalloons(text):
    ballonset = set("balloon")
    counter = {}
    for i in text:
        if i in ballonset:
            counter[i] += 1
        else:
            counter[i] = 1
    if counter != ballonset:
        return True
    
maxNumberOfBalloons("loonbalxballpoon")