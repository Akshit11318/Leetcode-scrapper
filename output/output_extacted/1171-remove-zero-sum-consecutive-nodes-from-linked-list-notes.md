## Remove Zero Sum Consecutive Nodes from Linked List
**Problem Link:** https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description

**Problem Statement:**
- Input: The head of a linked list where each node contains an integer value.
- Constraints: The number of nodes in the list is in the range $[1, 10^5]$ and each node has a value in the range $[-10^5, 10^5]$.
- Expected Output: The head of the modified linked list after removing all nodes that form a zero sum.
- Key Requirements:
  - Identify sequences of nodes that sum up to zero.
  - Remove these sequences from the linked list.
- Edge Cases:
  - An empty list or a list with a single node.
  - A list where all nodes sum up to zero.
- Example Test Cases:
  - Example 1: Input: `[1, 2, -3]`, Output: `[3]`, Explanation: The sum of the nodes is 0, so we remove them and return the new head.
  - Example 2: Input: `[3, 2, -3, 4, 1]`, Output: `[4, 1]`, Explanation: The sum of the nodes from the 2nd node to the 4th node is 0, so we remove them and return the new head.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the linked list and check every possible sequence of nodes to see if their sum is zero.
- We can use a nested loop to generate all possible sequences and then calculate their sums.
- If a sequence's sum is zero, we remove it from the list.

```cpp
// Brute Force Solution
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        // Create a dummy node to simplify edge cases
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        bool changed;
        do {
            changed = false;
            ListNode* current = dummy;
            while (current->next) {
                long sum = 0;
                ListNode* temp = current->next;
                while (temp) {
                    sum += temp->val;
                    if (sum == 0) {
                        // Remove the sequence
                        current->next = temp->next;
                        changed = true;
                        break;
                    }
                    temp = temp->next;
                }
                if (!changed) {
                    current = current->next;
                }
            }
        } while (changed);
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of nodes in the linked list. This is because we are potentially checking every node against every other node.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, since we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity. The space complexity is constant because we do not allocate any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is to use a hash map (or unordered map in C++) to store the cumulative sum of the nodes as we traverse the list.
- For each node, we calculate the cumulative sum from the beginning of the list to the current node.
- If we encounter a cumulative sum that we have seen before, it means that the sum of the nodes between the previous occurrence of this cumulative sum and the current node is zero. Thus, we can remove this sequence.
- We use a dummy node to simplify the handling of edge cases, such as when the sequence to be removed starts from the head of the list.

```cpp
// Optimal Solution
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        int prefix = 0;
        unordered_map<int, ListNode*> seen;
        seen[0] = dummy;
        
        while (head) {
            prefix += head->val;
            if (seen.find(prefix) != seen.end()) {
                ListNode* node = seen[prefix];
                ListNode* tmp = node->next;
                int tmpPrefix = prefix + tmp->val;
                while (tmp != head) {
                    seen.erase(tmpPrefix);
                    tmp = tmp->next;
                    tmpPrefix += tmp->val;
                }
                node->next = head->next;
            } else {
                seen[prefix] = head;
            }
            head = head->next;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. We make a single pass through the list.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every node in the hash map.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the linked list and uses a hash map to efficiently keep track of cumulative sums, allowing for constant time lookups and insertions.

---

### Final Notes

**Learning Points:**
- The importance of cumulative sums in solving problems involving sequences and sums.
- The use of hash maps to efficiently store and retrieve cumulative sums.
- How to handle edge cases in linked list problems, such as using a dummy node.

**Mistakes to Avoid:**
- Not considering all possible sequences of nodes when checking for zero sums.
- Failing to handle edge cases properly, such as sequences starting from the head of the list.
- Not optimizing the solution by using a hash map to store cumulative sums.