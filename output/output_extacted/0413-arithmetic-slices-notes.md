## Arithmetic Slices
**Problem Link:** https://leetcode.com/problems/arithmetic-slices/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` of size `n`, find the number of arithmetic slices in the array.
- Expected output format: Return the number of arithmetic slices.
- Key requirements and edge cases to consider:
  - An arithmetic slice is a sequence of at least three numbers whose difference between any two successive members is constant.
  - The array `nums` contains only integers.
  - The size of the array `n` is between 1 and $10^5$.
  - The range of each element in `nums` is between $-10^9$ and $10^9$.
- Example test cases with explanations:
  - Input: `nums = [1,2,3,4]`, Output: `3`
    Explanation: Arithmetic slices are `[1, 2, 3]`, `[2, 3, 4]`, and `[1, 2, 3, 4]`.
  - Input: `nums = [1, 2, 3, 5]`, Output: `1`
    Explanation: The only arithmetic slice is `[1, 2, 3]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Check every possible subarray of `nums` to see if it forms an arithmetic sequence.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, check if the difference between consecutive elements is constant.
  3. If the subarray has at least three elements and forms an arithmetic sequence, increment the count of arithmetic slices.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that checks every possibility.

```cpp
int numberOfArithmeticSlices(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 2; j <= n; j++) {
            bool isArithmetic = true;
            int diff = nums[i + 1] - nums[i];
            for (int k = i + 2; k < j; k++) {
                if (nums[k] - nums[k - 1] != diff) {
                    isArithmetic = false;
                    break;
                }
            }
            if (isArithmetic) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of `nums`. This is because for each element, we potentially generate all subarrays starting from that element and then check each subarray to see if it's arithmetic.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The high time complexity comes from the nested loops that generate all possible subarrays and then check each one. The space complexity is low because we don't use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible subarray, we can keep track of the current difference between consecutive elements as we iterate through the array. When the difference changes, we know we've moved past the end of an arithmetic sequence and can calculate how many sequences we've found so far.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the current difference and the count of arithmetic slices.
  2. Iterate through the array, updating the current difference and checking for changes.
  3. When a change is detected, calculate the number of arithmetic slices that ended at the previous position.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, resulting in a significant reduction in time complexity compared to the brute force approach.

```cpp
int numberOfArithmeticSlices(vector<int>& nums) {
    int n = nums.size();
    if (n < 3) return 0;
    
    int count = 0;
    int lastDiff = nums[1] - nums[0];
    int currentLength = 2;
    
    for (int i = 2; i < n; i++) {
        int diff = nums[i] - nums[i - 1];
        if (diff == lastDiff) {
            currentLength++;
        } else {
            // Calculate the number of arithmetic slices that ended at the previous position
            if (currentLength >= 3) {
                int length = currentLength;
                count += (length - 2) * (length - 1) / 2;
            }
            currentLength = 2;
            lastDiff = diff;
        }
    }
    
    // Calculate the number of arithmetic slices for the last sequence
    if (currentLength >= 3) {
        int length = currentLength;
        count += (length - 2) * (length - 1) / 2;
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our variables.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the input array, and it calculates the number of arithmetic slices in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of recognizing patterns in sequences and using dynamic programming to solve problems efficiently.
- Problem-solving patterns identified: Looking for ways to reduce the number of operations by identifying patterns or using more efficient algorithms.
- Optimization techniques learned: Using a single pass through the data to calculate the desired result, rather than generating all possible subarrays.
- Similar problems to practice: Other problems involving sequences and patterns, such as finding the longest increasing subsequence or the longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty input array or an array with fewer than three elements.
- Edge cases to watch for: Arrays with duplicate elements, or arrays where the difference between consecutive elements is zero.
- Performance pitfalls: Using algorithms with high time complexities, such as the brute force approach, for large input sizes.
- Testing considerations: Make sure to test the function with a variety of input arrays, including edge cases, to ensure it works correctly.