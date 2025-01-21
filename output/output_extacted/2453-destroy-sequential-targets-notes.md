## Destroy Sequential Targets
**Problem Link:** https://leetcode.com/problems/destroy-sequential-targets/description

**Problem Statement:**
- Input format: `nums` - an array of integers, and `space` - a set of integers.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`, and `1 <= space.length <= 10^5`.
- Expected output format: The minimum number of operations required to destroy all targets in `nums` by using the given `space`.
- Key requirements and edge cases to consider:
  - Each target can be destroyed by using a number in `space` that is either one more or one less than the target.
  - If a target cannot be destroyed, return `-1`.
- Example test cases with explanations:
  - `nums = [3, 7, 8, 2, 1, 5, 9, 4, 6]`, `space = [2, 3, 5]`. The minimum number of operations is `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of using numbers in `space` to destroy targets in `nums`.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `space`.
  2. For each permutation, try to destroy targets in `nums` by using the numbers in the permutation.
  3. Keep track of the minimum number of operations required to destroy all targets.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

int destroyTargets(std::vector<int>& nums, std::set<int>& space) {
    int minOperations = INT_MAX;
    std::sort(nums.begin(), nums.end());
    do {
        int operations = 0;
        bool destroyedAll = true;
        for (int num : nums) {
            bool destroyed = false;
            for (int s : space) {
                if (s == num - 1 || s == num + 1) {
                    destroyed = true;
                    break;
                }
            }
            if (!destroyed) {
                destroyedAll = false;
                break;
            }
            operations++;
        }
        if (destroyedAll) {
            minOperations = std::min(minOperations, operations);
        }
    } while (std::next_permutation(space.begin(), space.end()));
    return minOperations == INT_MAX ? -1 : minOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m \cdot n)$, where $n$ is the size of `space` and $m$ is the size of `nums`. This is because we generate all permutations of `space` and for each permutation, we iterate over `nums`.
> - **Space Complexity:** $O(n)$, where $n$ is the size of `space`. This is because we need to store the current permutation of `space`.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, which leads to a high time complexity. The space complexity is relatively low because we only need to store the current permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all permutations, we can use a greedy approach to destroy targets in `nums`.
- Detailed breakdown of the approach:
  1. Sort `nums` in ascending order.
  2. Initialize a variable to store the minimum number of operations required.
  3. Iterate over `nums` and for each target, check if it can be destroyed by using a number in `space`.
  4. If a target can be destroyed, increment the minimum number of operations required.
- Proof of optimality: This approach is optimal because it ensures that we destroy all targets in `nums` with the minimum number of operations required.

```cpp
int destroyTargets(std::vector<int>& nums, std::set<int>& space) {
    std::sort(nums.begin(), nums.end());
    int minOperations = 0;
    for (int num : nums) {
        bool destroyed = false;
        for (int s : space) {
            if (s == num - 1 || s == num + 1) {
                destroyed = true;
                break;
            }
        }
        if (!destroyed) {
            return -1;
        }
        minOperations++;
    }
    return minOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `nums` and $m` is the size of `space`. This is because we iterate over `nums` and for each target, we iterate over `space`.
> - **Space Complexity:** $O(1)$, where the space is constant. This is because we only need to store a few variables.
> - **Optimality proof:** This approach is optimal because it ensures that we destroy all targets in `nums` with the minimum number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting, and iteration.
- Problem-solving patterns identified: Using a greedy approach to solve problems that require finding the minimum number of operations.
- Optimization techniques learned: Avoiding unnecessary permutations and using a greedy approach to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a target can be destroyed before incrementing the minimum number of operations required.
- Edge cases to watch for: If a target cannot be destroyed, return `-1`.
- Performance pitfalls: Using a brute force approach that tries all permutations, which leads to a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it works correctly.