"""
private PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
private PriorityQueue<Integer> large = new PriorityQueue<>();
private boolean even = true;

public double findMedian() {
    if (even)
        return (small.peek() + large.peek()) / 2.0;
    else
        return small.peek();
}

public void addNum(int num) {
    if (even) {
        large.offer(num);
        small.offer(large.poll());
    } else {
        small.offer(num);
        large.offer(small.poll());
    }
    even = !even;
}

======Python
Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
Alltogether, the add operation is O(logn), The findMedian operation is O(1).

Note that the heapq in python is a min heap, thus we need to invert the values in the smaller half to mimic a "max heap".
"""

from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 388 ms
