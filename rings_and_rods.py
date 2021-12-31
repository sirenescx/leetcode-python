class Solution:
    def countPoints(self, rings: str) -> int:
        colors: List[set] = [set(), set(), set()]
        for i, color in enumerate(rings):
            if color == 'R':
                colors[0].add(rings[i + 1])
            if color == 'G':
                colors[1].add(rings[i + 1])
            if color == 'B':
                colors[2].add(rings[i + 1])
        
        return len((colors[0].intersection(colors[1])).intersection(colors[2]))
