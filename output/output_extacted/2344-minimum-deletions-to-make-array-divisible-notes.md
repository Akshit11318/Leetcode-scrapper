## Minimum Deletions to Make Array Divisible
**Problem Link:** https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `2 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^6`, `2 <= k <= 10^6`.
- Expected Output: The minimum number of elements that must be deleted to make all elements in the array divisible by `k`.
- Key Requirements:
  - The array can be modified.
  - The goal is to minimize the number of deletions.
- Example Test Cases:
  - `nums = [3,2,5,3], k = 2` -> The array can be modified to `[2,2]` by deleting `3` and `5`. Thus, `2` deletions are needed.
  - `nums = [1,2,3,4], k = 4` -> All elements can be modified to be divisible by `4` except `1`, `2`, and `3`. Thus, `3` deletions are needed.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible subset of the array to see if all its elements can be made divisible by `k`.
- Step-by-Step Breakdown:
  1. Generate all possible subsets of the array.
  2. For each subset, check if all elements can be made divisible by `k`.
  3. Keep track of the minimum number of elements not in any subset that meets the condition.

```cpp
#include <vector>
#include <algorithm>

int minDeletionsBruteForce(std::vector<int>& nums, int k) {
    int minDeletions = nums.size(); // Maximum possible deletions
    // Generate all possible subsets
    for (int mask = 0; mask < (1 << nums.size()); ++mask) {
        std::vector<int> subset;
        for (int i = 0; i < nums.size(); ++i) {
            if (mask & (1 << i)) {
                subset.push_back(nums[i]);
            }
        }
        // Check if all elements in the subset are divisible by k
        bool allDivisible = true;
        for (int num : subset) {
            if (num % k != 0) {
                allDivisible = false;
                break;
            }
        }
        if (allDivisible) {
            // Update minimum deletions if necessary
            minDeletions = std::min(minDeletions, static_cast<int>(nums.size() - subset.size()));
        }
    }
    return minDeletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ where $n$ is the size of `nums`. The reason is that we generate $2^n$ subsets and for each subset, we potentially check all $n$ elements.
> - **Space Complexity:** $O(n)$ for storing the current subset.
> - **Why these complexities occur:** The brute force approach is inherently exponential due to generating all subsets. The linear factor in time complexity comes from checking divisibility for each element in a subset.

---

### Optimal Approach (Required)
**Explanation:**
- Key Insight: Instead of generating all subsets, we can count how many numbers in the array are divisible by `k` and then consider the remaining numbers that are not divisible by `k`.
- Detailed Breakdown:
  1. Count how many numbers in the array are divisible by `k`.
  2. For numbers not divisible by `k`, consider their remainders when divided by `k`. If two numbers have the same remainder, only one of them can stay in the array (to minimize deletions).
  3. Calculate the minimum deletions required based on the counts of numbers with unique remainders and those divisible by `k`.

```cpp
int minDeletionsOptimal(std::vector<int>& nums, int k) {
    std::vector<int> counts(k, 0); // Count occurrences of each remainder
    int divisibleCount = 0; // Count numbers divisible by k
    for (int num : nums) {
        if (num % k == 0) {
            divisibleCount++;
        } else {
            counts[num % k]++;
        }
    }
    int deletions = nums.size() - divisibleCount; // Initial deletions for non-divisible numbers
    for (int count : counts) {
        // For each remainder, we can keep at most one number
        deletions -= std::min(1, count);
    }
    return deletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$ where $n$ is the size of `nums` and $k$ is the divisor. This is because we make a single pass through `nums` and then process the counts array of size `k`.
> - **Space Complexity:** $O(k)$ for storing the counts of remainders.
> - **Optimality proof:** This approach is optimal because it considers all possible scenarios for minimizing deletions: it counts numbers already divisible by `k` and optimally selects one number for each remainder class, thus minimizing the total number of deletions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, remainder analysis, and optimization.
- Problem-solving patterns identified: Considering all possible scenarios for optimization.
- Optimization techniques learned: Minimizing deletions by considering unique remainders and numbers divisible by `k`.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating remainders or counts.
- Edge cases to watch for: Handling arrays with all elements divisible by `k` or arrays with no elements divisible by `k`.
- Performance pitfalls: Using inefficient algorithms like brute force for large inputs.
- Testing considerations: Ensure the solution works correctly for various inputs, including edge cases.