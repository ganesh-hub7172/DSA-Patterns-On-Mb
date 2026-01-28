#include <vector>
#include <cstdlib>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int target = nums.size() - k;  // kth largest -> (n-k)th smallest
        return quickSelect(nums, 0, nums.size() - 1, target);
    }

    int quickSelect(vector<int>& nums, int left, int right, int k) {
        if (left == right) return nums[left];

        int pivotIndex = left + rand() % (right - left + 1);
        pivotIndex = partition(nums, left, right, pivotIndex);

        if (pivotIndex == k)
            return nums[pivotIndex];
        else if (pivotIndex < k)
            return quickSelect(nums, pivotIndex + 1, right, k);
        else
            return quickSelect(nums, left, pivotIndex - 1, k);
    }

    int partition(vector<int>& nums, int left, int right, int pivotIndex) {
        int pivot = nums[pivotIndex];
        swap(nums[pivotIndex], nums[right]);  // move pivot to end

        int storeIndex = left;
        for (int i = left; i < right; i++) {
            if (nums[i] < pivot) {
                swap(nums[storeIndex], nums[i]);
                storeIndex++;
            }
        }

        swap(nums[storeIndex], nums[right]);  // move pivot to final place
        return storeIndex;
    }
};
