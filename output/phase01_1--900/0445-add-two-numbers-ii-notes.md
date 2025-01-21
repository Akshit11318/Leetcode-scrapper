## Add Two Numbers II

**Problem Link:** https://leetcode.com/problems/add-two-numbers-ii/description

**Problem Statement:**
- Input: Two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
- Constraints: The number of nodes in each linked list is in the range $[1, 100]$, $0 \leq Node.val \leq 9$, and the lists do not contain any leading zero, except the number 0 itself.
- Expected Output: The sum of the two integers represented by the linked lists, also in the form of a linked list where each node contains a single digit.
- Key Requirements: Handle carry-overs from the addition of digits.
- Edge Cases: Empty lists, lists of different lengths, lists with leading zeros (which should not be present according to the problem statement).

### Brute Force Approach

**Explanation:**
- The initial thought process involves converting the linked lists into a format that can be easily added, such as integers or strings, performing the addition, and then converting the result back into a linked list.
- Step-by-step breakdown:
  1. Traverse both linked lists and store their values in vectors or arrays.
  2. Reverse the vectors or arrays since the linked lists store digits in reverse order.
  3. Convert the vectors or arrays into integers.
  4. Add the two integers.
  5. Convert the sum back into a vector or array.
  6. Create a new linked list from the vector or array.

```cpp
// Brute Force Approach
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    // Convert linked lists to vectors
    vector<int> v1, v2;
    while (l1) {
        v1.push_back(l1->val);
        l1 = l1->next;
    }
    while (l2) {
        v2.push_back(l2->val);
        l2 = l2->next;
    }
    
    // Reverse vectors to get correct order
    reverse(v1.begin(), v1.end());
    reverse(v2.begin(), v2.end());
    
    // Convert vectors to integers
    int num1 = 0, num2 = 0;
    for (int i = 0; i < v1.size(); i++) {
        num1 += v1[i] * pow(10, i);
    }
    for (int i = 0; i < v2.size(); i++) {
        num2 += v2[i] * pow(10, i);
    }
    
    // Add the integers
    int sum = num1 + num2;
    
    // Convert sum back to vector
    vector<int> sumVec;
    while (sum) {
        sumVec.push_back(sum % 10);
        sum /= 10;
    }
    
    // Create new linked list from vector
    ListNode* dummy = new ListNode(0);
    ListNode* curr = dummy;
    for (int val : sumVec) {
        curr->next = new ListNode(val);
        curr = curr->next;
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(m, n))$ where $m$ and $n$ are the lengths of the linked lists, because we traverse each list once and then perform operations that scale with the maximum length.
> - **Space Complexity:** $O(max(m, n))$ for storing the vectors and the new linked list.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node in the input lists. The space complexity is also linear because in the worst case, we might need to store all nodes from both lists in our vectors and then create a new linked list of similar size.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves directly manipulating the digits in the linked lists without converting them into integers or strings, thus avoiding potential overflow issues and improving efficiency.
- Detailed breakdown:
  1. Reverse the linked lists to align with the conventional way of adding numbers from right to left.
  2. Iterate through the reversed lists, adding corresponding digits along with any carry from the previous addition.
  3. Create a new node for each sum and handle any carry-over.
  4. After iterating through both lists, if there's a remaining carry, add it as a new node.

```cpp
// Optimal Approach
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    // Reverse linked lists
    ListNode* revL1 = reverseList(l1);
    ListNode* revL2 = reverseList(l2);
    
    // Dummy node for new list
    ListNode* dummy = new ListNode(0);
    ListNode* curr = dummy;
    int carry = 0;
    
    // Iterate through reversed lists
    while (revL1 || revL2 || carry) {
        int sum = carry;
        if (revL1) {
            sum += revL1->val;
            revL1 = revL1->next;
        }
        if (revL2) {
            sum += revL2->val;
            revL2 = revL2->next;
        }
        
        // Create new node and update carry
        curr->next = new ListNode(sum % 10);
        curr = curr->next;
        carry = sum / 10;
    }
    
    // Reverse new list to original order
    return reverseList(dummy->next);
}

ListNode* reverseList(ListNode* head) {
    ListNode* prev = NULL;
    ListNode* curr = head;
    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(m, n))$ where $m$ and $n$ are the lengths of the linked lists, because we reverse each list and then iterate through them once.
> - **Space Complexity:** $O(max(m, n))$ for the new linked list.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input lists after reversing them, and it avoids the potential for integer overflow by dealing with digits individually.

### Final Notes

**Learning Points:**
- Linked list manipulation, including reversal.
- Handling carry-overs in addition.
- Avoiding potential overflows by dealing with numbers in parts.

**Mistakes to Avoid:**
- Not handling carry-overs correctly.
- Not checking for edge cases like empty lists or lists of different lengths.
- Potential integer overflow when converting linked lists to integers.