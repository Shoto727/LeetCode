import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        # Keep only k largest elements in minHeap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # If heap grows beyond k, pop smallest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Top of heap is the k-th largest
        return self.minHeap[0]
