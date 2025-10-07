class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        list_set = set(bannedWords)
        return sum([i in list_set for i in message]) >= 2