class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        superpose = zip(position, speed)
        superpose = sorted(superpose, key=lambda x: x[0], reverse=True)
        count = 0
        prevtime = 0
        for index, item in enumerate(superpose):
            dis, sp = item
            dis = target-dis
            time = dis/sp
            if time > prevtime:
                count += 1
                prevtime = time
        return count
