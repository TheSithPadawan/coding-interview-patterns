class ZigzagKIterator:
    # input: list of list
    def __init__(self, lists) -> None:
        self.queue = []
        self.lists = lists
        self.iters = [0] * len(lists)
        self.init_queue()

    def next(self) -> int:
        ans = self.queue.pop(0)
        self.init_queue()
        return ans

    def hasNext(self) -> bool:
        return len(self.queue) > 0

    def init_queue(self):
        for i, itr in enumerate(self.iters):
            if itr < len(self.lists[i]):
                # perform an update
                self.queue.append(self.lists[i][itr])
                self.iters[i] = itr + 1

def main():
    itr = ZigzagKIterator([[1,2,3], [4,5,6,7], [8,9]])
    while itr.hasNext():
        print(itr.next())
main()