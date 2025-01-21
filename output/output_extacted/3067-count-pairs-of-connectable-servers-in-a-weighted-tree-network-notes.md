## Count Pairs of Connectable Servers in a Weighted Tree Network

**Problem Link:** https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/description

**Problem Statement:**
- Input: A tree network represented as a graph with `n` nodes and `edges` list of weighted edges.
- Constraints: Each edge is represented as `[u, v, w]`, where `u` and `v` are nodes and `w` is the weight of the edge. The network is a tree, meaning it is connected and has no cycles.
- Expected Output: The number of pairs of servers that can be connected.
- Key Requirements: Two servers can be connected if there is a path between them with a total weight not exceeding the limit.
- Edge Cases: The limit can vary, and the tree structure ensures there is always a unique path between any two nodes.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible pair of servers and calculate the total weight of the path between them.
- Step-by-step breakdown:
  1. Generate all possible pairs of servers.
  2. For each pair, find the path between the servers using a depth-first search (DFS) or breadth-first search (BFS).
  3. Calculate the total weight of the path.
  4. If the total weight does not exceed the limit, count this pair as connectable.

```cpp
#include <vector>
using namespace std;

int countPairs(vector<vector<int>>& edges, int n, int limit) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].emplace_back(edge[1], edge[2]);
        graph[edge[1]].emplace_back(edge[0], edge[2]);
    }

    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int weight = dfs(graph, i, j, -1, limit);
            if (weight <= limit) {
                count++;
            }
        }
    }
    return count;
}

int dfs(vector<vector<pair<int, int>>>& graph, int start, int target, int parent, int limit) {
    if (start == target) {
        return 0;
    }
    int minWeight = INT_MAX;
    for (auto& neighbor : graph[start]) {
        if (neighbor.first != parent) {
            int weight = neighbor.second + dfs(graph, neighbor.first, target, start, limit);
            if (weight < minWeight) {
                minWeight = weight;
            }
        }
    }
    return minWeight;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of servers and $m$ is the number of edges, because we are checking every pair of servers and potentially traversing the entire tree for each pair.
> - **Space Complexity:** $O(n + m)$, for storing the graph and the recursion stack.
> - **Why these complexities occur:** The brute force approach involves generating all pairs of servers and then finding the shortest path between each pair, which leads to high time complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Since the network is a tree, we can use a single DFS traversal to calculate the distance from the root to all other nodes.
- Detailed breakdown:
  1. Choose an arbitrary node as the root.
  2. Perform a DFS traversal from the root to calculate the distance to all other nodes.
  3. For each node, calculate the number of other nodes within the limit.
  4. Sum up these counts, but since each pair is counted twice (once from each end), we need to divide the total count by 2.

```cpp
#include <vector>
using namespace std;

int countPairs(vector<vector<int>>& edges, int n, int limit) {
    vector<vector<pair<int, int>>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].emplace_back(edge[1], edge[2]);
        graph[edge[1]].emplace_back(edge[0], edge[2]);
    }

    int count = 0;
    vector<int> distances(n, 0);
    dfs(graph, 0, -1, distances, count, limit);
    return count;
}

void dfs(vector<vector<pair<int, int>>>& graph, int node, int parent, vector<int>& distances, int& count, int limit) {
    for (auto& neighbor : graph[node]) {
        if (neighbor.first != parent) {
            distances[neighbor.first] = distances[node] + neighbor.second;
            dfs(graph, neighbor.first, node, distances, count, limit);
        }
    }
    int localCount = 0;
    for (int i = 0; i < distances.size(); ++i) {
        if (distances[i] <= limit && i != node) {
            localCount++;
        }
    }
    count += localCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of servers and $m$ is the number of edges, because we perform a single DFS traversal.
> - **Space Complexity:** $O(n + m)$, for storing the graph and the recursion stack.
> - **Optimality proof:** This approach is optimal because it only requires a single traversal of the tree, leveraging the tree structure to efficiently calculate distances and count connectable pairs.

### Final Notes

**Learning Points:**
- The importance of leveraging the structure of the input data (in this case, a tree) to optimize the solution.
- Using DFS to efficiently traverse and calculate distances within the tree.
- Avoiding redundant calculations by performing a single traversal.

**Mistakes to Avoid:**
- Not considering the tree structure and attempting to apply more general graph algorithms.
- Failing to account for the fact that each pair is counted twice when calculating the total count.
- Not optimizing the solution for the specific constraints of the problem (e.g., the limit on the total weight of the path).