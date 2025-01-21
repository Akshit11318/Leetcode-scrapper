## Intersection of Two Linked Lists
**Problem Link:** https://leetcode.com/problems/intersection-of-two-linked-lists/description

**Problem Statement:**
- Input format: Two non-empty linked lists, `headA` and `headB`.
- Constraints: Each linked list node is defined as `struct ListNode { int val; ListNode *next; ListNode(int x) : val(x), next(NULL) {} };`.
- Expected output format: The node where the intersection occurs, or `NULL` if no intersection exists.
- Key requirements and edge cases to consider:
  - The lists may intersect at some node or may not intersect at all.
  - Lists can be of varying lengths.
- Example test cases with explanations:
  - Two lists with an intersection point.
  - Two lists without an intersection point.
  - Lists of different lengths.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse one list and for each node, traverse the other list to check for intersection.
- Step-by-step breakdown of the solution:
  1. Start at the head of the first list (`headA`).
  2. For each node in the first list, start at the head of the second list (`headB`).
  3. Compare the current nodes from both lists. If they match, it's an intersection point.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that checks every possibility.

```cpp
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return NULL;
        
        ListNode *ptrA = headA;
        while (ptrA) {
            ListNode *ptrB = headB;
            while (ptrB) {
                if (ptrA == ptrB) return ptrA; // Found intersection
                ptrB = ptrB->next;
            }
            ptrA = ptrA->next;
        }
        return NULL; // No intersection found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m*n)$, where $m$ and $n$ are the lengths of the two linked lists. This is because in the worst case, for each node in one list, we traverse the entire other list.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our pointers.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, while the constant space usage is due to only using a few pointers regardless of input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Calculate the total length of both lists and then offset the longer list by the difference in lengths. This way, both lists can be traversed simultaneously without needing to check every node against every other node.
- Detailed breakdown of the approach:
  1. Calculate the lengths of both linked lists.
  2. Determine the longer list and calculate the difference in lengths.
  3. Move the pointer of the longer list forward by the difference in lengths.
  4. Traverse both lists simultaneously with the pointers. When they meet, it's the intersection point, or if they reach the end, there is no intersection.
- Proof of optimality: This approach minimizes the number of node visits by ensuring that both lists are traversed in a single pass after the initial length calculation.

```cpp
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return NULL;
        
        int lenA = length(headA), lenB = length(headB);
        if (lenA > lenB) {
            headA = skipNodes(headA, lenA - lenB);
        } else {
            headB = skipNodes(headB, lenB - lenA);
        }
        
        while (headA && headB) {
            if (headA == headB) return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
    
    int length(ListNode *head) {
        int len = 0;
        while (head) {
            len++;
            head = head->next;
        }
        return len;
    }
    
    ListNode *skipNodes(ListNode *head, int k) {
        while (k--) {
            head = head->next;
        }
        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, where $m$ and $n$ are the lengths of the two linked lists. This is because we traverse each list once to calculate lengths and then once more to find the intersection.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our pointers and lengths.
> - **Optimality proof:** This is optimal because we only traverse each list a constant number of times, minimizing the number of operations required to find the intersection.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list traversal, length calculation, and simultaneous traversal with offset.
- Problem-solving patterns identified: Optimizing brute force solutions by reducing unnecessary comparisons.
- Optimization techniques learned: Calculating lengths and offsetting longer lists to reduce comparisons.
- Similar problems to practice: Other linked list problems involving traversal and intersection.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for `NULL` pointers before traversal, incorrect length calculations.
- Edge cases to watch for: Empty lists, lists of different lengths, and lists with no intersection.
- Performance pitfalls: Using nested loops for traversal, which leads to high time complexity.
- Testing considerations: Test with lists of varying lengths, with and without intersections, and edge cases like empty lists.