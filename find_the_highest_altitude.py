class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n: int = len(gain)
        altitude: int = 0
        maximum: int = 0
        
        for i in range(0, n):
            altitude = altitude + gain[i]
            maximum = max(maximum, altitude)
        
        return maximum
