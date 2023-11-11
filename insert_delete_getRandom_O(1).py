#10 mins
import random 
class RandomizedSet:

    def __init__(self):
        self.object = {}

    def insert(self, val: int) -> bool:
        if val in self.object:
            return False
        else:
            self.object[val] = True
            return True

    def remove(self, val: int) -> bool:
        if val in self.object:
            del self.object[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.object.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()