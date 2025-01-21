## Complete Binary Tree Inserter
**Problem Link:** https://leetcode.com/problems/complete-binary-tree-inserter/description

**Problem Statement:**
- Input: A complete binary tree where each node has a unique value.
- Constraints: The tree is complete, and each node has a unique value between 1 and 100.
- Expected output: A `CompleteBinaryTreeInserter` class that supports the following operations:
  - `CompleteBinaryTreeInserter(TreeNode* root)`: Initializes the `CompleteBinaryTreeInserter` with a given `root` node.
  - `int insert(int val)`: Inserts a new node with the given `val` into the complete binary tree and returns the value of the parent node.
- Key requirements and edge cases to consider:
  - The tree is initially empty, and we need to handle this case.
  - The tree is complete, so we need to maintain this property after insertion.
- Example test cases with explanations:
  - `CompleteBinaryTreeInserter(root = [1, 2, 3, 4, 5, 6])`
  - `insert(7)` returns `3` because the new node is inserted as the left child of node `3`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can start by performing a level-order traversal of the tree to find the first node that has an empty child slot.
- Step-by-step breakdown of the solution:
  1. Perform a level-order traversal of the tree.
  2. For each node, check if it has an empty child slot (either left or right child is `NULL`).
  3. If we find a node with an empty child slot, insert the new node as its child and return the parent node's value.
- Why this approach comes to mind first: It's a straightforward way to find the first available slot in the tree.

```cpp
class CompleteBinaryTreeInserter {
public:
    CompleteBinaryTreeInserter(TreeNode* root) : root_(root) {}

    int insert(int val) {
        TreeNode* new_node = new TreeNode(val);
        if (!root_) {
            root_ = new_node;
            return -1; // or throw an exception
        }

        queue<TreeNode*> q;
        q.push(root_);
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if (!node->left) {
                node->left = new_node;
                return node->val;
            }
            q.push(node->left);
            if (!node->right) {
                node->right = new_node;
                return node->val;
            }
            q.push(node->right);
        }
        return -1; // or throw an exception
    }

private:
    TreeNode* root_;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because in the worst case, we need to traverse the entire tree to find the first available slot.
> - **Space Complexity:** $O(n)$, because we use a queue to store nodes during the level-order traversal.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it involves traversing the entire tree for each insertion.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can maintain a queue of nodes that have empty child slots and insert new nodes into the first node in the queue.
- Detailed breakdown of the approach:
  1. Initialize a queue with the root node.
  2. For each insertion, check if the front node in the queue has an empty child slot.
  3. If it does, insert the new node as its child and return the parent node's value.
  4. If the front node has two children, remove it from the queue and add its children to the queue.
- Proof of optimality: This approach ensures that we always insert new nodes into the first available slot in the tree, maintaining the complete binary tree property.

```cpp
class CompleteBinaryTreeInserter {
public:
    CompleteBinaryTreeInserter(TreeNode* root) : root_(root) {
        if (root_) {
            q_.push(root_);
        }
    }

    int insert(int val) {
        TreeNode* new_node = new TreeNode(val);
        if (!root_) {
            root_ = new_node;
            return -1; // or throw an exception
        }

        while (q_.front()->left && q_.front()->right) {
            TreeNode* node = q_.front();
            q_.pop();
            q_.push(node->left);
            q_.push(node->right);
        }

        TreeNode* parent = q_.front();
        if (!parent->left) {
            parent->left = new_node;
        } else {
            parent->right = new_node;
        }
        q_.push(new_node);
        return parent->val;
    }

private:
    TreeNode* root_;
    queue<TreeNode*> q_;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we only need to perform a constant amount of work for each insertion.
> - **Space Complexity:** $O(n)$, because we use a queue to store nodes with empty child slots.
> - **Optimality proof:** The optimal approach has a constant time complexity because we maintain a queue of nodes with empty child slots and insert new nodes into the first node in the queue.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal, queue data structure, and maintaining a complete binary tree.
- Problem-solving patterns identified: Using a queue to keep track of nodes with empty child slots.
- Optimization techniques learned: Maintaining a queue of nodes with empty child slots to reduce the time complexity of insertion.
- Similar problems to practice: Other problems involving binary trees and queue data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: Handling the case where the tree is initially empty or has a single node.
- Performance pitfalls: Using a brute force approach that involves traversing the entire tree for each insertion.
- Testing considerations: Testing the implementation with different tree structures and insertion scenarios to ensure correctness.