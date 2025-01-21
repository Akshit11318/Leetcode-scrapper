## Reorder Routes to Make All Paths Lead to The City Zero

**Problem Link:** https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description

**Problem Statement:**
- Input: `n` (number of cities) and `connections` (a list of routes between cities)
- Output: The minimum number of operations to reorder routes so that all paths lead to city 0
- Key requirements:
  - Each city is connected to every other city.
  - Each connection is either `0 -> i` or `i -> 0` for some city `i`.
- Edge cases:
  - `n` can be as large as 1000.
  - `connections` can contain up to 2000 routes.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible reorderings of the routes and count the number of operations required for each.
- Step-by-step breakdown:
  1. Generate all permutations of the `connections` list.
  2. For each permutation, iterate through the routes and count the number of operations required to make all paths lead to city 0.
  3. Keep track of the minimum number of operations found across all permutations.
- Why this approach comes to mind first: It is a straightforward, albeit inefficient, way to solve the problem by trying all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minOperations(int n, vector<vector<int>>& connections) {
    int minOps = INT_MAX;
    do {
        int ops = 0;
        vector<bool> visited(n, false);
        for (auto& connection : connections) {
            if (connection[0] == 0) {
                visited[connection[1]] = true;
            } else if (connection[1] == 0) {
                if (!visited[connection[0]]) {
                    ops++;
                }
            }
        }
        minOps = min(minOps, ops);
    } while (next_permutation(connections.begin(), connections.end()));
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of cities and $m$ is the number of connections. This is because there are $n!$ permutations of the connections, and for each permutation, we iterate through the $m$ connections.
> - **Space Complexity:** $O(n + m)$, for storing the visited cities and the connections.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to the exponential number of permutations.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of trying all permutations, we can simply count the number of routes that need to be reversed to make all paths lead to city 0.
- Detailed breakdown:
  1. Initialize a variable `ops` to 0.
  2. Iterate through the connections. For each connection, if it is not in the direction `0 -> i`, increment `ops`.
- Proof of optimality: This approach is optimal because it directly counts the minimum number of operations required to make all paths lead to city 0, without trying unnecessary permutations.

```cpp
int minOperations(int n, vector<vector<int>>& connections) {
    int ops = 0;
    for (auto& connection : connections) {
        if (connection[0] != 0) {
            ops++;
        }
    }
    return ops;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of connections. This is because we only need to iterate through the connections once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the `ops` variable.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best possible for this problem since we must at least read the input connections once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: counting, iteration, and optimization.
- Problem-solving patterns identified: looking for a direct approach instead of trying all possibilities.
- Optimization techniques learned: reducing the problem to a simple counting problem.
- Similar problems to practice: other graph theory and optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: using unnecessary complex data structures or algorithms.
- Edge cases to watch for: handling empty input or invalid connections.
- Performance pitfalls: using brute force approaches for large inputs.
- Testing considerations: testing with different input sizes and edge cases.