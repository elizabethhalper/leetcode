# 252. Meeting Rooms

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        busy = {}
        for interval in intervals:
            for i in range(interval[0],interval[1]):
                if i in busy.keys():
                    return False
                else:
                    busy[i] = 1
            
        return True