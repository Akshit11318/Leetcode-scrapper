## Minimum Replacements to Sort the Array

**Problem Link:** https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The array is non-empty and contains at least one element.
- Expected output format: The minimum number of replacements required to make the array sorted.
- Key requirements and edge cases to consider: The array may contain duplicate elements, and the replacements can be any integer, not just the ones present in the array.
- Example test cases with explanations:
  - For the input `[1, 2, 3, 4, 5]`, the output is `0` because the array is already sorted.
  - For the input `[5, 4, 3, 2, 1]`, the output is `4` because we need to replace four elements to make the array sorted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to use a brute force approach, where we try all possible replacements for each element in the array and check if the resulting array is sorted.
- Step-by-step breakdown of the solution:
  1. Generate all possible replacements for each element in the array.
  2. For each replacement, create a new array with the replacement applied.
  3. Check if the new array is sorted.
  4. If the new array is sorted, count the number of replacements made.
  5. Keep track of the minimum number of replacements required to make the array sorted.

```cpp
int minReplacements(vector<int>& nums) {
    int n = nums.size();
    int minReplacements = n;
    
    // Generate all possible replacements for each element
    for (int mask = 0; mask < (1 << n); mask++) {
        int replacements = 0;
        vector<int> newNums = nums;
        
        // Apply the replacements
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                newNums[i] = i + 1; // Replace with the correct value
                replacements++;
            }
        }
        
        // Check if the new array is sorted
        if (isSorted(newNums)) {
            minReplacements = min(minReplacements, replacements);
        }
    }
    
    return minReplacements;
}

bool isSorted(vector<int>& nums) {
    for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible replacements for each element, which takes $O(2^n)$ time, and then check if the resulting array is sorted, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we need to store the new array with the replacements applied.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible replacements for each element, which results in an exponential number of possibilities. The space complexity is linear because we need to store the new array with the replacements applied.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a **LIS (Longest Increasing Subsequence)** approach. The idea is to find the longest increasing subsequence in the input array, and then the minimum number of replacements required is the difference between the length of the array and the length of the LIS.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` of size `n`, where `dp[i]` represents the length of the LIS ending at index `i`.
  2. Initialize `dp[i]` to 1 for all `i`, because a single element is always an increasing subsequence of length 1.
  3. Iterate through the array, and for each element, compare it with all previous elements. If the current element is greater than a previous element, update `dp[i]` to be the maximum of its current value and `dp[j] + 1`, where `j` is the index of the previous element.
  4. The minimum number of replacements required is `n - max(dp)`, where `max(dp)` is the maximum value in the `dp` table.

```cpp
int minReplacements(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    
    int maxLIS = *max_element(dp.begin(), dp.end());
    return n - maxLIS;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we iterate through the array and compare each element with all previous elements.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we need to store the dynamic programming table `dp`.
> - **Optimality proof:** The LIS approach is optimal because it finds the longest increasing subsequence in the input array, which means that we need to replace the minimum number of elements to make the array sorted.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, longest increasing subsequence.
- Problem-solving patterns identified: Using dynamic programming to solve optimization problems.
- Optimization techniques learned: Using the LIS approach to find the minimum number of replacements required.
- Similar problems to practice: Other problems that involve finding the minimum number of operations required to achieve a certain goal.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, not updating the `dp` table correctly.
- Edge cases to watch for: Handling arrays with duplicate elements, handling arrays with a single element.
- Performance pitfalls: Using a brute force approach, not using dynamic programming to optimize the solution.
- Testing considerations: Testing the solution with different input sizes, testing the solution with different types of input arrays.