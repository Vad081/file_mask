class MaskItem(object):
    def __init__(self,mask=0):
        self.mask = mask
    # read = 0b100
    # write = 0b010
    # execute = 0b001

    def is_readable(self):
        return bool(self.mask & 0b100)

    def is_writable(self):
        return bool(self.mask & 0b010)

    def is_executable(self):
        return bool(self.mask & 0b001)

    def __str__(self):
        return f'{"r" if self.is_readable() else "-"}{"w" if self.is_writable() else "-"}{"x" if self.is_executable() else "-"}'

    def __repr__ (self):
        return f'MaskItem({bin(self.mask) if self.mask else ""})'

class Mask(object):
    def __init__(self, author, group, other):
        self.author = author
        self.group = group
        self.other = other

    def __str__(self):
        return f'{self.author}{self.group}{self.other}'


    def __repr__(self):
        return f'Mask({self.author.__repr__()}, {self.group.__repr__()}, {self.other.__repr__()})'
