## Kth Smallest Element in a BST
**Problem Link:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/description

**Problem Statement:**
- Input: The root of a binary search tree (`root`) and an integer `k`.
- Constraints: `1 <= k <= n <= 2^31 - 1`, where `n` is the number of nodes in the BST.
- Expected Output: The `k`th smallest element in the BST.
- Key Requirements: The solution should efficiently find the `k`th smallest element without modifying the BST.
- Edge Cases: Consider cases where `k` is 1 or `n`, and when the BST is skewed.

**Example Test Cases:**
- For a balanced BST with nodes 5, 3, 7, 2, 4, 6, 8, the 3rd smallest element is 4.
- For a skewed BST with nodes 5, 3, 2, 1, the 4th smallest element is 5.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves traversing the BST and storing all node values in a vector.
- Then, sort the vector and return the `k`th element.
- This approach comes to mind first because it directly addresses the problem statement without requiring a deep understanding of BST properties.

```cpp
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> values;
        // Perform an in-order traversal to get all node values in ascending order
        inOrderTraversal(root, values);
        // Since values are already in order due to in-order traversal, no need to sort
        return values[k - 1];
    }
    
    void inOrderTraversal(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        inOrderTraversal(node->left, values);
        values.push_back(node->val);
        inOrderTraversal(node->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST. This is because we visit each node once during the in-order traversal.
> - **Space Complexity:** $O(n)$, as in the worst case (a skewed tree), the recursion stack can go up to $n$ levels, and we also store $n$ values in the vector.
> - **Why these complexities occur:** The time complexity is linear due to the single pass through the tree, and the space complexity is also linear due to the storage of all node values and the recursion stack.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use the properties of a BST to our advantage. An in-order traversal of a BST visits nodes in ascending order.
- We can modify the in-order traversal to stop once we've found the `k`th smallest element, reducing unnecessary work.
- This approach is optimal because it leverages the BST's structure to minimize the number of nodes that need to be visited.

```cpp
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        int result = -1;
        inOrderTraversal(root, k, count, result);
        return result;
    }
    
    void inOrderTraversal(TreeNode* node, int& k, int& count, int& result) {
        if (node == nullptr || count >= k) return;
        inOrderTraversal(node->left, k, count, result);
        count++;
        if (count == k) {
            result = node->val;
            return;
        }
        inOrderTraversal(node->right, k, count, result);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h + k)$, where $h$ is the height of the tree. In the worst case (a skewed tree), this becomes $O(n)$, but for a balanced BST, it's $O(\log n + k)$.
> - **Space Complexity:** $O(h)$, for the recursion stack. In the worst case, this is $O(n)$, but for a balanced BST, it's $O(\log n)$.
> - **Optimality proof:** This approach is optimal because it stops as soon as it finds the `k`th smallest element, minimizing the number of nodes visited and the recursion depth.

---

### Final Notes
**Learning Points:**
- Leveraging the properties of data structures (in this case, BSTs) to optimize solutions.
- Modifying standard traversal algorithms (like in-order traversal) to fit specific problem requirements.
- Balancing time and space complexity based on problem constraints.

**Mistakes to Avoid:**
- Failing to consider the properties of the BST and instead treating it as a general tree.
- Not optimizing the traversal to stop once the `k`th smallest element is found.
- Ignoring the potential for skewed trees when analyzing time and space complexity.