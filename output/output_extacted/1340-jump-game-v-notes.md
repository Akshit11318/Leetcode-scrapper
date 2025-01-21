## Jump Game V
**Problem Link:** https://leetcode.com/problems/jump-game-v/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `arr` and an integer `d`, return the maximum value of the array that can be reached by starting at any index and jumping `d` steps at a time. The value at each index can be used as the maximum reachable value.
- Expected output format: The maximum value of the array that can be reached by jumping `d` steps at a time.
- Key requirements and edge cases to consider: The array can contain negative numbers, and the value of `d` can be larger than the length of the array. We need to consider all possible starting indices and jumps.
- Example test cases with explanations:
  - Example 1: `arr = [1, -1, -2, 4, -7, 3]`, `d = 2`, Output: `5`. Explanation: We can start at index 4 and jump to index 6, getting a value of 3, then jump to index 4 again, getting a value of -7. We can also start at index 0 and jump to index 2, getting a value of -2, then jump to index 4, getting a value of -7. The maximum value we can get is 5 by starting at index 1 and jumping to index 3.
  - Example 2: `arr = [1, 1, 1, 1, 1, 1]`, `d = 3`, Output: `4`. Explanation: We can start at any index and jump to any other index, getting a value of 1. The maximum value we can get is 4 by starting at index 0 and jumping to index 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can try all possible starting indices and jumps, and keep track of the maximum value we can reach.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible starting indices.
  2. For each starting index, try all possible jumps.
  3. For each jump, calculate the maximum value we can reach.
  4. Update the maximum value we can reach if necessary.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. However, it has a high time complexity because we need to try all possible starting indices and jumps.

```cpp
int maxSmarterJump(vector<int>& arr, int d) {
    int n = arr.size();
    int maxVal = INT_MIN;
    for (int i = 0; i < n; i++) {
        int val = arr[i];
        int jump = 0;
        while (jump <= d) {
            if (i + jump < n) {
                val = max(val, arr[i + jump]);
            }
            if (i - jump >= 0) {
                val = max(val, arr[i - jump]);
            }
            jump++;
        }
        maxVal = max(maxVal, val);
    }
    return maxVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot d)$, where $n$ is the length of the array and $d$ is the jump distance. This is because we iterate over all possible starting indices and jumps.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum value.
> - **Why these complexities occur:** The time complexity occurs because we try all possible starting indices and jumps. The space complexity occurs because we only use a constant amount of space to store the maximum value.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `priority_queue` to keep track of the maximum value we can reach at each index.
- Detailed breakdown of the approach:
  1. Create a `priority_queue` to store the maximum value we can reach at each index.
  2. Iterate over the array, and for each index, try all possible jumps.
  3. For each jump, calculate the maximum value we can reach and push it into the `priority_queue`.
  4. Update the maximum value we can reach if necessary.
- Proof of optimality: This approach is optimal because we only try each possible jump once, and we use a `priority_queue` to keep track of the maximum value we can reach at each index.

```cpp
int maxSmarterJump(vector<int>& arr, int d) {
    int n = arr.size();
    priority_queue<int> pq;
    int maxVal = INT_MIN;
    for (int i = 0; i < n; i++) {
        for (int j = max(0, i - d); j <= min(n - 1, i + d); j++) {
            pq.push(arr[j]);
        }
        maxVal = max(maxVal, pq.top());
        pq.pop();
    }
    return maxVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot d \cdot log(n))$, where $n$ is the length of the array and $d$ is the jump distance. This is because we iterate over all possible jumps and use a `priority_queue` to keep track of the maximum value.
> - **Space Complexity:** $O(n)$, because we use a `priority_queue` to store the maximum value we can reach at each index.
> - **Optimality proof:** This approach is optimal because we only try each possible jump once, and we use a `priority_queue` to keep track of the maximum value we can reach at each index.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `priority_queue` to keep track of the maximum value we can reach at each index.
- Problem-solving patterns identified: Trying all possible jumps and keeping track of the maximum value we can reach.
- Optimization techniques learned: Using a `priority_queue` to reduce the time complexity of the algorithm.
- Similar problems to practice: Jump Game, Jump Game II, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the array when trying jumps.
- Edge cases to watch for: When the jump distance is larger than the length of the array.
- Performance pitfalls: Not using a `priority_queue` to keep track of the maximum value we can reach at each index.
- Testing considerations: Testing the algorithm with different input arrays and jump distances.