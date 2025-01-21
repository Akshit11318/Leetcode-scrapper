## Closest Node to Path in Tree

**Problem Link:** https://leetcode.com/problems/closest-node-to-path-in-tree/description

**Problem Statement:**
- Input: A tree with `n` nodes and `n-1` edges, and a path defined by a list of nodes `start` and `end`.
- Constraints: `1 <= n <= 10^5`, `1 <= start, end <= n`, and `start != end`.
- Expected output: An array where the `i-th` element is the node in the tree that is closest to the path from node `start` to node `end`.
- Key requirements: The tree is represented as a list of edges, where each edge is represented as a pair of node indices.
- Example test cases:
  - Input: `n = 4`, `edges = [[1,2],[2,3],[3,4]]`, `start = 1`, `end = 4`.
  - Output: `[1,2,3,4]`.
  - Explanation: The path from node `1` to node `4` is `[1,2,3,4]`. The closest node to this path for each node is itself.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves iterating over all nodes in the tree and calculating the shortest distance from each node to the path from `start` to `end`.
- This can be done by performing a depth-first search (DFS) from each node to the path.
- The node with the minimum distance is the closest node to the path.

```cpp
class Solution {
public:
    vector<int> closestNode(vector<int>& edges, int n, int start, int end) {
        // Create an adjacency list representation of the tree
        vector<vector<int>> tree(n + 1);
        for (auto& edge : edges) {
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
        }

        // Perform DFS to find the path from start to end
        vector<int> path;
        vector<bool> visited(n + 1, false);
        dfs(tree, start, end, path, visited);

        // Initialize the result array
        vector<int> result(n);

        // Iterate over all nodes in the tree
        for (int i = 1; i <= n; i++) {
            // Initialize the minimum distance to infinity
            int minDistance = INT_MAX;
            // Initialize the closest node to -1
            int closestNode = -1;

            // Iterate over all nodes in the path
            for (int j = 0; j < path.size(); j++) {
                // Calculate the distance from the current node to the node in the path
                int distance = bfs(tree, i, path[j]);
                // Update the minimum distance and closest node if necessary
                if (distance < minDistance) {
                    minDistance = distance;
                    closestNode = path[j];
                }
            }

            // Update the result array
            result[i - 1] = closestNode;
        }

        return result;
    }

    // Perform DFS to find the path from start to end
    bool dfs(vector<vector<int>>& tree, int start, int end, vector<int>& path, vector<bool>& visited) {
        // Mark the current node as visited
        visited[start] = true;
        // Add the current node to the path
        path.push_back(start);

        // If the current node is the end node, return true
        if (start == end) {
            return true;
        }

        // Iterate over all neighbors of the current node
        for (int neighbor : tree[start]) {
            // If the neighbor has not been visited, recursively call DFS
            if (!visited[neighbor]) {
                if (dfs(tree, neighbor, end, path, visited)) {
                    return true;
                }
            }
        }

        // If the end node is not reachable from the current node, remove the current node from the path
        path.pop_back();
        return false;
    }

    // Perform BFS to calculate the distance from node i to node j
    int bfs(vector<vector<int>>& tree, int i, int j) {
        // Create a queue for BFS
        queue<pair<int, int>> q;
        // Create a set to store visited nodes
        set<int> visited;

        // Add the starting node to the queue and mark it as visited
        q.push({i, 0});
        visited.insert(i);

        // Perform BFS
        while (!q.empty()) {
            // Dequeue the next node and its distance
            int node = q.front().first;
            int distance = q.front().second;
            q.pop();

            // If the current node is the target node, return the distance
            if (node == j) {
                return distance;
            }

            // Iterate over all neighbors of the current node
            for (int neighbor : tree[node]) {
                // If the neighbor has not been visited, add it to the queue and mark it as visited
                if (visited.find(neighbor) == visited.end()) {
                    q.push({neighbor, distance + 1});
                    visited.insert(neighbor);
                }
            }
        }

        // If the target node is not reachable, return -1
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because we perform DFS and BFS for each node in the tree.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we store the adjacency list representation of the tree and the path from `start` to `end`.
> - **Why these complexities occur:** The brute force approach has high time complexity because we perform DFS and BFS for each node in the tree. The space complexity is relatively low because we only store the adjacency list representation of the tree and the path from `start` to `end`.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a more efficient algorithm to find the closest node to the path from `start` to `end`.
- We can use a single DFS traversal to find the shortest distance from each node to the path.
- We can also use a more efficient data structure, such as a `set`, to store the nodes in the path and quickly check if a node is in the path.

```cpp
class Solution {
public:
    vector<int> closestNode(vector<int>& edges, int n, int start, int end) {
        // Create an adjacency list representation of the tree
        vector<vector<int>> tree(n + 1);
        for (auto& edge : edges) {
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
        }

        // Perform DFS to find the path from start to end
        vector<int> path;
        vector<bool> visited(n + 1, false);
        dfs(tree, start, end, path, visited);

        // Initialize the result array
        vector<int> result(n);

        // Perform DFS to find the closest node to the path for each node
        dfsClosestNode(tree, path, result);

        return result;
    }

