## Add Two Numbers

**Problem Link:** [leetcode.com/problems/add-two-numbers/description](https://leetcode.com/problems/add-two-numbers/description)

**Problem Statement (in your own words):**

Given two non-empty linked lists representing two non-negative integers, where each node in the linked list represents a digit in the number, the task is to add these two numbers and return the result as a linked list. The digits are stored in reverse order, i.e., the least significant digit is at the head of the list.

---

### Brute Force Approach

**Explanation:**

The brute force approach involves traversing both linked lists, storing the digits in two separate vectors, and then adding these vectors element-wise while handling carryovers. This results in a new vector representing the sum, which is then converted back into a linked list.

```cpp
// Definition for singly-linked list.
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode(int x) : val(x), next(NULL) {}
// };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int> v1, v2;
        
        // Store digits from l1
        while (l1) {
            v1.push_back(l1->val);
            l1 = l1->next;
        }
        
        // Store digits from l2
        while (l2) {
            v2.push_back(l2->val);
            l2 = l2->next;
        }
        
        vector<int> sum;
        int carry = 0;
        
        // Find max length between v1 and v2
        int maxLen = max(v1.size(), v2.size());
        
        for (int i = 0; i < maxLen; ++i) {
            int d1 = (i < v1.size()) ? v1[i] : 0;
            int d2 = (i < v2.size()) ? v2[i] : 0;
            int total = d1 + d2 + carry;
            sum.push_back(total % 10);
            carry = total / 10;
        }
        
        if (carry > 0) {
            sum.push_back(carry);
        }
        
        // Create linked list
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        
        for (int d : sum) {
            curr->next = new ListNode(d);
            curr = curr->next;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> 
> **Time Complexity:** O(max(m, n)), where m and n are the lengths of the input linked lists. This is because we are traversing both lists once and then performing operations on the vectors, which in total does not exceed the sum of the lengths of the lists.
> 
> **Space Complexity:** O(max(m, n)), for storing the digits in the vectors and creating the new linked list.

---

### Optimal Approach

**Explanation:**

The optimal approach involves directly manipulating the linked lists as we add the numbers. We initialize a dummy node to simplify the code and keep track of the carryover. This approach avoids the need to store all digits in vectors, making it more memory-efficient.

```cpp
// Definition for singly-linked list.
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode(int x) : val(x), next(NULL) {}
// };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int carry = 0;
        
        while (l1 || l2 || carry) {
            int x = (l1) ? l1->val : 0;
            int y = (l2) ? l2->val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
            
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> 
> - **Time Complexity:** O(max(m, n)), where m and n are the lengths of the input linked lists. This is because we are only traversing the lists once.
> - **Space Complexity:** O(max(m, n)), for creating the new linked list.

---

### Alternative/Greedy Approach (if applicable)

**Explanation:**

There isn't a significantly different greedy or two-pointer approach that would change the complexity in this case, as the problem inherently requires traversing both lists once. The provided optimal approach already benefits from a straightforward, single-pass strategy.

---

### Final Notes

**Learning Points:**

1. **Linked List Manipulation:** This problem highlights the importance of understanding how to manipulate linked lists, including iteration, node creation, and connection.
2. **Carry Handling:** Properly handling carryovers in addition is crucial. This problem demonstrates how to manage carryovers in a digit-by-digit addition scenario.
3. **Optimization:** Starting with a brute force approach can help in understanding the problem, but optimizing it (as shown with the optimal approach) is key to improving efficiency.

**Mistakes to Avoid:**

1. **Not Considering Carryovers:** Failing to account for carryovers when adding digits can lead to incorrect results.
2. **Inefficient Memory Usage:** Initially storing all digits in vectors before creating the new linked list can be inefficient, especially for large inputs.
3. **Not Simplifying the Code with Dummy Nodes:** Using a dummy node can simplify the code by avoiding special cases for the head of the result list.