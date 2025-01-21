## Count Good Nodes in Binary Tree
**Problem Link:** https://leetcode.com/problems/count-good-nodes-in-binary-tree/description

**Problem Statement:**
- Input format and constraints: Given a binary tree `root`, count the number of **good nodes**. A **good node** is a node that has a value greater than or equal to the **maximum value** on the path from the root to that node.
- Expected output format: The number of **good nodes** in the binary tree.
- Key requirements and edge cases to consider: The input tree can be empty, and the values in the tree can be any integer.
- Example test cases with explanations:
  - Example 1: 
    - Input: `root = [3,1,4,3,null,1,2]`
    - Output: `4`
    - Explanation: The good nodes are the nodes with values 3, 1, 3, and 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) on the binary tree, keeping track of the maximum value seen so far on the path to each node.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to perform DFS.
  2. Pass the current node, the maximum value seen so far, and the current path as parameters to the recursive function.
  3. If the current node is `nullptr`, return 0.
  4. If the current node's value is greater than or equal to the maximum value seen so far, increment the count of good nodes.
  5. Recursively call the function for the left and right child nodes, updating the maximum value seen so far.
- Why this approach comes to mind first: It is a straightforward way to explore all nodes in the tree and check if each node is a good node.

```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        int count = 0;
        dfs(root, INT_MIN, count);
        return count;
    }
    
    void dfs(TreeNode* node, int maxVal, int& count) {
        if (!node) return;
        
        if (node->val >= maxVal) {
            count++;
            maxVal = node->val;
        }
        
        dfs(node->left, maxVal, count);
        dfs(node->right, maxVal, count);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the binary tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is dependent on the height of the tree because that determines the maximum depth of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can avoid passing the count as a reference by returning the count from the recursive function.
- Detailed breakdown of the approach:
  1. Define a recursive function to perform DFS.
  2. Pass the current node and the maximum value seen so far as parameters to the recursive function.
  3. If the current node is `nullptr`, return 0.
  4. If the current node's value is greater than or equal to the maximum value seen so far, increment the count of good nodes.
  5. Recursively call the function for the left and right child nodes, updating the maximum value seen so far, and return the total count.
- Proof of optimality: This approach is optimal because it still visits each node once, but avoids the unnecessary parameter passing.

```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        return dfs(root, INT_MIN);
    }
    
    int dfs(TreeNode* node, int maxVal) {
        if (!node) return 0;
        
        int count = node->val >= maxVal ? 1 : 0;
        maxVal = max(maxVal, node->val);
        
        return count + dfs(node->left, maxVal) + dfs(node->right, maxVal);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the binary tree, due to the recursive call stack.
> - **Optimality proof:** This is the best possible time complexity because we must visit each node at least once to determine if it is a good node. The space complexity is also optimal because we only use a recursive call stack that is as deep as the height of the tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), recursive functions, and tree traversal.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (in this case, traversing the tree and checking each node).
- Optimization techniques learned: Avoiding unnecessary parameter passing and using return values instead.
- Similar problems to practice: Other tree traversal problems, such as finding the maximum depth of a binary tree or checking if a binary tree is balanced.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the maximum value seen so far, or not handling the base case of an empty tree correctly.
- Edge cases to watch for: Empty trees, trees with a single node, and trees with negative values.
- Performance pitfalls: Using an inefficient traversal algorithm or not optimizing the recursive function calls.
- Testing considerations: Make sure to test the solution with different types of input trees, including empty trees, trees with a single node, and trees with multiple levels.