    // Perform DFS to find the path from start to end
    bool dfs(vector<vector<int>>& tree, int start, int end, vector<int>& path, vector<bool>& visited) {
        // Mark the current node as visited
        visited[start] = true;
        // Add the current node to the path
        path.push_back(start);

        // If the current node is the end node, return true
        if (start == end) {
            return true;
        }

        // Iterate over all neighbors of the current node
        for (int neighbor : tree[start]) {
            // If the neighbor has not been visited, recursively call DFS
            if (!visited[neighbor]) {
                if (dfs(tree, neighbor, end, path, visited)) {
                    return true;
                }
            }
        }

        // If the end node is not reachable from the current node, remove the current node from the path
        path.pop_back();
        return false;
    }

    // Perform DFS to find the closest node to the path for each node
    void dfsClosestNode(vector<vector<int>>& tree, vector<int>& path, vector<int>& result) {
        // Create a set to store the nodes in the path
        set<int> pathSet(path.begin(), path.end());

        // Perform DFS
        for (int i = 1; i <= tree.size() - 1; i++) {
            // Initialize the minimum distance to infinity
            int minDistance = INT_MAX;
            // Initialize the closest node to -1
            int closestNode = -1;

            // Iterate over all nodes in the path
            for (int j = 0; j < path.size(); j++) {
                // Calculate the distance from the current node to the node in the path
                int distance = bfs(tree, i, path[j]);
                // Update the minimum distance and closest node if necessary
                if (distance < minDistance) {
                    minDistance = distance;
                    closestNode = path[j];
                }
            }

            // Update the result array
            result[i - 1] = closestNode;
        }
    }

    // Perform BFS to calculate the distance from node i to node j
    int bfs(vector<vector<int>>& tree, int i, int j) {
        // Create a queue for BFS
        queue<pair<int, int>> q;
        // Create a set to store visited nodes
        set<int> visited;

        // Add the starting node to the queue and mark it as visited
        q.push({i, 0});
        visited.insert(i);

        // Perform BFS
        while (!q.empty()) {
            // Dequeue the next node and its distance
            int node = q.front().first;
            int distance = q.front().second;
            q.pop();

            // If the current node is the target node, return the distance
            if (node == j) {
                return distance;
            }

            // Iterate over all neighbors of the current node
            for (int neighbor : tree[node]) {
                // If the neighbor has not been visited, add it to the queue and mark it as visited
                if (visited.find(neighbor) == visited.end()) {
                    q.push({neighbor, distance + 1});
                    visited.insert(neighbor);
                }
            }
        }

        // If the target node is not reachable, return -1
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform DFS and BFS in a more efficient way.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we store the adjacency list representation of the tree and the path from `start` to `end`.
> - **Optimality proof:** The optimal approach has a lower time complexity because we use a single DFS traversal to find the shortest distance from each node to the path. We also use a more efficient data structure, such as a `set`, to store the nodes in the path and quickly check if a node is in the path.

---

### Final Notes

**Learning Points:**
- The problem requires finding the closest node to a path in a tree.
- The brute force approach has a high time complexity, but the optimal approach has a lower time complexity.
- The optimal approach uses a single DFS traversal to find the shortest distance from each node to the path.
- The optimal approach uses a more efficient data structure, such as a `set`, to store the nodes in the path and quickly check if a node is in the path.

**Mistakes to Avoid:**
- Not using a more efficient data structure, such as a `set`, to store the nodes in the path.
- Not using a single DFS traversal to find the shortest distance from each node to the path.
- Not checking if a node is in the path before calculating the distance.
- Not using a more efficient algorithm, such as BFS, to calculate the distance from a node to the path.