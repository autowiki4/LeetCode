import random

class RandomizedCollection:

    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.indices[val] = set()
        
        self.indices[val].add(len(self.arr))
        self.arr.append(val)
        
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.indices or len(self.indices[val]) == 0:
            return False
        idx_to_remove = self.indices[val].pop()
        last_element = self.arr[-1]
        
        self.arr[idx_to_remove] = last_element
        
        self.indices[last_element].add(idx_to_remove)
        self.indices[last_element].remove(len(self.arr) - 1)
        
        
        self.arr.pop()
        
        if len(self.indices[val]) == 0:
            del self.indices[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()