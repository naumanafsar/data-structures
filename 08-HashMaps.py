class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [ None ] * self.size
    
def _get_hash(self, key):
    if type(key) is str:
        return len(key) % self.size
    elif type(key) is int:
        return key % self.size
    else:
        tuple_key = key[0] + key[1]
        return tuple_key % self.size
HashMap._get_hash = _get_hash

def get(self, key):
    key_hash = self._get_hash(key)
    
    if self.map[key_hash] is not None:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]
    raise KeyError(str(key))
HashMap.get = get

def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]
    
    if self.map[key_hash] is None:
        self.map[key_hash] = [key_value]
        return True
    else:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.map[key_hash].append(key_value)
        return True

HashMap.add = add

def delete(self, key):
    key_hash = self._get_hash(key)
    
    if self.map[key_hash] is None:
        return KeyError(str(key))
    
    for i in range(0, len(self.map[key_hash])):
        if self.map[key_hash][i][0] == key:
            self.map[key_hash].pop(i)
            return True
HashMap.delete = delete

def __str__(self):
    ret = " "
    for i, item in enumerate(self.map):
        if item is not None:
            ret += str(i) + ": " + str(item) + "\n"
    return ret
HashMap.__str__ = __str__


if __name__ == '__main__': 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")

    print(h)
