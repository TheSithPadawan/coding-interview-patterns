# lc link: https://leetcode.com/problems/my-calendar-ii/
# two list solution

class MyCalendarTwo:

    def __init__(self):
        self.nonoverlaps = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # case when we have triple booking
        # print(self.overlaps)
        for l, r in self.overlaps:
            if not (start >= r or end <= l):
                return False
        # update on double bookings
        for l, r in self.nonoverlaps:
            if start >= r or end <= l:
                continue
            # find the double booking and update the double booking list
            s, e = max(start, l), min(end ,r)
            self.overlaps.append((s, e))
        self.nonoverlaps.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
