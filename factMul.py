



class Mul:

    def __init__(self, val):

        self.val = val
        self.val2 = 0

    def factByFor(self):

        for i in range(1, self.val):
            self.val = self.val*i
        return self.val

    def factByWhile(self):

        self.val2 = self.val-1
        while self.val2 > 1:
            self.val *= self.val2 #Is eequal to self.val = self.val*self.val2
            self.val2 -= 1
        return self.val

def main():

    mul = Mul(9)
    mul.factByWhile()
    print(mul.val)

main()
