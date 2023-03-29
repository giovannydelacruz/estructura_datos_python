import random
from functools import reduce

class Array_Reto:
    def __init__(self, capacity, fill_value=None): # Su capacidad siempre es definida desde un principio y no podrá ser cambiada.
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __randReplace__(self, start, final):
        return [self.__setitem__(i,random.randint(start, final)) for i in range(self.__len__)]
    
    def __sum__(self):
        return reduce(lambda start, finish: start+finish, self.items)

        