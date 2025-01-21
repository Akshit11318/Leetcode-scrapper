## Number of Nodes with Value One
**Problem Link:** https://leetcode.com/problems/number-of-nodes-with-value-one/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree, return the number of nodes with value 1. The input tree is a binary tree where each node has a value and two children (left and right).
- Expected output format: The function should return the count of nodes with value 1.
- Key requirements and edge cases to consider: The tree can be empty, and nodes can have any integer value.
- Example test cases with explanations:
  - For the tree [1,1,0,1,0,0,1], the function should return 4 because there are 4 nodes with value 1.
  - For an empty tree, the function should return 0.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the number of nodes with value 1, we can traverse the entire tree and check each node's value.
- Step-by-step breakdown of the solution:
  1. Start at the root node.
  2. Check if the current node's value is 1. If it is, increment a counter.
  3. Recursively traverse the left and right subtrees.
- Why this approach comes to mind first: It is straightforward and ensures that every node in the tree is visited.

```cpp
class Solution {
public:
    int countNodesWithValueOne(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        
        int count = 0;
        if (root->val == 1) {
            count++;
        }
        
        count += countNodesWithValueOne(root->left);
        count += countNodesWithValueOne(root->right);
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack. In the worst case, the tree is skewed, and $h = n$.
> - **Why these complexities occur:** The time complexity is linear because we visit each node exactly once. The space complexity depends on the height of the tree due to recursive calls.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must visit each node at least once to count the nodes with value 1. No optimization can reduce the number of nodes we need to visit.
- Detailed breakdown of the approach: The optimal approach remains the same as the brute force approach because it is inherently optimal for this problem.
- Proof of optimality: Any algorithm that solves this problem must visit each node at least once to determine its value. Therefore, the time complexity cannot be better than $O(n)$.
- Why further optimization is impossible: Since we must examine every node, and each node is visited exactly once, no further optimization is possible without changing the problem constraints.

```cpp
class Solution {
public:
    int countNodesWithValueOne(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        
        int count = (root->val == 1) ? 1 : 0;
        count += countNodesWithValueOne(root->left);
        count += countNodesWithValueOne(root->right);
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** The time complexity is optimal because we must visit each node at least once. The space complexity is also optimal for this recursive implementation.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal (specifically, recursive traversal), and the importance of considering the minimum number of operations required to solve a problem.
- Problem-solving patterns identified: The need to visit every node in a tree to solve problems that require examining each node's value.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the inherent requirements of the problem.
- Similar problems to practice: Other tree traversal problems, such as finding the maximum or minimum value in a tree, or problems that require counting nodes based on specific conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case (e.g., an empty tree), or not correctly updating the count of nodes with value 1.
- Edge cases to watch for: An empty tree, or a tree with a single node.
- Performance pitfalls: Using an inefficient traversal method, such as unnecessarily visiting nodes multiple times.
- Testing considerations: Ensure that the solution works correctly for trees of varying sizes and structures, including edge cases like an empty tree or a tree with all nodes having value 1.