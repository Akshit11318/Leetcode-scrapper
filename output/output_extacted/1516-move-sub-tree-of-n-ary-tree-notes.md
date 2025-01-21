## Move Sub-Tree of N-ary Tree

**Problem Link:** https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/description

**Problem Statement:**
- Input: The root of an N-ary tree, the `origin` node, and the `dest` node.
- Constraints: The `origin` node will exist in the tree, the `dest` node will exist in the tree, the `origin` node will not be the root of the tree, and the `dest` node will not be a descendant of the `origin` node.
- Expected Output: The root of the modified N-ary tree after moving the `origin` node to be a child of the `dest` node.
- Key Requirements: Find the `origin` node, find the parent of the `origin` node, remove the `origin` node from its parent, add the `origin` node as a child of the `dest` node.
- Example Test Cases:
  - Example 1: Given the following tree:
        ```
        1
       /|\
      3 2 4
     / \
    5   6
        ```
    Move the node 3 to be a child of node 4. The resulting tree should be:
        ```
        1
       /|\
      2 4 3
         / \
        5   6
        ```
  - Example 2: Given the following tree:
        ```
        1
       / \
      3   2
     / \
    5   6
        ```
    Move the node 3 to be a child of node 2. The resulting tree should be:
        ```
        1
       / \
      2   3
     /   / \
    5   6
        ```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) to find the `origin` node and its parent. Then, remove the `origin` node from its parent and add it as a child of the `dest` node.
- Step-by-step breakdown of the solution:
  1. Perform a DFS to find the `origin` node and its parent.
  2. Remove the `origin` node from its parent.
  3. Perform another DFS to find the `dest` node.
  4. Add the `origin` node as a child of the `dest` node.

```cpp
class Solution {
public:
    Node* moveSubTree(Node* root, Node* origin, Node* dest) {
        // Find the origin node and its parent
        Node* originParent = findParent(root, origin);
        
        // Remove the origin node from its parent
        removeNode(originParent, origin);
        
        // Add the origin node as a child of the dest node
        dest->children.push_back(origin);
        
        return root;
    }
    
    Node* findParent(Node* root, Node* target) {
        if (root == nullptr) {
            return nullptr;
        }
        
        if (root->children.empty()) {
            return nullptr;
        }
        
        for (Node* child : root->children) {
            if (child == target) {
                return root;
            }
        }
        
        for (Node* child : root->children) {
            Node* parent = findParent(child, target);
            if (parent != nullptr) {
                return parent;
            }
        }
        
        return nullptr;
    }
    
    void removeNode(Node* parent, Node* target) {
        if (parent == nullptr) {
            return;
        }
        
        for (auto it = parent->children.begin(); it != parent->children.end(); ++it) {
            if (*it == target) {
                parent->children.erase(it);
                return;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, since we perform a DFS to find the `origin` node and its parent, and another DFS to find the `dest` node.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The DFS operations cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Perform a single DFS to find the `origin` node, its parent, and the `dest` node.
- Detailed breakdown of the approach:
  1. Perform a DFS to find the `origin` node, its parent, and the `dest` node.
  2. Remove the `origin` node from its parent.
  3. Add the `origin` node as a child of the `dest` node.

```cpp
class Solution {
public:
    Node* moveSubTree(Node* root, Node* origin, Node* dest) {
        // Perform a DFS to find the origin node, its parent, and the dest node
        findNodes(root, origin, dest);
        
        // Remove the origin node from its parent
        removeNode(originParent, origin);
        
        // Add the origin node as a child of the dest node
        dest->children.push_back(origin);
        
        return root;
    }
    
    Node* originParent;
    Node* origin;
    Node* dest;
    
    void findNodes(Node* root, Node* targetOrigin, Node* targetDest) {
        if (root == nullptr) {
            return;
        }
        
        if (root == targetOrigin) {
            origin = root;
        }
        
        if (root == targetDest) {
            dest = root;
        }
        
        for (Node* child : root->children) {
            if (child == targetOrigin) {
                originParent = root;
            }
            
            findNodes(child, targetOrigin, targetDest);
        }
    }
    
    void removeNode(Node* parent, Node* target) {
        if (parent == nullptr) {
            return;
        }
        
        for (auto it = parent->children.begin(); it != parent->children.end(); ++it) {
            if (*it == target) {
                parent->children.erase(it);
                return;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, since we perform a single DFS to find the `origin` node, its parent, and the `dest` node.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This is the optimal solution since we only perform a single DFS to find all the required nodes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, tree traversal, node removal, and node insertion.
- Problem-solving patterns identified: Using a single DFS to find multiple nodes in a tree.
- Optimization techniques learned: Reducing the number of DFS operations from two to one.
- Similar problems to practice: Tree traversal, node insertion, and node removal problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the parent node when removing a child node.
- Edge cases to watch for: Handling the case where the `origin` node is the root of the tree.
- Performance pitfalls: Performing multiple DFS operations when a single DFS can suffice.
- Testing considerations: Testing the solution with different tree structures and node configurations.