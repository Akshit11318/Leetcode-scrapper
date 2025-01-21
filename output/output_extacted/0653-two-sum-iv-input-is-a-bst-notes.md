## Two Sum IV - Input is a BST
**Problem Link:** https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description

**Problem Statement:**
- Input: The root of a `Binary Search Tree` (`BST`) and an integer `target`.
- Output: Return `true` if there exist two numbers `x` and `y` in the `BST` such that `x + y == target`. Otherwise, return `false`.
- Key requirements: The `BST` property must be utilized to optimize the solution.
- Edge cases: Consider an empty tree or a tree with a single node.

**Example Test Cases:**
- Test case 1: `root = [5,3,6,2,4,null,7]`, `target = 9`
- Test case 2: `root = [5,3,6,2,4,null,7]`, `target = 28`
- Explanation: For test case 1, `x = 2` and `y = 7` satisfy the condition `x + y == 9`. For test case 2, no such `x` and `y` exist.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree and store all node values in a data structure.
- Then, for each value, check if its complement (target - value) exists in the stored values.
- This approach comes to mind first because it directly addresses the problem statement without considering the BST property.

```cpp
class Solution {
public:
    bool findTarget(TreeNode* root, int target) {
        vector<int> values;
        inorderTraversal(root, values);
        
        for (int i = 0; i < values.size(); ++i) {
            for (int j = i + 1; j < values.size(); ++j) {
                if (values[i] + values[j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
    
    void inorderTraversal(TreeNode* node, vector<int>& values) {
        if (node == nullptr) {
            return;
        }
        inorderTraversal(node->left, values);
        values.push_back(node->val);
        inorderTraversal(node->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the BST. This is because in the worst case, we are checking every pair of nodes.
> - **Space Complexity:** $O(n)$, as we are storing all node values in a vector.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops and a linear space complexity due to storing all node values.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to utilize the BST property: for any node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater.
- We can perform an in-order traversal of the BST and store the values in a set. For each value, check if its complement (target - value) exists in the set.
- This approach is optimal because it takes advantage of the BST property to reduce the time complexity.

```cpp
class Solution {
public:
    bool findTarget(TreeNode* root, int target) {
        unordered_set<int> values;
        return findTargetHelper(root, target, values);
    }
    
    bool findTargetHelper(TreeNode* node, int target, unordered_set<int>& values) {
        if (node == nullptr) {
            return false;
        }
        
        if (values.find(target - node->val) != values.end()) {
            return true;
        }
        values.insert(node->val);
        
        return findTargetHelper(node->left, target, values) || findTargetHelper(node->right, target, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST. This is because we are performing a single traversal of the tree.
> - **Space Complexity:** $O(n)$, as we are storing all node values in a set.
> - **Optimality proof:** This approach is optimal because it takes advantage of the BST property to reduce the time complexity to linear, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: utilizing the BST property to optimize the solution.
- Problem-solving patterns identified: using a set to store values and checking for complements.
- Optimization techniques learned: taking advantage of the BST property to reduce time complexity.
- Similar problems to practice: other problems involving BSTs and optimization.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases (e.g., empty tree or tree with a single node).
- Edge cases to watch for: considering the BST property to optimize the solution.
- Performance pitfalls: not utilizing the BST property, leading to a high time complexity.
- Testing considerations: testing with different types of BSTs (e.g., balanced, unbalanced) and edge cases.