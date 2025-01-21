## Reverse Odd Levels of Binary Tree
**Problem Link:** https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range $[1, 2^{14} - 1]$.
- Expected Output: The root of the modified binary tree where all odd levels are reversed.
- Key Requirements:
  - Identify odd levels in a binary tree.
  - Reverse the nodes at these odd levels.
- Edge Cases:
  - A tree with a single node (already reversed).
  - An empty tree (no operation needed).
- Example Test Cases:
  - Given a binary tree with nodes [2,3,5,8,13,21,34], reversing odd levels should yield a specific modified tree structure.

---

### Brute Force Approach
**Explanation:**
- Initial Thought Process: Perform a level-order traversal (BFS) of the binary tree, identify the odd levels, and then reverse the nodes at these levels.
- Step-by-Step Breakdown:
  1. Implement a level-order traversal using a queue.
  2. For each level, check if it's an odd level (starting from level 1 as the first odd level).
  3. If it's an odd level, reverse the nodes in the queue before proceeding to the next level.

```cpp
#include <queue>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* reverseOddLevels(TreeNode* root) {
        if (!root) return nullptr;
        
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        
        while (!q.empty()) {
            int size = q.size();
            vector<TreeNode*> nodesAtLevel;
            
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front(); q.pop();
                nodesAtLevel.push_back(node);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (level % 2 == 1) { // Odd level
                int left = 0, right = nodesAtLevel.size() - 1;
                while (left < right) {
                    swap(nodesAtLevel[left]->val, nodesAtLevel[right]->val);
                    left++;
                    right--;
                }
            }
            
            level++;
        }
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree, since we visit each node once during the level-order traversal.
> - **Space Complexity:** $O(N)$ for storing nodes at each level in the queue and vector.
> - **Why these complexities occur:** The level-order traversal inherently visits each node once, leading to linear time complexity. The space complexity is due to the queue and vector used to store nodes at each level.

---

### Optimal Approach (Required)
**Explanation:**
- Key Insight: The brute force approach is already optimal in terms of time complexity because we must visit each node at least once to reverse the odd levels.
- Detailed Breakdown:
  - The provided brute force solution is already optimal because it uses a level-order traversal and reverses nodes at odd levels efficiently.
  - No further optimization is possible without changing the fundamental approach of visiting each node.

```cpp
// Same code as the brute force approach, as it's already optimal.
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree.
> - **Space Complexity:** $O(N)$ for storing nodes in the queue and vector.
> - **Optimality Proof:** This approach is optimal because it visits each node exactly once, which is necessary for reversing odd levels, and it does so with minimal additional space for the queue and vector.

---

### Final Notes

**Learning Points:**
- Key Algorithmic Concepts: Level-order traversal, reversing nodes at specific levels.
- Problem-Solving Patterns: Identifying the need for a level-order traversal when dealing with level-specific operations.
- Optimization Techniques: Ensuring each node is visited only once for efficiency.

**Mistakes to Avoid:**
- Incorrectly identifying odd levels (remember that level 1 is the first odd level).
- Failing to handle edge cases like an empty tree or a tree with a single node.
- Inefficiently reversing nodes (using a vector to store nodes at each level can simplify the reversal process).