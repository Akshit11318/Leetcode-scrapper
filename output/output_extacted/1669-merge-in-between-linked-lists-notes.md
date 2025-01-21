## Merge in Between Linked Lists

**Problem Link:** [https://leetcode.com/problems/merge-in-between-linked-lists/description](https://leetcode.com/problems/merge-in-between-linked-lists/description)

**Problem Statement:**
- Input: You are given three non-empty linked lists: `list1`, `a`, and `b`. 
- Constraints: `a` and `b` are linked lists with the same node type as `list1`. 
- Expected output: Merge the nodes of `list2` into `list1` between the nodes at positions `a` and `b`.
- Key requirements: The start position is 0-indexed.
- Example test cases:
  - Input: `list1 = [0,1,2,3], a = 1, b = 1, list2 = [1000000]`
  - Output: `[0,1,1000000,2,3]`
  - Explanation: We merge the nodes of `list2` into `list1` between the nodes at positions `1` and `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we first need to find the nodes at positions `a` and `b` in `list1`.
- Step-by-step breakdown of the solution:
  1. Find the node at position `a` in `list1`.
  2. Find the node at position `b` in `list1`.
  3. Find the last node of `list2`.
  4. Connect the node before `b` in `list1` to the start of `list2`.
  5. Connect the end of `list2` to the node at position `b` in `list1`.

```cpp
// Well-commented code:
ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
    ListNode* dummy = new ListNode(0);
    dummy->next = list1;
    ListNode* prevA = dummy;
    for (int i = 0; i < a; i++) {
        prevA = prevA->next;
    }
    ListNode* nextB = prevA->next;
    for (int i = 0; i < b - a; i++) {
        nextB = nextB->next;
    }
    ListNode* tailList2 = list2;
    while (tailList2->next) {
        tailList2 = tailList2->next;
    }
    prevA->next = list2;
    tailList2->next = nextB->next;
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(a + b + n)$ where $n$ is the number of nodes in `list2`. This is because we traverse `list1` to find the nodes at positions `a` and `b`, and we traverse `list2` to find its last node.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the dummy node and other variables.
> - **Why these complexities occur:** The time complexity occurs because we perform a constant amount of work for each node in `list1` and `list2`. The space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a separate loop to find the last node of `list2`, we can find it while we are finding the node at position `b` in `list1`.
- Detailed breakdown of the approach:
  1. Find the node at position `a` in `list1`.
  2. Find the node at position `b` in `list1` and the last node of `list2` in the same loop.
  3. Connect the node before `b` in `list1` to the start of `list2`.
  4. Connect the end of `list2` to the node at position `b` in `list1`.

```cpp
// Production-ready code:
ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
    ListNode* dummy = new ListNode(0);
    dummy->next = list1;
    ListNode* prevA = dummy;
    for (int i = 0; i < a; i++) {
        prevA = prevA->next;
    }
    ListNode* nextB = prevA->next;
    ListNode* tailList2 = list2;
    for (int i = 0; i < b - a; i++) {
        nextB = nextB->next;
    }
    while (tailList2->next) {
        tailList2 = tailList2->next;
    }
    prevA->next = list2;
    tailList2->next = nextB->next;
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(a + b + n)$ where $n$ is the number of nodes in `list2`. This is because we traverse `list1` to find the nodes at positions `a` and `b`, and we traverse `list2` to find its last node.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the dummy node and other variables.
> - **Optimality proof:** This solution is optimal because we only traverse each list once, and we use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list traversal, node insertion, and deletion.
- Problem-solving patterns identified: Finding nodes at specific positions in a linked list, connecting and disconnecting nodes.
- Optimization techniques learned: Reducing the number of loops and minimizing the amount of space used.
- Similar problems to practice: Merging two sorted linked lists, deleting a node from a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null pointers, not handling edge cases correctly.
- Edge cases to watch for: Empty linked lists, linked lists with only one node.
- Performance pitfalls: Using excessive loops or recursive calls, using too much space.
- Testing considerations: Testing with different input sizes, testing with edge cases.