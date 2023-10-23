class cui_game:
    def __init__(self):
        self.root = "+----------------------------------------------------------------+\n"+("+"+("".ljust(64,' '))+"+\n")*12+"+----------------------------------------------------------------+"
        self.name = "cui_game"
    def strset(self,*str):
        self.root = self.root[:67]
        self.root += "+" + self.name.ljust(64," ") + "+\n"
        for i in range(11):
            try:
                self.root += "+" +str[i].ljust(64," ") + "+\n"
            except IndexError:
                self.root += "+" + 64*" " + "+\n"
        self.root += "+----------------------------------------------------------------+"