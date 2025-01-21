## Merge K Sorted Lists
**Problem Link:** [https://leetcode.com/problems/merge-k-sorted-lists/description](https://leetcode.com/problems/merge-k-sorted-lists/description)

**Problem Statement:**
- Input format and constraints: The problem takes a list of `k` sorted linked lists as input, where each linked list can be of varying lengths. The goal is to merge these lists into a single sorted linked list.
- Expected output format: The output should be a sorted linked list containing all elements from the input lists.
- Key requirements and edge cases to consider: Handle cases where some or all input lists are empty, and ensure the solution can scale for large inputs.
- Example test cases with explanations: For example, merging `[[1,4,5],[1,3,4],[2,6]]` should result in `[1,1,2,3,4,4,5,6]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to concatenate all lists and then sort the combined list.
- Step-by-step breakdown of the solution:
  1. Concatenate all linked lists into one.
  2. Sort the combined list.
- Why this approach comes to mind first: It's the simplest way to ensure all elements are sorted together, but it doesn't leverage the fact that input lists are already sorted.

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> values;
        for (auto list : lists) {
            while (list) {
                values.push_back(list->val);
                list = list->next;
            }
        }
        sort(values.begin(), values.end());
        if (values.empty()) return nullptr;
        
        ListNode* head = new ListNode(values[0]);
        ListNode* current = head;
        for (int i = 1; i < values.size(); ++i) {
            current->next = new ListNode(values[i]);
            current = current->next;
        }
        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$, where $N$ is the total number of elements across all lists, due to the sorting step.
> - **Space Complexity:** $O(N)$, as we store all elements in a vector.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing all elements in a vector for sorting contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a priority queue (min-heap) to keep track of the smallest unmerged element from each list. This approach takes advantage of the fact that input lists are already sorted.
- Detailed breakdown of the approach:
  1. Initialize a min-heap with the first element from each list, along with the list it comes from and its position in the list.
  2. Extract the smallest element from the heap, add it to the result list, and insert the next element from the same list into the heap if it exists.
  3. Repeat step 2 until the heap is empty.
- Proof of optimality: This solution has a time complexity of $O(N \log k)$, where $N$ is the total number of elements and $k$ is the number of lists, because each insertion and extraction from the heap takes $O(\log k)$ time, and we do this $N$ times.

```cpp
class Solution {
public:
    struct Node {
        int val;
        ListNode* node;
        Node(int v, ListNode* n) : val(v), node(n) {}
        bool operator<(const Node& other) const {
            return val > other.val; // For min-heap, smaller value has higher priority
        }
    };
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<Node> pq;
        for (auto list : lists) {
            if (list) pq.push(Node(list->val, list));
        }
        
        ListNode* head = new ListNode(0);
        ListNode* current = head;
        
        while (!pq.empty()) {
            Node top = pq.top();
            pq.pop();
            current->next = new ListNode(top.val);
            current = current->next;
            if (top.node->next) {
                pq.push(Node(top.node->next->val, top.node->next));
            }
        }
        
        return head->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log k)$, where $N$ is the total number of elements and $k$ is the number of lists, due to the heap operations.
> - **Space Complexity:** $O(k)$, as the heap stores one element from each list at most.
> - **Optimality proof:** This is optimal because we minimize the number of comparisons needed to merge the lists by always choosing the smallest element next, leveraging the existing order in the input lists.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Utilizing a priority queue (min-heap) to efficiently merge sorted lists.
- Problem-solving patterns identified: Leverage existing order in data to reduce computational complexity.
- Optimization techniques learned: Use of data structures like heaps to minimize comparison operations.
- Similar problems to practice: Other problems involving merging or sorting, such as merging two sorted arrays or sorting a nearly sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like empty input lists.
- Edge cases to watch for: Lists of varying lengths, including empty lists.
- Performance pitfalls: Not leveraging the existing sorted order of input lists, leading to unnecessary comparisons.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases like empty lists, lists of different lengths, and lists with duplicate values.