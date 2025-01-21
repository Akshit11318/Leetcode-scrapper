## Symmetric Tree

**Problem Link:** [https://leetcode.com/problems/symmetric-tree/description](https://leetcode.com/problems/symmetric-tree/description)

**Problem Statement:**
- Input format: The root of a binary tree where each node has a value and two child nodes (left and right).
- Constraints: The number of nodes in the tree is in the range [1, 1000], and each node's value is in the range [-100, 100].
- Expected output format: A boolean indicating whether the binary tree is symmetric around its center.
- Key requirements and edge cases to consider:
  - An empty tree is symmetric.
  - A tree with a single node is symmetric.
  - The tree's symmetry should be checked based on the mirror image of its structure and node values.
- Example test cases with explanations:
  - Example 1: The binary tree [1,2,2,3,4,4,3] is symmetric because its structure and node values are mirrored around its center.
  - Example 2: The binary tree [1,2,2,null,3,null,3] is symmetric for the same reason.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if a binary tree is symmetric, we can first traverse the tree and store its nodes in a data structure such as a vector or array. Then, we can compare the nodes from the start and end of the array, moving towards the center. If all pairs of nodes have the same value, the tree is symmetric.
- Step-by-step breakdown of the solution:
  1. Perform a level-order traversal of the binary tree and store the node values in a vector.
  2. Initialize two pointers, one at the start and one at the end of the vector.
  3. Compare the node values at the current positions of the two pointers. If they are different, the tree is not symmetric.
  4. Move the pointers towards the center of the vector and repeat step 3 until the pointers meet or cross.
- Why this approach comes to mind first: It is a straightforward approach that involves traversing the tree and comparing node values, which are basic operations in tree problems.

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        
        vector<int> nodes;
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node) {
                    nodes.push_back(node->val);
                    q.push(node->left);
                    q.push(node->right);
                } else {
                    nodes.push_back(-101); // Use a sentinel value to represent null nodes
                }
            }
        }
        
        int left = 0, right = nodes.size() - 1;
        while (left < right) {
            if (nodes[left] != nodes[right]) return false;
            left++;
            right--;
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once during the level-order traversal and then potentially once more during the comparison.
> - **Space Complexity:** $O(n)$, because in the worst case (a complete binary tree), the queue will contain $n/2$ nodes at the last level, and the vector will store $n$ node values.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear because we need to store all node values in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all node values in a vector and then comparing them, we can directly compare the left and right subtrees of the root node by recursively checking if they are mirror images of each other.
- Detailed breakdown of the approach:
  1. Define a helper function to check if two trees are mirror images of each other.
  2. In the helper function, if both trees are empty, they are mirror images. If one is empty and the other is not, they are not mirror images.
  3. If both trees are not empty, compare the node values. If they are different, the trees are not mirror images.
  4. Recursively call the helper function on the left subtree of the first tree and the right subtree of the second tree, and on the right subtree of the first tree and the left subtree of the second tree.
- Proof of optimality: This approach is optimal because it only visits each node once, resulting in a time complexity of $O(n)$, and it uses a recursive call stack that can go up to $O(h)$ in the worst case (where $h$ is the height of the tree), which is more efficient than storing all node values in a vector.

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) return true;
        if (!t1 || !t2) return false;
        return (t1->val == t2->val) && isMirror(t1->right, t2->left) && isMirror(t1->left, t2->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because it minimizes the number of node visits and uses a minimal amount of extra space for the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, recursive functions, and symmetry checking.
- Problem-solving patterns identified: Breaking down a problem into smaller sub-problems (e.g., checking if two trees are mirror images) and using recursive functions to solve them.
- Optimization techniques learned: Minimizing the number of node visits and using a minimal amount of extra space.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where one of the trees is empty, or incorrectly comparing node values.
- Edge cases to watch for: Empty trees, trees with a single node, and trees with a large number of nodes.
- Performance pitfalls: Using an inefficient algorithm that visits each node multiple times or uses a large amount of extra space.
- Testing considerations: Testing the function with different types of trees, including symmetric and asymmetric trees, and checking for correct results.