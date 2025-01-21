## Print Binary Tree

**Problem Link:** https://leetcode.com/problems/print-binary-tree/description

**Problem Statement:**
- Input: A binary tree where each node has a unique integer value.
- Output: Print the binary tree in a way that each level is on a new line, with nodes on the same level separated by a single space.
- Key requirements and edge cases to consider:
  - Handling empty trees.
  - Handling trees with a single node.
  - Handling trees with multiple levels.
- Example test cases with explanations:
  - A tree with a single node should print the node's value on a single line.
  - A tree with multiple levels should print each level on a new line, with nodes on the same level separated by a single space.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a level-order traversal of the binary tree and print each node's value as we traverse.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the root node.
  2. While the queue is not empty, dequeue a node and print its value.
  3. Enqueue the node's children (if any) to the queue.
- Why this approach comes to mind first: It is a straightforward way to traverse the tree level by level.

```cpp
void printTree(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int levelSize = q.size();
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            cout << node->val << " ";
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        cout << endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(w)$, where $w$ is the maximum width of the tree (i.e., the maximum number of nodes at any level), since this is the maximum number of nodes we need to store in the queue at any given time.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is related to the width of the tree because we need to store all nodes at a given level in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem, as we need to visit each node at least once to print its value.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: Since we need to visit each node at least once, the time complexity of $O(n)$ is optimal. The space complexity of $O(w)$ is also optimal because we need to store all nodes at a given level in the queue.
- Why further optimization is impossible: We cannot avoid visiting each node, and we cannot store fewer nodes in the queue without losing information about the tree structure.

```cpp
void printTree(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int levelSize = q.size();
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            cout << node->val << " ";
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        cout << endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(w)$, where $w$ is the maximum width of the tree.
> - **Optimality proof:** The time and space complexities are optimal because we need to visit each node and store all nodes at a given level in the queue.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal, queue data structure.
- Problem-solving patterns identified: Breaking down a problem into smaller sub-problems (i.e., printing each level separately).
- Optimization techniques learned: Avoiding unnecessary work by only visiting each node once.
- Similar problems to practice: Printing a binary tree in a different format (e.g., pre-order, in-order, post-order).

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for an empty tree, forgetting to enqueue a node's children.
- Edge cases to watch for: Empty trees, trees with a single node, trees with multiple levels.
- Performance pitfalls: Using a data structure with high overhead (e.g., a linked list) instead of a queue.
- Testing considerations: Testing with different tree structures and sizes to ensure correctness and efficiency.