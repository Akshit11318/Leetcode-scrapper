## Binary Tree Nodes
**Problem Link:** https://leetcode.com/problems/binary-tree-nodes/description

**Problem Statement:**
- Input format: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [1, 100].
- Expected output format: The number of nodes that have exactly one child.
- Key requirements and edge cases to consider:
  - Handling empty trees.
  - Counting nodes with exactly one child.
- Example test cases with explanations:
  - Example 1: Given the root: [2,2,5,5,5,1,1]
    - The output should be: 3
  - Example 2: Given the root: [1,2,3]
    - The output should be: 2

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the binary tree and count the nodes that have exactly one child.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) traversal of the binary tree.
  2. For each node, check if it has exactly one child.
  3. If a node has exactly one child, increment the count.
- Why this approach comes to mind first: It is a straightforward solution that involves checking each node in the tree.

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        int count = 0;
        if (root == nullptr) {
            return count;
        }
        
        if (root->left == nullptr && root->right != nullptr) {
            count++;
        } else if (root->left != nullptr && root->right == nullptr) {
            count++;
        }
        
        count += countNodes(root->left);
        count += countNodes(root->right);
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node once during the DFS traversal.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is dependent on the height of the tree due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we must visit each node in the tree to count the nodes with exactly one child.
- Detailed breakdown of the approach:
  1. Perform a DFS traversal of the binary tree.
  2. For each node, check if it has exactly one child.
  3. If a node has exactly one child, increment the count.
- Proof of optimality: This solution is optimal because we must visit each node in the tree to count the nodes with exactly one child, resulting in a time complexity of $O(n)$.

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        
        int count = 0;
        if ((root->left == nullptr && root->right != nullptr) || (root->left != nullptr && root->right == nullptr)) {
            count++;
        }
        
        return count + countNodes(root->left) + countNodes(root->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node once during the DFS traversal.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree.
> - **Optimality proof:** This solution is optimal because we must visit each node in the tree to count the nodes with exactly one child, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, recursive call stack management.
- Problem-solving patterns identified: Counting nodes with specific properties in a binary tree.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Counting nodes with specific properties in a graph or tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case (empty tree), incorrect recursive call stack management.
- Edge cases to watch for: Empty trees, trees with a single node.
- Performance pitfalls: Using an inefficient traversal algorithm.
- Testing considerations: Test with different tree structures, including empty trees and trees with a single node.