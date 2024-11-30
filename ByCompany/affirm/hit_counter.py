# lc 362. only looking for fixed array solution
class HitCounter:

    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        # if it is not current time it means it is 300s or 600s ago, need to reset hits count back to 1
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        count = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                count += self.hits[i]
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
