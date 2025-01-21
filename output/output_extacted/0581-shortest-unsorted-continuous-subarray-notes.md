## Shortest Unsorted Continuous Subarray

**Problem Link:** https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description

**Problem Statement:**
- Input format: An integer array `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^4`.
- Expected output format: The length of the shortest subarray that needs to be sorted in place so that the entire array becomes sorted.
- Key requirements and edge cases to consider:
  - If the array is already sorted, return `0`.
  - If the array contains duplicate elements, the shortest subarray that needs to be sorted might include these duplicates.
- Example test cases with explanations:
  - Input: `nums = [2,6,4,8,10,9,15]`, Output: `5`. Explanation: You need to sort the subarray `[6,4,8,10,9]` in place so that the entire array becomes sorted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to generate all possible subarrays, check if the subarray is sorted, and then check the rest of the array to see if it's sorted as well.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, sort it and replace the original subarray in the array with the sorted subarray.
  3. Check if the entire array is sorted after the replacement.
  4. If the array is sorted, calculate the length of the subarray that was replaced.
- Why this approach comes to mind first: It's a straightforward approach that tries to solve the problem by brute force, checking every possible subarray.

```cpp
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        int min_len = n;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                vector<int> temp = nums;
                sort(temp.begin() + i, temp.begin() + j + 1);
                if (isSorted(temp)) {
                    min_len = min(min_len, j - i + 1);
                }
            }
        }
        
        return min_len == n ? 0 : min_len;
    }
    
    bool isSorted(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we're generating all possible subarrays ($O(n^2)$), sorting each subarray ($O(n \log n)$), and then checking if the entire array is sorted ($O(n)$).
> - **Space Complexity:** $O(n)$, because we're creating a temporary copy of the input array.
> - **Why these complexities occur:** The high time complexity occurs because of the brute force approach, where we're checking every possible subarray and sorting each one. The space complexity occurs because we're creating a temporary copy of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible subarrays and checking if they're sorted, we can find the first and last elements that are out of order.
- Detailed breakdown of the approach:
  1. Find the first element that is out of order by iterating through the array from left to right.
  2. Find the last element that is out of order by iterating through the array from right to left.
  3. The subarray that needs to be sorted is the one between the first and last elements that are out of order.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array to find the first and last elements that are out of order.

```cpp
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        
        int start = n, end = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != sorted_nums[i]) {
                start = min(start, i);
                end = max(end, i);
            }
        }
        
        return end - start >= 0 ? end - start + 1 : 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we're sorting the input array.
> - **Space Complexity:** $O(n)$, because we're creating a sorted copy of the input array.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array to find the first and last elements that are out of order, and then it uses the sorted array to find the subarray that needs to be sorted.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and comparison.
- Problem-solving patterns identified: Finding the first and last elements that are out of order.
- Optimization techniques learned: Using a sorted copy of the input array to find the subarray that needs to be sorted.
- Similar problems to practice: Finding the longest increasing subsequence, finding the shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the input array is empty, not handling edge cases.
- Edge cases to watch for: Empty input array, input array with a single element.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Testing the solution with different input arrays, including edge cases.