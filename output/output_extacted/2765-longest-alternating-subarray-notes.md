## Longest Alternating Subarray

**Problem Link:** https://leetcode.com/problems/longest-alternating-subarray/description

**Problem Statement:**
- Input: An integer array `nums` of length `n`.
- Constraints: `1 <= n <= 10^5`.
- Expected Output: The length of the longest alternating subarray in `nums`.
- Key Requirements:
  - Alternating subarray: A subarray where each element is either greater than or less than its previous element.
  - Longest: The subarray with the maximum length.
- Edge Cases:
  - Single-element array: Returns 1.
  - Array with all elements equal: Returns 1.
- Example Test Cases:
  - `[1, 2, 3, 4, 5]`: Returns 2 because `[1, 2]` or `[2, 3]` or `[3, 4]` or `[4, 5]` are the longest alternating subarrays.
  - `[5, 4, 3, 2, 1]`: Returns 2 because `[5, 4]` or `[4, 3]` or `[3, 2]` or `[2, 1]` are the longest alternating subarrays.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray to see if it's alternating.
- Step-by-step breakdown:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, check if it's alternating by comparing each element with its previous one.
  3. Keep track of the longest alternating subarray found.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by checking all possibilities.

```cpp
#include <iostream>
#include <vector>

int longestAlternatingSubarray(std::vector<int>& nums) {
    int n = nums.size();
    int maxLength = 1; // Initialize with the minimum possible length

    // Generate all possible subarrays
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            std::vector<int> subarray(nums.begin() + i, nums.begin() + j);

            // Check if the subarray is alternating
            bool isAlternating = true;
            for (int k = 1; k < subarray.size(); k++) {
                if (subarray[k] == subarray[k - 1]) {
                    isAlternating = false;
                    break;
                }
            }

            if (isAlternating) {
                // Update maxLength if the current subarray is longer
                maxLength = std::max(maxLength, (int)subarray.size());
            }
        }
    }

    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the input array. This is because we're generating all possible subarrays ($O(n^2)$) and then checking each one to see if it's alternating ($O(n)$).
> - **Space Complexity:** $O(n)$, as we're storing each subarray.
> - **Why these complexities occur:** The brute force approach involves checking all possible subarrays, which leads to high time complexity. The space complexity is due to storing each subarray.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible subarrays, we can use a single pass through the array and keep track of the longest alternating subarray ending at each position.
- Detailed breakdown:
  1. Initialize variables to keep track of the maximum length and the current length of the alternating subarray.
  2. Iterate through the array. For each element, check if it's greater than or less than the previous element.
  3. If the current element is different from the previous one, update the current length of the alternating subarray.
  4. Update the maximum length if the current length is greater.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, resulting in linear time complexity.

```cpp
#include <iostream>
#include <vector>

int longestAlternatingSubarray(std::vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return 1; // Edge case: single-element array

    int maxLength = 1;
    int currentLength = 1;

    for (int i = 1; i < n; i++) {
        if (nums[i] != nums[i - 1]) {
            currentLength++;
            maxLength = std::max(maxLength, currentLength);
        } else {
            currentLength = 1;
        }
    }

    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we're making a single pass through the array.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store variables.
> - **Optimality proof:** This approach is optimal because it has the lowest possible time complexity for this problem, which is linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Single pass through the array, keeping track of maximum and current lengths.
- Problem-solving patterns: Using variables to keep track of relevant information, updating them based on the current element.
- Optimization techniques: Avoiding unnecessary iterations, using a single pass through the array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not updating variables correctly.
- Edge cases to watch for: Single-element array, array with all elements equal.
- Performance pitfalls: Using unnecessary iterations, not optimizing the solution.
- Testing considerations: Testing with different input sizes, testing with edge cases.