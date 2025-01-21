## Find the Duplicate Number
**Problem Link:** https://leetcode.com/problems/find-the-duplicate-number/description

**Problem Statement:**
- Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
- There is only one duplicate number in `nums`, return this duplicate number.
- You must solve the problem without modifying the array `nums` and uses only constant extra space.
- Example test cases: `nums = [1,3,4,2,2]`, output: `2`; `nums = [3,1,3,4,2]`, output: `3`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to use a hash set to store unique numbers encountered and check for duplicates.
- Step-by-step breakdown:
  1. Initialize an empty hash set `unique_nums`.
  2. Iterate through the array `nums`.
  3. For each number, check if it exists in `unique_nums`.
  4. If it does, return the number as it's the duplicate.
  5. If not, add the number to `unique_nums`.
- This approach comes to mind first because it's straightforward and leverages a common data structure for tracking uniqueness.

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> unique_nums;
        for (int num : nums) {
            if (unique_nums.find(num) != unique_nums.end()) {
                return num; // Duplicate found
            }
            unique_nums.insert(num);
        }
        return -1; // Should not reach here for valid input
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because we potentially iterate through the entire array once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every element in the hash set.
> - **Why these complexities occur:** The brute force approach requires iterating through the array and storing elements in a set, leading to linear time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is recognizing that this problem can be treated as a cycle detection problem in a linked list, where each number in the array is considered a node, and its value points to the next node.
- Detailed breakdown:
  1. Recognize that the array can be seen as a linked list where the value at each index `i` points to index `nums[i]`.
  2. Use Floyd's Tortoise and Hare (Cycle Detection) algorithm to find the start of the cycle, which corresponds to the duplicate number.
  3. Initialize two pointers, `tortoise` and `hare`, both starting at `nums[0]`.
  4. In each step, move `tortoise` one step at a time and `hare` two steps at a time.
  5. When `tortoise` and `hare` meet, reset `tortoise` to `nums[0]` and move both one step at a time to find the start of the cycle.
- Proof of optimality: This approach is optimal because it only uses constant extra space and has a time complexity of $O(n)$, which is the best we can achieve given the need to examine every element at least once.

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // Phase 1: Detecting the cycle using Floyd's Tortoise and Hare algorithm
        int tortoise = nums[0];
        int hare = nums[0];
        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);

        // Phase 2: Finding the start of the cycle
        tortoise = nums[0];
        while (tortoise != hare) {
            tortoise = nums[tortoise];
            hare = nums[hare];
        }

        return hare; // Start of the cycle, which is the duplicate number
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because in the worst case, we might need to traverse the entire array to detect and then find the start of the cycle.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our pointers.
> - **Optimality proof:** This is the best possible time complexity for this problem since we must examine every element at least once. The space complexity is optimal as well, given the constraint of using only constant extra space.

---

### Final Notes

**Learning Points:**
- The problem can be solved by recognizing the array as a linked list and applying cycle detection algorithms.
- Floyd's Tortoise and Hare algorithm is efficient for detecting cycles in linked lists and can be adapted for array problems with similar structures.
- Optimization techniques include reducing space complexity by using constant space algorithms and leveraging problem-specific insights.

**Mistakes to Avoid:**
- Modifying the input array, which is against the problem's constraints.
- Using more space than necessary, which can lead to inefficient solutions.
- Not considering the cyclic nature of the problem, which is key to the optimal solution.