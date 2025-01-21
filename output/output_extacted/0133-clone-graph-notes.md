## Clone Graph
**Problem Link:** https://leetcode.com/problems/clone-graph/description

**Problem Statement:**
- Input format: A `Node` object representing a graph where each node has a `val`, `neighbors` list, and a method to clone the graph.
- Constraints: The number of nodes in the graph is in the range `[0, 100]`.
- Expected output format: A `Node` object representing the cloned graph.
- Key requirements and edge cases to consider:
  - The graph may contain cycles.
  - The graph may be empty.
  - The graph may contain nodes with no neighbors.
- Example test cases with explanations:
  - Cloning a graph with a single node.
  - Cloning a graph with multiple nodes and edges.
  - Cloning an empty graph.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Create a new node for each node in the original graph, then iterate through each node's neighbors and clone them recursively.
- Step-by-step breakdown of the solution:
  1. Create a new node for the current node.
  2. Iterate through each neighbor of the current node.
  3. Recursively clone each neighbor.
  4. Add the cloned neighbors to the cloned node's neighbors list.
- Why this approach comes to mind first: It's a straightforward, recursive approach that directly addresses the problem statement.

```cpp
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        // Create a new node for the current node
        Node* newNode = new Node(node->val);
        
        // Iterate through each neighbor of the current node
        for (Node* neighbor : node->neighbors) {
            // Recursively clone each neighbor
            Node* newNeighbor = cloneGraph(neighbor);
            // Add the cloned neighbors to the cloned node's neighbors list
            newNode->neighbors.push_back(newNeighbor);
        }
        
        return newNode;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$, where $N$ is the number of nodes and $M$ is the number of edges, because we visit each node and edge once. However, this approach has an exponential time complexity due to the recursive cloning of neighbors, resulting in $O(2^N)$ in the worst case.
> - **Space Complexity:** $O(N + M)$, because we create a new node for each node in the original graph and store the cloned nodes in the neighbors list.
> - **Why these complexities occur:** The recursive cloning of neighbors causes the exponential time complexity, while the creation of new nodes and storage of cloned nodes in the neighbors list results in the linear space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a depth-first search (DFS) approach with a `visited` map to keep track of cloned nodes and avoid revisiting them.
- Detailed breakdown of the approach:
  1. Create a `visited` map to store the cloned nodes.
  2. Perform a DFS traversal of the graph, starting from the given node.
  3. For each node, check if it has been visited before. If not, create a new node and add it to the `visited` map.
  4. Iterate through each neighbor of the current node and recursively clone them using the DFS approach.
- Proof of optimality: This approach ensures that each node is visited only once, resulting in a linear time complexity.

```cpp
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        unordered_map<Node*, Node*> visited;
        
        function<Node*(Node*)> dfs = [&](Node* curr) {
            if (visited.count(curr)) return visited[curr];
            
            Node* newNode = new Node(curr->val);
            visited[curr] = newNode;
            
            for (Node* neighbor : curr->neighbors) {
                newNode->neighbors.push_back(dfs(neighbor));
            }
            
            return newNode;
        };
        
        return dfs(node);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$, where $N$ is the number of nodes and $M$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(N + M)$, because we create a new node for each node in the original graph and store the cloned nodes in the `visited` map and neighbors list.
> - **Optimality proof:** This approach ensures that each node is visited only once, resulting in a linear time complexity, making it the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), recursive cloning, and using a `visited` map to avoid revisiting nodes.
- Problem-solving patterns identified: Using a `visited` map to keep track of cloned nodes and avoiding recursive cloning of neighbors.
- Optimization techniques learned: Using DFS with a `visited` map to reduce time complexity from exponential to linear.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a node has been visited before cloning it, resulting in infinite recursion.
- Edge cases to watch for: Empty graphs, graphs with a single node, and graphs with cycles.
- Performance pitfalls: Recursive cloning of neighbors without using a `visited` map, resulting in exponential time complexity.
- Testing considerations: Testing the solution with different graph structures, including empty graphs, single-node graphs, and graphs with cycles.