## Longest Cycle in a Graph
**Problem Link:** https://leetcode.com/problems/longest-cycle-in-a-graph/description

**Problem Statement:**
- Input: A graph represented as a list of edges `edges` where each edge is a pair of nodes.
- Constraints: The graph is directed, and each node is represented by an integer from 1 to `n`, where `n` is the number of nodes.
- Expected Output: The length of the longest cycle in the graph. If no cycle exists, return `-1`.
- Key Requirements:
  - A cycle is defined as a path that starts and ends at the same node and passes through at least one edge.
  - The graph may contain multiple cycles, and we are interested in the longest one.
- Example Test Cases:
  - Input: `edges = [[3,3],[4,4],[5,6],[6,7],[7,5]]`, Output: `4` because the longest cycle is `5 -> 6 -> 7 -> 5`.
  - Input: `edges = [[1,2],[2,3],[3,4]]`, Output: `-1` because there is no cycle.

---

### Brute Force Approach
**Explanation:**
- Initial Thought Process: The first approach that comes to mind is to use a depth-first search (DFS) to explore all possible paths from each node and keep track of the longest cycle found.
- Step-by-Step Breakdown:
  1. Initialize the longest cycle length to `-1`.
  2. For each node in the graph, perform a DFS starting from that node.
  3. During the DFS, keep track of the current path and its length.
  4. If a cycle is detected (i.e., we reach a node that is already in the current path), update the longest cycle length if the current cycle is longer.
  5. Backtrack and explore other paths.
- Why This Approach Comes to Mind First: It's a straightforward, brute-force approach that guarantees finding the longest cycle if one exists, but it's inefficient due to its high time complexity.

```cpp
#include <vector>
using namespace std;

int longestCycle(vector<vector<int>>& edges) {
    int n = edges.size();
    vector<vector<int>> graph(n + 1);
    for (int i = 0; i < n; i++) {
        if (edges[i][0] != -1) {
            graph[edges[i][0]].push_back(edges[i][1]);
        }
    }

    int longest = -1;
    for (int i = 1; i <= n; i++) {
        vector<bool> visited(n + 1, false);
        vector<int> currentPath;
        dfs(graph, i, visited, currentPath, longest);
    }
    return longest;
}

void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited, vector<int>& currentPath, int& longest) {
    visited[node] = true;
    currentPath.push_back(node);
    for (int neighbor : graph[node]) {
        if (visited[neighbor]) {
            // Cycle detected, update longest cycle if necessary
            int cycleLength = currentPath.size() - (lower_bound(currentPath.begin(), currentPath.end(), neighbor) - currentPath.begin());
            longest = max(longest, cycleLength);
        } else {
            dfs(graph, neighbor, visited, currentPath, longest);
        }
    }
    currentPath.pop_back();
    visited[node] = false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n)$, where $n$ is the number of nodes. This is because in the worst case, we might explore all possible subsets of nodes (each node can either be included or not in a path, leading to $2^n$ possibilities) from each starting node.
> - **Space Complexity:** $O(n)$ for storing the visited nodes and the current path.
> - **Why These Complexities Occur:** The exponential time complexity comes from the brute-force exploration of all possible paths, which is inefficient for large graphs.

---

### Optimal Approach (Required)
**Explanation:**
- Key Insight: Instead of exploring all possible paths, we can use a single DFS traversal to detect cycles and keep track of the longest one. This is because a cycle will always have a node that is visited again after some number of steps, and we can use a timestamp to track when each node was first visited.
- Detailed Breakdown:
  1. Initialize the longest cycle length to `-1`.
  2. Perform a DFS traversal of the graph, keeping track of the timestamp when each node is first visited and the current path.
  3. If a node is visited again and it's within the current path (i.e., its timestamp is less than the current timestamp), a cycle is detected. Update the longest cycle length if the current cycle is longer.
- Proof of Optimality: This approach is optimal because it explores the graph only once, avoiding the exponential complexity of the brute-force approach, and it guarantees finding the longest cycle by tracking the timestamps of visited nodes.

```cpp
#include <vector>
using namespace std;

int longestCycle(vector<vector<int>>& edges) {
    int n = edges.size();
    vector<vector<int>> graph(n + 1);
    for (int i = 0; i < n; i++) {
        if (edges[i][0] != -1) {
            graph[edges[i][0]].push_back(edges[i][1]);
        }
    }

    int longest = -1;
    vector<bool> visited(n + 1, false);
    vector<int> timestamp(n + 1, -1);
    int time = 1;
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            longest = max(longest, dfs(graph, i, visited, timestamp, time));
            time++;
        }
    }
    return longest;
}

int dfs(vector<vector<int>>& graph, int node, vector<bool>& visited, vector<int>& timestamp, int& time) {
    visited[node] = true;
    timestamp[node] = time;
    int longest = -1;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            longest = max(longest, dfs(graph, neighbor, visited, timestamp, time + 1));
        } else if (timestamp[neighbor] >= 0 && timestamp[neighbor] < timestamp[node]) {
            // Cycle detected, update longest cycle if necessary
            longest = max(longest, timestamp[node] - timestamp[neighbor]);
        }
    }
    timestamp[node] = -1; // Reset timestamp to indicate node is no longer in the current path
    return longest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges. This is because we visit each node and edge once during the DFS traversal.
> - **Space Complexity:** $O(n)$ for storing the visited nodes and their timestamps.
> - **Optimality Proof:** This approach is optimal because it has a linear time complexity with respect to the size of the input graph, which is the best we can achieve for detecting cycles in a graph.

---

### Final Notes

**Learning Points:**
- The importance of understanding graph traversal algorithms like DFS.
- How to detect cycles in a graph efficiently.
- The use of timestamps to keep track of visited nodes and detect cycles.

**Mistakes to Avoid:**
- Not resetting the timestamp of a node after it's no longer in the current path, which can lead to incorrect cycle detection.
- Not checking if a neighbor has been visited before exploring it, which can result in incorrect longest cycle length.
- Not considering the case where a node has no outgoing edges, which should be handled properly in the DFS traversal.