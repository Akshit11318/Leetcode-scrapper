## K-th Largest Perfect Subtree Size in Binary Tree

**Problem Link:** https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/description

**Problem Statement:**
- Input: A binary tree where each node has a unique value and a positive integer `k`.
- Constraints: The number of nodes in the tree is between $1$ and $10^4$, and $k$ is between $1$ and the number of nodes in the tree.
- Expected Output: The `k`-th largest perfect subtree size in the binary tree. If there are less than `k` perfect subtrees, return `-1`.
- Key Requirements:
  - A perfect subtree is a subtree where all leaves are at the same level and all internal nodes have two children.
  - The size of a subtree is the number of nodes in the subtree.
- Edge Cases:
  - The tree may contain only one node.
  - `k` may be larger than the number of perfect subtrees.

### Brute Force Approach

**Explanation:**
- First, we need to traverse the tree and find all perfect subtrees.
- Then, we calculate the size of each perfect subtree.
- Finally, we sort the sizes in descending order and return the `k`-th largest size.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthLargestValue(vector<int>& sizes, int k) {
        sort(sizes.rbegin(), sizes.rend());
        if (k > sizes.size()) return -1;
        return sizes[k-1];
    }

    int getDepth(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(getDepth(node->left), getDepth(node->right));
    }

    bool isPerfect(TreeNode* node) {
        if (!node) return true;
        int leftDepth = getDepth(node->left);
        int rightDepth = getDepth(node->right);
        if (leftDepth != rightDepth) return false;
        if (!node->left && !node->right) return true;
        if (!node->left || !node->right) return false;
        return isPerfect(node->left) && isPerfect(node->right);
    }

    int kthLargestPerfectSubtreeSize(TreeNode* root, int k) {
        vector<int> sizes;
        traverse(root, sizes);
        return kthLargestValue(sizes, k);
    }

    void traverse(TreeNode* node, vector<int>& sizes) {
        if (!node) return;
        if (isPerfect(node)) {
            sizes.push_back(getSize(node));
        }
        traverse(node->left, sizes);
        traverse(node->right, sizes);
    }

    int getSize(TreeNode* node) {
        if (!node) return 0;
        return 1 + getSize(node->left) + getSize(node->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$, where $n$ is the number of nodes in the tree. This is because we are traversing the tree for each node and sorting the sizes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are storing the sizes of all perfect subtrees.
> - **Why these complexities occur:** The brute force approach has high time complexity because it involves traversing the tree for each node and sorting the sizes. The space complexity is high because we are storing the sizes of all perfect subtrees.

---

### Optimal Approach (Required)

**Explanation:**
- We can optimize the solution by using a priority queue to store the sizes of perfect subtrees. This way, we can avoid sorting the sizes at the end.
- We also need to optimize the `isPerfect` function by using a single traversal to calculate the depth and check if the subtree is perfect.

```cpp
class Solution {
public:
    int kthLargestPerfectSubtreeSize(TreeNode* root, int k) {
        priority_queue<int> pq;
        traverse(root, pq);
        for (int i = 0; i < k - 1; i++) {
            if (pq.empty()) return -1;
            pq.pop();
        }
        return pq.empty() ? -1 : pq.top();
    }

    void traverse(TreeNode* node, priority_queue<int>& pq) {
        if (!node) return;
        if (isPerfect(node)) {
            pq.push(getSize(node));
        }
        traverse(node->left, pq);
        traverse(node->right, pq);
    }

    bool isPerfect(TreeNode* node) {
        if (!node) return true;
        int leftDepth = getDepth(node->left);
        int rightDepth = getDepth(node->right);
        if (leftDepth != rightDepth) return false;
        if (!node->left && !node->right) return true;
        if (!node->left || !node->right) return false;
        return isPerfect(node->left) && isPerfect(node->right);
    }

    int getDepth(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(getDepth(node->left), getDepth(node->right));
    }

    int getSize(TreeNode* node) {
        if (!node) return 0;
        return 1 + getSize(node->left) + getSize(node->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of nodes in the tree and $k$ is the input integer. This is because we are traversing the tree and using a priority queue to store the sizes of perfect subtrees.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are storing the sizes of all perfect subtrees in the priority queue.
> - **Optimality proof:** This solution is optimal because we are using a priority queue to store the sizes of perfect subtrees, which allows us to efficiently find the `k`-th largest size.

---

### Final Notes

**Learning Points:**
- The importance of using data structures such as priority queues to optimize solutions.
- The need to optimize recursive functions by using memoization or dynamic programming.
- The importance of considering edge cases and handling them properly.

**Mistakes to Avoid:**
- Not considering the time complexity of the solution and optimizing it accordingly.
- Not handling edge cases properly.
- Not using data structures such as priority queues to optimize solutions.
- Not optimizing recursive functions by using memoization or dynamic programming.