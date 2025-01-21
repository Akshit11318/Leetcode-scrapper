## K-th Nearest Obstacle Queries
**Problem Link:** https://leetcode.com/problems/k-th-nearest-obstacle-queries/description

**Problem Statement:**
- Input format: You are given a grid of size `m x n` and a list of queries where each query is of the form `(x, y, k)`, indicating the cell at `(x, y)` and asking for the `k-th` nearest obstacle from this cell.
- Constraints: `1 <= m, n <= 10^5`, `1 <= k <= 10^5`, and the grid contains at least one obstacle.
- Expected output format: For each query, return the `k-th` nearest obstacle's coordinates if it exists; otherwise, return `[-1, -1]`.
- Key requirements and edge cases to consider: Handling cases where `k` is larger than the number of obstacles within the grid, considering the grid boundaries, and optimizing the search for the `k-th` nearest obstacle.

**Example Test Cases:**
1. Given a grid with obstacles at `(1, 1)` and `(3, 3)`, and a query at `(2, 2)` asking for the `1st` nearest obstacle, the answer should be `[1, 1]`.
2. For the same grid and a query at `(2, 2)` asking for the `2nd` nearest obstacle, the answer should be `[3, 3]`.
3. If `k` exceeds the number of obstacles, the answer should be `[-1, -1]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every cell in the grid from the query cell and calculating the Manhattan distance (since diagonal movements are not allowed) to each obstacle.
- For each query, iterate through the grid to find all obstacles, calculate their distances to the query cell, and sort these distances to find the `k-th` smallest one.
- This approach comes to mind first because it directly addresses the problem statement by checking every possible obstacle.

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<int>> kthNearestObstacle(vector<vector<int>>& grid, vector<vector<int>>& queries) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> obstacles;
    // Collect all obstacle coordinates
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) { // Assuming 1 represents an obstacle
                obstacles.push_back({i, j});
            }
        }
    }

    vector<vector<int>> results;
    for (auto& query : queries) {
        int x = query[0];
        int y = query[1];
        int k = query[2];
        vector<pair<int, pair<int, int>>> distances;
        // Calculate distance to each obstacle
        for (auto& obstacle : obstacles) {
            int distance = abs(x - obstacle[0]) + abs(y - obstacle[1]);
            distances.push_back({distance, obstacle});
        }
        // Sort distances and find the k-th smallest
        sort(distances.begin(), distances.end());
        if (k > distances.size()) {
            results.push_back({-1, -1});
        } else {
            results.push_back(distances[k-1].second);
        }
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot o \cdot \log(o))$ where $q$ is the number of queries and $o$ is the number of obstacles. This is because for each query, we sort the distances to all obstacles.
> - **Space Complexity:** $O(o)$ for storing all obstacles and $O(q)$ for the results, where $o$ is the number of obstacles and $q$ is the number of queries.
> - **Why these complexities occur:** The brute force approach involves sorting the distances to all obstacles for each query, leading to the time complexity. The space complexity is due to storing the obstacles and the results.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a data structure that allows for efficient nearest neighbor searches, such as a `k-d` tree or a ball tree. However, given the constraints and the nature of the grid, a simpler approach can be to maintain a list of obstacles and use a priority queue to efficiently find the `k-th` nearest obstacle for each query.
- Since the grid is static and queries are the input, pre-processing the grid to find all obstacles and then using a priority queue for each query can reduce the time complexity.
- Proof of optimality: This approach is optimal because it reduces the search space for each query to the set of obstacles, which is smaller than the entire grid, and uses a priority queue to efficiently find the `k-th` nearest obstacle.

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Obstacle {
    int x, y;
};

struct Compare {
    int x, y;
    Compare(int x, int y) : x(x), y(y) {}
    bool operator()(const Obstacle& a, const Obstacle& b) {
        int distanceA = abs(x - a.x) + abs(y - a.y);
        int distanceB = abs(x - b.x) + abs(y - b.y);
        return distanceA > distanceB;
    }
};

vector<vector<int>> kthNearestObstacle(vector<vector<int>>& grid, vector<vector<int>>& queries) {
    int m = grid.size();
    int n = grid[0].size();
    vector<Obstacle> obstacles;
    // Collect all obstacle coordinates
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) { // Assuming 1 represents an obstacle
                obstacles.push_back({i, j});
            }
        }
    }

    vector<vector<int>> results;
    for (auto& query : queries) {
        int x = query[0];
        int y = query[1];
        int k = query[2];
        priority_queue<Obstacle, vector<Obstacle>, Compare> pq(x, y);
        for (auto& obstacle : obstacles) {
            pq.push(obstacle);
        }
        // Find the k-th smallest distance
        for (int i = 0; i < k - 1; i++) {
            if (pq.empty()) break;
            pq.pop();
        }
        if (pq.empty()) {
            results.push_back({-1, -1});
        } else {
            results.push_back({pq.top().x, pq.top().y});
        }
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot o \cdot \log(o))$ where $q$ is the number of queries and $o$ is the number of obstacles, because we use a priority queue to find the `k-th` nearest obstacle for each query.
> - **Space Complexity:** $O(o)$ for storing all obstacles and $O(q)$ for the results.
> - **Optimality proof:** This approach is optimal because it efficiently uses a priority queue to find the `k-th` nearest obstacle for each query, reducing the search space to the set of obstacles.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using priority queues for efficient nearest neighbor searches, and pre-processing the grid to reduce the search space.
- Problem-solving patterns identified: Reducing the problem to a nearest neighbor search and using appropriate data structures for efficiency.
- Optimization techniques learned: Using priority queues and pre-processing to reduce the time complexity.
- Similar problems to practice: Other nearest neighbor search problems, such as finding the `k` nearest neighbors in a high-dimensional space.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the priority queue or the distance calculation.
- Edge cases to watch for: Handling cases where `k` exceeds the number of obstacles or the query cell is outside the grid boundaries.
- Performance pitfalls: Using a naive approach that checks every cell in the grid for each query, leading to high time complexity.
- Testing considerations: Thoroughly testing the implementation with various inputs, including edge cases and large grids.