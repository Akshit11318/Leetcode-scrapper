## Find Eventual Safe States

**Problem Link:** [https://leetcode.com/problems/find-eventual-safe-states/description](https://leetcode.com/problems/find-eventual-safe-states/description)

**Problem Statement:**
- Input format: A graph represented as a 2D vector `graph` where `graph[i]` is a list of nodes that can be directly reached from node `i`.
- Constraints: `1 <= graph.length <= 10^4`, `0 <= graph[i].length <= 10^4`, `0 <= graph[i][j] <= graph.length - 1`.
- Expected output format: A vector of integers representing the eventual safe states.
- Key requirements: Identify nodes that can reach a cycle as not safe and those that cannot reach a cycle as safe.
- Example test cases:
  - `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`, the output should be `[2,4,5,6]`.
  - `graph = [[1,2,3,4],[1,2],[3,4],[0,4],[3,5],[0]`, the output should be `[]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) from each node to check if it can reach a cycle.
- Step-by-step breakdown:
  1. Start DFS from each node.
  2. Mark the current node as visited.
  3. For each neighbor of the current node:
    - If the neighbor is already visited and in the current DFS path, it means a cycle is detected, so mark the current node as not safe.
    - If the neighbor is not visited, continue DFS from the neighbor.
  4. If DFS completes without finding a cycle, mark the current node as safe.
- Why this approach comes to mind first: It directly addresses the requirement to identify nodes that can reach a cycle.

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> result;
        vector<bool> visited(n, false);
        vector<bool> safe(n, false);
        
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                dfs(graph, i, visited, safe);
            }
        }
        
        for (int i = 0; i < n; ++i) {
            if (safe[i]) {
                result.push_back(i);
            }
        }
        
        return result;
    }
    
    void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited, vector<bool>& safe) {
        visited[node] = true;
        bool isSafe = true;
        
        for (int neighbor : graph[node]) {
            if (visited[neighbor]) {
                isSafe = false;
            } else if (!safe[neighbor]) {
                dfs(graph, neighbor, visited, safe);
                if (!safe[neighbor]) {
                    isSafe = false;
                }
            }
        }
        
        safe[node] = isSafe;
        visited[node] = false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$ where $N$ is the number of nodes and $M$ is the number of edges, since each node and edge is visited once.
> - **Space Complexity:** $O(N)$ for the visited and safe vectors.
> - **Why these complexities occur:** The algorithm visits each node and edge once, resulting in linear time complexity. The space complexity is due to the additional vectors used to keep track of visited and safe nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of performing DFS from each node, we can perform a reverse DFS from all nodes that have no outgoing edges, as these are guaranteed to be safe.
- Detailed breakdown:
  1. Identify nodes with no outgoing edges as the initial set of safe nodes.
  2. Perform reverse DFS from these safe nodes to mark all nodes that can reach them as safe.
  3. Continue this process until no new safe nodes are added.
- Proof of optimality: This approach ensures that all safe nodes are identified in the minimum number of iterations, as it starts from the nodes that are guaranteed to be safe and propagates this safety information to all reachable nodes.

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> result;
        vector<int> outDegree(n, 0);
        vector<vector<int>> reverseGraph(n);
        
        for (int i = 0; i < n; ++i) {
            outDegree[i] = graph[i].size();
            for (int neighbor : graph[i]) {
                reverseGraph[neighbor].push_back(i);
            }
        }
        
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (outDegree[i] == 0) {
                q.push(i);
            }
        }
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            result.push_back(node);
            
            for (int neighbor : reverseGraph[node]) {
                outDegree[neighbor]--;
                if (outDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        sort(result.begin(), result.end());
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$ where $N$ is the number of nodes and $M$ is the number of edges, as each node and edge is visited once.
> - **Space Complexity:** $O(N + M)$ for the outDegree and reverseGraph vectors.
> - **Optimality proof:** This approach is optimal as it identifies all safe nodes in a single pass through the graph, without the need for recursive DFS calls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph traversal, reverse DFS, and the use of queues for efficient node processing.
- Problem-solving patterns identified: Identifying safe nodes in a graph by propagating safety information from nodes with no outgoing edges.
- Optimization techniques learned: Using reverse DFS to reduce the number of iterations required to identify all safe nodes.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling nodes with multiple outgoing edges, or failing to properly update the outDegree vector.
- Edge cases to watch for: Graphs with self-loops or multiple edges between the same pair of nodes.
- Performance pitfalls: Using recursive DFS calls instead of a queue-based approach, which can lead to increased time complexity and stack overflow errors.
- Testing considerations: Thoroughly testing the implementation with various graph structures, including cycles, self-loops, and nodes with multiple outgoing edges.