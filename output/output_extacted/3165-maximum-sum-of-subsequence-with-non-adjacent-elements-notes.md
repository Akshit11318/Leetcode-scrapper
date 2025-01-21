## Maximum Sum of Subsequence with Non-adjacent Elements

**Problem Link:** https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` will be in the range `[1, 100]`, and the integers in `nums` will be in the range `[-100, 100]`.
- Expected output format: The maximum sum of a subsequence where no two elements are adjacent.
- Key requirements and edge cases to consider: The subsequence must not contain adjacent elements, and the input array can be empty or contain negative numbers.
- Example test cases with explanations:
  - For `nums = [2,7,9,3,1]`, the maximum sum is `11` (by selecting `2`, `9`, and `1`).
  - For `nums = [1,2,3,4]`, the maximum sum is `6` (by selecting `1` and `3`, or `2` and `4`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible subsequences and check if they satisfy the condition of not having adjacent elements.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, check if any two elements are adjacent in the original array.
  3. If a subsequence does not contain adjacent elements, calculate its sum.
  4. Keep track of the maximum sum found among all valid subsequences.
- Why this approach comes to mind first: It is a straightforward way to ensure that all possible solutions are considered, but it is inefficient due to its high time complexity.

```cpp
#include <vector>
#include <algorithm>

int maxSum(vector<int>& nums) {
    int n = nums.size();
    int maxSum = 0;
    
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); mask++) {
        int sum = 0;
        bool valid = true;
        
        // Check each bit in the mask to decide whether to include the corresponding element
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                sum += nums[i];
                // Check if the previous element is also included
                if (i > 0 && (mask & (1 << (i-1))) != 0) {
                    valid = false;
                    break;
                }
            }
        }
        
        // Update maxSum if the current subsequence is valid and has a larger sum
        if (valid) {
            maxSum = max(maxSum, sum);
        }
    }
    
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in the input array. This is because we generate $2^n$ subsequences and for each, we potentially iterate through all $n$ elements to calculate the sum and check for adjacency.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input and output, because we only use a constant amount of space to store the mask, sum, and validity flag.
> - **Why these complexities occur:** The high time complexity comes from generating all possible subsequences, which grows exponentially with the size of the input array. The space complexity is low because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can solve this problem using dynamic programming by maintaining two variables: one for the maximum sum including the current element and another for the maximum sum excluding the current element.
- Detailed breakdown of the approach:
  1. Initialize two variables, `incl` and `excl`, to the first element of the array and 0, respectively.
  2. Iterate through the array starting from the second element. For each element, update `incl` and `excl` based on whether including the current element would violate the adjacency rule.
  3. After iterating through all elements, the maximum of `incl` and `excl` gives the maximum sum of a subsequence without adjacent elements.
- Proof of optimality: This approach ensures that we consider all possible subsequences without actually generating them, thus avoiding the exponential time complexity of the brute force approach. It has a linear time complexity because we only need to make one pass through the input array.

```cpp
int maxSum(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    if (nums.size() == 1) return nums[0];
    
    int incl = nums[0];
    int excl = 0;
    
    for (int i = 1; i < nums.size(); i++) {
        int new_incl = excl + nums[i];
        excl = max(incl, excl);
        incl = new_incl;
    }
    
    return max(incl, excl);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the `incl` and `excl` variables, regardless of the input size.
> - **Optimality proof:** This solution is optimal because it achieves a linear time complexity, which is the best possible for this problem since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and the importance of choosing the right approach to avoid exponential time complexity.
- Problem-solving patterns identified: Breaking down complex problems into simpler sub-problems and solving them only once.
- Optimization techniques learned: Using dynamic programming to store and reuse the results of expensive function calls.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input array.
- Edge cases to watch for: Arrays with a single element, or arrays with all elements being negative.
- Performance pitfalls: Using a brute force approach for large input sizes.
- Testing considerations: Ensure that the solution works correctly for arrays of varying lengths and with different combinations of positive and negative numbers.