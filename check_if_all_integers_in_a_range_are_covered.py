class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges)
        if ranges[0][0] <= left and right <= ranges[0][1]:
            return True
        
        stacked_ranges: List[List[int]] = [[ranges[0][0], ranges[0][1]]]
        end: int = ranges[0][1]
        index: int = 0
        for i in range(1, len(ranges)):
            if ranges[i][0] <= left and right <= ranges[i][1]:
                return True
            if ranges[i][0] - 1 <= end:
                stacked_ranges[index][1] = max(ranges[i][1], stacked_ranges[index][1])
            else:
                stacked_ranges.append([ranges[i][0], ranges[i][1]])
                index += 1
            end = max(end, ranges[i][1])

        for stacked_range in stacked_ranges:
            if stacked_range[0] <= left and right <= stacked_range[1]:
                return True

        return False
                
                
