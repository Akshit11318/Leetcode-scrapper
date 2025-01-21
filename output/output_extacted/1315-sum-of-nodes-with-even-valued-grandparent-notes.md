## Sum of Nodes with Even-Valued Grandparent
**Problem Link:** https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree, return the sum of values of nodes with even-valued grandparent.
- Expected output format: The sum of node values.
- Key requirements and edge cases to consider: The tree can be empty, or nodes can have one or no children. A node's grandparent is its parent's parent.
- Example test cases with explanations: 
    - For the tree [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5], the sum of nodes with even-valued grandparent is 18 (2 + 7 + 9).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree and check each node's grandparent value.
- Step-by-step breakdown of the solution:
    1. Perform a depth-first search (DFS) on the tree.
    2. For each node, check if it has a grandparent.
    3. If the grandparent exists and its value is even, add the current node's value to the sum.
- Why this approach comes to mind first: It directly addresses the problem by checking every node's grandparent.

```cpp
class Solution {
public:
    int sumEvenGrandparent(TreeNode* root) {
        int sum = 0;
        dfs(root, nullptr, nullptr, sum);
        return sum;
    }
    
    void dfs(TreeNode* node, TreeNode* parent, TreeNode* grandparent, int& sum) {
        if (!node) return;
        
        if (grandparent && grandparent->val % 2 == 0) {
            sum += node->val;
        }
        
        dfs(node->left, node, parent, sum);
        dfs(node->right, node, parent, sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack. In the worst case, the tree is skewed, and $h = n$.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is due to the recursive calls, which in the worst case can go as deep as the height of the tree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by simply keeping track of the parent and grandparent of each node during the traversal.
- Detailed breakdown of the approach:
    1. Perform a DFS traversal of the tree.
    2. For each node, pass its parent and grandparent to the recursive calls.
    3. If a node's grandparent exists and is even, add the node's value to the sum.
- Proof of optimality: This solution visits each node exactly once and performs a constant amount of work for each node, making it optimal.
- Why further optimization is impossible: The problem requires checking each node, so any solution must have at least a linear time complexity.

```cpp
class Solution {
public:
    int sumEvenGrandparent(TreeNode* root) {
        return dfs(root, nullptr, nullptr);
    }
    
    int dfs(TreeNode* node, TreeNode* parent, TreeNode* grandparent) {
        if (!node) return 0;
        
        int sum = 0;
        if (grandparent && grandparent->val % 2 == 0) {
            sum += node->val;
        }
        
        sum += dfs(node->left, node, parent);
        sum += dfs(node->right, node, parent);
        
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** The time complexity is optimal because we must visit each node. The space complexity is also optimal because we only use a recursive call stack that is as deep as the height of the tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) traversal of a binary tree.
- Problem-solving patterns identified: Using recursive functions to traverse tree structures and keeping track of ancestors (parent, grandparent) during traversal.
- Optimization techniques learned: Minimizing the number of recursive calls and using a single pass through the tree to calculate the sum.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case (when the node is nullptr) in the recursive function.
- Edge cases to watch for: Empty trees or trees with a single node.
- Performance pitfalls: Using an inefficient traversal method or not optimizing the recursive calls.
- Testing considerations: Ensure the solution works correctly for different tree structures (balanced, skewed) and edge cases (empty tree, single node).