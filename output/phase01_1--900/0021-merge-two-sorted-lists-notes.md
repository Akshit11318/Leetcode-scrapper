## Merge Two Sorted Lists
**Problem Link:** https://leetcode.com/problems/merge-two-sorted-lists/description

**Problem Statement:**
- Input format and constraints: Given two sorted linked lists `l1` and `l2`, merge them into one sorted linked list and return the head of the merged list.
- Expected output format: A sorted linked list where each node contains a value from either `l1` or `l2`, in ascending order.
- Key requirements and edge cases to consider:
  - The input lists can be empty.
  - The lists are singly linked and sorted in ascending order.
- Example test cases with explanations:
  - If `l1 = [1, 2, 4]` and `l2 = [1, 3, 4]`, the output should be `[1, 1, 2, 3, 4, 4]`.
  - If one list is empty, the output should be the other list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To merge two sorted lists, we could simply concatenate them and then sort the resulting list.
- Step-by-step breakdown of the solution:
  1. Concatenate `l1` and `l2`.
  2. Sort the concatenated list.
- Why this approach comes to mind first: It's a straightforward way to ensure the output is sorted, but it doesn't take advantage of the input lists being sorted.

```cpp
// Brute Force Approach
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a new list to store the merged result
        ListNode* head = new ListNode(0);
        ListNode* current = head;
        
        // Concatenate l1 and l2 into a vector for sorting
        vector<int> values;
        while (l1) {
            values.push_back(l1->val);
            l1 = l1->next;
        }
        while (l2) {
            values.push_back(l2->val);
            l2 = l2->next;
        }
        
        // Sort the concatenated list
        sort(values.begin(), values.end());
        
        // Populate the new list with sorted values
        for (int val : values) {
            current->next = new ListNode(val);
            current = current->next;
        }
        
        return head->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O((m + n) \log(m + n))$ due to the sorting operation, where $m$ and $n$ are the lengths of `l1` and `l2`, respectively.
> - **Space Complexity:** $O(m + n)$ for storing the concatenated list in a vector.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing all values in a vector dominates the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since both input lists are already sorted, we can merge them in a single pass by comparing the current nodes of each list and adding the smaller value to the result list.
- Detailed breakdown of the approach:
  1. Create a new list to store the merged result.
  2. Compare the current nodes of `l1` and `l2`, and add the smaller value to the new list.
  3. Move to the next node in the list from which the value was taken.
  4. Repeat steps 2-3 until one list is exhausted.
  5. Append the remaining nodes from the non-exhausted list to the new list.
- Proof of optimality: This approach takes advantage of the sorted input lists, allowing for a single pass through both lists, resulting in linear time complexity.

```cpp
// Optimal Approach
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a dummy node to simplify code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge smaller elements first
        while (l1 && l2) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // If l1 or l2 is not exhausted, append the remaining nodes
        if (l1) {
            current->next = l1;
        } else if (l2) {
            current->next = l2;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, where $m$ and $n$ are the lengths of `l1` and `l2`, respectively, because we make a single pass through both lists.
> - **Space Complexity:** $O(m + n)$ for the new list, but this is necessary to store the merged result.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input lists once to merge them.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Merging sorted lists, iterative approach.
- Problem-solving patterns identified: Taking advantage of pre-existing order in input data.
- Optimization techniques learned: Avoiding unnecessary sorting operations.
- Similar problems to practice: Merging k sorted lists, sorting a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where one list is empty, not updating pointers correctly.
- Edge cases to watch for: Empty input lists, lists of different lengths.
- Performance pitfalls: Using a sorting algorithm when the input is already sorted.
- Testing considerations: Test with lists of varying lengths, including empty lists, and lists with duplicate values.