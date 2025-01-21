## Convert Doubly Linked List to Array I

**Problem Link:** https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/description

**Problem Statement:**
- Input format and constraints: The input is a doubly linked list where each node has an integer value and pointers to the next and previous nodes. The list may be empty.
- Expected output format: The output should be a vector of integers representing the node values in the order they appear in the list.
- Key requirements and edge cases to consider: Handle empty lists and ensure the output vector is in the correct order.
- Example test cases with explanations:
  - Example 1: Input: `1 <-> 2 <-> 3`, Output: `[1,2,3]`
  - Example 2: Input: `1 <-> 2 <-> 3 <-> 4 <-> 5`, Output: `[1,2,3,4,5]`
  - Example 3: Input: `1 <-> 2`, Output: `[1,2]`
  - Example 4: Input: `1`, Output: `[1]`
  - Example 5: Input: `null`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the doubly linked list and store the node values in a vector.
- Step-by-step breakdown of the solution:
  1. Initialize an empty vector to store node values.
  2. Start at the head of the list and traverse to the next node until the tail is reached.
  3. During traversal, append each node's value to the vector.
- Why this approach comes to mind first: It is the most straightforward way to convert a linked list to an array.

```cpp
/**
 * Definition for doubly-linked list.
 * struct DoublyLinkedListNode {
 *     int val;
 *     DoublyLinkedListNode *next;
 *     DoublyLinkedListNode *prev;
 *     DoublyLinkedListNode(int x) : val(x), next(NULL), prev(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> vec;
    vector<int> convertDoublyLinkedListToArray(DoublyLinkedListNode* head) {
        // Traverse the list and store node values in the vector
        while (head) {
            vec.push_back(head->val);
            head = head->next;
        }
        return vec;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because we visit each node once.
> - **Space Complexity:** $O(n)$, as in the worst case, the vector will store all node values.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear because we store all node values in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because it visits each node exactly once, which is necessary to collect all node values.
- Detailed breakdown of the approach: The approach remains the same as the brute force: traverse the list and store node values in a vector.
- Proof of optimality: Since we must visit each node at least once to collect its value, the time complexity cannot be improved beyond $O(n)$.
- Why further optimization is impossible: Any algorithm must at least read the input, which for a linked list of $n$ nodes requires $O(n)$ time.

```cpp
class Solution {
public:
    vector<int> convertDoublyLinkedListToArray(DoublyLinkedListNode* head) {
        vector<int> result;
        while (head) {
            result.push_back(head->val);
            head = head->next;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(n)$, as we store all node values in the vector.
> - **Optimality proof:** The algorithm is optimal because it achieves the minimum necessary time complexity to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list traversal and vector manipulation.
- Problem-solving patterns identified: The need to visit each element in a data structure to collect its information.
- Optimization techniques learned: Recognizing when an algorithm is already optimal based on the problem's constraints.
- Similar problems to practice: Other linked list and array conversion problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the pointer during traversal or not handling the case where the list is empty.
- Edge cases to watch for: Empty lists and lists with a single node.
- Performance pitfalls: Using inefficient data structures or algorithms for the problem at hand.
- Testing considerations: Ensure to test with various list lengths and configurations, including edge cases.