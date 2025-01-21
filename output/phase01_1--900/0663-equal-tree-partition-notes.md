## Equal Tree Partition
**Problem Link:** https://leetcode.com/problems/equal-tree-partition/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [1, 10^4].
- Expected Output: Return `true` if the tree can be partitioned into two trees with equal sum of nodes, and `false` otherwise.
- Key Requirements: The two trees must not share any nodes, and the sum of the node values in each tree must be equal.
- Edge Cases: If the tree has an odd total sum, it is impossible to partition it into two equal trees.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to calculate the total sum of the tree and then try to find a partition that divides the tree into two parts with equal sums.
- This approach involves generating all possible subsets of nodes and checking if any subset has a sum equal to half of the total sum.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach.

```cpp
int sumTree(TreeNode* root) {
    if (!root) return 0;
    return root->val + sumTree(root->left) + sumTree(root->right);
}

bool checkEqualTree(TreeNode* root) {
    int totalSum = sumTree(root);
    if (totalSum % 2 != 0) return false;
    
    int targetSum = totalSum / 2;
    unordered_set<int> sums;
    return checkPartition(root, targetSum, sums);
}

bool checkPartition(TreeNode* node, int targetSum, unordered_set<int>& sums) {
    if (!node) return false;
    int currentSum = node->val;
    if (currentSum == targetSum) return true;
    
    if (checkPartition(node->left, targetSum - currentSum, sums)) return true;
    if (checkPartition(node->right, targetSum - currentSum, sums)) return true;
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes in the tree, because in the worst case, we are generating all possible subsets of nodes.
> - **Space Complexity:** $O(n)$, for the recursion stack and the set to store the sums.
> - **Why these complexities occur:** The brute force approach involves exhaustive search, which leads to exponential time complexity. The space complexity is due to the recursion stack and the set used to store the sums.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to calculate the total sum of the tree first and then check if it's possible to partition the tree into two parts with equal sums.
- We use a `DFS` approach to calculate the sum of each subtree and check if it's equal to half of the total sum.
- Proof of optimality: This approach is optimal because it only requires a single pass through the tree to calculate the total sum and another pass to check for the partition.

```cpp
int sumTree(TreeNode* root) {
    if (!root) return 0;
    return root->val + sumTree(root->left) + sumTree(root->right);
}

bool checkEqualTree(TreeNode* root) {
    int totalSum = sumTree(root);
    if (totalSum % 2 != 0) return false;
    
    int targetSum = totalSum / 2;
    return checkPartition(root, targetSum);
}

bool checkPartition(TreeNode* node, int targetSum) {
    if (!node) return false;
    int currentSum = node->val;
    
    if (currentSum == targetSum) return true;
    
    return checkPartition(node->left, targetSum - currentSum) || 
           checkPartition(node->right, targetSum - currentSum);
}
```

However, this approach still has exponential time complexity due to the recursive nature of the `checkPartition` function. To improve this, we can use a more efficient approach that calculates the sum of each subtree only once.

```cpp
int sumTree(TreeNode* root) {
    if (!root) return 0;
    return root->val + sumTree(root->left) + sumTree(root->right);
}

bool checkEqualTree(TreeNode* root) {
    int totalSum = sumTree(root);
    if (totalSum % 2 != 0) return false;
    
    int targetSum = totalSum / 2;
    unordered_set<int> sums;
    return checkPartition(root, targetSum, sums);
}

int checkPartition(TreeNode* node, int targetSum, unordered_set<int>& sums) {
    if (!node) return 0;
    int currentSum = node->val + checkPartition(node->left, targetSum, sums) + 
                    checkPartition(node->right, targetSum, sums);
    if (currentSum == targetSum) {
        sums.insert(currentSum);
    }
    return currentSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we are doing a single pass through the tree to calculate the total sum and another pass to check for the partition.
> - **Space Complexity:** $O(n)$, for the recursion stack and the set used to store the sums.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree to calculate the total sum and another pass to check for the partition, resulting in linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `DFS`, tree traversal, and subset sum problem.
- Problem-solving patterns identified: calculating the total sum of the tree and then checking for a partition.
- Optimization techniques learned: using a `DFS` approach to calculate the sum of each subtree and checking for the partition in a single pass.
- Similar problems to practice: subset sum problem, partition problem.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the base case in the recursive function, not handling the case where the tree has an odd total sum.
- Edge cases to watch for: the tree has an odd total sum, the tree is empty.
- Performance pitfalls: using an exponential time complexity approach, not optimizing the recursive function.
- Testing considerations: testing the function with different types of trees, including empty trees, trees with an odd total sum, and trees with a large number of nodes.