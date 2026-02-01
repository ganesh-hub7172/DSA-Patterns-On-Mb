import heapq

class Solution:
    def getFinalState(self, nums, k, multiplier):
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)

        for _ in range(k):
            val, idx = heapq.heappop(heap)
            val *= multiplier
            nums[idx] = val
            heapq.heappush(heap, (val, idx))

        return nums
