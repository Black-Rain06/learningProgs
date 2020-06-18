class Cards:


    def __init__(self, lstofCards = ['d', 's', 'c', 'h']): #initializes the class Cards

        self.lstofCards = lstofCards
        self.card = []
        self.newlst = []

    def assignVal(self, maxValofSet): #assigns value to suits

        for i in self.lstofCards:
            for j in range(1, maxValofSet+1):
                self.newlst.append((i+str(j)))
        return self.newlst
                
                
                #self.card.append(

        
lstofcard = ['d', 's', 'c', 'h']

lstofvalue = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

card = []

def cardDeal():

    for suit in lstofcard:
        for val in lstofvalue:
            card.append((suit+val))
    return card

def main():

    c = Cards()
    c.assignVal(13)

    cd = cardDeal()

    if c.newlst == cd:
        print('true')



main()
