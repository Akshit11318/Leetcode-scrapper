## Linked List in Binary Tree

**Problem Link:** https://leetcode.com/problems/linked-list-in-binary-tree/description

**Problem Statement:**
- Input format: A binary tree (`root`) and a linked list (`head`).
- Constraints: The number of nodes in the linked list is in the range `[1, 100]`, and the number of nodes in the binary tree is in the range `[1, 2500]`. The binary tree node values are unique.
- Expected output format: Return `true` if the linked list exists in the binary tree, and `false` otherwise.
- Key requirements and edge cases to consider:
  - The linked list must be a contiguous sublist of the pre-order traversal of the binary tree.
  - Handle cases where the linked list is empty or the binary tree is empty.
- Example test cases with explanations:
  - Example 1:
    - Input: `root = [4, 5, 2], head = [4, 5]`
    - Output: `true`
    - Explanation: The linked list `[4, 5]` is a contiguous sublist of the pre-order traversal of the binary tree `[4, 5, 2]`.
  - Example 2:
    - Input: `root = [4, 5, 2], head = [5, 2]`
    - Output: `false`
    - Explanation: The linked list `[5, 2]` is not a contiguous sublist of the pre-order traversal of the binary tree `[4, 5, 2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can perform a pre-order traversal of the binary tree and check if the linked list is a contiguous sublist of the traversal.
- Step-by-step breakdown of the solution:
  1. Perform a pre-order traversal of the binary tree and store the node values in a vector.
  2. Iterate over the vector and check if the linked list is a contiguous sublist.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the traversal and iteration.

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
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        vector<int> preorder;
        traverse(root, preorder);
        int m = preorder.size();
        int n = 0;
        ListNode* temp = head;
        while (temp) {
            temp = temp->next;
            n++;
        }
        for (int i = 0; i <= m - n; i++) {
            bool match = true;
            ListNode* node = head;
            for (int j = 0; j < n; j++) {
                if (node->val != preorder[i + j]) {
                    match = false;
                    break;
                }
                node = node->next;
            }
            if (match) return true;
        }
        return false;
    }
    
    void traverse(TreeNode* node, vector<int>& preorder) {
        if (!node) return;
        preorder.push_back(node->val);
        traverse(node->left, preorder);
        traverse(node->right, preorder);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of nodes in the binary tree and $n$ is the number of nodes in the linked list. The pre-order traversal takes $O(m)$ time, and the iteration over the vector takes $O(m - n + 1) \cdot O(n)$ time.
> - **Space Complexity:** $O(m)$, where $m$ is the number of nodes in the binary tree. The vector used to store the pre-order traversal takes $O(m)$ space.
> - **Why these complexities occur:** The high time complexity occurs due to the iteration over the vector and the traversal of the binary tree. The space complexity occurs due to the storage of the pre-order traversal.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing a pre-order traversal of the entire binary tree, we can use a recursive approach to traverse the tree and check if the linked list is a contiguous sublist.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes a binary tree node and a linked list node as input.
  2. If the linked list node is null, return true, indicating that the linked list is a contiguous sublist.
  3. If the binary tree node is null or the values of the nodes do not match, return false.
  4. Recursively call the function on the left and right child nodes of the binary tree node.
- Proof of optimality: This approach has a lower time complexity than the brute force approach, as it avoids the unnecessary traversal of the binary tree.

```cpp
class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!head) return true;
        if (!root) return false;
        return match(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
    
    bool match(ListNode* head, TreeNode* root) {
        if (!head) return true;
        if (!root) return false;
        if (head->val != root->val) return false;
        return match(head->next, root->left) || match(head->next, root->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of nodes in the binary tree and $n$ is the number of nodes in the linked list. The recursive function takes $O(m)$ time, and the match function takes $O(n)$ time.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the binary tree. The recursive function call stack takes $O(h)$ space.
> - **Optimality proof:** This approach is optimal because it avoids the unnecessary traversal of the binary tree and uses a recursive approach to check if the linked list is a contiguous sublist.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, traversal of binary tree, and checking for contiguous sublist.
- Problem-solving patterns identified: Using a recursive approach to solve problems that involve traversal of a data structure.
- Optimization techniques learned: Avoiding unnecessary traversal of a data structure and using a recursive approach to improve time complexity.
- Similar problems to practice: Problems that involve traversal of a data structure and checking for contiguous sublists.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base cases correctly, not checking for null nodes, and not using a recursive approach to improve time complexity.
- Edge cases to watch for: Handling cases where the linked list is empty or the binary tree is empty.
- Performance pitfalls: Not optimizing the time complexity of the solution.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness.