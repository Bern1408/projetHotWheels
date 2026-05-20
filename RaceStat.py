class RaceStat:
    def __init__(self, id, time, state, c1, c2, c3, c4):
        self.id = id
        self.time = time
        self.state = state
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

    def setId(self, id):
        self.id = id

    def setTime(self, time):
        self.time = time

    def setState(self, state):
        self.state = state
    
    def setC(self, i, time):
        if i == 1:
            self.c1 = time
        if i == 2:
            self.c2 = time
        if i == 3:
            self.c3 = time
        if i == 4:
            self.c4 = time

    def toString(self):
        return ("{'id':'" + self.id + "', 'timeDepart':'" + self.time + ", 'state':'" + self.state + "', 'c1':'" + self.c1 + "', 'c2':'" + self.c2 + "', 'c3':'" + self.c3 + "', 'c4':'" + self.c4 + "'}")
