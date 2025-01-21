## Sort List

**Problem Link:** [https://leetcode.com/problems/sort-list/description](https://leetcode.com/problems/sort-list/description)

**Problem Statement:**
- Input: The head of a linked list.
- Constraints: The number of nodes in the list is in the range $[0, 5 \times 10^4]$.
- Expected Output: The head of the sorted linked list.
- Key Requirements: Sort the linked list in ascending order using any sorting algorithm.
- Edge Cases: Handle cases where the list is empty or contains only one node.

**Example Test Cases:**
- Example 1: Input: `head = [4,2,1,3]`, Output: `[1,2,3,4]`.
- Example 2: Input: `head = []`, Output: `[]`.
- Example 3: Input: `head = [1]`, Output: `[1]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves converting the linked list to a vector or array, sorting the array, and then reconstructing the linked list from the sorted array.
- This approach is straightforward but may not be the most efficient due to the overhead of converting between data structures.

```cpp
// Brute Force Implementation
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // Base case
        if (!head || !head->next) return head;

        // Convert linked list to vector
        vector<int> values;
        ListNode* current = head;
        while (current) {
            values.push_back(current->val);
            current = current->next;
        }

        // Sort the vector
        sort(values.begin(), values.end());

        // Reconstruct the linked list from the sorted vector
        ListNode* sortedHead = new ListNode(values[0]);
        ListNode* currentSorted = sortedHead;
        for (int i = 1; i < values.size(); i++) {
            currentSorted->next = new ListNode(values[i]);
            currentSorted = currentSorted->next;
        }

        return sortedHead;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation on the vector, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(n)$ for storing the vector of node values.
> - **Why these complexities occur:** The brute force approach involves sorting a vector of $n$ elements, which has a time complexity of $O(n \log n)$ for comparison-based sorting algorithms like `std::sort`. The space complexity is $O(n)$ because we need to store all node values in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a divide-and-conquer strategy, specifically merge sort, which is well-suited for linked lists.
- Merge sort divides the list into two halves, recursively sorts them, and then merges the sorted halves.

```cpp
// Optimal Implementation using Merge Sort
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // Base case
        if (!head || !head->next) return head;

        // Find the middle of the list
        ListNode* mid = getMiddle(head);
        ListNode* midNext = mid->next;

        // Split the list into two halves
        mid->next = nullptr;

        // Recursively sort the two halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // Merge the sorted halves
        return merge(left, right);
    }

    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        while (left && right) {
            if (left->val < right->val) {
                current->next = left;
                left = left->next;
            } else {
                current->next = right;
                right = right->next;
            }
            current = current->next;
        }
        current->next = left ? left : right;
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of nodes in the linked list. This is because merge sort divides the list in half at each level of recursion, resulting in $\log n$ levels, and at each level, it performs $n$ operations to merge the lists.
> - **Space Complexity:** $O(\log n)$ for the recursive call stack.
> - **Optimality proof:** Merge sort is an optimal comparison-based sorting algorithm for linked lists because it minimizes the number of comparisons required to sort the list, achieving a time complexity of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- **Divide-and-Conquer Strategy:** Understanding how to apply divide-and-conquer strategies like merge sort to solve complex problems.
- **Optimization Techniques:** Recognizing the importance of choosing the right data structures and algorithms to minimize time and space complexities.
- **Problem-Solving Patterns:** Identifying patterns in problems that can be solved using specific algorithms or techniques.

**Mistakes to Avoid:**
- **Inefficient Data Structures:** Using data structures that are not optimized for the problem, leading to unnecessary complexity.
- **Incorrect Algorithm Choice:** Choosing an algorithm that does not fit the problem's constraints or requirements.
- **Lack of Input Validation:** Failing to validate inputs, which can lead to incorrect results or crashes.