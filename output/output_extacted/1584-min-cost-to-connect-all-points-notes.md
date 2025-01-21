## Min Cost to Connect All Points
**Problem Link:** https://leetcode.com/problems/min-cost-to-connect-all-points/description

**Problem Statement:**
- Input format: `n` points in a 2D plane, where each point is represented as an array of two integers `[x, y]`.
- Constraints: `1 <= n <= 10^4`, `-10^5 <= x, y <= 10^5`, and no two points are identical.
- Expected output format: The minimum cost to connect all points.
- Key requirements and edge cases to consider: The cost to connect two points is the Manhattan distance between them (`|x1 - x2| + |y1 - y2|`). We need to find the minimum spanning tree that connects all points.
- Example test cases with explanations: For example, given points `[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]`, the minimum cost to connect all points is `20`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can calculate the Manhattan distance between each pair of points and then use a brute force approach to find the minimum spanning tree.
- Step-by-step breakdown of the solution:
  1. Calculate the Manhattan distance between each pair of points.
  2. Use a brute force approach to find the minimum spanning tree by trying all possible combinations of edges.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient for large inputs.

```cpp
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<vector<int>> edges;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                edges.push_back({cost, i, j});
            }
        }
        sort(edges.begin(), edges.end());
        int result = 0;
        vector<int> parent(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (auto& edge : edges) {
            int x = findParent(parent, edge[1]);
            int y = findParent(parent, edge[2]);
            if (x != y) {
                result += edge[0];
                parent[x] = y;
            }
        }
        return result;
    }
    
    int findParent(vector<int>& parent, int x) {
        if (parent[x] != x) {
            parent[x] = findParent(parent, parent[x]);
        }
        return parent[x];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n + n^2 \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n^2)$, for storing all edges.
> - **Why these complexities occur:** The time complexity is dominated by sorting the edges and finding the parent of each node. The space complexity is dominated by storing all edges.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use Kruskal's algorithm to find the minimum spanning tree.
- Detailed breakdown of the approach:
  1. Calculate the Manhattan distance between each pair of points.
  2. Use Kruskal's algorithm to find the minimum spanning tree.
- Proof of optimality: Kruskal's algorithm is guaranteed to find the minimum spanning tree.
- Why further optimization is impossible: Kruskal's algorithm has a time complexity of $O(n^2 \log n + n^2 \alpha(n))$, which is optimal for this problem.

```cpp
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<vector<int>> edges;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                edges.push_back({cost, i, j});
            }
        }
        sort(edges.begin(), edges.end());
        int result = 0;
        vector<int> parent(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (auto& edge : edges) {
            int x = findParent(parent, edge[1]);
            int y = findParent(parent, edge[2]);
            if (x != y) {
                result += edge[0];
                parent[x] = y;
            }
        }
        return result;
    }
    
    int findParent(vector<int>& parent, int x) {
        if (parent[x] != x) {
            parent[x] = findParent(parent, parent[x]);
        }
        return parent[x];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n + n^2 \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n^2)$, for storing all edges.
> - **Optimality proof:** Kruskal's algorithm is guaranteed to find the minimum spanning tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Kruskal's algorithm, minimum spanning tree, union-find data structure.
- Problem-solving patterns identified: using a union-find data structure to keep track of connected components.
- Optimization techniques learned: using Kruskal's algorithm to find the minimum spanning tree.
- Similar problems to practice: finding the minimum spanning tree of a graph, finding the minimum cost to connect all points in a graph.

**Mistakes to Avoid:**
- Common implementation errors: not using a union-find data structure to keep track of connected components, not sorting the edges by cost.
- Edge cases to watch for: duplicate points, points with the same x or y coordinate.
- Performance pitfalls: using a brute force approach to find the minimum spanning tree, not using Kruskal's algorithm.
- Testing considerations: testing the algorithm with different inputs, including edge cases and large inputs.