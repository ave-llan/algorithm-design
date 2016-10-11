class Sequence_Alignment(object):

    def __init__(self, string1, string2):
        self._GAP_COST = 1
        self.__cost_table = self.__make_cost_table(string1, string2)

    @property
    def cost(self):
        return self.__cost_table[-1][-1]

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

def unit_test():
    sa = Sequence_Alignment('bee', 'bee')
    assert sa.cost == 0

    sa = Sequence_Alignment('bee', '')
    assert sa.cost == 3

    sa = Sequence_Alignment('flow', 'cow')
    assert sa.cost == 2
    return "unit_test pass"

    sa = Sequence_Alignment('flower', 'tower')
    assert sa.cost == 2

    sa = Sequence_Alignment('wisdom', 'whiskey')
    assert sa.cost == 0

if __name__ == "__main__":
    print(unit_test())
