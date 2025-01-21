## Squirrel Simulation
**Problem Link:** https://leetcode.com/problems/squirrel-simulation/description

**Problem Statement:**
- Input format: `n`, `m`, `nuts`, `maxDist`
- Constraints: `1 <= n <= 5`, `1 <= m <= 20`, `1 <= maxDist <= 100`
- Expected output format: Minimum number of steps to collect all nuts
- Key requirements: The squirrel can move in any of the four cardinal directions (up, down, left, right) to collect nuts
- Example test cases:
  - `n = 5`, `m = 3`, `nuts = [[0, 2], [2, 2], [0, 0]]`, `maxDist = 7`
  - `n = 1`, `m = 2`, `nuts = [[2, 2], [4, 4]]`, `maxDist = 2`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible paths to collect nuts
- Step-by-step breakdown:
  1. Generate all possible paths to collect nuts
  2. Calculate the total distance for each path
  3. Return the minimum distance among all paths
- Why this approach comes to mind first: It's a straightforward solution that checks all possibilities

```cpp
class Solution {
public:
    int minDistance(int n, int m, vector<vector<int>>& nuts, int maxDist) {
        int minDist = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int dist = 0;
                for (int k = 0; k < m; k++) {
                    dist += abs(nuts[k][0] - i) + abs(nuts[k][1] - j);
                }
                minDist = min(minDist, dist);
            }
        }
        return minDist;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of rows/columns and $m$ is the number of nuts
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is constant because we don't use any data structures that scale with the input size

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The squirrel should start from the position that minimizes the total distance to all nuts
- Detailed breakdown:
  1. Calculate the total distance from each cell to all nuts
  2. Return the minimum distance among all cells
- Proof of optimality: This approach is optimal because it tries all possible starting positions and returns the one with the minimum total distance

```cpp
class Solution {
public:
    int minDistance(int n, int m, vector<vector<int>>& nuts, int maxDist) {
        int minDist = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int dist = 0;
                for (int k = 0; k < m; k++) {
                    dist += abs(nuts[k][0] - i) + abs(nuts[k][1] - j);
                }
                minDist = min(minDist, dist);
            }
        }
        return minDist;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of rows/columns and $m$ is the number of nuts
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space
> - **Optimality proof:** This approach is optimal because it tries all possible starting positions and returns the one with the minimum total distance

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts: Brute force, exhaustive search
- Problem-solving patterns: Try all possible solutions and return the best one
- Optimization techniques: None, as the problem requires trying all possible solutions
- Similar problems to practice: Other problems that involve trying all possible solutions, such as the Traveling Salesman Problem

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, using incorrect data structures
- Edge cases to watch for: When the input size is large, the brute force approach may take a long time to run
- Performance pitfalls: Using inefficient algorithms or data structures
- Testing considerations: Test the solution with different input sizes and edge cases to ensure correctness and performance.