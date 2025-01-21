## Maximum Subarray

**Problem Link:** https://leetcode.com/problems/maximum-subarray/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The input array will have at least one element, and the array size will not exceed 3 * 10^4.
- Expected output format: The maximum sum of a subarray.
- Key requirements and edge cases to consider: Handling negative numbers, arrays with all negative numbers, and arrays with all positive numbers.
- Example test cases with explanations:
  - Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`, Output: `6` (from subarray `[4,-1,2,1]`)
  - Input: `nums = [1]`, Output: `1`
  - Input: `nums = [5,4,-1,7,8]`, Output: `23`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray to find the one with the maximum sum.
- Step-by-step breakdown of the solution:
  1. Iterate over the array to consider each element as a starting point for a subarray.
  2. For each starting point, iterate over the rest of the array to consider all possible ending points.
  3. Calculate the sum of the subarray defined by the current starting and ending points.
  4. Update the maximum sum found so far if the current subarray's sum is larger.
- Why this approach comes to mind first: It's straightforward and ensures all possibilities are considered.

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            int currentSum = 0;
            for (int j = i; j < nums.size(); j++) {
                currentSum += nums[j];
                maxSum = max(maxSum, currentSum);
            }
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we have two nested loops that each iterate over the array.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the maximum sum and the current sum.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, and the space complexity is constant because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible subarrays, we can use Kadane's algorithm to keep track of the maximum sum of a subarray ending at each position.
- Detailed breakdown of the approach:
  1. Initialize the maximum sum and the current sum to the first element of the array.
  2. Iterate over the rest of the array. For each element, calculate the current sum by adding the current element to the previous current sum. If the current sum becomes negative, reset it to the current element.
  3. Update the maximum sum if the current sum is larger.
- Proof of optimality: Kadane's algorithm has a linear time complexity because it only requires a single pass through the array, making it the most efficient solution for this problem.

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            currentSum = max(nums[i], currentSum + nums[i]);
            maxSum = max(maxSum, currentSum);
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we only need to iterate over the array once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the maximum sum and the current sum.
> - **Optimality proof:** The time complexity is linear, which is the best possible for this problem since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Kadane's algorithm for finding the maximum sum of a subarray.
- Problem-solving patterns identified: Using dynamic programming or similar techniques to avoid redundant calculations and improve efficiency.
- Optimization techniques learned: Reducing the time complexity from $O(n^2)$ to $O(n)$ by avoiding nested loops.
- Similar problems to practice: Minimum window subarray, maximum product subarray, etc.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing variables, forgetting to handle edge cases (like an empty array or an array with all negative numbers).
- Edge cases to watch for: Arrays with all negative numbers, arrays with all positive numbers, arrays with a single element.
- Performance pitfalls: Using unnecessary nested loops or data structures that lead to high time or space complexity.
- Testing considerations: Ensure that the solution works correctly for various inputs, including edge cases and large inputs to verify efficiency.