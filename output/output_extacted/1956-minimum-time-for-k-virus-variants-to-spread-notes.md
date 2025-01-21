## Minimum Time for K Virus Variants to Spread
**Problem Link:** https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/description

**Problem Statement:**
- Input format and constraints: The problem provides a grid representing a lab where virus variants are spreading. The input includes the grid size (`m` and `n`), the grid itself (`grid`), the number of virus variants (`k`), and the time it takes for each variant to spread (`s`).
- Expected output format: The minimum time required for `k` virus variants to spread.
- Key requirements and edge cases to consider: The virus spreads from each cell to its adjacent cells (up, down, left, right) after a certain time (`s`). We need to find the minimum time for `k` virus variants to spread.
- Example test cases with explanations: For example, given a 3x3 grid with two virus variants and a spread time of 1, the minimum time to spread both variants would depend on their initial positions and the spread pattern.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach could involve simulating the spread of each virus variant over time, counting the number of cells infected at each step until we reach `k` variants.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the starting positions of the virus variants and the time elapsed.
  2. Simulate the spread of the virus by iterating through the queue, updating the time, and adding new positions to the queue based on the spread pattern.
  3. Keep track of the number of unique virus variants spread at each time step.
- Why this approach comes to mind first: It directly simulates the problem statement, making it an intuitive first step.

```cpp
#include <iostream>
#include <queue>
#include <unordered_set>

using namespace std;

int minTimeToSpread(vector<vector<int>>& grid, int k, int s) {
    int m = grid.size();
    int n = grid[0].size();
    int directions[][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    queue<pair<int, pair<int, int>>> q; // time, (x, y)
    unordered_set<int> visited; // keep track of visited cells

    // Initialize queue with initial positions of virus variants
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != 0) {
                q.push({0, {i, j}});
                visited.insert(i * n + j);
            }
        }
    }

    int time = 0;
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [currTime, pos] = q.front(); q.pop();
            int x = pos.first, y = pos.second;

            // Update time if current time is greater
            time = max(time, currTime);

            // Spread virus to adjacent cells
            for (auto& dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && visited.find(nx * n + ny) == visited.end()) {
                    q.push({currTime + s, {nx, ny}});
                    visited.insert(nx * n + ny);
                }
            }
        }
    }

    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot s)$, where $m$ and $n$ are the dimensions of the grid and $s$ is the spread time. This is because in the worst case, each cell could be visited once for each spread time step.
> - **Space Complexity:** $O(m \cdot n)$, for storing the visited cells.
> - **Why these complexities occur:** The brute force approach requires simulating the spread of the virus over time, which involves iterating over the grid and keeping track of visited cells, leading to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the spread of the virus over time, we can use a more efficient algorithm that directly calculates the minimum time required for `k` virus variants to spread based on their initial positions and the spread pattern.
- Detailed breakdown of the approach:
  1. Identify the initial positions of the `k` virus variants.
  2. For each variant, calculate the time it takes to reach all other cells in the grid, considering the spread time `s`.
  3. Determine the minimum time required for all `k` variants to spread based on their calculated spread times.
- Proof of optimality: This approach is optimal because it directly calculates the minimum time required without unnecessary simulations, avoiding redundant calculations and minimizing computational overhead.

```cpp
int minTimeToSpreadOptimal(vector<vector<int>>& grid, int k, int s) {
    int m = grid.size();
    int n = grid[0].size();
    int directions[][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int minTime = 0;

    // Function to calculate spread time from a given position
    auto calculateSpreadTime = [&](int x, int y) {
        queue<pair<int, pair<int, int>>> q; // time, (x, y)
        unordered_set<int> visited; // keep track of visited cells
        q.push({0, {x, y}});
        visited.insert(x * n + y);

        int spreadTime = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto [currTime, pos] = q.front(); q.pop();
                int cx = pos.first, cy = pos.second;

                // Update spread time if current time is greater
                spreadTime = max(spreadTime, currTime);

                // Spread virus to adjacent cells
                for (auto& dir : directions) {
                    int nx = cx + dir[0], ny = cy + dir[1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && visited.find(nx * n + ny) == visited.end()) {
                        q.push({currTime + s, {nx, ny}});
                        visited.insert(nx * n + ny);
                    }
                }
            }
        }

        return spreadTime;
    };

    // Calculate spread time for each variant and update minimum time
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != 0) {
                minTime = max(minTime, calculateSpreadTime(i, j));
            }
        }
    }

    return minTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot (m \cdot n))$, where $k$ is the number of virus variants, and $m$ and $n$ are the dimensions of the grid. This is because we calculate the spread time for each variant, and in the worst case, each cell could be visited once for each variant.
> - **Space Complexity:** $O(m \cdot n)$, for storing the visited cells during the spread time calculation.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum time required for all `k` virus variants to spread without unnecessary simulations, minimizing computational overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, graph traversal (BFS), and time complexity optimization.
- Problem-solving patterns identified: Breaking down complex problems into simpler sub-problems (e.g., calculating spread time for each variant) and using data structures efficiently (e.g., queues and sets).
- Optimization techniques learned: Avoiding redundant calculations and minimizing computational overhead by directly calculating the minimum time required.
- Similar problems to practice: Other graph traversal and simulation problems, such as finding the shortest path in a graph or simulating a process over time.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., grid boundaries), failing to update time correctly, and not considering the spread pattern accurately.
- Edge cases to watch for: Grid size, number of virus variants, spread time, and initial positions of the variants.
- Performance pitfalls: Using inefficient algorithms or data structures, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various input scenarios, including edge cases and large inputs, to ensure correctness and efficiency.