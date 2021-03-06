class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if not newInterval: return intervals
        nl, nr = newInterval
        n = len(intervals)

        if intervals[-1][1] < nl: return intervals + [newInterval]
        if intervals[0][0] > nr: return [newInterval] + intervals

        def intersect(l1, r1, l2, r2):
            l = max(l1, l2)
            r = min(r1, r2)
            return l <= r

        output, l, r = [], None, None
        for i, itv in enumerate(intervals):
            il, ir = itv
            
            if intersect(il, ir, nl, nr):
                if l is None: l = min(il, nl)
                if r is None: r = max(ir, nr)
                l, r = min(l, il), max(r, ir)
            else:
                if r is not None:
                    output.append([l, r])
                    l, r = None, None
                if i and intervals[i - 1][1] < nl and nr < il:
                    output.append(newInterval)
                output.append(itv)
                
        if r is not None: 
            output.append([l, r])
            
        return output
