class HashSet:
    def __init__(self, n=1000):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.key_value = list()
        for idx in range(self.n):
            self.key_value.append([idx])

    def _hash(self, value):
        return value % self.n

    def add(self, value):
        """
        :type value: int
        :rtype: void
        """
        hash_value = self._hash(value)
        if self.contains(value):
            print("Duplicate Insert of {0}".format(value))
        else:
            self.key_value[hash_value].append(value)

    def remove(self, value):
        """
        :type value: int
        :rtype: void
        """
        hash_value = self._hash(value)
        if self.contains(value):
            self.key_value[hash_value].remove(value)
        else:
            print("{0} is not present in the HashSet.".format(value))

    def contains(self, value):
        """
        Returns true if this set contains the specified element
        :type value: int
        :rtype: bool
        """
        hash_value = self._hash(value)
        if value in self.key_value[hash_value][1:]:
            return True
        else:
            return False

'''
# Your MyHashSet object will be instantiated and called as such:
obj = HashSet()
obj.add(1)
obj.add(1001)
obj.remove(1)
param_3 = obj.contains(1001)
print(param_3)
'''
