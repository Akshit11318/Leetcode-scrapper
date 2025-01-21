## Redundant Connection II
**Problem Link:** https://leetcode.com/problems/redundant-connection-ii/description

**Problem Statement:**
- Input: An array of `edges` where `edges[i] = [u, v]` represents a connection between nodes `u` and `v`.
- Constraints: `1 <= n <= 1000`, `0 <= edges.length <= n`, `edges[i].length == 2`, `1 <= u, v <= n`.
- Expected Output: The redundant connection that causes a cycle in the graph.
- Key Requirements: The graph must not have a cycle for it to be valid. Identify the connection that introduces the cycle.
- Edge Cases: 
  - The graph may have multiple cycles.
  - There might be multiple redundant connections.

**Example Test Cases:**
- `edges = [[1,2],[1,3],[2,3]]`, Output: `[2,3]`.
- `edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]`, Output: `[1,4]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subset of connections to see if they introduce a cycle into the graph.
- We can use a depth-first search (DFS) to detect cycles in the graph.
- For each edge, we temporarily remove it and check if the graph has a cycle. If removing the edge eliminates the cycle, it's the redundant connection.

```cpp
class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n + 1);
        vector<int> candidate1, candidate2;
        for (auto& edge : edges) {
            if (parent[edge[1]] != 0) {
                candidate1 = {parent[edge[1]], edge[1]};
                candidate2 = edge;
                edge[1] = 0; // Temporarily remove this edge
            } else {
                parent[edge[1]] = edge[0];
            }
        }
        
        vector<int> root(n + 1);
        for (int i = 1; i <= n; i++) root[i] = i;
        
        for (auto& edge : edges) {
            if (edge[1] == 0) continue; // Skip the edge we temporarily removed
            int rootX = find(root, edge[0]);
            int rootY = find(root, edge[1]);
            if (rootX == rootY) {
                if (candidate1.empty()) return edge;
                else return candidate1;
            }
            root[rootY] = rootX;
        }
        
        return candidate2;
    }
    
    int find(vector<int>& root, int x) {
        return root[x] == x ? x : root[x] = find(root, root[x]);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to the DFS traversal for cycle detection.
> - **Space Complexity:** $O(n)$ for storing the parent and root arrays.
> - **Why these complexities occur:** The brute force approach involves checking all possible subsets of connections, leading to high time complexity. The space complexity is due to the need to store the parent and root information for each node.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use Union-Find to detect cycles in the graph efficiently.
- We maintain two arrays: `parent` to track the parent of each node and `root` to track the root of each connected component.
- We iterate over the edges, and for each edge, we check if the destination node has a parent. If it does, it means we've found a candidate for the redundant connection.
- We then use Union-Find to detect cycles in the graph. If we find a cycle, we return the candidate connection.

```cpp
class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n + 1), root(n + 1);
        vector<int> candidate1, candidate2;
        for (auto& edge : edges) {
            if (parent[edge[1]] != 0) {
                candidate1 = {parent[edge[1]], edge[1]};
                candidate2 = edge;
            } else {
                parent[edge[1]] = edge[0];
            }
        }
        
        for (int i = 1; i <= n; i++) root[i] = i;
        
        for (auto& edge : edges) {
            if (edge[1] == 0) continue;
            int rootX = find(root, edge[0]);
            int rootY = find(root, edge[1]);
            if (rootX == rootY) {
                if (candidate1.empty()) return edge;
                else return candidate1;
            }
            root[rootY] = rootX;
        }
        
        return candidate2;
    }
    
    int find(vector<int>& root, int x) {
        return root[x] == x ? x : root[x] = find(root, root[x]);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n)$ for storing the parent and root arrays.
> - **Optimality proof:** This approach is optimal because it uses Union-Find to detect cycles in the graph efficiently, reducing the time complexity significantly.

---

### Final Notes

**Learning Points:**
- **Union-Find** is a powerful technique for detecting cycles in graphs.
- **Path compression** and **union by rank** can optimize the Union-Find algorithm.
- **Graph traversal** techniques, such as DFS, can be used to detect cycles in graphs.

**Mistakes to Avoid:**
- Not handling the case where the destination node has a parent.
- Not using Union-Find to detect cycles in the graph efficiently.
- Not optimizing the Union-Find algorithm using path compression and union by rank.
- Not considering the candidate connection when detecting cycles in the graph.