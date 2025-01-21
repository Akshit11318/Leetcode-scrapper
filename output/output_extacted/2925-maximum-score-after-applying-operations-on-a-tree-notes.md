## Maximum Score After Applying Operations on a Tree
**Problem Link:** https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/description

**Problem Statement:**
- Input format: You are given a tree with `n` nodes, where each node has a unique integer value from `1` to `n`. Each node has a list of its child nodes.
- Constraints: The tree is guaranteed to be connected and have no cycles.
- Expected output format: The maximum score that can be obtained by applying operations on the tree.
- Key requirements and edge cases to consider: The score is calculated by counting the number of nodes with an even number of children. If a node has an odd number of children, you can choose to add or remove a child node to make it even.
- Example test cases with explanations:
    - Example 1: A tree with 3 nodes, where node 1 has children 2 and 3. The maximum score is 1, which can be obtained by removing one child from node 1.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of adding or removing child nodes to make each node have an even number of children.
- Step-by-step breakdown of the solution:
    1. Initialize a variable to store the maximum score.
    2. Iterate over all nodes in the tree.
    3. For each node, try all possible combinations of adding or removing child nodes.
    4. Calculate the score for each combination and update the maximum score if necessary.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Define the structure for a tree node
struct TreeNode {
    int val;
    vector<TreeNode*> children;
};

// Function to calculate the maximum score using brute force
int maxScoreBruteForce(TreeNode* root) {
    int maxScore = 0;

    // Function to try all possible combinations of adding or removing child nodes
    void tryCombinations(TreeNode* node, int score) {
        if (node == nullptr) return;

        // Calculate the score for the current node
        int nodeScore = (node->children.size() % 2 == 0) ? 1 : 0;

        // Update the maximum score if necessary
        maxScore = max(maxScore, score + nodeScore);

        // Try all possible combinations of adding or removing child nodes
        for (int i = 0; i < node->children.size(); i++) {
            TreeNode* child = node->children[i];
            node->children.erase(node->children.begin() + i);
            tryCombinations(child, score + nodeScore);
            node->children.insert(node->children.begin() + i, child);
        }
    }

    tryCombinations(root, 0);

    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes in the tree. This is because we try all possible combinations of adding or removing child nodes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the recursive call stack.
> - **Why these complexities occur:** The time complexity is exponential because we try all possible combinations, and the space complexity is linear because we need to store the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a dynamic programming approach to calculate the maximum score.
- Detailed breakdown of the approach:
    1. Initialize a variable to store the maximum score.
    2. Iterate over all nodes in the tree.
    3. For each node, calculate the score for the current node and its children.
    4. Update the maximum score if necessary.
- Proof of optimality: This approach is optimal because we only need to calculate the score for each node once.

```cpp
// Function to calculate the maximum score using dynamic programming
int maxScoreOptimal(TreeNode* root) {
    int maxScore = 0;

    // Function to calculate the score for a node and its children
    int calculateScore(TreeNode* node) {
        if (node == nullptr) return 0;

        int score = (node->children.size() % 2 == 0) ? 1 : 0;

        // Calculate the score for the children
        for (TreeNode* child : node->children) {
            score += calculateScore(child);
        }

        return score;
    }

    maxScore = calculateScore(root);

    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we only need to calculate the score for each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the recursive call stack.
> - **Optimality proof:** This approach is optimal because we only need to calculate the score for each node once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive call stack management.
- Problem-solving patterns identified: Using dynamic programming to solve problems with overlapping subproblems.
- Optimization techniques learned: Avoiding redundant calculations by using dynamic programming.
- Similar problems to practice: Other problems that involve calculating scores or maximizing values in a tree or graph.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the maximum score, incorrect calculation of the score for a node and its children.
- Edge cases to watch for: Handling empty trees, trees with a single node, trees with nodes that have no children.
- Performance pitfalls: Using an exponential-time approach instead of a dynamic programming approach.
- Testing considerations: Testing the function with different types of trees, including empty trees and trees with a single node.