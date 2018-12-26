class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def hash_(key, TABLESIZE):
    total = 0
    for c in key:
        key_num = ord(c)
        total += key_num
    return total % TABLESIZE


class HashTable:
    TABLESIZE = 20

    def __init__(self):
        # self.list = [0] * self.TABLESIZE
        self.list = [[] for _ in range(0, self.TABLESIZE)]

    def get(self, key):
        index = hash_(key, self.TABLESIZE)
        # collision non-aware
        # return self.list[index]
        key_val = next((e for e in self.list[index] if e.key == key), None)
        return key_val.value

    def set(self, key, value):
        index = hash_(key, self.TABLESIZE)

        # collision non-aware
        # self.list[index] = value
        key_val = KeyValue(key, value)
        self.list[index].append(key_val)
        pass


hashTable = HashTable()
hashTable.set("hello", "hola")
hashTable.set("helol", "hoal")
assert hashTable.get("hello") == 'hola'
assert hashTable.get("helol") == 'hoal'
