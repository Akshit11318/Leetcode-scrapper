## Clone Graph
**Problem Link:** https://leetcode.com/problems/clone-graph/description

**Problem Statement:**
- Input format: A reference to a `Node` object, where each `Node` has a `val` and a list of its neighbors.
- Constraints: The number of nodes in the graph is in the range `[0, 100]`.
- Expected output format: A reference to the cloned graph's corresponding node.
- Key requirements: Clone the graph and return the reference to the cloned node.
- Edge cases to consider: An empty graph (i.e., `nullptr`), a graph with a single node, and a graph with multiple nodes.
- Example test cases:
  - Cloning an empty graph should return `nullptr`.
  - Cloning a graph with a single node should return a new node with the same value and no neighbors.
  - Cloning a graph with multiple nodes should return a new graph with the same structure and values.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a new graph by iterating over each node in the original graph, cloning each node, and then iterating over each neighbor of the original node to clone the edges.
- Step-by-step breakdown of the solution:
  1. Create a new `Node` for each node in the original graph.
  2. Iterate over each neighbor of the original node and add the corresponding cloned node to the new node's neighbors.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem by creating a new copy of the graph.

```cpp
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        unordered_map<Node*, Node*> visited;
        
        function<Node*(Node*)> clone = [&](Node* node) {
            if (!node) return nullptr;
            if (visited.count(node)) return visited[node];
            
            Node* newNode = new Node(node->val);
            visited[node] = newNode;
            
            for (auto neighbor : node->neighbors) {
                newNode->neighbors.push_back(clone(neighbor));
            }
            
            return newNode;
        };
        
        return clone(node);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$, where $N$ is the number of nodes and $M$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(N)$, because we store each node in the `visited` map.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node and edge. The space complexity is linear because we store each node in the `visited` map to avoid revisiting nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a depth-first search (DFS) approach with memoization to avoid revisiting nodes.
- Detailed breakdown of the approach:
  1. Create a `visited` map to store the cloned nodes.
  2. Define a recursive DFS function to clone each node and its neighbors.
  3. If a node has already been cloned, return the cloned node from the `visited` map.
- Proof of optimality: This approach has the same time and space complexity as the brute force approach but is more efficient in practice because it avoids revisiting nodes.
- Why further optimization is impossible: The time complexity is already linear, and the space complexity is necessary to store the cloned nodes.

```cpp
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        unordered_map<Node*, Node*> visited;
        
        function<Node*(Node*)> clone = [&](Node* node) {
            if (!node) return nullptr;
            if (visited.count(node)) return visited[node];
            
            Node* newNode = new Node(node->val);
            visited[node] = newNode;
            
            for (auto neighbor : node->neighbors) {
                newNode->neighbors.push_back(clone(neighbor));
            }
            
            return newNode;
        };
        
        return clone(node);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$, where $N$ is the number of nodes and $M$ is the number of edges, because we visit each node and edge once.
> - **Space Complexity:** $O(N)$, because we store each node in the `visited` map.
> - **Optimality proof:** This approach is optimal because it has the same time and space complexity as the brute force approach but is more efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search, memoization, and graph traversal.
- Problem-solving patterns identified: Using a recursive function to solve a problem and storing intermediate results in a map to avoid revisiting nodes.
- Optimization techniques learned: Using memoization to avoid revisiting nodes and reducing the time complexity of the algorithm.
- Similar problems to practice: Other graph traversal problems, such as finding the shortest path between two nodes or detecting cycles in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check if a node has already been cloned before cloning it again.
- Edge cases to watch for: An empty graph (i.e., `nullptr`) and a graph with a single node.
- Performance pitfalls: Revisiting nodes multiple times, which can increase the time complexity of the algorithm.
- Testing considerations: Testing the algorithm with different types of graphs, including empty graphs, graphs with a single node, and graphs with multiple nodes and edges.