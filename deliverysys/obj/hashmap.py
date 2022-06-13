class Hashmap:
    def __init__(self, startsize):
        self.map = []

        for i in range(startsize):
            self.map.append([])

    # Get hash value from given key
    # O(1)
    def _get_hash(self, key):
        hash = key % len(self.map)

        return hash

    # Add new element to map
    # O(1)
    def insert(self, key, item):
        key_hash = self._get_hash(key)
        self.map[key_hash] = [key, item]

        return True

    # Remove element from hashmap
    # O(1)
    def remove(self, key):
        key_hash = self._get_hash(key)
        bucket = self.map[key_hash]

        if bucket[0] == key:
            bucket.remove(key_hash)

    # Find element with matching key
    # O(1)
    def search(self, key):
        key_hash = self._get_hash(key)
        bucket = self.map[key_hash]

        if bucket[0] == key:
            return bucket[1]

        return None

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.map):
            val = self.map[self.n]

            self.n += 1

            return val
        else:
            raise StopIteration

    def __len__(self):
        return len(self.map)
