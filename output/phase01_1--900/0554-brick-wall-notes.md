## Brick Wall
**Problem Link:** [https://leetcode.com/problems/brick-wall/description](https://leetcode.com/problems/brick-wall/description)

**Problem Statement:**
- Input format: A list of lists of integers `wall` where each sublist represents the widths of bricks in a row.
- Constraints: Each row is a non-empty list of integers, and each integer in the list is an integer representing the width of a brick.
- Expected output format: The number of bricks that need to be removed to make the wall one brick wide at each row.
- Key requirements and edge cases to consider: The wall is made of bricks of different widths, and we can only remove bricks, not add or modify them.
- Example test cases with explanations:
  - `[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]` should return `2` because if we remove two bricks from the third row and the fifth row, the wall becomes one brick wide at each row.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing bricks from the wall to make it one brick wide at each row.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the minimum number of bricks to remove.
  2. Iterate over all possible combinations of removing bricks from the wall.
  3. For each combination, check if the wall becomes one brick wide at each row.
  4. If it does, update the minimum number of bricks to remove.
- Why this approach comes to mind first: It's a straightforward approach to try all possible combinations and see which one works.

```cpp
#include <vector>
#include <algorithm>

int leastBricks(std::vector<std::vector<int>>& wall) {
    int minBricks = INT_MAX;
    for (int row = 0; row < wall.size(); row++) {
        for (int i = 0; i < (1 << wall[row].size()); i++) {
            std::vector<int> newWall = wall;
            int removed = 0;
            for (int j = 0; j < wall[row].size(); j++) {
                if ((i & (1 << j)) != 0) {
                    newWall[row].erase(newWall[row].begin() + j);
                    removed++;
                    j--;
                }
            }
            if (isValid(newWall)) {
                minBricks = std::min(minBricks, removed);
            }
        }
    }
    return minBricks;
}

bool isValid(std::vector<std::vector<int>>& wall) {
    for (int row = 0; row < wall.size(); row++) {
        if (wall[row].size() != 1) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$ where $n$ is the maximum number of bricks in a row and $m$ is the number of rows, because we're trying all possible combinations of removing bricks from the wall.
> - **Space Complexity:** $O(m \cdot n)$ because we're storing a copy of the wall for each combination.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of removing bricks from the wall, which leads to exponential time complexity. The space complexity is linear in the size of the wall because we're storing a copy of the wall for each combination.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible combinations of removing bricks, we can count the frequency of each edge (i.e., the position where two bricks meet) in the wall.
- Detailed breakdown of the approach:
  1. Initialize a map to store the frequency of each edge.
  2. Iterate over each row in the wall.
  3. For each row, iterate over each brick and update the frequency of the edge at the end of the brick.
  4. Find the edge with the maximum frequency.
  5. Return the total number of bricks minus the maximum frequency, because we can remove all bricks that do not contain the most frequent edge.
- Proof of optimality: This approach is optimal because it finds the minimum number of bricks to remove to make the wall one brick wide at each row.

```cpp
#include <vector>
#include <unordered_map>

int leastBricks(std::vector<std::vector<int>>& wall) {
    std::unordered_map<int, int> edgeCount;
    for (const auto& row : wall) {
        int width = 0;
        for (int i = 0; i < row.size() - 1; i++) {
            width += row[i];
            edgeCount[width]++;
        }
    }
    int maxEdgeCount = 0;
    for (const auto& pair : edgeCount) {
        maxEdgeCount = std::max(maxEdgeCount, pair.second);
    }
    return wall.size() - maxEdgeCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ is the number of rows and $n$ is the maximum number of bricks in a row, because we're iterating over each brick in the wall.
> - **Space Complexity:** $O(m \cdot n)$ because we're storing the frequency of each edge in the wall.
> - **Optimality proof:** This approach is optimal because it finds the minimum number of bricks to remove to make the wall one brick wide at each row. It does this by counting the frequency of each edge in the wall and finding the edge with the maximum frequency.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, edge cases.
- Problem-solving patterns identified: Finding the minimum number of operations to achieve a goal.
- Optimization techniques learned: Counting the frequency of each edge in the wall instead of trying all possible combinations.
- Similar problems to practice: Other problems involving frequency counting and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not initializing variables correctly.
- Edge cases to watch for: Empty wall, wall with only one row, wall with only one brick in each row.
- Performance pitfalls: Trying all possible combinations of removing bricks, not using a map to store the frequency of each edge.
- Testing considerations: Test the function with different inputs, including edge cases.