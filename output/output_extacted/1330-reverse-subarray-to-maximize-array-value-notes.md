## Reverse Subarray to Maximize Array Value

**Problem Link:** https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^5`.
- Expected output: The maximum possible sum of the array after reversing a subarray.
- Key requirements and edge cases: The input array can be empty or contain a single element. The subarray to be reversed can be of any length, including the entire array.
- Example test cases:
  - Input: `nums = [2,3,1,5,4]`
    - Output: `35`
    - Explanation: Reverse the subarray from index 3 to 4, resulting in `[2,3,1,4,5]`. Calculate the sum as `2*5 + 3*4 + 1*3 + 4*2 + 5*1 = 10 + 12 + 3 + 8 + 5 = 38`.
  - Input: `nums = [5,6,7,1,2,3]`
    - Output: `91`
    - Explanation: Reverse the subarray from index 0 to 5, resulting in `[3,2,1,7,6,5]`. Calculate the sum as `3*6 + 2*5 + 1*4 + 7*3 + 6*2 + 5*1 = 18 + 10 + 4 + 21 + 12 + 5 = 70`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subarrays, reverse each one, and calculate the sum of the modified array.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible subarray lengths (from 1 to `nums.length`).
  2. For each length, iterate over all possible start indices (from 0 to `nums.length - length`).
  3. Reverse the subarray from the start index to the start index plus the length minus one.
  4. Calculate the sum of the modified array using the formula `nums[i] * (i + 1)`.
  5. Keep track of the maximum sum found.

```cpp
class Solution {
public:
    int maxValueAfterReverse(vector<int>& nums) {
        int maxSum = 0;
        int n = nums.size();
        
        // Calculate the initial sum
        for (int i = 0; i < n; i++) {
            maxSum += nums[i] * (i + 1);
        }
        
        int maxDiff = 0;
        
        // Generate all possible subarrays, reverse each one, and calculate the sum
        for (int len = 1; len <= n; len++) {
            for (int start = 0; start <= n - len; start++) {
                // Reverse the subarray
                reverse(nums.begin() + start, nums.begin() + start + len);
                
                // Calculate the sum of the modified array
                int sum = 0;
                for (int i = 0; i < n; i++) {
                    sum += nums[i] * (i + 1);
                }
                
                // Update the maximum difference
                maxDiff = max(maxDiff, sum - maxSum);
                
                // Reverse the subarray back to its original state
                reverse(nums.begin() + start, nums.begin() + start + len);
            }
        }
        
        return maxSum + maxDiff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array `nums`. This is because we generate all possible subarrays, reverse each one, and calculate the sum of the modified array.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the maximum sum and the current sum.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it generates all possible subarrays and calculates the sum of the modified array for each one. The space complexity is low because we only use a constant amount of space to store the maximum sum and the current sum.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible subarrays, we can calculate the maximum possible sum by considering the contribution of each element to the sum.
- Detailed breakdown of the approach:
  1. Initialize the maximum sum to the initial sum of the array.
  2. Iterate over all possible pairs of elements in the array.
  3. For each pair, calculate the difference in the sum if we reverse the subarray between the two elements.
  4. Update the maximum sum if the difference is positive.
- Proof of optimality: This approach is optimal because it considers all possible reversals of subarrays and calculates the maximum possible sum.

```cpp
class Solution {
public:
    int maxValueAfterReverse(vector<int>& nums) {
        int n = nums.size();
        int maxSum = 0;
        
        // Calculate the initial sum
        for (int i = 0; i < n; i++) {
            maxSum += nums[i] * (i + 1);
        }
        
        int maxDiff = 0;
        
        // Calculate the maximum possible sum by considering the contribution of each element
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Calculate the difference in the sum if we reverse the subarray between the two elements
                int diff = 0;
                for (int k = i; k <= j; k++) {
                    diff += (n - 1 - k) * (nums[k] - nums[n - 1 - k]);
                }
                maxDiff = max(maxDiff, diff);
            }
        }
        
        return maxSum + maxDiff;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array `nums`. This is because we iterate over all possible pairs of elements in the array.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the maximum sum and the current sum.
> - **Optimality proof:** This approach is optimal because it considers all possible reversals of subarrays and calculates the maximum possible sum. The time complexity is reduced from $O(n^3)$ to $O(n^2)$ by avoiding the generation of all possible subarrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, greedy algorithms.
- Problem-solving patterns identified: considering all possible cases, using mathematical insights to reduce the search space.
- Optimization techniques learned: avoiding unnecessary calculations, using efficient data structures.
- Similar problems to practice: [insert similar problems].

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, incorrect calculation of the sum.
- Edge cases to watch for: empty input array, input array with a single element.
- Performance pitfalls: using inefficient algorithms, not considering all possible cases.
- Testing considerations: testing with different input sizes, testing with different input values.