class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        meetings = []
        
        for element in A:
            meetings.append ( (element[0],1) ) #element[0] is start time, encoded with 1
            meetings.append ( (element[1],0) ) #element[1] is end time, encoded with 0
        
        meetings.sort()  #sort meetings in place, same time end time encoded tuple placed before than start time encoded tuple 
        
        max_room = 0
        room = 0
        
        for meeting in meetings:
            if meeting[1] == 1:
                room += 1
            else:
                room -= 1
            
            max_room = max(room,max_room)
        
        return max_room