## Closest Binary Search Tree Value II
**Problem Link:** https://leetcode.com/problems/closest-binary-search-tree-value-ii/description

**Problem Statement:**
- Given the root of a binary search tree and a target value, return a list of the `k` closest numbers to the target in the BST. You may return the answer in any order.
- Input format and constraints:
  - The number of nodes in the tree is in the range `[1, 10^4]`.
  - `1 <= k <= 10^4`.
  - `0 <= Node.val <= 10^9`.
  - `-10^9 <= target <= 10^9`.
- Expected output format:
  - A list of `k` integers representing the closest values to the target in the BST.
- Key requirements and edge cases to consider:
  - The BST may contain duplicate values.
  - The target value may not be present in the BST.
- Example test cases with explanations:
  - Example 1: Given the root of a BST with values [4,2,5,1,3], target = 3.714286, and k = 2, return [4,3].

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the BST and store all node values in a list.
- Then, calculate the absolute difference between each node value and the target.
- Sort the list of node values based on their differences with the target.
- Return the first `k` elements from the sorted list.

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
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        vector<int> values;
        inorderTraversal(root, values);
        vector<pair<double, int>> diffValues;
        for (int value : values) {
            diffValues.push_back({abs(value - target), value});
        }
        sort(diffValues.begin(), diffValues.end());
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(diffValues[i].second);
        }
        return result;
    }

    void inorderTraversal(TreeNode* root, vector<int>& values) {
        if (root == nullptr) return;
        inorderTraversal(root->left, values);
        values.push_back(root->val);
        inorderTraversal(root->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the list of node values, where $n$ is the number of nodes in the BST.
> - **Space Complexity:** $O(n)$ for storing the node values and their differences with the target.
> - **Why these complexities occur:** The brute force approach involves traversing the BST to collect node values, calculating differences, and sorting the list, which leads to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a priority queue to store the `k` closest values to the target.
- Traverse the BST and calculate the absolute difference between each node value and the target.
- Push the difference and node value into the priority queue.
- If the queue size exceeds `k`, remove the largest difference from the queue.
- Finally, return the node values from the priority queue.

```cpp
class Solution {
public:
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        priority_queue<pair<double, int>> maxHeap;
        inorderTraversal(root, target, k, maxHeap);
        vector<int> result;
        while (!maxHeap.empty()) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return result;
    }

    void inorderTraversal(TreeNode* root, double target, int k, priority_queue<pair<double, int>>& maxHeap) {
        if (root == nullptr) return;
        inorderTraversal(root->left, target, k, maxHeap);
        double diff = abs(root->val - target);
        if (maxHeap.size() < k) {
            maxHeap.push({diff, root->val});
        } else if (diff < maxHeap.top().first) {
            maxHeap.pop();
            maxHeap.push({diff, root->val});
        }
        inorderTraversal(root->right, target, k, maxHeap);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$ due to using a priority queue to store the `k` closest values, where $n$ is the number of nodes in the BST.
> - **Space Complexity:** $O(n)$ for storing the node values in the priority queue.
> - **Optimality proof:** This approach is optimal because it only stores the `k` closest values in the priority queue, reducing the space complexity and avoiding unnecessary sorting.

---

### Final Notes

**Learning Points:**
- Using a priority queue to store the `k` closest values reduces the space complexity and avoids unnecessary sorting.
- The optimal approach has a time complexity of $O(n \log k)$, which is more efficient than the brute force approach for large values of `n`.
- The problem requires careful consideration of edge cases, such as duplicate values in the BST and the target value not being present in the BST.

**Mistakes to Avoid:**
- Not considering the edge cases, such as duplicate values in the BST and the target value not being present in the BST.
- Using a brute force approach with a time complexity of $O(n \log n)$, which can be optimized to $O(n \log k)$ using a priority queue.
- Not validating the input values, such as checking for null pointers and invalid values of `k`.