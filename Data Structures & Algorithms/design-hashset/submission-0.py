
class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert a value
    def add(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for value in bucket:
            if value == key:
                return

        bucket.append(key)

    # Check whether value exists
    def contains(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for value in bucket:
            if value == key:
                return True

        return False

    # Remove a value
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                return
