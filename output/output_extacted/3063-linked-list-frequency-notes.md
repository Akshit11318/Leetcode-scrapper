## Linked List Frequency

**Problem Link:** https://leetcode.com/problems/linked-list-frequency/description

**Problem Statement:**
- Input format and constraints: The problem involves a linked list with nodes containing integer values. The input is a linked list and an integer `k`.
- Expected output format: The output is a list of integers representing the values in the linked list that appear at least `k` times.
- Key requirements and edge cases to consider: The solution should handle cases where the input linked list is empty or contains duplicate values. It should also handle cases where `k` is greater than the total number of nodes in the linked list.
- Example test cases with explanations:
    - Example 1: Input: linked list = [1, 2, 2, 3, 3, 3], k = 2. Output: [2, 3]. Explanation: The values 2 and 3 appear at least 2 times in the linked list.
    - Example 2: Input: linked list = [1, 1, 1, 1, 1], k = 5. Output: [1]. Explanation: The value 1 appears at least 5 times in the linked list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves traversing the linked list and counting the frequency of each node value. Then, it checks which values appear at least `k` times and includes them in the output list.
- Step-by-step breakdown of the solution:
    1. Create a hash map to store the frequency of each node value.
    2. Traverse the linked list and update the frequency of each node value in the hash map.
    3. Traverse the hash map and include the node values that appear at least `k` times in the output list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. It involves a simple traversal of the linked list and a hash map to store the frequency of each node value.

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    vector<int> getFrequency(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        vector<int> result;
        for (auto& pair : freq) {
            if (pair.second >= k) {
                result.push_back(pair.first);
            }
        }
        return result;
    }

    vector<int> getFrequency(ListNode* head, int k) {
        unordered_map<int, int> freq;
        while (head) {
            freq[head->val]++;
            head = head->next;
        }
        vector<int> result;
        for (auto& pair : freq) {
            if (pair.second >= k) {
                result.push_back(pair.first);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of unique node values. The first pass through the linked list takes $O(n)$ time, and the second pass through the hash map takes $O(m)$ time.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique node values. The hash map stores the frequency of each node value.
> - **Why these complexities occur:** The time complexity occurs because we need to traverse the linked list once to count the frequency of each node value and then traverse the hash map to include the node values that appear at least `k` times in the output list. The space complexity occurs because we need to store the frequency of each node value in the hash map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach. We can optimize the solution by using a single pass through the linked list to count the frequency of each node value and then include the node values that appear at least `k` times in the output list.
- Detailed breakdown of the approach:
    1. Create a hash map to store the frequency of each node value.
    2. Traverse the linked list and update the frequency of each node value in the hash map.
    3. Traverse the hash map and include the node values that appear at least `k` times in the output list.
- Proof of optimality: The optimal solution has a time complexity of $O(n + m)$ and a space complexity of $O(m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of unique node values. This is the best possible time and space complexity for this problem.

```cpp
class Solution {
public:
    vector<int> getFrequency(ListNode* head, int k) {
        unordered_map<int, int> freq;
        while (head) {
            freq[head->val]++;
            head = head->next;
        }
        vector<int> result;
        for (auto& pair : freq) {
            if (pair.second >= k) {
                result.push_back(pair.first);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of unique node values. The first pass through the linked list takes $O(n)$ time, and the second pass through the hash map takes $O(m)$ time.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique node values. The hash map stores the frequency of each node value.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n + m)$ and a space complexity of $O(m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of unique node values. This is the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of hash maps to count the frequency of each node value in a linked list.
- Problem-solving patterns identified: The problem identifies the pattern of using a single pass through the linked list to count the frequency of each node value and then including the node values that appear at least `k` times in the output list.
- Optimization techniques learned: The problem learns the optimization technique of using a hash map to store the frequency of each node value.
- Similar problems to practice: Similar problems to practice include counting the frequency of each element in an array, finding the most frequent element in a linked list, and finding the first duplicate in a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Common implementation errors include not checking for edge cases, such as an empty linked list, and not handling duplicate node values.
- Edge cases to watch for: Edge cases to watch for include an empty linked list, a linked list with duplicate node values, and a linked list with a large number of nodes.
- Performance pitfalls: Performance pitfalls include using a slow algorithm to count the frequency of each node value and not using a hash map to store the frequency of each node value.
- Testing considerations: Testing considerations include testing the solution with different types of linked lists, such as an empty linked list, a linked list with duplicate node values, and a linked list with a large number of nodes.