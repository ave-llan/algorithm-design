class HashSet(object):

    def __init__(self, modulo=31):
        self.M = modulo
        self.table = [[] for _ in range(modulo)]

    def insert(self, s):
        row = self.table[self.__hash(s)]
        if s not in row:
            row.append(s)

    def contains(self, s):
        return s in self.table[self.__hash(s)]

    def __hash(self, s):
        R = 1 << 8
        hash = 0
        for char in s:
            hash = (hash * R + ord(char)) % self.M
        return hash

def unit_test():
    h = HashSet()
    assert not h.contains('flower')
    h.insert('flower')
    assert h.contains('flower')
    flower_types = ['tulip', 'daisy', 'rose', 'violet', 'bloodroot', 'bleeding heart']
    map(h.insert, flower_types)
    assert all(map(h.contains, flower_types))
    assert not h.contains("sassafras")
    print(h.table)
    return "unit_test pass"

if __name__ == "__main__":
    print(unit_test())