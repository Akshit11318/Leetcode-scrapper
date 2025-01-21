## Remove Linked List Elements
**Problem Link:** https://leetcode.com/problems/remove-linked-list-elements/description

**Problem Statement:**
- Input: The head of a linked list and an integer `val`.
- Expected output: The head of the modified linked list after removing all the nodes with a value equal to `val`.
- Key requirements: 
  - Remove all nodes with the given value `val`.
  - Handle edge cases like an empty list, a list with one node, or a list with multiple nodes to remove.
- Example test cases:
  - Example 1: Given the linked list `1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6`, `val = 6`. After removing all `6`s, the linked list becomes `1 -> 2 -> 3 -> 4 -> 5`.
  - Example 2: Given the linked list ``, `val = 1`. The function should return an empty list since there are no nodes to remove from an empty list.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through the linked list and checking each node's value. If the value matches `val`, we remove that node.
- This approach is straightforward but may not be the most efficient due to the potential need to update node pointers for each removal.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* removeElements(ListNode* head, int val) {
    // Create a dummy node to simplify some corner cases such as a list with only one node, or removing the head of the list.
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* current = dummy;
    
    while (current->next) {
        if (current->next->val == val) {
            // Remove the node
            ListNode* temp = current->next;
            current->next = current->next->next;
            delete temp;
        } else {
            current = current->next;
        }
    }
    
    // Return the next of dummy as the new head
    ListNode* newHead = dummy->next;
    delete dummy;
    return newHead;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list, because we visit each node once.
> - **Space Complexity:** $O(1)$ since we use a constant amount of space to store the dummy node and other variables, regardless of the input size.
> - **Why these complexities occur:** The time complexity is linear because we potentially iterate through the entire list once. The space complexity is constant because, aside from the dummy node, we do not use any additional data structures that scale with input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight here is recognizing that the brute force approach is already quite efficient and optimal for this problem. It iterates through the list once, removing nodes as necessary, which is the minimum number of operations required to solve the problem.
- The use of a dummy node simplifies the code and reduces the number of special cases we need to handle, such as when the head of the list needs to be removed.
- This approach is optimal because we must at least look at each node once to determine if it should be removed, making the time complexity $O(n)$.

```cpp
ListNode* removeElements(ListNode* head, int val) {
    // Create a dummy node to simplify some corner cases such as a list with only one node, or removing the head of the list.
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* current = dummy;
    
    while (current->next) {
        if (current->next->val == val) {
            // Remove the node
            ListNode* temp = current->next;
            current->next = current->next->next;
            delete temp;
        } else {
            current = current->next;
        }
    }
    
    // Return the next of dummy as the new head
    ListNode* newHead = dummy->next;
    delete dummy;
    return newHead;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list, because we visit each node once.
> - **Space Complexity:** $O(1)$ since we use a constant amount of space to store the dummy node and other variables, regardless of the input size.
> - **Optimality proof:** This is optimal because we must examine each node at least once to determine if it should be removed, making $O(n)$ the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- The importance of iterating through a linked list to examine or modify its nodes.
- Using a dummy node to simplify edge cases in linked list problems.
- Understanding that sometimes, the brute force approach can be optimal or very close to optimal, especially when the problem requires examining each element at least once.

**Mistakes to Avoid:**
- Not handling edge cases properly, such as an empty list or a list with one node.
- Failing to update node pointers correctly when removing nodes, which can lead to memory leaks or incorrect results.
- Not considering the use of a dummy node to simplify code and reduce special case handling.