class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # Invalid case: prefix is longer (e.g., "abcd" before "abc")
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break # Only the first differing character defines the order
        
        visited = {} # False = visiting, True = visited
        res = []

        def dfs(c):
            if c in visited:
                return visited[c] # Return True if visited, False if currently visiting (cycle)
            
            visited[c] = False # Mark as "visiting"
            for neighbor in adj[c]:
                if not dfs(neighbor): # If a cycle is detected down the line
                    return False
            
            visited[c] = True # Mark as "visited"
            res.append(c)
            return True

        # Check every character (since the graph might be disconnected)
        for char in adj:
            if not dfs(char):
                return "" # Cycle detected
        
        res.reverse()
        return "".join(res) 