

#(1) (log n) (n) (n log n) (n^2) (n^3).....

#Big O notation (n^2)
lstofcards = ['d', 's', 'c', 'h']

lstofvalues = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

cards = []

def cardDeal():

    for suit in lstofcards:
        for val in lstofvalues:
            cards.append((suit+val))
    print(cards)

cardDeal()
