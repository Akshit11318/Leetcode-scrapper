## Count the Number of Good Nodes
**Problem Link:** https://leetcode.com/problems/count-the-number-of-good-nodes/description

**Problem Statement:**
- Input format and constraints: The input is a binary tree where each node has a value. The constraints are that the binary tree can be empty, and the values in the nodes can range from $-10^4$ to $10^4$.
- Expected output format: The output should be the number of good nodes in the binary tree. A good node is defined as a node where all the ancestors of the node have values less than or equal to the node's value.
- Key requirements and edge cases to consider: The key requirement is to count the number of good nodes in the binary tree. Edge cases include an empty binary tree, a binary tree with one node, and a binary tree with multiple nodes.
- Example test cases with explanations: 
  - For the binary tree [3,1,4,3,null,1,2], the output should be 4 because the good nodes are 3, 1, 3, and 1.
  - For the binary tree [3,3,null,4,2], the output should be 3 because the good nodes are 3, 3, and 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to traverse the binary tree and check each node to see if it is a good node.
- Step-by-step breakdown of the solution: 
  1. Traverse the binary tree using a depth-first search (DFS) or breadth-first search (BFS) algorithm.
  2. For each node, check if all the ancestors of the node have values less than or equal to the node's value.
  3. If the node is a good node, increment the count of good nodes.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to solve the problem. However, it is not the most efficient approach because it requires checking all the ancestors of each node, which can result in a high time complexity.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int goodNodes(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        
        int count = 0;
        dfs(root, root->val, count);
        return count;
    }
    
    void dfs(TreeNode* node, int maxVal, int& count) {
        if (node == nullptr) {
            return;
        }
        
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
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the binary tree, because of the recursive call stack. In the worst case, $h = n$ for an unbalanced binary tree.
> - **Why these complexities occur:** These complexities occur because we are using a recursive DFS algorithm to traverse the binary tree. The time complexity is $O(n)$ because we visit each node once, and the space complexity is $O(h)$ because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a recursive DFS algorithm to traverse the binary tree and keep track of the maximum value seen so far.
- Detailed breakdown of the approach: 
  1. Traverse the binary tree using a recursive DFS algorithm.
  2. Keep track of the maximum value seen so far.
  3. For each node, check if the node's value is greater than or equal to the maximum value seen so far.
  4. If the node's value is greater than or equal to the maximum value seen so far, increment the count of good nodes and update the maximum value seen so far.
- Proof of optimality: This approach is optimal because it visits each node once and keeps track of the maximum value seen so far, which is necessary to determine if a node is a good node.

```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        
        int count = 0;
        dfs(root, root->val, count);
        return count;
    }
    
    void dfs(TreeNode* node, int maxVal, int& count) {
        if (node == nullptr) {
            return;
        }
        
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
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the binary tree, because of the recursive call stack. In the worst case, $h = n$ for an unbalanced binary tree.
> - **Optimality proof:** This approach is optimal because it visits each node once and keeps track of the maximum value seen so far, which is necessary to determine if a node is a good node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive DFS algorithm, keeping track of the maximum value seen so far.
- Problem-solving patterns identified: Using a recursive DFS algorithm to traverse a binary tree and keep track of a maximum value.
- Optimization techniques learned: Visiting each node once and keeping track of the maximum value seen so far.
- Similar problems to practice: Counting the number of nodes in a binary tree that satisfy a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the count of good nodes, not updating the maximum value seen so far.
- Edge cases to watch for: An empty binary tree, a binary tree with one node, a binary tree with multiple nodes.
- Performance pitfalls: Visiting each node multiple times, not keeping track of the maximum value seen so far.
- Testing considerations: Testing the function with different binary trees, including an empty binary tree, a binary tree with one node, and a binary tree with multiple nodes.