## Maximum Depth of N-ary Tree

**Problem Link:** https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description

**Problem Statement:**
- Input: An N-ary tree, where each node has a `val` attribute and a `children` attribute.
- Constraints: The tree is guaranteed to be non-empty and have at most $10^4$ nodes.
- Expected Output: The maximum depth of the tree, which is the number of nodes along the longest path from the root node down to the farthest leaf node.
- Key Requirements and Edge Cases:
  - The tree can have any number of children for each node.
  - The tree can be empty, but in this problem, it's guaranteed to be non-empty.
- Example Test Cases:
  - A tree with a single node has a depth of 1.
  - A tree with multiple levels and multiple children per node has a depth equal to the number of levels.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the depth of each subtree and keep track of the maximum depth found so far.
- Step-by-step breakdown:
  1. Define a recursive function to calculate the depth of a subtree.
  2. For each node, calculate the depth of its children and add 1 to the maximum depth found.
  3. Keep track of the maximum depth found so far.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
class Solution {
public:
    int maxDepth(Node* root) {
        if (!root) return 0; // Base case: empty tree
        int max_child_depth = 0;
        for (Node* child : root->children) {
            max_child_depth = max(max_child_depth, maxDepth(child));
        }
        return max_child_depth + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree, because that's the maximum depth of the recursion stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is proportional to the height of the tree because that's how deep our recursion stack can get.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The brute force approach is already optimal because it has to visit each node at least once to determine the maximum depth.
- Detailed breakdown: The optimal approach is the same as the brute force approach because it's already optimal.
- Proof of optimality: Any algorithm that calculates the maximum depth of an N-ary tree must visit each node at least once, so the optimal time complexity is $O(N)$.
- Why further optimization is impossible: We can't do better than visiting each node once because that's the minimum amount of work required to calculate the maximum depth.

```cpp
class Solution {
public:
    int maxDepth(Node* root) {
        if (!root) return 0;
        int max_child_depth = 0;
        for (Node* child : root->children) {
            max_child_depth = max(max_child_depth, maxDepth(child));
        }
        return max_child_depth + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree.
> - **Optimality proof:** The algorithm visits each node once, which is the minimum amount of work required to calculate the maximum depth.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Recursion, tree traversal.
- Problem-solving patterns: Divide and conquer, dynamic programming.
- Optimization techniques: None, because the brute force approach is already optimal.
- Similar problems to practice: Maximum depth of a binary tree, minimum depth of a binary tree.

**Mistakes to Avoid:**
- Not checking for an empty tree.
- Not keeping track of the maximum depth found so far.
- Not visiting each node at least once.
- Not considering the height of the tree when analyzing space complexity.

---