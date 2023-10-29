class Solution:
    def interval_record_in_intervals(self,interval):
        if len(interval) == 1:
            return str(interval[0])
        else:
            return str(interval[0])+'->'+str(interval[-1])
            # return '->'.join(map(str, [interval[0], interval[-1]]))   
            #  
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []

        intervals = []
        interval = []

        for num in nums:
            if interval == []:
                interval.append(num)
            else:
                if num == interval[-1] + 1:
                    interval.append(num)
                else:
                    intervals.append(self.interval_record_in_intervals(interval))
                    interval = []
                    interval.append(num)

        if len(interval) > 0:
            intervals.append(self.interval_record_in_intervals(interval))
        
        return intervals


            

