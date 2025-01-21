## Convert Sorted List to Binary Search Tree
**Problem Link:** https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description

**Problem Statement:**
- Input format: A sorted linked list.
- Constraints: The number of nodes in the linked list is in the range `[0, 5000]`.
- Expected output format: A balanced binary search tree.
- Key requirements: The binary search tree should be as balanced as possible.
- Edge cases to consider: An empty linked list, a linked list with one node, a linked list with two nodes.
- Example test cases with explanations:
  - Example 1:
    - Input: `[-10,-3,0,5,9]`
    - Output: `[0,-3,9,-10,null,5]`
    - Explanation: The output is a balanced binary search tree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can first convert the linked list into an array, then use a recursive approach to construct the binary search tree.
- Step-by-step breakdown of the solution:
  1. Convert the linked list into an array.
  2. Define a recursive function to construct the binary search tree.
  3. In each recursive call, find the middle element of the current array and make it the root of the current subtree.
  4. Recursively construct the left and right subtrees using the elements before and after the middle element.
- Why this approach comes to mind first: It is a straightforward approach that involves converting the linked list into an array, which is easier to work with, and then using a recursive approach to construct the binary search tree.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

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
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) return nullptr;
        
        vector<int> vals;
        while (head) {
            vals.push_back(head->val);
            head = head->next;
        }
        
        return sortedArrayToBST(vals, 0, vals.size() - 1);
    }
    
    TreeNode* sortedArrayToBST(vector<int>& vals, int start, int end) {
        if (start > end) return nullptr;
        
        int mid = start + (end - start) / 2;
        TreeNode* node = new TreeNode(vals[mid]);
        node->left = sortedArrayToBST(vals, start, mid - 1);
        node->right = sortedArrayToBST(vals, mid + 1, end);
        
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list. This is because we are converting the linked list into an array, which takes $O(n)$ time, and then constructing the binary search tree, which also takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list. This is because we are storing the elements of the linked list in an array, which takes $O(n)$ space.
> - **Why these complexities occur:** The time complexity occurs because we are converting the linked list into an array and then constructing the binary search tree. The space complexity occurs because we are storing the elements of the linked list in an array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can construct the binary search tree directly from the linked list without converting it into an array.
- Detailed breakdown of the approach:
  1. Define a recursive function to construct the binary search tree.
  2. In each recursive call, find the middle element of the current linked list and make it the root of the current subtree.
  3. Recursively construct the left and right subtrees using the elements before and after the middle element.
- Proof of optimality: This approach is optimal because it avoids the extra space required to store the elements of the linked list in an array.
- Why further optimization is impossible: This approach is already optimal because it has a time complexity of $O(n)$ and a space complexity of $O(log n)$, which is the best possible time and space complexity for this problem.

```cpp
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) return nullptr;
        
        return sortedListToBSTHelper(head, nullptr);
    }
    
    TreeNode* sortedListToBSTHelper(ListNode* head, ListNode* tail) {
        if (head == tail) return nullptr;
        
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != tail && fast->next->next != tail) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        TreeNode* node = new TreeNode(slow->val);
        node->left = sortedListToBSTHelper(head, slow);
        node->right = sortedListToBSTHelper(slow->next, tail);
        
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list. This is because we are constructing the binary search tree directly from the linked list, which takes $O(n)$ time.
> - **Space Complexity:** $O(log n)$ where $n$ is the number of nodes in the linked list. This is because the maximum depth of the recursion tree is $O(log n)$.
> - **Optimality proof:** The time complexity is optimal because we are constructing the binary search tree directly from the linked list. The space complexity is optimal because we are using a recursive approach, which has a space complexity of $O(log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, binary search tree construction.
- Problem-solving patterns identified: Constructing a balanced binary search tree from a sorted linked list.
- Optimization techniques learned: Avoiding extra space by constructing the binary search tree directly from the linked list.
- Similar problems to practice: Constructing a balanced binary search tree from a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not updating the pointers correctly.
- Edge cases to watch for: An empty linked list, a linked list with one node, a linked list with two nodes.
- Performance pitfalls: Using a non-recursive approach, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different inputs, including edge cases.