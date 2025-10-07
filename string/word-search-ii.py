class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
        
        m, n = len(board), len(board[0])
        result = set()
        
        def dfs(r, c, node, path):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == '*':
                return
            
            char = board[r][c]
            if char not in node.children:
                return
                
            node = node.children[char]
            path += char
            
            if node.is_end_of_word:
                result.add(path)
            
            board[r][c] = '*'
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(r + dr, c + dc, node, path)
            
            board[r][c] = char
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        
        return list(result)