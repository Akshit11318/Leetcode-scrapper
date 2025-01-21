## Insert Greatest Common Divisors in Linked List

**Problem Link:** https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description

**Problem Statement:**
- Input: A linked list `list1` and an integer `val`.
- Constraints: The number of nodes in `list1` is in the range `[1, 10^5]`. The values of the nodes in `list1` and `val` are in the range `[1, 10^6]`.
- Expected output: A linked list where every node's value is the greatest common divisor (GCD) of the corresponding node in `list1` and `val`.
- Key requirements and edge cases to consider:
  - Handling cases where `val` is 1 or a prime number.
  - Ensuring the GCD is calculated correctly for all nodes.
- Example test cases with explanations:
  - For `list1 = [2,4,6]` and `val = 4`, the output should be `[2,2,2]` because the GCDs are `gcd(2,4) = 2`, `gcd(4,4) = 4` but since `4` is the input `val` we take `2` as the GCD for the second node, and `gcd(6,4) = 2`.
  - For `list1 = [3,6,9]` and `val = 6`, the output should be `[3,6,3]` because the GCDs are `gcd(3,6) = 3`, `gcd(6,6) = 6`, and `gcd(9,6) = 3`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the linked list and calculating the GCD of each node's value and `val` using a simple GCD algorithm like Euclid's algorithm.
- This approach is straightforward but might be inefficient due to the repeated calculation of GCDs.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

ListNode* insertGCDList(ListNode* list1, int val) {
    if (!list1) return nullptr;
    
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    
    while (list1) {
        int nodeGCD = gcd(list1->val, val);
        current->next = new ListNode(nodeGCD);
        current = current->next;
        list1 = list1->next;
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of nodes in the linked list and $m$ is the average time complexity of calculating the GCD of two numbers, which can be considered as $O(\log \min(a, b))$ using Euclid's algorithm.
> - **Space Complexity:** $O(n)$, for creating a new linked list.
> - **Why these complexities occur:** The time complexity is due to the iteration over the linked list and the calculation of GCD for each node. The space complexity is due to the creation of a new linked list.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is recognizing that the GCD calculation can be optimized by using a more efficient GCD algorithm, but in this case, the algorithm itself is already optimal for calculating GCDs.
- However, we can slightly optimize the code by avoiding unnecessary object creations and directly calculating the GCD in the new node creation step.

```cpp
ListNode* insertGCDListOptimal(ListNode* list1, int val) {
    if (!list1) return nullptr;
    
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    
    while (list1) {
        int a = list1->val;
        int b = val;
        int nodeGCD = a;
        while (b) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        nodeGCD = a;
        
        current->next = new ListNode(nodeGCD);
        current = current->next;
        list1 = list1->next;
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log \min(a, b))$, where $n$ is the number of nodes in the linked list and $a$, $b$ are the values for which GCD is calculated.
> - **Space Complexity:** $O(n)$, for creating a new linked list.
> - **Optimality proof:** This is optimal because we must iterate over the list and calculate the GCD for each node, and the GCD calculation itself is done with the most efficient algorithm available, Euclid's algorithm.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: GCD calculation using Euclid's algorithm, linked list traversal.
- Problem-solving patterns identified: Optimizing algorithms by reducing unnecessary operations.
- Optimization techniques learned: Using efficient algorithms for sub-problems.
- Similar problems to practice: Other problems involving linked lists and mathematical operations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating GCD, not handling edge cases properly.
- Edge cases to watch for: Empty linked list, `val` being 1 or a prime number.
- Performance pitfalls: Using inefficient algorithms for GCD calculation.
- Testing considerations: Thoroughly testing with different linked list lengths and `val` values.