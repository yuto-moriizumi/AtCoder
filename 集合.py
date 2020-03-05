class Set:
    index = 0
    toOrigin = list()
    toBit = dict()

    def __init__(self, iterable):
        super().__init__()
        self.bit = 0
        for i in iterable:
            self.bit = self.bit | 1 << self.convertBit(i)

    @classmethod
    def convertBit(cls, item):
        if cls.toBit.get(item, -1) != -1:
            return cls.toBit[item]
        cls.toOrigin.append(item)
        cls.toBit[item] = cls.index
        cls.index += 1
        return cls.index - 1

    @classmethod
    def createFromBit(cls, bit):
        SET = cls()
        SET.bit = bit
        return SET

    def add(self, item):
        self.bit = self.bit | 1 << self.convertBit(item)

    def __str__(self):
        return bin(s.bit)

    def toOriginSet(self):
        s = set()
        for i in range(self.index):
            if (self.bit >> i) & 1 == 1:
                s.add(self.toOrigin[i])
        return s

    def __len__(self):
        return bin(self.bit).count('1')

    def __add__(self, other):
        return self.bit | other.bit


s = Set([1, 2, 3])
print(s.bit)
s.add(6)
print(s.bit)
s.add(6)
print(s.bit)
print(s)
print(s.toOriginSet())
print(len(s))
