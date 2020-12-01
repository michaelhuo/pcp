class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 1:
            return True
        size = len(intervals)
        intervals.sort(key = lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, size):
            s, e = intervals[i]
            if s < end:
                return False
            else:
                start = s
                end = e
        return True
            
