## Tree Diameter
**Problem Link:** https://leetcode.com/problems/tree-diameter/description

**Problem Statement:**
- Input format: The input is given as a graph represented by an adjacency list `edges`.
- Constraints: The number of nodes in the graph is given as `n`.
- Expected output format: The function should return the length of the diameter of the tree.
- Key requirements and edge cases to consider: The tree is not necessarily connected, and we need to find the longest path between any two nodes in the tree.
- Example test cases with explanations:
  - For example, given `n = 4` and `edges = [[1, 0], [1, 2], [1, 3]]`, the output should be `3` because the longest path is `0 -> 1 -> 2` or `0 -> 1 -> 3`.
  - For example, given `n = 2` and `edges = [[1, 0]]`, the output should be `1` because the longest path is `0 -> 1`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves finding all possible paths between all pairs of nodes in the tree and then finding the longest path.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list to represent the tree.
  2. Use depth-first search (DFS) to find all possible paths between all pairs of nodes.
  3. Keep track of the longest path found so far.
- Why this approach comes to mind first: This approach is straightforward and involves a simple DFS traversal of the tree.

```cpp
class Solution {
public:
    int treeDiameter(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adjList(n);
        for (auto& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        
        int maxDiameter = 0;
        for (int i = 0; i < n; i++) {
            vector<bool> visited(n, false);
            int maxDepth = dfs(i, adjList, visited);
            maxDiameter = max(maxDiameter, maxDepth);
        }
        
        return maxDiameter;
    }
    
    int dfs(int node, vector<vector<int>>& adjList, vector<bool>& visited) {
        visited[node] = true;
        int maxDepth = 0;
        for (int neighbor : adjList[node]) {
            if (!visited[neighbor]) {
                maxDepth = max(maxDepth, 1 + dfs(neighbor, adjList, visited));
            }
        }
        visited[node] = false;
        return maxDepth;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we are performing DFS from each node, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$ because we need to store the adjacency list and the visited array.
> - **Why these complexities occur:** The time complexity is high because we are performing DFS from each node, and the space complexity is moderate because we need to store the adjacency list and the visited array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of finding all possible paths between all pairs of nodes, we can find the longest path by performing DFS twice: once to find the farthest node from an arbitrary node, and then again to find the farthest node from the first farthest node.
- Detailed breakdown of the approach:
  1. Perform DFS from an arbitrary node to find the farthest node.
  2. Perform DFS again from the farthest node to find the longest path.
- Proof of optimality: This approach is optimal because it only requires two DFS traversals, which reduces the time complexity significantly.
- Why further optimization is impossible: This approach is already optimal because it only requires two DFS traversals, which is the minimum required to find the longest path.

```cpp
class Solution {
public:
    int treeDiameter(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adjList(n);
        for (auto& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        
        int farthestNode = dfs(0, adjList);
        int maxDiameter = dfs(farthestNode, adjList);
        
        return maxDiameter;
    }
    
    int dfs(int node, vector<vector<int>>& adjList) {
        vector<bool> visited(adjList.size(), false);
        return dfsHelper(node, adjList, visited);
    }
    
    int dfsHelper(int node, vector<vector<int>>& adjList, vector<bool>& visited) {
        visited[node] = true;
        int maxDepth = 0;
        int farthestNode = node;
        for (int neighbor : adjList[node]) {
            if (!visited[neighbor]) {
                int depth = 1 + dfsHelper(neighbor, adjList, visited);
                if (depth > maxDepth) {
                    maxDepth = depth;
                    farthestNode = neighbor;
                }
            }
        }
        visited[node] = false;
        if (node == 0) {
            return farthestNode;
        } else {
            return maxDepth;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are performing DFS twice, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$ because we need to store the adjacency list and the visited array.
> - **Optimality proof:** This approach is optimal because it only requires two DFS traversals, which reduces the time complexity significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, graph traversal, longest path.
- Problem-solving patterns identified: finding the longest path in a tree.
- Optimization techniques learned: reducing the number of DFS traversals.
- Similar problems to practice: finding the longest path in a graph, finding the shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not using visited array.
- Edge cases to watch for: empty graph, graph with one node.
- Performance pitfalls: using brute force approach, not optimizing DFS traversals.
- Testing considerations: testing with different graph sizes, testing with different graph structures.