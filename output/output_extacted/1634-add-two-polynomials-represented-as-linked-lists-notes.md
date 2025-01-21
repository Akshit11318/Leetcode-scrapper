## Add Two Polynomials Represented as Linked Lists

**Problem Link:** https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/description

**Problem Statement:**
- Input format and constraints: The input consists of two linked lists representing polynomials. Each node in the linked list contains a `coefficient` and an `exponent`. The coefficients and exponents are integers. The input polynomials are represented in descending order of exponents.
- Expected output format: The output should be a linked list representing the sum of the two input polynomials, also in descending order of exponents.
- Key requirements and edge cases to consider: Handle cases where the input linked lists are empty, or where the exponents are the same but the coefficients are different.
- Example test cases with explanations: For example, if the input polynomials are $3x^2 + 2x$ and $2x^2 - 3x$, the output should be $5x^2 - x$.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through both linked lists simultaneously and adding the coefficients of terms with the same exponent.
- Step-by-step breakdown of the solution:
  1. Create a new linked list to store the result.
  2. Iterate through both input linked lists.
  3. For each term in the input linked lists, check if there is a term with the same exponent in the other linked list.
  4. If a term with the same exponent is found, add the coefficients and create a new term in the result linked list.
  5. If no term with the same exponent is found, simply add the term to the result linked list.
- Why this approach comes to mind first: This approach is straightforward and involves simple iteration and addition of terms.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int coefficient;
    int exponent;
    ListNode *next;
    ListNode(int x, int y) : coefficient(x), exponent(y), next(NULL) {}
};

ListNode* addPolynomials(ListNode* p1, ListNode* p2) {
    // Create a new linked list to store the result
    ListNode* dummy = new ListNode(0, 0);
    ListNode* current = dummy;
    
    // Iterate through both input linked lists
    while (p1 && p2) {
        if (p1->exponent > p2->exponent) {
            // Add the term with the higher exponent to the result
            current->next = new ListNode(p1->coefficient, p1->exponent);
            p1 = p1->next;
        } else if (p1->exponent < p2->exponent) {
            // Add the term with the higher exponent to the result
            current->next = new ListNode(p2->coefficient, p2->exponent);
            p2 = p2->next;
        } else {
            // Add the coefficients of terms with the same exponent
            int coefficient = p1->coefficient + p2->coefficient;
            if (coefficient != 0) {
                current->next = new ListNode(coefficient, p1->exponent);
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        current = current->next;
    }
    
    // Add any remaining terms
    while (p1) {
        current->next = new ListNode(p1->coefficient, p1->exponent);
        p1 = p1->next;
        current = current->next;
    }
    while (p2) {
        current->next = new ListNode(p2->coefficient, p2->exponent);
        p2 = p2->next;
        current = current->next;
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of the input linked lists.
> - **Space Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of the input linked lists.
> - **Why these complexities occur:** The time complexity is linear because we iterate through both linked lists once. The space complexity is linear because we create a new linked list to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a similar approach to the brute force solution, but with some minor optimizations.
- Detailed breakdown of the approach:
  1. Create a new linked list to store the result.
  2. Iterate through both input linked lists.
  3. For each term in the input linked lists, check if there is a term with the same exponent in the other linked list.
  4. If a term with the same exponent is found, add the coefficients and create a new term in the result linked list.
  5. If no term with the same exponent is found, simply add the term to the result linked list.
- Why further optimization is impossible: The optimal solution has a time complexity of $O(n + m)$, which is the minimum possible time complexity because we must iterate through both linked lists at least once.

```cpp
ListNode* addPolynomials(ListNode* p1, ListNode* p2) {
    // Create a new linked list to store the result
    ListNode* dummy = new ListNode(0, 0);
    ListNode* current = dummy;
    
    // Iterate through both input linked lists
    while (p1 && p2) {
        if (p1->exponent > p2->exponent) {
            // Add the term with the higher exponent to the result
            current->next = p1;
            p1 = p1->next;
        } else if (p1->exponent < p2->exponent) {
            // Add the term with the higher exponent to the result
            current->next = p2;
            p2 = p2->next;
        } else {
            // Add the coefficients of terms with the same exponent
            p1->coefficient += p2->coefficient;
            current->next = p1;
            p1 = p1->next;
            p2 = p2->next;
        }
        current = current->next;
    }
    
    // Add any remaining terms
    current->next = p1 ? p1 : p2;
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of the input linked lists.
> - **Space Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of the input linked lists.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n + m)$, which is the minimum possible time complexity because we must iterate through both linked lists at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked lists, iteration, and addition of terms.
- Problem-solving patterns identified: The problem can be solved by iterating through both linked lists and adding the coefficients of terms with the same exponent.
- Optimization techniques learned: The optimal solution involves using a similar approach to the brute force solution, but with some minor optimizations.
- Similar problems to practice: Other problems involving linked lists and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the input linked lists are empty.
- Edge cases to watch for: The case where the exponents are the same but the coefficients are different.
- Performance pitfalls: Not using the optimal solution, which has a time complexity of $O(n + m)$.
- Testing considerations: Test the solution with different input linked lists, including empty linked lists and linked lists with the same exponents but different coefficients.