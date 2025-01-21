## Maximum Product of Splitted Binary Tree
**Problem Link:** https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description

**Problem Statement:**
- Input format: A binary tree where each node has a unique value and two child pointers (`left` and `right`).
- Constraints: The tree has at least one node and at most $10^5$ nodes. Each node's value is between $1$ and $10^6$.
- Expected output format: The maximum product of two sums of node values in two non-empty, non-overlapping subtrees.
- Key requirements and edge cases to consider:
  - The tree must be split into exactly two non-empty, non-overlapping subtrees.
  - Each subtree must contain at least one node.
  - Example test cases:
    - A tree with one node should return $0$ since it cannot be split into two non-empty subtrees.
    - A balanced tree with multiple nodes can be split in various ways to find the maximum product.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Enumerate all possible ways to split the binary tree into two non-empty subtrees and calculate the sum of each subtree.
- Step-by-step breakdown:
  1. Perform a depth-first search (DFS) to calculate the sum of all node values in the tree.
  2. Enumerate all possible splits of the tree by considering each node as a potential split point.
  3. For each split, calculate the sum of the two resulting subtrees.
  4. Keep track of the maximum product of two sums found so far.
- Why this approach comes to mind first: It's a straightforward way to ensure all possible splits are considered.

```cpp
class Solution {
public:
    int maxProduct(TreeNode* root) {
        long long totalSum = 0;
        long long maxProduct = 0;
        
        // Calculate total sum of the tree
        totalSum = getTotalSum(root);
        
        // Perform DFS to find the maximum product
        dfs(root, totalSum, maxProduct);
        
        return maxProduct % (int)(1e9 + 7);
    }
    
    long long getTotalSum(TreeNode* root) {
        if (root == nullptr) return 0;
        return root->val + getTotalSum(root->left) + getTotalSum(root->right);
    }
    
    long long dfs(TreeNode* root, long long totalSum, long long& maxProduct) {
        if (root == nullptr) return 0;
        
        long long leftSum = dfs(root->left, totalSum, maxProduct);
        long long rightSum = dfs(root->right, totalSum, maxProduct);
        
        long long currentSum = leftSum + rightSum + root->val;
        
        maxProduct = max(maxProduct, currentSum * (totalSum - currentSum));
        
        return currentSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, due to the recursion stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a single DFS traversal. The space complexity is proportional to the tree height due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Realize that we can calculate the sum of each subtree only once during the DFS traversal and store it for later use.
- Detailed breakdown:
  1. Perform a DFS traversal to calculate the sum of each subtree and store it in a data structure (e.g., a vector).
  2. Iterate through the stored sums to find the maximum product of two sums.
- Proof of optimality: This approach has the same time complexity as the brute force approach but reduces the number of calculations required to find the maximum product.

```cpp
class Solution {
public:
    int maxProduct(TreeNode* root) {
        long long totalSum = 0;
        long long maxProduct = 0;
        vector<long long> subtreeSums;
        
        // Calculate total sum of the tree
        totalSum = getTotalSum(root);
        
        // Perform DFS to calculate subtree sums
        dfs(root, subtreeSums);
        
        // Find the maximum product
        for (int i = 0; i < subtreeSums.size(); i++) {
            for (int j = i + 1; j < subtreeSums.size(); j++) {
                maxProduct = max(maxProduct, subtreeSums[i] * subtreeSums[j]);
            }
        }
        
        return maxProduct % (int)(1e9 + 7);
    }
    
    long long getTotalSum(TreeNode* root) {
        if (root == nullptr) return 0;
        return root->val + getTotalSum(root->left) + getTotalSum(root->right);
    }
    
    long long dfs(TreeNode* root, vector<long long>& subtreeSums) {
        if (root == nullptr) return 0;
        
        long long leftSum = dfs(root->left, subtreeSums);
        long long rightSum = dfs(root->right, subtreeSums);
        
        long long currentSum = leftSum + rightSum + root->val;
        subtreeSums.push_back(currentSum);
        
        return currentSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, due to the storage of subtree sums.
> - **Optimality proof:** This approach is optimal because it minimizes the number of calculations required to find the maximum product while still considering all possible splits.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, calculation of subtree sums, and finding the maximum product of two sums.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (calculating subtree sums) and combining the solutions to find the overall maximum product.
- Optimization techniques learned: Reducing the number of calculations required to find the maximum product by storing subtree sums for later use.

**Mistakes to Avoid:**
- Common implementation errors: Failing to consider all possible splits of the tree or incorrectly calculating subtree sums.
- Edge cases to watch for: Handling trees with a single node or empty trees.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the implementation with various input trees to ensure correctness and performance.