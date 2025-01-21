## Find Maximum Non-Decreasing Array Length

**Problem Link:** https://leetcode.com/problems/find-maximum-non-decreasing-array-length/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`.
- Expected output format: The length of the longest non-decreasing subarray.
- Key requirements and edge cases to consider: Non-decreasing subarrays can be formed by one or more elements where each element is greater than or equal to its predecessor.
- Example test cases with explanations: 
  - For `nums = [1,3,5,4,7]`, the longest non-decreasing subarray is `[1,3,5]` with length 3.
  - For `nums = [2,2,2,2,2]`, the longest non-decreasing subarray is the entire array with length 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray to see if it's non-decreasing.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, check if it's non-decreasing by comparing each element with its predecessor.
  3. Keep track of the maximum length of non-decreasing subarrays found so far.
- Why this approach comes to mind first: It's straightforward and ensures we don't miss any potential non-decreasing subarrays.

```cpp
int findLengthOfLCIS(vector<int>& nums) {
    int n = nums.size();
    int maxLength = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            bool isNonDecreasing = true;
            for (int k = i; k < j; k++) {
                if (nums[k] > nums[k + 1]) {
                    isNonDecreasing = false;
                    break;
                }
            }
            if (isNonDecreasing) {
                maxLength = max(maxLength, j - i + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops: one for generating subarrays and two for checking if a subarray is non-decreasing.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum length and other variables.
> - **Why these complexities occur:** The brute force approach is inefficient due to the nested loops, which lead to high time complexity. However, it uses minimal extra space, hence the low space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can keep track of the length of the current non-decreasing subarray as we iterate through the array, resetting the length whenever we encounter a decrease.
- Detailed breakdown of the approach:
  1. Initialize a variable `maxLength` to keep track of the maximum length of non-decreasing subarrays and `currentLength` to track the length of the current non-decreasing subarray.
  2. Iterate through the array. If the current element is greater than or equal to the previous one, increment `currentLength`.
  3. Otherwise, update `maxLength` if `currentLength` is greater, and reset `currentLength` to 1.
- Proof of optimality: This approach ensures we consider all possible non-decreasing subarrays in a single pass through the array, making it more efficient than the brute force method.

```cpp
int findLengthOfLCIS(vector<int>& nums) {
    if (nums.empty()) return 0;
    
    int maxLength = 1;
    int currentLength = 1;
    
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] >= nums[i - 1]) {
            currentLength++;
        } else {
            maxLength = max(maxLength, currentLength);
            currentLength = 1;
        }
    }
    return max(maxLength, currentLength);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum length and other variables.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem, considering we must examine each element at least once to determine if it's part of a non-decreasing subarray.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative approach, dynamic programming (in a simplified form by keeping track of current and maximum lengths).
- Problem-solving patterns identified: Looking for patterns or sequences in arrays, using variables to keep track of current and maximum states.
- Optimization techniques learned: Reducing the number of iterations and avoiding unnecessary computations by using a single pass through the data.
- Similar problems to practice: Finding the longest increasing subsequence, maximum sum subarray, etc.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (like an empty array), not updating variables correctly.
- Edge cases to watch for: Empty array, single-element array, array with all elements being equal.
- Performance pitfalls: Using inefficient algorithms (like the brute force approach for large inputs).
- Testing considerations: Ensure to test with various inputs, including edge cases, to verify the correctness of the solution.