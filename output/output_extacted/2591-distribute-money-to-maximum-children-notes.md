## Distribute Money to Maximum Children
**Problem Link:** https://leetcode.com/problems/distribute-money-to-maximum-children/description

**Problem Statement:**
- Input: `n` representing the number of children and `candies` representing the number of candies each child currently has.
- Constraints: `1 <= n <= 100`, `0 <= candies <= 100`.
- Expected output: The maximum number of children that can be given an extra candy so that they have more candies than the children adjacent to them.
- Key requirements: Each child can only receive one extra candy.

**Example Test Cases:**
- For `n = 3` and `candies = [1,2,2]`, the maximum number of children that can be given an extra candy is `1`.
- For `n = 4` and `candies = [1,2,2,1]`, the maximum number of children that can be given an extra candy is `2`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over all possible combinations of children that can receive an extra candy and check for each combination if the conditions are met.
- Step-by-step breakdown:
  1. Generate all possible subsets of children.
  2. For each subset, give an extra candy to each child in the subset.
  3. Check if the conditions are met for each child in the subset.
- Why this approach comes to mind first: It's a straightforward way to ensure we consider all possibilities.

```cpp
#include <vector>
#include <algorithm>

int max_children(const std::vector<int>& candies) {
    int max_count = 0;
    for (int mask = 0; mask < (1 << candies.size()); ++mask) {
        int count = 0;
        std::vector<int> temp_candies = candies;
        for (int i = 0; i < candies.size(); ++i) {
            if ((mask & (1 << i)) != 0) {
                temp_candies[i]++;
            }
        }
        for (int i = 0; i < temp_candies.size(); ++i) {
            bool is_greater = true;
            if (i > 0 && temp_candies[i] <= temp_candies[i - 1]) {
                is_greater = false;
            }
            if (i < temp_candies.size() - 1 && temp_candies[i] <= temp_candies[i + 1]) {
                is_greater = false;
            }
            if (is_greater) {
                count++;
            }
        }
        max_count = std::max(max_count, count);
    }
    return max_count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ where $n$ is the number of children. This is because we generate all subsets of children ($2^n$ possibilities) and for each subset, we iterate over the children to check the conditions.
> - **Space Complexity:** $O(n)$ for storing the temporary candies vector.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsets of children, which leads to exponential time complexity. The space complexity is linear due to the need to store a temporary vector of candies for each subset.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The problem can be solved by iterating over the children and checking if giving an extra candy to the current child would satisfy the condition. We only need to consider the local maximums.
- Detailed breakdown:
  1. Initialize a variable to store the maximum count of children that can receive an extra candy.
  2. Iterate over the children.
  3. For each child, check if giving an extra candy would make it have more candies than its neighbors.
  4. If the condition is met, increment the count.
- Proof of optimality: This approach is optimal because it considers all local maximums and ensures that the conditions are met for each child.

```cpp
int max_children(const std::vector<int>& candies) {
    int max_count = 0;
    for (int i = 0; i < candies.size(); ++i) {
        bool is_greater = true;
        if (i > 0 && candies[i] + 1 <= candies[i - 1]) {
            is_greater = false;
        }
        if (i < candies.size() - 1 && candies[i] + 1 <= candies[i + 1]) {
            is_greater = false;
        }
        if (is_greater) {
            max_count++;
        }
    }
    return max_count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of children. This is because we only need to iterate over the children once.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the count.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and only considers the necessary conditions for each child.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks.
- Problem-solving patterns identified: Local maximums, conditions checking.
- Optimization techniques learned: Avoiding unnecessary iterations, using simple conditional checks.
- Similar problems to practice: Other problems involving local maximums and conditions checking.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect iteration, missing conditions.
- Edge cases to watch for: Children at the boundaries, children with equal candies.
- Performance pitfalls: Using unnecessary iterations or complex data structures.
- Testing considerations: Test cases with different numbers of children, different distributions of candies.