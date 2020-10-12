class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) == 1 or len(B) == 1 or len(A) != len(B): return False
        if A == B: return len(A) > len(set(A))
        
        diffs = []
        for a, b in zip(A, B):
            if a != b: diffs.append((a, b))
            if len(diffs) > 2: return False
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
            
