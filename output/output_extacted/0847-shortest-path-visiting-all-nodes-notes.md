## Shortest Path Visiting All Nodes

**Problem Link:** https://leetcode.com/problems/shortest-path-visiting-all-nodes/description

**Problem Statement:**
- Input format and constraints: The problem takes a graph represented as an adjacency list `graph` with `n` nodes as input, where `graph[i]` is a list of nodes directly connected to node `i`. The task is to find the shortest path that visits all nodes exactly once and returns to the starting node.
- Expected output format: The output should be the length of the shortest path.
- Key requirements and edge cases to consider: The graph is guaranteed to be connected, and all nodes must be visited exactly once before returning to the starting node.
- Example test cases with explanations: For instance, given a graph with 4 nodes where each node is connected to every other node, the shortest path would involve visiting each node in any order and then returning to the start, resulting in a total path length of 4 (or 3 if the path doesn't require returning to the start).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible permutations of nodes (since the order matters) and calculate the total distance for each permutation. This involves calculating the distance between each pair of consecutive nodes in the permutation and summing these distances.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of nodes from 0 to n-1.
  2. For each permutation, calculate the total distance by summing the distances between consecutive nodes in the permutation.
  3. Keep track of the minimum total distance found across all permutations.
- Why this approach comes to mind first: It's a straightforward, exhaustive method that ensures all possible paths are considered.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int shortestPathLength(vector<vector<int>>& graph) {
    int n = graph.size();
    int minPathLength = INT_MAX;

    // Function to calculate the distance of a path
    auto calculatePathDistance = [&](const vector<int>& path) {
        int distance = 0;
        for (int i = 0; i < path.size() - 1; ++i) {
            distance += graph[path[i]].size(); // Assuming distance between connected nodes is 1
        }
        return distance;
    };

    // Generate all permutations of nodes
    vector<int> nodes(n);
    for (int i = 0; i < n; ++i) nodes[i] = i;
    do {
        int pathLength = calculatePathDistance(nodes);
        minPathLength = min(minPathLength, pathLength);
    } while (next_permutation(nodes.begin(), nodes.end()));

    return minPathLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of nodes, because there are $n!$ permutations of $n$ nodes, and for each permutation, we calculate the path length which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, for storing the current permutation of nodes.
> - **Why these complexities occur:** The brute force approach generates all permutations of nodes, leading to a factorial time complexity. The space complexity is linear because we only need to store the current permutation being processed.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations, we can use a bitmask to represent the set of visited nodes. This approach is known as bitmasking or bit manipulation and is commonly used in problems involving subsets or permutations.
- Detailed breakdown of the approach:
  1. Initialize a queue with the starting node and a bitmask representing the visited nodes.
  2. Perform a BFS, where each state is a node and a bitmask of visited nodes.
  3. When a node is visited, update the bitmask to mark the node as visited.
  4. If all nodes have been visited (i.e., the bitmask has all bits set), return the current path length.
- Proof of optimality: This approach is optimal because it explores all possible paths in a systematic way, ensuring that the shortest path that visits all nodes is found.
- Why further optimization is impossible: This approach has a time complexity of $O(n \cdot 2^n)$, which is the best possible for this problem since we must consider all subsets of nodes.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int shortestPathLength(vector<vector<int>>& graph) {
    int n = graph.size();
    queue<pair<int, int>> q; // Node, bitmask
    vector<vector<bool>> visited(n, vector<bool>(1 << n, false));
    int steps = 0;

    // Initialize queue with all nodes as starting points
    for (int i = 0; i < n; ++i) {
        q.push({i, 1 << i}); // Bitmask with only the current node set
        visited[i][1 << i] = true;
    }

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; ++i) {
            auto [node, bitmask] = q.front(); q.pop();
            // If all nodes have been visited
            if (bitmask == (1 << n) - 1) return steps;

            // Explore neighbors
            for (int neighbor : graph[node]) {
                int newBitmask = bitmask | (1 << neighbor);
                if (!visited[neighbor][newBitmask]) {
                    q.push({neighbor, newBitmask});
                    visited[neighbor][newBitmask] = true;
                }
            }
        }
        steps++;
    }

    return -1; // Should not reach here if the graph is connected
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n)$, where $n$ is the number of nodes. The reason is that in the worst case, we might need to explore all possible subsets of nodes (represented by the bitmask), and for each subset, we perform a constant amount of work.
> - **Space Complexity:** $O(n \cdot 2^n)$, for storing the visited states.
> - **Optimality proof:** This approach ensures that the shortest path visiting all nodes is found by systematically exploring all possible paths in a breadth-first manner, which guarantees finding the shortest path first.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitmasking, BFS.
- Problem-solving patterns identified: Using bitmasks to represent subsets or permutations of items.
- Optimization techniques learned: Avoiding unnecessary computation by using visited states.
- Similar problems to practice: Other problems involving permutations, subsets, or graph traversals.

**Mistakes to Avoid:**
- Common implementation errors: Not correctly updating the bitmask or not checking for visited states.
- Edge cases to watch for: Handling disconnected graphs or graphs with self-loops.
- Performance pitfalls: Not using an efficient data structure for storing visited states.
- Testing considerations: Ensure to test with graphs of varying sizes and connectivity.