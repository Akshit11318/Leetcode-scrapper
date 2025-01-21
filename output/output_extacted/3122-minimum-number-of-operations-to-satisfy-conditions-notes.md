## Minimum Number of Operations to Satisfy Conditions

**Problem Link:** https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/description

**Problem Statement:**
- Given a 2D array `conditions` where `conditions[i] = [a, b, op]`, `a` and `b` are integers, and `op` is an operator, either 0 (representing ==) or 1 (representing !=).
- The task is to find the minimum number of operations required to satisfy all conditions.
- Input constraints: `1 <= conditions.length <= 5 * 10^4`, `0 <= a, b <= 5 * 10^4`.
- Expected output format: The minimum number of operations required to satisfy all conditions.

**Key Requirements and Edge Cases:**
- Consider cases where `a` and `b` are equal or unequal.
- Analyze the impact of `op` on the conditions.
- Edge cases include empty conditions, conditions with no operations, and conditions with all equal or unequal elements.

**Example Test Cases:**
- `conditions = [[0, 1, 0], [1, 2, 1]]` should return `2` because we need to change `0` to `1` and `1` to `2` to satisfy the conditions.
- `conditions = [[0, 1, 1], [1, 2, 0]]` should return `1` because we only need to change `1` to `2` to satisfy the conditions.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of operations to satisfy the conditions.
- We can start by iterating over each condition and checking if the operation is satisfied.
- If not, we can try changing the values of `a` and `b` to satisfy the condition.
- This approach involves a lot of trial and error and is not efficient for large inputs.

```cpp
#include <vector>

int minOperations(std::vector<std::vector<int>>& conditions) {
    int n = conditions.size();
    int minOps = 0;

    // Iterate over each condition
    for (int i = 0; i < n; i++) {
        int a = conditions[i][0];
        int b = conditions[i][1];
        int op = conditions[i][2];

        // Check if the condition is satisfied
        if (op == 0 && a != b) {
            // If not, try changing the values of a and b to satisfy the condition
            minOps++;
        } else if (op == 1 && a == b) {
            minOps++;
        }
    }

    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of conditions. This is because we iterate over each condition once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum number of operations.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over each condition once, and the space complexity is constant because we only use a fixed amount of space to store the minimum number of operations.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a `std::unordered_map` to store the frequency of each number.
- We can then iterate over each condition and update the frequency of the numbers accordingly.
- This approach is more efficient than the brute force approach because it avoids trying all possible combinations of operations.

```cpp
#include <vector>
#include <unordered_map>

int minOperations(std::vector<std::vector<int>>& conditions) {
    int n = conditions.size();
    std::unordered_map<int, int> freq;
    int minOps = 0;

    // Iterate over each condition
    for (int i = 0; i < n; i++) {
        int a = conditions[i][0];
        int b = conditions[i][1];
        int op = conditions[i][2];

        // Update the frequency of the numbers
        if (op == 0) {
            if (a != b) {
                minOps++;
            }
        } else {
            if (a == b) {
                minOps++;
            }
        }
    }

    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of conditions. This is because we iterate over each condition once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum number of operations.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the conditions and uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- The importance of using `std::unordered_map` to store frequency of numbers.
- The need to avoid trying all possible combinations of operations.
- The use of a single pass over the conditions to minimize time complexity.

**Mistakes to Avoid:**
- Trying all possible combinations of operations, which can lead to exponential time complexity.
- Not using a `std::unordered_map` to store the frequency of numbers, which can lead to slower lookup times.
- Not considering the impact of the `op` operator on the conditions.