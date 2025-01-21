## Number of Zero-Filled Subarrays
**Problem Link:** https://leetcode.com/problems/number-of-zero-filled-subarrays/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` will be in the range $[1, 10^5]$ and each element `nums[i]` will be in the range $[0, 10^9]$.
- Expected output format: The number of zero-filled subarrays.
- Key requirements and edge cases to consider: Handling arrays with all zeros, arrays with no zeros, and arrays with a mix of zeros and non-zeros.
- Example test cases with explanations:
  - For `nums = [0,0,0,2,0,0]`, the output should be 9 because there are 9 zero-filled subarrays: `[0]`, `[0,0]`, `[0,0,0]`, `[0,0,0,2,0]`, `[0,0,0,2,0,0]`, `[0,0]`, `[0,0,0]`, `[0]`, and `[0,0]`.
  - For `nums = [1,3,0]`, the output should be 2 because there are 2 zero-filled subarrays: `[0]` and `[0]`.
  - For `nums = [0,0,0,1,0,1,0,1,0,1]`, the output should be 26 because there are 26 zero-filled subarrays.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible subarrays of `nums` and count those that contain only zeros.
- Step-by-step breakdown of the solution:
  1. Iterate through all possible start indices of subarrays.
  2. For each start index, iterate through all possible end indices.
  3. For each subarray, check if it contains only zeros.
  4. If it does, increment the count of zero-filled subarrays.
- Why this approach comes to mind first: It is straightforward and checks every possible subarray, ensuring that no zero-filled subarray is missed.

```cpp
int numberOfSubarrays(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            bool isZeroFilled = true;
            for (int k = i; k <= j; k++) {
                if (nums[k] != 0) {
                    isZeroFilled = false;
                    break;
                }
            }
            if (isZeroFilled) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`, because for each of the $n$ possible start indices, we iterate up to $n$ times to consider all possible end indices, and for each subarray, we check up to $n$ elements to ensure it's zero-filled.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The brute force approach is inefficient because it checks every possible subarray and for each, it checks every element, leading to cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every subarray, we can keep track of the current sequence of zeros as we iterate through `nums`. When we encounter a non-zero, we calculate the number of subarrays that can be formed from the sequence of zeros we've seen so far.
- Detailed breakdown of the approach:
  1. Initialize a variable to keep track of the current sequence length of zeros.
  2. Initialize a variable to store the total count of zero-filled subarrays.
  3. Iterate through `nums`. For each zero, increment the sequence length.
  4. When a non-zero is encountered, calculate the number of subarrays that can be formed from the current sequence of zeros using the formula for the sum of an arithmetic series: $n*(n+1)/2$, where $n$ is the length of the sequence of zeros.
  5. Add this to the total count and reset the sequence length.
- Proof of optimality: This approach ensures we count every zero-filled subarray exactly once and does so in a single pass through `nums`, making it more efficient than the brute force approach.

```cpp
int numberOfSubarrays(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    int zeros = 0;
    for (int num : nums) {
        if (num == 0) {
            zeros++;
        } else {
            count += (zeros * (zeros + 1)) / 2;
            zeros = 0;
        }
    }
    // Don't forget to count any trailing zeros
    count += (zeros * (zeros + 1)) / 2;
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, because we make a single pass through `nums`.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the count and the current sequence length.
> - **Optimality proof:** This is optimal because we only need to make one pass through `nums` to count all zero-filled subarrays, and we do so in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of recognizing patterns and sequences in arrays, and how to efficiently count subarrays that meet certain conditions.
- Problem-solving patterns identified: Looking for ways to avoid checking every possible subarray and instead finding a pattern or a formula that can be applied to simplify the problem.
- Optimization techniques learned: Reducing the time complexity by avoiding unnecessary iterations and using mathematical formulas to calculate counts directly.
- Similar problems to practice: Other problems involving counting subarrays or subsequences with specific properties.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as arrays with all zeros or arrays with no zeros.
- Edge cases to watch for: Arrays with a single element, arrays with alternating zeros and non-zeros, and arrays with long sequences of zeros.
- Performance pitfalls: Using brute force approaches for large inputs, which can lead to timeouts or inefficiencies.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases, to ensure it works correctly in all scenarios.