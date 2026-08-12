class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""

        adj = {c: set() for w in words for c in w}
        indegree = {c:0 for c in adj.keys()}

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]

            min_length = len(w1) if len(w1) < len(w2) else len(w2)
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min_length):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        q = deque([c for c in adj if indegree[c] == 0])
        res = ""
        while q:
            c = q.popleft()
            res += c
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) != len(adj):
            return ""
        return res