class Log:
    def __init__(self, position, classname):
        self.position = position
        self.classname = classname

    def __str__(self):
        return str(self.position) + " " + str(self.classname)

    def __lt__(self, other):
        return self.position < other.position
