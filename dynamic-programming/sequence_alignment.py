class Sequence_Alignment(object):

    def __init__(self, string1, string2):
        self.string1, self.string2 = string1, string2
        self._GAP_COST = 1
        self._GAP_CHAR = " "
        self.__cost_table = self.__make_cost_table(string1, string2)

    @property
    def cost(self):
        return self.__cost_table[-1][-1]

    @property
    def alignment(self):
        return self.__get_alignment_from_table(self.__cost_table)

    def __make_cost_table(self, string1, string2):
        n, m = len(string1), len(string2)
        table = [[i + j for j in range(m + 1)] 
                 for i in range(n + 1)]

        for i, char1 in zip(range(1, n + 1), string1):
            for j, char2 in zip(range(1, m + 1), string2):
                cost = 0 if char1 == char2 else 1
                table[i][j] = min(table[i - 1][j - 1] + cost,
                                  table[i - 1][j] + self._GAP_COST,
                                  table[i][j - 1] + self._GAP_COST)
        return table

    def __get_alignment_from_table(self, table):
        i, j = len(self.string1), len(self.string2)
        aligned1, aligned2 = [], []
        while i or j:
            if (i and j and
               table[i - 1][j - 1] <= table[i - 1][j] and
               table[i - 1][j - 1] <= table[i][j - 1]):
                aligned1.append(self.string1[i - 1])
                aligned2.append(self.string2[j - 1])
                i, j = i - 1, j - 1
            elif not j or table[i - 1][j] <= table[i][j - 1]:
                aligned1.append(self.string1[i - 1])
                aligned2.append(self._GAP_CHAR)
                i -= 1
            else:
                aligned1.append(self._GAP_CHAR)
                aligned2.append(self.string2[j - 1])
                j -= 1

        return ''.join(reversed(aligned1)), ''.join(reversed(aligned2))


def unit_test():
    sa = Sequence_Alignment('bee', 'bee')
    assert sa.cost == 0

    sa = Sequence_Alignment('bee', '')
    assert sa.cost == 3

    sa = Sequence_Alignment('flow', 'cow')
    assert sa.cost == 2
    assert sa.alignment == ("flow", " cow",)

    sa = Sequence_Alignment('flower', 'tower')
    assert sa.cost == 2
    assert sa.alignment == ("flower", " tower")

    sa = Sequence_Alignment('wisdom', 'whiskey')
    assert sa.alignment == ('w isdom', 'whiskey')
    assert sa.cost == 4

    return "unit_test pass"


if __name__ == "__main__":
    print(unit_test())
