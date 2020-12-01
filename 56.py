class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        f = lambda x: x[0]
        intervals.sort(key = f)
        answer = []
        start = end = -1
        for starti, endi in intervals:
            if start < 0:
                start = starti
                end = endi
            elif starti > end:
                answer.append([start, end])
                start = starti
                end = endi
            elif endi > end:
                end = endi

        if start >= 0 and end >= start:
            answer.append([start, end])
            
        return answer
    
