# lc 362. only looking for fixed array solution
"""
让你实现两个支付接口， 第一个接口是记录下每笔存入的金额与时间， 接口二是返回过去60
分钟所有存入的钱。 要求，时间颗粒度（granularity） 到秒； put, get调用频率很高，需要常数
时间复杂度。
def putTransaction(amount, timestamp):
def getTotalTransactionInLastOneHour():

deque solution: getTotalTransactionInLastOneHour() takes O(n) in the worst case

60 min -> 3600 s -> create a fixed size buffer of 3600
hit -> bucket count += loan_amount
"""
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
    
# more optimized solution using Ring Buffer
# learnt from: https://leetcode.com/problems/design-hit-counter/solutions/83490/java-circular-array-solution-with-a-really-detailed-explanation-post
class HitCounter:

    def __init__(self):
        self.N = 300
        self.counts = [0] * self.N
        self.last_time = 0
        self.last_position = 0
        self.sum = 0

    def hit(self, timestamp: int) -> None:
        self.move(timestamp)
        self.counts[self.last_position] += 1
        self.last_position += 1
        self.sum += 1
        print(self.last_position)

    def getHits(self, timestamp: int) -> int:
        self.move(timestamp)
        return self.sum

    def move(self, timestamp: int):
        # in other words, when gap is valid <= N, we are clearing ahead. like the current
        # bucket for the hit to write to.
        gap = min(timestamp - self.last_time, self.N)
        for i in range(gap):
            self.last_position = (self.last_position + 1) % self.N
            self.sum -= self.counts[self.last_position]
            self.counts[self.last_position] = 0
        self.last_time = timestamp


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
