class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""

        adj = {c: set() for w in words for c in w}

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
        
        res = []
        visiting = set()
        visited = set()
        def dfs(c):

            if c in visiting:
                return True   # Cycle detected!

            if c in visited:
                return False  # Already processed and safe, no cycle here
            visiting.add(c)
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return False

        for c in adj:
            if dfs(c):
                return ""
        print("RES", res)
        return "".join(res[::-1])