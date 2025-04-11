things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'
def p():
    print(things)
    things = list(things)
    print(things)

    for i in things:
        print(i)
    for i, j in enumerate(things):
        print(i, j)
