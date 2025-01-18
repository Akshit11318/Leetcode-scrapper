## Reorder List

**Problem Link:** [leetcode.com/problems/reorder-list/description](https://leetcode.com/problems/reorder-list/description)

**Problem Statement (in your own words):**

The problem requires reordering a singly linked list such that the nodes are rearranged in a specific way. Given a list with nodes 1 -> 2 -> 3 -> 4, the reordered list should be 1 -> 4 -> 2 -> 3. The input is a linked list, and the output should be the reordered linked list.

---

### Brute Force Approach

**Explanation:**

The brute force approach involves storing the nodes in a data structure like a vector, then rearranging them as required. 

1.  Traverse the linked list and store all nodes in a vector.
2.  Initialize two pointers, one at the beginning and one at the end of the vector.
3.  Create a new linked list by alternating between the nodes at the start and end of the vector, moving the pointers towards the center.

```cpp
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
    void reorderList(ListNode* head) {
        // Base case
        if (!head || !head->next || !head->next->next) {
            return;
        }

        // Store nodes in a vector
        vector<ListNode*> nodes;
        ListNode* curr = head;
        while (curr) {
            nodes.push_back(curr);
            curr = curr->next;
        }

        // Reorder the nodes
        int i = 0, j = nodes.size() - 1;
        while (i < j) {
            nodes[i]->next = nodes[j];
            i++;
            if (i == j) {
                break;
            }
            nodes[j]->next = nodes[i];
            j--;
        }

        // Set the next pointer of the last node to nullptr
        nodes[i]->next = nullptr;
    }
};
```

> Complexity Analysis:
> 
> **Time Complexity:** O(N), where N is the number of nodes in the linked list, because we are traversing the list once to store the nodes and then reordering them. The time complexity can be broken down into two parts: O(N) for storing the nodes and O(N) for reordering them.
> 
> **Space Complexity:** O(N), because we are storing all nodes in a vector.

---

### Optimal Approach

**Explanation:**

A more optimal approach involves finding the middle of the linked list, reversing the second half, and then merging the two halves.

1.  Find the middle of the linked list using the slow and fast pointer technique.
2.  Reverse the second half of the linked list.
3.  Merge the two halves by alternating between the nodes of the first and second halves.

```cpp
class Solution {
public:
    void reorderList(ListNode* head) {
        // Base case
        if (!head || !head->next || !head->next->next) {
            return;
        }

        // Find the middle of the linked list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse the second half
        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        while (curr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }

        // Update the next pointer of the middle node to nullptr
        slow->next = nullptr;

        // Merge the two halves
        ListNode* first = head;
        ListNode* second = prev;
        while (second) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};
```

> Complexity Analysis:
> 
> - **Time Complexity:** O(N), where N is the number of nodes in the linked list, because we are finding the middle, reversing the second half, and then merging the two halves.
> - **Space Complexity:** O(1), because we are not using any extra space.

---

### Alternative/Greedy Approach (if applicable)

There isn't a suitable alternative or greedy approach for this problem.

---

### Final Notes

**Learning Points:**

*   The problem requires reordering a linked list, which involves manipulating the next pointers of the nodes.
*   The optimal approach involves finding the middle of the linked list, reversing the second half, and then merging the two halves.
*   The time complexity of the optimal approach is O(N), and the space complexity is O(1).

**Mistakes to Avoid:**

*   Not handling the base case correctly, where the linked list has less than 3 nodes.
*   Not updating the next pointers correctly while reordering the nodes.
*   Using extra space unnecessarily, which can increase the space complexity of the solution.