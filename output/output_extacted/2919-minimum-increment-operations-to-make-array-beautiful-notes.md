## Minimum Increment Operations to Make Array Beautiful

**Problem Link:** https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^6`.
- Expected output: The minimum number of operations to make the array `beautiful`.
- Key requirements: An array is `beautiful` if it is sorted in ascending order and the difference between any two adjacent elements is at most one.
- Edge cases: An array with a single element is always `beautiful`.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible increment operation to make the array `beautiful`.
- Step-by-step breakdown:
  1. Generate all permutations of increment operations.
  2. For each permutation, apply the operations to the array.
  3. Check if the resulting array is `beautiful`.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that guarantees finding the minimum number of operations if executed correctly.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

int minIncrementForBeautifulArray(std::vector<int>& nums) {
    int n = nums.size();
    int minOperations = INT_MAX;

    // Generate all permutations of increment operations
    for (int mask = 0; mask < (1 << n); mask++) {
        std::vector<int> temp = nums;
        int operations = 0;

        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                temp[i]++;
                operations++;
            }
        }

        // Check if the resulting array is beautiful
        bool isBeautiful = true;
        for (int i = 1; i < n; i++) {
            if (temp[i] - temp[i - 1] > 1) {
                isBeautiful = false;
                break;
            }
        }

        if (isBeautiful) {
            minOperations = std::min(minOperations, operations);
        }
    }

    return minOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate $2^n$ permutations and for each permutation, we perform $O(n)$ work to apply the operations and check if the array is `beautiful`.
> - **Space Complexity:** $O(n)$, as we need to store the temporary array `temp`.
> - **Why these complexities occur:** The brute force approach involves an exhaustive search, leading to exponential time complexity. The space complexity is linear due to the need to store the temporary array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all permutations, we can use a greedy approach to increment the elements in a way that minimizes the number of operations.
- Detailed breakdown:
  1. Sort the array in ascending order.
  2. Initialize the minimum number of operations to 0.
  3. Iterate through the sorted array, and for each element, calculate the minimum number of operations required to make it `beautiful` with respect to the previous element.
  4. Update the minimum number of operations accordingly.

```cpp
int minIncrementForBeautifulArray(std::vector<int>& nums) {
    int n = nums.size();
    int minOperations = 0;

    // Sort the array in ascending order
    std::sort(nums.begin(), nums.end());

    for (int i = 1; i < n; i++) {
        // Calculate the minimum number of operations required to make the current element beautiful
        int operations = std::max(0, nums[i] - nums[i - 1] - 1);
        minOperations += operations;
        // Update the current element to make it beautiful
        nums[i] += operations;
    }

    return minOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we sort the array, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum number of operations.
> - **Optimality proof:** The greedy approach ensures that we minimize the number of operations required to make the array `beautiful`. By sorting the array and incrementing the elements in a way that minimizes the difference between adjacent elements, we achieve the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, sorting, and iteration.
- Problem-solving patterns identified: Using a greedy approach to minimize the number of operations.
- Optimization techniques learned: Sorting the array and incrementing the elements in a way that minimizes the difference between adjacent elements.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the array before iterating through it.
- Edge cases to watch for: Handling arrays with a single element or empty arrays.
- Performance pitfalls: Using an exhaustive search approach instead of a greedy approach.
- Testing considerations: Testing the function with different input arrays, including edge cases.