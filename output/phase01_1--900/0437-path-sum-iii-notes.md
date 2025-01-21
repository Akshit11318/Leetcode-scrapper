## Path Sum III
**Problem Link:** https://leetcode.com/problems/path-sum-iii/description

**Problem Statement:**
- Given a binary tree and a target sum, find the number of paths where the sum of the node values equals the target sum.
- The path can start at any node and can be of any length.
- The input is the root of the binary tree and the target sum.
- The expected output is the number of paths that sum up to the target sum.
- Key requirements and edge cases to consider:
  - The input tree can be empty.
  - The target sum can be zero or negative.
  - The path can be of any length, including a single node.

**Example Test Cases:**
- Example 1:
  - Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
  - Output: 3
  - Explanation: There are three paths that sum up to 8: [5,3], [3,5], and [11].
- Example 2:
  - Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
  - Output: 3
  - Explanation: There are three paths that sum up to 22: [5,4,11,2], [5,8,9], and [11,7,4].

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree and check every possible path.
- For each node, we can start a new path and check if the sum of the current path equals the target sum.
- We can use a recursive function to traverse the tree and check all possible paths.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        if (!root) return 0;
        int count = 0;
        count += pathSumFromRoot(root, targetSum);
        count += pathSum(root->left, targetSum);
        count += pathSum(root->right, targetSum);
        return count;
    }

    int pathSumFromRoot(TreeNode* root, int targetSum) {
        if (!root) return 0;
        int count = 0;
        if (root->val == targetSum) count++;
        count += pathSumFromRoot(root->left, targetSum - root->val);
        count += pathSumFromRoot(root->right, targetSum - root->val);
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because we are traversing the tree for each node, and in the worst case, the tree is skewed to one side.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is high because we are traversing the tree for each node, and the space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a prefix sum hash map to store the cumulative sum of node values.
- We can then use this hash map to find the number of paths that sum up to the target sum.
- The optimal solution uses a recursive function to traverse the tree and update the prefix sum hash map.
- The proof of optimality is that we are only traversing the tree once and using a hash map to store the prefix sums, which reduces the time complexity to $O(n)$.

```cpp
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<int, int> prefixSum;
        prefixSum[0] = 1;
        return pathSumFromRoot(root, targetSum, 0, prefixSum);
    }

    int pathSumFromRoot(TreeNode* root, int targetSum, int currentSum, unordered_map<int, int>& prefixSum) {
        if (!root) return 0;
        int count = 0;
        currentSum += root->val;
        count += prefixSum[currentSum - targetSum];
        prefixSum[currentSum]++;
        count += pathSumFromRoot(root->left, targetSum, currentSum, prefixSum);
        count += pathSumFromRoot(root->right, targetSum, currentSum, prefixSum);
        prefixSum[currentSum]--;
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are only traversing the tree once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the recursive call stack and the prefix sum hash map.
> - **Optimality proof:** The time complexity is optimal because we are only traversing the tree once, and the space complexity is optimal because we are using a hash map to store the prefix sums.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sum, hash map, recursive traversal.
- Problem-solving patterns identified: using a hash map to store prefix sums to reduce time complexity.
- Optimization techniques learned: using a hash map to store prefix sums to reduce time complexity.
- Similar problems to practice: Path Sum, Path Sum II.

**Mistakes to Avoid:**
- Common implementation errors: not updating the prefix sum hash map correctly.
- Edge cases to watch for: empty tree, target sum is zero or negative.
- Performance pitfalls: not using a hash map to store prefix sums, resulting in high time complexity.
- Testing considerations: test with different tree structures, target sums, and edge cases.