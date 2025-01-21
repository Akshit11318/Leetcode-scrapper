## Maximum Average Subtree

**Problem Link:** https://leetcode.com/problems/maximum-average-subtree/description

**Problem Statement:**
- Given the `root` of a binary tree, return the maximum average value of a subtree.
- A subtree is a tree that includes a node and all of its descendants.
- The average value of a tree is the sum of its node values divided by the number of nodes.
- Input: `root` of a binary tree.
- Output: The maximum average value of a subtree.
- Key requirements: The solution should handle all possible binary tree structures and node values.
- Edge cases: Empty tree, single-node tree, trees with negative values.

**Example Test Cases:**
- Test case 1: A balanced binary tree with positive node values.
- Test case 2: A skewed binary tree with negative node values.
- Test case 3: An empty binary tree.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the sum and count of nodes for every possible subtree.
- This can be achieved by using a recursive approach to traverse the tree and calculate the sum and count of nodes for each subtree.
- The maximum average value can be updated during the traversal.

```cpp
class Solution {
public:
    double maxAverage = 0.0;
    double maximumAverageSubtree(TreeNode* root) {
        dfs(root);
        return maxAverage;
    }
    void dfs(TreeNode* root) {
        if (!root) return;
        vector<double> sums;
        vector<int> counts;
        dfsHelper(root, sums, counts);
        for (int i = 0; i < sums.size(); i++) {
            maxAverage = max(maxAverage, sums[i] / counts[i]);
        }
        dfs(root->left);
        dfs(root->right);
    }
    void dfsHelper(TreeNode* root, vector<double>& sums, vector<int>& counts) {
        if (!root) return;
        sums.push_back(root->val);
        counts.push_back(1);
        dfsHelper(root->left, sums, counts);
        dfsHelper(root->right, sums, counts);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because for each node, we are potentially calculating the sum and count of all its descendants.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the storage of sums and counts.
> - **Why these complexities occur:** The brute force approach involves redundant calculations for each subtree, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a recursive approach with a `post-order` traversal to calculate the sum and count of nodes for each subtree.
- During the traversal, we can update the maximum average value.
- This approach avoids redundant calculations and ensures that each subtree is visited only once.

```cpp
class Solution {
public:
    double maxAverage = 0.0;
    double maximumAverageSubtree(TreeNode* root) {
        dfs(root);
        return maxAverage;
    }
    pair<double, int> dfs(TreeNode* root) {
        if (!root) return {0.0, 0};
        pair<double, int> left = dfs(root->left);
        pair<double, int> right = dfs(root->right);
        double sum = left.first + right.first + root->val;
        int count = left.second + right.second + 1;
        maxAverage = max(maxAverage, sum / count);
        return {sum, count};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node only once.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it visits each node only once and calculates the sum and count of nodes for each subtree in a single pass.

---

### Final Notes

**Learning Points:**
- The importance of choosing the correct traversal order (post-order) to avoid redundant calculations.
- The use of recursive functions to calculate the sum and count of nodes for each subtree.
- The optimization of the brute force approach by avoiding redundant calculations.

**Mistakes to Avoid:**
- Using a pre-order or in-order traversal, which can lead to redundant calculations.
- Not updating the maximum average value during the traversal.
- Not considering the base case (empty tree) in the recursive function.