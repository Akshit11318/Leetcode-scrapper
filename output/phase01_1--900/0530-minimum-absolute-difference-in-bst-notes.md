## Minimum Absolute Difference in BST

**Problem Link:** https://leetcode.com/problems/minimum-absolute-difference-in-bst/description

**Problem Statement:**
- Input format: The root of a binary search tree (BST).
- Constraints: The number of nodes in the tree is in the range [2, 10^5]. 0 <= Node.val <= 10^5.
- Expected output format: The minimum absolute difference between any two nodes in the BST.
- Key requirements and edge cases to consider: The BST may not be balanced, and the difference should be calculated between any two nodes, not just adjacent ones in the tree structure.
- Example test cases with explanations:
  - Example 1: Given the root of the BST `[4,2,6,1,3]`, the minimum absolute difference is `1`.
  - Example 2: Given the root of the BST `[1,0,48,1,99,2]`, the minimum absolute difference is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the minimum absolute difference between any two nodes in the BST, we can consider all possible pairs of nodes and calculate their differences.
- Step-by-step breakdown of the solution:
  1. Traverse the BST and store all node values in a vector.
  2. Iterate over the vector to compare each pair of values.
  3. Calculate the absolute difference for each pair.
  4. Keep track of the minimum difference found so far.
- Why this approach comes to mind first: It's a straightforward way to ensure we're considering all possible pairs of nodes, which is necessary to find the minimum absolute difference.

```cpp
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> values;
        // Traverse the BST and store node values
        traverse(root, values);
        
        int minDiff = INT_MAX;
        // Compare each pair of values to find the minimum difference
        for (int i = 0; i < values.size(); i++) {
            for (int j = i + 1; j < values.size(); j++) {
                minDiff = min(minDiff, abs(values[i] - values[j]));
            }
        }
        
        return minDiff;
    }
    
    void traverse(TreeNode* node, vector<int>& values) {
        if (node) {
            traverse(node->left, values);
            values.push_back(node->val);
            traverse(node->right, values);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the BST. This is because we're comparing each pair of node values, resulting in a quadratic number of comparisons.
> - **Space Complexity:** $O(n)$, as we store all node values in a vector.
> - **Why these complexities occur:** The brute force approach requires comparing all pairs of nodes, leading to a quadratic time complexity. Storing all node values for comparison requires linear space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the given tree is a binary search tree, we can take advantage of its property that the in-order traversal of the tree yields a sorted sequence of node values.
- Detailed breakdown of the approach:
  1. Perform an in-order traversal of the BST to get a sorted sequence of node values.
  2. Initialize the minimum difference with the difference between the first two values in the sequence.
  3. Iterate through the rest of the sequence, updating the minimum difference whenever a smaller difference is found between adjacent values.
- Proof of optimality: This approach is optimal because it only requires a single pass through the sorted sequence of node values, resulting in a linear time complexity.
- Why further optimization is impossible: The problem inherently requires examining each node value at least once to determine the minimum absolute difference, making a linear time complexity the best achievable.

```cpp
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> values;
        // In-order traversal to get a sorted sequence of node values
        inOrderTraversal(root, values);
        
        int minDiff = INT_MAX;
        // Find the minimum difference between adjacent values in the sorted sequence
        for (int i = 1; i < values.size(); i++) {
            minDiff = min(minDiff, values[i] - values[i - 1]);
        }
        
        return minDiff;
    }
    
    void inOrderTraversal(TreeNode* node, vector<int>& values) {
        if (node) {
            inOrderTraversal(node->left, values);
            values.push_back(node->val);
            inOrderTraversal(node->right, values);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST. This is because we perform a single pass through the tree during the in-order traversal.
> - **Space Complexity:** $O(n)$, as we store the sorted sequence of node values.
> - **Optimality proof:** The optimal approach achieves a linear time complexity by leveraging the sorted nature of the in-order traversal of a BST, making it the most efficient solution possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal of a BST, leveraging the properties of BSTs for efficient solutions.
- Problem-solving patterns identified: Using the sorted nature of in-order traversal to simplify the problem.
- Optimization techniques learned: Taking advantage of the properties of data structures (like BSTs) to reduce time complexity.
- Similar problems to practice: Other problems involving BSTs and leveraging their properties for efficient solutions.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: Ensuring the solution works correctly for both balanced and unbalanced BSTs.
- Performance pitfalls: Failing to leverage the properties of the BST, leading to inefficient solutions with higher time complexities.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.