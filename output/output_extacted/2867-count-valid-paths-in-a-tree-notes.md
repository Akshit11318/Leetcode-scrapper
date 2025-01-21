## Count Valid Paths in a Tree
**Problem Link:** https://leetcode.com/problems/count-valid-paths-in-a-tree/description

**Problem Statement:**
- Input: An array `edges` of size `n` where `edges[i] = [a, b]` indicates that there is an edge between nodes `a` and `b` in a tree.
- Output: The number of valid paths in the tree, where a valid path is a path from a node to its descendant.
- Key requirements: The tree is undirected and connected.
- Edge cases: The input tree may be unbalanced, and the number of nodes `n` can vary.

**Example Test Cases:**
- For `edges = [[0,1],[0,2],[0,3],[1,4],[1,5]]`, the output is `10` because there are `10` valid paths: `[0,1]`, `[0,2]`, `[0,3]`, `[0,1,4]`, `[0,1,5]`, `[0,2]`, `[0,3]`, `[1,4]`, `[1,5]`, and `[0,1]`.
- For `edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]`, the output is `13` because there are `13` valid paths.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to perform a depth-first search (DFS) from each node and count the number of valid paths.
- We can use a recursive function to perform the DFS and count the number of valid paths.
- This approach comes to mind first because it is a straightforward way to solve the problem.

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int countValidPaths(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int count = 0;
        for (int i = 0; i < n; i++) {
            count += dfs(graph, i, -1);
        }
        
        return count;
    }
    
    int dfs(vector<vector<int>>& graph, int node, int parent) {
        int count = 0;
        for (int neighbor : graph[node]) {
            if (neighbor != parent) {
                count += 1 + dfs(graph, neighbor, node);
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot (n + m))$ where $n$ is the number of nodes and $m$ is the number of edges, because in the worst case, we perform a DFS from each node.
> - **Space Complexity:** $O(n + m)$ because we need to store the graph and the recursion stack.
> - **Why these complexities occur:** The time complexity occurs because we perform a DFS from each node, and the space complexity occurs because we need to store the graph and the recursion stack.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to perform a single DFS from an arbitrary node and count the number of valid paths.
- We can use a recursive function to perform the DFS and count the number of valid paths.
- This approach is optimal because it only requires a single DFS pass.

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int countValidPaths(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int count = 0;
        dfs(graph, 0, -1, count);
        
        return count;
    }
    
    void dfs(vector<vector<int>>& graph, int node, int parent, int& count) {
        count += graph[node].size();
        for (int neighbor : graph[node]) {
            if (neighbor != parent) {
                dfs(graph, neighbor, node, count);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of nodes and $m$ is the number of edges, because we only need to perform a single DFS pass.
> - **Space Complexity:** $O(n + m)$ because we need to store the graph and the recursion stack.
> - **Optimality proof:** This is the optimal solution because we only need to perform a single DFS pass to count the number of valid paths.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, graph traversal, and counting valid paths.
- Problem-solving patterns identified: using a recursive function to perform DFS and count valid paths.
- Optimization techniques learned: reducing the number of DFS passes from $n$ to $1$.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where a node has no neighbors.
- Edge cases to watch for: the input tree may be unbalanced, and the number of nodes $n$ can vary.
- Performance pitfalls: performing multiple DFS passes when a single pass is sufficient.
- Testing considerations: testing the solution with different input trees and verifying the correctness of the output.