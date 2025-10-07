class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        set1 = {}
        set2 = {}
        for i in word1:
            set1[i] = set1.get(i, 0) + 1
        for i in word2:
            set2[i] = set2.get(i, 0) + 1
        if set(set1.keys()) != set(set2.keys()):
            return False
        if sorted(set1.values()) != sorted(set2.values()):
            return False
        return True
            
        
        
