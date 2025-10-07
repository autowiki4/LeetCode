class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = {}
        for product in products:
            d = trie
            for char in product:
                if char not in d:
                    d[char] = {'prod': [], 'child':{}}
                d[char]['prod'].append(product)
                d = d[char]['child']
        result = []
        d = trie
        for char in searchWord:
            if char in d:
                result.append(d[char]['prod'][:3])
                d = d[char]['child']
            else:
                result.append([])
                d = {}
        return result