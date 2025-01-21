## Partition Array Such That Maximum Difference Is K

**Problem Link:** https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 5 * 10^4`, `0 <= nums[i] <= 10^9`, and `0 <= k <= 10^9`.
- Expected Output: The minimum number of partitions such that the maximum difference in each partition is at most `k`.
- Key Requirements and Edge Cases:
  - The array can be partitioned into multiple subarrays.
  - Each subarray should have a maximum difference of at most `k`.
  - The goal is to minimize the number of partitions.

**Example Test Cases:**
- Input: `nums = [1,2,3], k = 1`, Output: `2`. The array can be partitioned into `[1,2]` and `[3]`.
- Input: `nums = [2,2,4,5], k = 0`, Output: `3`. The array can be partitioned into `[2]`, `[2]`, and `[4,5]`.
- Input: `nums = [1,2,3], k = 2`, Output: `1`. The array can be partitioned into `[1,2,3]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible partitions of the array.
- For each partition, calculate the maximum difference.
- If the maximum difference is at most `k`, consider it a valid partition.
- The goal is to find the minimum number of partitions that cover the entire array.

```cpp
class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        int n = nums.size();
        int result = 0;
        int start = 0;
        
        while (start < n) {
            int maxVal = nums[start];
            int minVal = nums[start];
            int end = start;
            
            while (end < n && maxVal - minVal <= k) {
                maxVal = max(maxVal, nums[end]);
                minVal = min(minVal, nums[end]);
                end++;
            }
            
            result++;
            start = end;
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array `nums`. This is because in the worst case, we might end up checking every possible partition of the array.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the variables `result`, `start`, `maxVal`, `minVal`, and `end`.
> - **Why these complexities occur:** The time complexity occurs because of the nested loop structure, where for each starting index, we potentially check every other index in the array. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy approach to find the minimum number of partitions.
- We maintain two pointers, `start` and `end`, representing the current partition.
- We expand the partition to the right as long as the maximum difference is at most `k`.
- Once we cannot expand the partition further, we move to the next partition.

```cpp
class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        int n = nums.size();
        int result = 0;
        int start = 0;
        
        while (start < n) {
            int maxVal = nums[start];
            int minVal = nums[start];
            int end = start;
            
            while (end < n && maxVal - minVal <= k) {
                maxVal = max(maxVal, nums[end]);
                minVal = min(minVal, nums[end]);
                end++;
            }
            
            result++;
            start = end;
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the variables `result`, `start`, `maxVal`, `minVal`, and `end`.
> - **Optimality proof:** This approach is optimal because we make a single pass through the array and use a greedy strategy to find the minimum number of partitions. We cannot do better than this because we must at least examine each element in the array once.

---

### Final Notes

**Learning Points:**
- The importance of using a greedy approach to solve optimization problems.
- How to maintain two pointers to represent a sliding window or partition.
- The need to carefully consider the termination conditions for the while loop.

**Mistakes to Avoid:**
- Not considering the maximum difference in each partition.
- Not using a greedy approach to minimize the number of partitions.
- Not carefully handling the edge cases, such as an empty input array or a `k` value of 0.