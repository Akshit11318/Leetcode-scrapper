## Maximum Twin Sum of a Linked List

**Problem Link:** https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description

**Problem Statement:**
- Input format and constraints: The problem takes a linked list as input, where each node contains an integer value. The linked list has `n` nodes, and we need to find the maximum twin sum.
- Expected output format: The function should return the maximum twin sum of the linked list.
- Key requirements and edge cases to consider: 
    - The linked list can have any number of nodes.
    - The values in the linked list can be any integer.
    - If the linked list has an odd number of nodes, the middle node is ignored.
- Example test cases with explanations:
    - Example 1: 
        - Input: `1 -> 2 -> 3 -> 4`
        - Output: `6` (2 + 4)
    - Example 2: 
        - Input: `1 -> 1000000 -> 1 -> 1000000`
        - Output: `2000000` (1000000 + 1000000)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to traverse the linked list, store the values in a vector, and then calculate the twin sum by adding corresponding elements from the start and end of the vector.
- Step-by-step breakdown of the solution:
    1. Traverse the linked list and store the values in a vector.
    2. Initialize a variable to store the maximum twin sum.
    3. Iterate through the vector from both ends towards the center, calculating the twin sum at each position.
    4. Update the maximum twin sum if the current twin sum is greater.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, making it a good starting point.

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
    int pairSum(ListNode* head) {
        vector<int> values;
        // Traverse the linked list and store the values in a vector
        while (head) {
            values.push_back(head->val);
            head = head->next;
        }
        
        int maxTwinSum = 0;
        int n = values.size();
        // Iterate through the vector from both ends towards the center
        for (int i = 0; i < n / 2; i++) {
            // Calculate the twin sum at each position
            int twinSum = values[i] + values[n - i - 1];
            // Update the maximum twin sum if the current twin sum is greater
            maxTwinSum = max(maxTwinSum, twinSum);
        }
        
        return maxTwinSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we traverse the linked list once to store the values in a vector, and then iterate through the vector once to calculate the twin sum.
> - **Space Complexity:** $O(n)$, as we need to store the values of the linked list in a vector.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node in the linked list. The space complexity is also linear because we need to store all the values of the linked list in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is similar to the brute force approach, but we can calculate the twin sum directly while traversing the linked list and storing the values in a vector.
- Detailed breakdown of the approach:
    1. Traverse the linked list and store the values in a vector.
    2. Initialize a variable to store the maximum twin sum.
    3. Iterate through the vector from both ends towards the center, calculating the twin sum at each position.
    4. Update the maximum twin sum if the current twin sum is greater.
- Proof of optimality: This approach is optimal because we only need to traverse the linked list once to store the values in a vector, and then iterate through the vector once to calculate the twin sum. This results in a time complexity of $O(n)$.

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
    int pairSum(ListNode* head) {
        vector<int> values;
        // Traverse the linked list and store the values in a vector
        while (head) {
            values.push_back(head->val);
            head = head->next;
        }
        
        int maxTwinSum = 0;
        int n = values.size();
        // Iterate through the vector from both ends towards the center
        for (int i = 0; i < n / 2; i++) {
            // Calculate the twin sum at each position
            int twinSum = values[i] + values[n - i - 1];
            // Update the maximum twin sum if the current twin sum is greater
            maxTwinSum = max(maxTwinSum, twinSum);
        }
        
        return maxTwinSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we traverse the linked list once to store the values in a vector, and then iterate through the vector once to calculate the twin sum.
> - **Space Complexity:** $O(n)$, as we need to store the values of the linked list in a vector.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each node in the linked list. The space complexity is also linear because we need to store all the values of the linked list in a vector.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of traversing a linked list and storing values in a vector, as well as iterating through a vector to calculate a twin sum.
- Problem-solving patterns identified: The problem requires identifying the maximum twin sum in a linked list, which involves calculating the sum of corresponding elements from the start and end of the vector.
- Optimization techniques learned: The problem demonstrates the importance of minimizing the number of iterations through the linked list and vector to achieve an optimal time complexity.
- Similar problems to practice: Other problems that involve traversing a linked list and calculating sums or products of corresponding elements.

**Mistakes to Avoid:**
- Common implementation errors: One common mistake is to forget to update the maximum twin sum when a greater twin sum is found.
- Edge cases to watch for: The problem requires handling the case where the linked list has an odd number of nodes, in which case the middle node is ignored.
- Performance pitfalls: The problem requires minimizing the number of iterations through the linked list and vector to achieve an optimal time complexity.
- Testing considerations: The problem requires testing with different inputs, including linked lists with an even and odd number of nodes, to ensure that the solution works correctly in all cases.