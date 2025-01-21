## Closest Binary Search Tree Value

**Problem Link:** https://leetcode.com/problems/closest-binary-search-tree-value/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
- Expected output format: The value in the BST closest to the target.
- Key requirements and edge cases to consider: The BST may not contain the target value, and we need to find the closest value. Also, if there are multiple values with the same minimum difference, we can return any of them.
- Example test cases with explanations:
  - Example 1: Input: root = [4,2,5,1,3], target = 3.8, Output: 4
  - Example 2: Input: root = [1], target = 0.9, Output: 1

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can traverse the entire BST, store all the node values, and then find the value closest to the target.
- Step-by-step breakdown of the solution:
  1. Perform an in-order traversal of the BST to get all node values in ascending order.
  2. Store these values in a vector.
  3. Initialize the minimum difference and the closest value with the first value in the vector.
  4. Iterate through the vector, updating the minimum difference and the closest value if a smaller difference is found.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's not efficient because it requires extra space to store all node values.

```cpp
class Solution {
public:
    int closestValue(TreeNode* root, double target) {
        vector<int> values;
        inOrderTraversal(root, values);
        int closest = values[0];
        double minDiff = abs(target - closest);
        
        for (int i = 1; i < values.size(); i++) {
            double diff = abs(target - values[i]);
            if (diff < minDiff) {
                minDiff = diff;
                closest = values[i];
            }
        }
        return closest;
    }
    
    void inOrderTraversal(TreeNode* root, vector<int>& values) {
        if (root == nullptr) return;
        inOrderTraversal(root->left, values);
        values.push_back(root->val);
        inOrderTraversal(root->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST, because we traverse the tree once and then iterate through the vector of node values.
> - **Space Complexity:** $O(n)$, because we store all node values in the vector.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we visit each node once during the traversal and then iterate through the vector. The space complexity is $O(n)$ because we store all node values in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can take advantage of the BST property that all values to the left of a node are smaller and all values to the right are larger. This allows us to prune branches that are guaranteed to be farther from the target.
- Detailed breakdown of the approach:
  1. Initialize the closest value with the root's value and the minimum difference with the absolute difference between the target and the root's value.
  2. Traverse the BST, at each step moving to the child node that is closer to the target (or the one that could potentially have a value closer to the target based on the BST property).
  3. Update the closest value and the minimum difference if a node with a value closer to the target is found.
- Proof of optimality: This approach is optimal because it visits the minimum number of nodes necessary to find the closest value. It leverages the BST property to avoid exploring branches that cannot contain the closest value.

```cpp
class Solution {
public:
    int closestValue(TreeNode* root, double target) {
        int closest = root->val;
        double minDiff = abs(target - closest);
        
        while (root != nullptr) {
            double diff = abs(target - root->val);
            if (diff < minDiff) {
                minDiff = diff;
                closest = root->val;
            }
            if (target < root->val) {
                root = root->left;
            } else {
                root = root->right;
            }
        }
        return closest;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the BST, because in the worst case, we traverse from the root to a leaf node. For a balanced BST, $h = \log(n)$, and for an unbalanced BST, $h = n$.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the closest value and the minimum difference.
> - **Optimality proof:** This solution is optimal because it visits the minimum number of nodes necessary to find the closest value, leveraging the BST property to minimize the number of comparisons needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary Search Tree traversal, leveraging BST properties for optimization.
- Problem-solving patterns identified: Using properties of data structures to reduce the search space.
- Optimization techniques learned: Pruning branches based on the BST property to minimize the number of node visits.
- Similar problems to practice: Other BST problems that involve finding specific values or ranges within the tree.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the closest value and minimum difference correctly during traversal.
- Edge cases to watch for: Handling the case where the target is equal to a node's value, and ensuring the traversal stops when the closest value is found.
- Performance pitfalls: Not leveraging the BST property to prune branches, leading to unnecessary node visits.
- Testing considerations: Testing with a variety of BSTs, including balanced and unbalanced trees, and targets that are both within and outside the range of values in the BST.