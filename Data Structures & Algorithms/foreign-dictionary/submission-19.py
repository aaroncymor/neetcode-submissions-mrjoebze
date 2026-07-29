class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for s in words for c in s }
        res = []
        visited = {}

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visited[c] = False
            res.append(c)
            return False
        
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            min_length = len(w1) if len(w1) < len(w2) else len(w2)

            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""
            
            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        for c in adj:
            if dfs(c):
                return ""
        
        return "".join(reversed(res))
