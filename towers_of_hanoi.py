class TowersOfHanoi(object):

    def __init__(self, num_disks):
        letters = list('abcdefghijklmnopqrstuvwxyz'.upper())
        self.towers = [[] for _ in range(3)]
        if num_disks <= len(letters):
            self.towers[0] = letters[:num_disks][::-1]
        else:
            self.towers[0] = range(num_disks, 0, -1)
        self.move(num_disks, atPosition=0, left=True)
        print(self.tower_string)

    def move(self, num_disks, atPosition, left):
        if not num_disks:
            return

        target_position = (atPosition + (-1 if left else 1)) % 3
        aux_position = (atPosition + (1 if left else -1)) % 3

        self.move(num_disks - 1, atPosition, not left)

        print('{} {} {}'.format(
            self.tower_string, self.towers[atPosition][-1], 'left' if left else 'right')
        )
        self.towers[target_position].append(self.towers[atPosition].pop())

        self.move(num_disks - 1, aux_position, not left)

    @property
    def tower_string(self):
        tower_strings = map(lambda disks: ''.join(map(str, disks)), self.towers)
        return ' '.join(map(lambda tower:'({})'.format(tower), tower_strings))


