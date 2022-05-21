import dictionary as dict


class cmd:
    total = []

    def __init__(self, words):
        self.words = words.split()
        self.op = ''
        self.per = 0
        self.call = 0
        cmd.total.append(self)
