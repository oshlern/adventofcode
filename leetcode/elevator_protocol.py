class Dinglemouse(object):
    def __init__(self, queues, capacity):
        self.q = {
            "UP":   [[x for x in q if x>f] for f,q in enumerate(queues)],
            "DOWN": [[x for x in q if x<f] for f,q in enumerate(queues)]
        }
        self.capacity = capacity
        self.passengers = []
        self.stopped = [0]
        self.floor = 0
        self.dir = "UP"

    def theLift(self):
        finished = False
        while not finished:
            finished = self.move() == "FINISHED"
        return self.stopped
    
    def move(self):
        if self.should_stop(): self.stop()
        if not self.passengers: # empty
            self.dir = self.next_dir()
            if self.should_stop(): self.stop()
        if self.finished():
            return "FINISHED"
        else:
            self.floor = self.floor + (1 if self.dir == "UP" else -1)
        
    def stop(self):
        if not self.stopped or self.stopped[-1] != self.floor:
            self.stopped.append(self.floor)
        self.disembark()
        self.board()

    def should_stop(self):
        if self.finished(): return True
        disembarking = self.floor in self.passengers
        boarding = bool(self.q[self.dir][self.floor])
        return disembarking or boarding

    def disembark(self):
        self.passengers = [p for p in self.passengers if p != self.floor]

    def board(self):
        q = self.q[self.dir][self.floor]
        n_boarding = min(self.capacity - len(self.passengers), len(q))
        self.passengers += q[:n_boarding]
        q[:] = q[n_boarding:]

    def next_dir(self):
        if self.passengers:
            return self.dir
        if not (any(self.q["UP"]) or any(self.q["DOWN"])):
            return "DOWN"

        match self.dir:
            case "UP":
                awaiting_ahead = any(self.q["UP"][self.floor+1:]) or any(self.q["DOWN"][self.floor+1:])
                OP = "DOWN"
            case "DOWN":
                awaiting_ahead = any(self.q["UP"][:self.floor]) or any(self.q["DOWN"][:self.floor])
                OP = "UP"
        if awaiting_ahead:
            return self.dir
        else:
            return OP

    def finished(self):
        return not (any(self.q["UP"]) or any(self.q["DOWN"])) and not self.passengers and self.floor == 0