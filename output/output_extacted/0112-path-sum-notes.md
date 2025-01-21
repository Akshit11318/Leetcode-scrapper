## Path Sum
**Problem Link:** https://leetcode.com/problems/path-sum/description

**Problem Statement:**
- Input format and constraints: Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`, and `false` otherwise.
- Expected output format: A boolean value indicating whether a path sum equals the target sum.
- Key requirements and edge cases to consider: 
  - The tree may contain negative numbers.
  - The tree may be empty.
- Example test cases with explanations:
  - Example 1:
    - Input: `root = [5,4,8,11,null,13,4,7,2,null,null,5,1]`, `targetSum = 22`
    - Output: `true`
    - Explanation: The path `5 -> 4 -> 11 -> 2` sums up to 22.
  - Example 2:
    - Input: `root = [1,2,3]`, `targetSum = 5`
    - Output: `false`
    - Explanation: No path sums up to 5.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible path from the root to a leaf node and see if any path sums up to the target sum.
- Step-by-step breakdown of the solution: 
  1. Start at the root node.
  2. For each node, calculate the sum of the current path.
  3. If the node is a leaf node and the sum equals the target sum, return `true`.
  4. Recursively explore the left and right subtrees.
- Why this approach comes to mind first: It's a straightforward way to ensure all paths are considered.

```cpp
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) return false; // Base case: empty tree
        return hasPathSumHelper(root, targetSum, 0);
    }
    
    bool hasPathSumHelper(TreeNode* node, int targetSum, int currentSum) {
        if (!node) return false; // Base case: current path is invalid
        
        currentSum += node->val; // Update the current sum
        
        // If this is a leaf node and the sum matches, return true
        if (!node->left && !node->right && currentSum == targetSum) {
            return true;
        }
        
        // Recursively check the left and right subtrees
        return hasPathSumHelper(node->left, targetSum, currentSum) ||
               hasPathSumHelper(node->right, targetSum, currentSum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because in the worst case, we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), $h = n$, and in the best case (a balanced tree), $h = \log(n)$.
> - **Why these complexities occur:** The time complexity is linear because we potentially visit every node. The space complexity is dependent on the height of the recursive call stack, which varies with the tree's structure.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but recognizing that the recursive approach already is quite efficient and straightforward for this problem. There isn't a significantly more efficient algorithm for this specific problem, as we must at least visit each node once to determine if a path sum exists.
- Detailed breakdown of the approach: Same as the brute force approach, as it's already optimal for this problem's constraints.
- Proof of optimality: Any algorithm must at least visit each node once to check for the path sum, making the time complexity $O(n)$ optimal for this problem.
- Why further optimization is impossible: Given the need to potentially visit every node, the $O(n)$ time complexity is the best achievable for this problem.

```cpp
// Same code as the brute force approach, as it's already optimal
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) return false; // Base case: empty tree
        return hasPathSumHelper(root, targetSum, 0);
    }
    
    bool hasPathSumHelper(TreeNode* node, int targetSum, int currentSum) {
        if (!node) return false; // Base case: current path is invalid
        
        currentSum += node->val; // Update the current sum
        
        // If this is a leaf node and the sum matches, return true
        if (!node->left && !node->right && currentSum == targetSum) {
            return true;
        }
        
        // Recursively check the left and right subtrees
        return hasPathSumHelper(node->left, targetSum, currentSum) ||
               hasPathSumHelper(node->right, targetSum, currentSum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** The algorithm visits each node at most once, making it optimal in terms of time complexity for this problem.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, path sum calculation.
- Problem-solving patterns identified: Checking all possible paths in a tree for a specific condition.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the nature of the problem.
- Similar problems to practice: Other tree traversal and path sum problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of an empty tree or a leaf node correctly.
- Edge cases to watch for: Trees with negative numbers, empty trees, and the case where the target sum is zero.
- Performance pitfalls: Unnecessary recursive calls or not optimizing the recursive function calls.
- Testing considerations: Ensure to test with various tree structures (balanced, skewed, empty) and different target sums.