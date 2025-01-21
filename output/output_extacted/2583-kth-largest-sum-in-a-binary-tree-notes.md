## Kth Largest Sum in a Binary Tree
**Problem Link:** https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description

**Problem Statement:**
- Given a binary tree where each node has a unique integer value and a target integer `k`, find the `k`-th largest sum of all possible paths from a leaf to the root.
- The input is the root of the binary tree and the integer `k`.
- The expected output is the `k`-th largest sum.
- Key requirements include handling the binary tree structure, calculating path sums, and efficiently finding the `k`-th largest sum.
- Edge cases include an empty tree, a tree with a single node, and when `k` is larger than the number of paths.

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating all possible path sums from leaves to the root and then sorting these sums to find the `k`-th largest.
- This approach comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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
    vector<int> sums;
    void dfs(TreeNode* node, int sum) {
        if (!node) return;
        sum += node->val;
        if (!node->left && !node->right) {
            sums.push_back(sum);
        } else {
            dfs(node->left, sum);
            dfs(node->right, sum);
        }
    }

    int kthLargestValue(TreeNode* root, int k) {
        dfs(root, 0);
        sort(sums.rbegin(), sums.rend());
        return sums[k-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N + 2^H)$, where $N$ is the number of nodes in the tree and $H$ is the height of the tree. $N$ represents the number of nodes to visit, and $2^H$ accounts for the worst-case number of paths in an unbalanced tree. The $\log N$ factor comes from sorting the sums.
> - **Space Complexity:** $O(N + 2^H)$, for storing the sums and the recursive call stack.
> - **Why these complexities occur:** The brute force approach requires visiting each node, calculating all possible path sums, and then sorting these sums, leading to the mentioned complexities.

### Optimal Approach (Required)

**Explanation:**
- The key insight for the optimal solution is to use a priority queue (like a heap) to keep track of the `k` largest sums encountered so far. This avoids the need to store all sums and sort them at the end.
- The detailed breakdown involves performing a depth-first search (DFS) of the tree, calculating the sum of each path from a leaf to the root, and updating the priority queue accordingly.

```cpp
#include <iostream>
#include <vector>
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
    int kthLargestValue(TreeNode* root, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        dfs(root, 0, pq, k);
        return pq.top();
    }

    void dfs(TreeNode* node, int sum, priority_queue<int, vector<int>, greater<int>>& pq, int& k) {
        if (!node) return;
        sum += node->val;
        if (!node->left && !node->right) {
            if (pq.size() < k) {
                pq.push(sum);
            } else if (sum > pq.top()) {
                pq.pop();
                pq.push(sum);
            }
        } else {
            dfs(node->left, sum, pq, k);
            dfs(node->right, sum, pq, k);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log k)$, where $N$ is the number of nodes in the tree. The $\log k$ factor comes from the priority queue operations.
> - **Space Complexity:** $O(N + k)$, for the recursive call stack and the priority queue.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the `k`-th largest sum, leveraging the efficiency of priority queue operations to avoid unnecessary sorting or storage.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of DFS for tree traversal and priority queues for efficient sorting and selection of the `k`-th largest element.
- Problem-solving patterns identified include breaking down complex problems into manageable parts (e.g., calculating path sums and then selecting the `k`-th largest) and leveraging data structures for efficiency.
- Optimization techniques learned include minimizing unnecessary operations and using appropriate data structures to reduce computational complexity.

**Mistakes to Avoid:**
- Common implementation errors include incorrect handling of edge cases (e.g., an empty tree or `k` larger than the number of paths) and inefficient use of data structures (e.g., sorting all sums instead of using a priority queue).
- Edge cases to watch for include trees with a single node, trees with no leaves, and scenarios where `k` exceeds the number of paths.
- Performance pitfalls include unnecessary recursive calls or iterations and inefficient memory usage.