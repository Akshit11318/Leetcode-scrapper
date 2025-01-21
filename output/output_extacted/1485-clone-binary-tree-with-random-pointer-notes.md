## Clone Binary Tree with Random Pointer

**Problem Link:** https://leetcode.com/problems/clone-binary-tree-with-random-pointer/description

**Problem Statement:**
- Input format: A binary tree `node` where each node has a `val`, `left`, `right`, and `random` pointer.
- Constraints: The number of nodes in the tree is in the range `[0, 100]`.
- Expected output format: A cloned binary tree with the same structure and values, including the `random` pointer.
- Key requirements and edge cases to consider: Handling the `random` pointer correctly, ensuring all nodes are cloned, and managing the tree structure.
- Example test cases with explanations:
  - A simple binary tree with a few nodes.
  - A tree with multiple levels and random pointers.
  - An empty tree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Recursively clone the tree, and for each node, also clone its `random` pointer if it exists.
- Step-by-step breakdown of the solution:
  1. Start at the root node.
  2. Recursively clone the `left` and `right` subtrees.
  3. For each node, clone its `random` pointer by finding the corresponding cloned node.
- Why this approach comes to mind first: It directly addresses the need to clone both the tree structure and the `random` pointers.

```cpp
class Solution {
public:
    NodeCopy* cloneTree(Node* original) {
        if (!original) return nullptr;
        
        // Clone the current node
        NodeCopy* newNode = new NodeCopy(original->val);
        
        // Recursively clone left and right subtrees
        newNode->left = cloneTree(original->left);
        newNode->right = cloneTree(original->right);
        
        // Clone the random pointer
        if (original->random) {
            // This step requires a way to find the cloned version of the node that the random pointer points to.
            // For simplicity, we assume a function `findClonedNode` that can find the cloned version of a node.
            newNode->random = findClonedNode(original->random);
        }
        
        return newNode;
    }
    
    NodeCopy* findClonedNode(Node* original) {
        // This function would need to traverse the cloned tree to find the node that corresponds to the original node.
        // For simplicity, this step is abstracted but in a real implementation, you'd need a way to keep track of cloned nodes.
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because for each node, we potentially traverse the entire tree again to find the cloned version of the node that the `random` pointer points to.
> - **Space Complexity:** $O(n)$, as we need to clone each node once.
> - **Why these complexities occur:** The $O(n^2)$ time complexity occurs because of the nested operations: cloning each node and then potentially searching through all cloned nodes for the `random` pointer's target.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of searching for the cloned version of a node every time we encounter a `random` pointer, we can use a hash map to store the mapping between original nodes and their clones. This allows us to find the clone of any node in constant time.
- Detailed breakdown of the approach:
  1. Create a hash map to store the mapping between original nodes and their clones.
  2. Recursively traverse the tree, cloning each node and storing the mapping in the hash map.
  3. When cloning a node, use the hash map to immediately set the `random` pointer to the clone of the original node's `random` target.
- Proof of optimality: This approach ensures that we visit each node exactly once, resulting in linear time complexity, and we use a hash map to store the node mappings, which allows for constant time lookup and insertion.

```cpp
class Solution {
public:
    NodeCopy* cloneTree(Node* original) {
        if (!original) return nullptr;
        
        // Use a hash map to store the mapping between original nodes and their clones
        unordered_map<Node*, NodeCopy*> nodeMap;
        
        return cloneNode(original, nodeMap);
    }
    
    NodeCopy* cloneNode(Node* original, unordered_map<Node*, NodeCopy*>& nodeMap) {
        if (!original) return nullptr;
        
        // If we've already cloned this node, return the clone
        if (nodeMap.find(original) != nodeMap.end()) {
            return nodeMap[original];
        }
        
        // Clone the current node
        NodeCopy* newNode = new NodeCopy(original->val);
        nodeMap[original] = newNode; // Store the mapping
        
        // Recursively clone left and right subtrees
        newNode->left = cloneNode(original->left, nodeMap);
        newNode->right = cloneNode(original->right, nodeMap);
        
        // Clone the random pointer using the hash map
        if (original->random) {
            newNode->random = cloneNode(original->random, nodeMap);
        }
        
        return newNode;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node exactly once.
> - **Space Complexity:** $O(n)$, as we need to clone each node and store the mapping in the hash map.
> - **Optimality proof:** This is optimal because we achieve linear time complexity by avoiding redundant operations and using a hash map for constant time lookups.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, use of hash maps for efficient node mapping.
- Problem-solving patterns identified: Breaking down complex problems into simpler recursive steps, using data structures like hash maps to optimize lookup operations.
- Optimization techniques learned: Avoiding redundant operations by storing and reusing previously computed results.
- Similar problems to practice: Other problems involving tree traversal and cloning, such as cloning graphs.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like empty trees or null nodes, incorrect usage of recursive functions.
- Edge cases to watch for: Handling the `random` pointer correctly, especially when it points to a node that has not been cloned yet.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the function with various tree structures and edge cases to ensure correctness.