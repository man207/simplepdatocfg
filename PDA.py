import itertools as it


class pushdownautomata():
    def __init__(self,states = [],symbols = [],initialstate = "",finalstates = [],stsymbols = []):
        self.states = states
        self.symbols = symbols
        self.stsymbols = stsymbols
        self.initialstate = initialstate
        self.finalstates = finalstates
        self.transistions = []
    def addsymbol(self , symbol):
        if symbol not in self.symbols:
            self.symbols.append(symbol)
    def addstacksymbol(self , symbol):
        if symbol not in self.stsymbols:
            self.stsymbols.append(symbol)

    def addfinalstate(self,finalstate):
        if finalstate not in self.finalstates:
            self.finalstates.append((finalstate))

    def setinitialstate(self,initialstate):
        self.initialstate = (initialstate)
        if initialstate not in self.states:
            self.states.insert(0,initialstate)
        else:
            self.states.remove(initialstate)
            self.states.insert(0,initialstate)

    def addtransistion(self,transistion):
        if transistion not in self.transistions:
            self.transistions.append(transistion)

        if transistion[0] not in self.states:
            self.states.append((transistion[0]))

        if transistion[3] not in self.states:
            self.states.append((transistion[3]))

        if transistion[2] not in self.stsymbols:
            if transistion[2] != "λ":
                self.stsymbols.append((transistion[2]))

        if transistion[4] not in self.stsymbols:
            if transistion[4] != "λ":
                self.stsymbols.append((transistion[4]))

        if transistion[1] not in self.symbols:
            if transistion[1] != "λ":
                self.symbols.append((transistion[1]))

        if transistion not in self.transistions:
            self.transistions.append(transistion)
    def standardlize(self):
        todo = []
        for transistion in self.transistions:
            if transistion[2] == "λ":
                for alphabet in self.stsymbols:
                    newalphabet = transistion[4] + (alphabet)
                    todo.append([transistion[0],transistion[1],alphabet,transistion[3],newalphabet])
        for that in todo:
            self.addtransistion(that)

    def toCFG(self):
        dacgf = []
        self.standardlize()
        for state in self.finalstates:
            rule = ["S",(self.initialstate,"λ",state)]
            dacgf.append(rule)
            
        for state in self.states:
            rule = [(state,"λ",state),"λ"]
            dacgf.append(rule)

        for transistion in self.transistions:
            prodcuts = it.product(self.states,repeat = len(transistion[4]))
            for stuff in prodcuts:
                rule = [(transistion[0],transistion[2],stuff[-1])]
                if transistion[1] != "λ":
                    rule.append(transistion[1])
                stuff = list(stuff)
                stuff.insert(0,transistion[3])
                for i,item in enumerate(transistion[4]):
                    rule.append((stuff[i],item,stuff[i+1]))
                dacgf.append(rule)
        return dacgf
ff = pushdownautomata()
ff.addtransistion(["s","l","λ","s","X"])
ff.addtransistion(["s","r","X","s","λ"])
ff.setinitialstate("s")
ff.addfinalstate("s")
jj = ff.toCFG()
print(ff.symbols)
print(ff.stsymbols)
print(ff.finalstates)
for s in jj:
    print(s)
