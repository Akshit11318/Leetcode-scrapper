## Linked List Random Node

**Problem Link:** https://leetcode.com/problems/linked-list-random-node/description

**Problem Statement:**
- Input format and constraints: Given the head of a singly linked list, return a random node from the linked list.
- Expected output format: A random node from the linked list.
- Key requirements and edge cases to consider:
  - The linked list may be empty.
  - The linked list may have only one node.
  - The linked list may have multiple nodes.
- Example test cases with explanations:
  - Example 1: Given the head of a linked list with nodes [1, 2, 3], return a random node from the linked list. The probability of each node being returned should be 1/3.
  - Example 2: Given the head of a linked list with nodes [1, 2, 3, 4, 5], return a random node from the linked list. The probability of each node being returned should be 1/5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach to solve this problem is to store all the nodes in a vector and then select a random node from the vector.
- Step-by-step breakdown of the solution:
  1. Create a vector to store all the nodes in the linked list.
  2. Traverse the linked list and store each node in the vector.
  3. Select a random index from the vector.
  4. Return the node at the random index.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. However, it has a high space complexity because it requires storing all the nodes in a vector.

```cpp
class Solution {
public:
    vector<ListNode*> nodes;
    Solution(ListNode* head) {
        while (head) {
            nodes.push_back(head);
            head = head->next;
        }
    }
    
    ListNode* getRandom() {
        int index = rand() % nodes.size();
        return nodes[index];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `getRandom` function, $O(n)$ for the constructor, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
> - **Why these complexities occur:** The time complexity of the `getRandom` function is $O(1)$ because it simply selects a random index from the vector. The time complexity of the constructor is $O(n)$ because it traverses the linked list and stores each node in the vector. The space complexity is $O(n)$ because it stores all the nodes in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use the Reservoir Sampling algorithm, which is a family of randomized algorithms for randomly choosing k samples from a list of n items, where n is either a very large or unknown number.
- Detailed breakdown of the approach:
  1. Initialize the reservoir with the first node in the linked list.
  2. Traverse the linked list starting from the second node.
  3. For each node, generate a random number between 1 and the current index (inclusive).
  4. If the random number is 1, replace the reservoir with the current node.
- Proof of optimality: The Reservoir Sampling algorithm ensures that each node in the linked list has an equal probability of being selected, which is $1/n$.
- Why further optimization is impossible: The Reservoir Sampling algorithm has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is optimal for this problem.

```cpp
class Solution {
public:
    ListNode* head;
    Solution(ListNode* head) {
        this->head = head;
    }
    
    ListNode* getRandom() {
        ListNode* reservoir = head;
        int count = 1;
        ListNode* current = head->next;
        while (current) {
            count++;
            if (rand() % count == 0) {
                reservoir = current;
            }
            current = current->next;
        }
        return reservoir;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(1)$, excluding the space required for the linked list.
> - **Optimality proof:** The Reservoir Sampling algorithm ensures that each node in the linked list has an equal probability of being selected, which is $1/n$. The time complexity is $O(n)$ because it traverses the linked list once. The space complexity is $O(1)$ because it only uses a constant amount of space to store the reservoir and the current node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reservoir Sampling algorithm.
- Problem-solving patterns identified: Using a reservoir to store a random sample of nodes.
- Optimization techniques learned: Using a single pass through the linked list to select a random node.
- Similar problems to practice: Randomly selecting a node from a large dataset.

**Mistakes to Avoid:**
- Common implementation errors: Not using a reservoir to store a random sample of nodes.
- Edge cases to watch for: An empty linked list or a linked list with only one node.
- Performance pitfalls: Using a brute force approach that requires storing all the nodes in a vector.
- Testing considerations: Testing the solution with a large linked list and verifying that each node has an equal probability of being selected.