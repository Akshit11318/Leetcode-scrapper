## Matchsticks to Square

**Problem Link:** https://leetcode.com/problems/matchsticks-to-square/description

**Problem Statement:**
- Input: An array of integers `matchsticks` where each integer represents the length of a matchstick.
- Constraints: `1 <= matchsticks.length <= 15`, `0 <= matchsticks[i] <= 10^9`, and the sum of all elements in `matchsticks` is a perfect square.
- Expected Output: Return `true` if it is possible to form a square with the given matchsticks, and `false` otherwise.
- Key Requirements: The sum of all matchsticks must form a perfect square, and each side of the square must be formed by the sum of some matchsticks.
- Edge Cases: The input array may be empty, or the sum of all matchsticks may not be a perfect square.
- Example Test Cases:
  - Input: `[1,1,2,2,2]`
    - Output: `true`
    - Explanation: We can form a square with side length 4 by using the matchsticks of lengths 1, 1, 1, and 1.
  - Input: `[3,3,3,3,4]`
    - Output: `false`
    - Explanation: We cannot form a square with the given matchsticks because the sum of all matchsticks is 16, but we cannot divide the matchsticks into four groups with equal sums.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of matchsticks to form four groups.
- Step-by-step breakdown of the solution:
  1. Calculate the total sum of all matchsticks and check if it is a perfect square.
  2. If the sum is a perfect square, calculate the side length of the square.
  3. Generate all possible combinations of matchsticks to form four groups.
  4. Check each combination to see if the sum of each group is equal to the side length of the square.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations of matchsticks.

```cpp
#include <vector>
#include <algorithm>

bool makesquare(std::vector<int>& matchsticks) {
    int sum = 0;
    for (int stick : matchsticks) {
        sum += stick;
    }
    if (sum % 4 != 0) {
        return false;
    }
    int side = sum / 4;
    std::sort(matchsticks.rbegin(), matchsticks.rend());
    std::vector<int> sides(4, 0);
    return dfs(matchsticks, sides, side, 0);
}

bool dfs(std::vector<int>& matchsticks, std::vector<int>& sides, int side, int index) {
    if (index == matchsticks.size()) {
        return std::all_of(sides.begin(), sides.end(), [side](int x) { return x == side; });
    }
    for (int i = 0; i < 4; i++) {
        if (sides[i] + matchsticks[index] <= side) {
            sides[i] += matchsticks[index];
            if (dfs(matchsticks, sides, side, index + 1)) {
                return true;
            }
            sides[i] -= matchsticks[index];
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the number of matchsticks. This is because in the worst case, we try all possible combinations of matchsticks.
> - **Space Complexity:** $O(n)$, where $n$ is the number of matchsticks. This is because we need to store the current combination of matchsticks.
> - **Why these complexities occur:** The time complexity occurs because we try all possible combinations of matchsticks, and the space complexity occurs because we need to store the current combination of matchsticks.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a depth-first search (DFS) algorithm to try all possible combinations of matchsticks.
- Detailed breakdown of the approach:
  1. Calculate the total sum of all matchsticks and check if it is a perfect square.
  2. If the sum is a perfect square, calculate the side length of the square.
  3. Use a DFS algorithm to try all possible combinations of matchsticks to form four groups.
  4. Check each combination to see if the sum of each group is equal to the side length of the square.
- Proof of optimality: This approach is optimal because it tries all possible combinations of matchsticks in a efficient manner.
- Why further optimization is impossible: This approach is already optimal because it uses a DFS algorithm to try all possible combinations of matchsticks.

```cpp
#include <vector>
#include <algorithm>

bool makesquare(std::vector<int>& matchsticks) {
    int sum = 0;
    for (int stick : matchsticks) {
        sum += stick;
    }
    if (sum % 4 != 0) {
        return false;
    }
    int side = sum / 4;
    std::sort(matchsticks.rbegin(), matchsticks.rend());
    std::vector<int> sides(4, 0);
    return dfs(matchsticks, sides, side, 0);
}

bool dfs(std::vector<int>& matchsticks, std::vector<int>& sides, int side, int index) {
    if (index == matchsticks.size()) {
        return std::all_of(sides.begin(), sides.end(), [side](int x) { return x == side; });
    }
    for (int i = 0; i < 4; i++) {
        if (sides[i] + matchsticks[index] <= side) {
            sides[i] += matchsticks[index];
            if (dfs(matchsticks, sides, side, index + 1)) {
                return true;
            }
            sides[i] -= matchsticks[index];
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the number of matchsticks. This is because in the worst case, we try all possible combinations of matchsticks.
> - **Space Complexity:** $O(n)$, where $n$ is the number of matchsticks. This is because we need to store the current combination of matchsticks.
> - **Optimality proof:** This approach is optimal because it uses a DFS algorithm to try all possible combinations of matchsticks in an efficient manner.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) algorithm.
- Problem-solving patterns identified: Using a DFS algorithm to try all possible combinations of matchsticks.
- Optimization techniques learned: Using a DFS algorithm to try all possible combinations of matchsticks in an efficient manner.
- Similar problems to practice: Other problems that involve trying all possible combinations of objects, such as the `Partition Equal Subset Sum` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the sum of all matchsticks is a perfect square before trying all possible combinations of matchsticks.
- Edge cases to watch for: The input array may be empty, or the sum of all matchsticks may not be a perfect square.
- Performance pitfalls: Trying all possible combinations of matchsticks without using a DFS algorithm can lead to inefficient performance.
- Testing considerations: Test the function with different input arrays, including empty arrays and arrays with different lengths and sums.