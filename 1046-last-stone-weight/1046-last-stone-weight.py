class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            next_largest = -heapq.heappop(stones)

            if largest != next_largest:
                # Push the difference back as negative
                heapq.heappush(stones, -(largest - next_largest))

        return -stones[0] if stones else 0