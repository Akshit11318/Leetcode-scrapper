## Array Nesting
**Problem Link:** https://leetcode.com/problems/array-nesting/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `nums` as input, where each integer is in the range `[0, n-1]` and `n` is the length of the array.
- Expected output format: The function should return the length of the largest `array nesting`, where an `array nesting` is defined as a sequence of elements where the value at each index `i` leads to the next index.
- Key requirements and edge cases to consider: The input array `nums` will have a length `n` in the range `[1, 10^4]`. Each element in `nums` is in the range `[0, n-1]`.
- Example test cases with explanations:
  - For the input `[5,4,0,3,1,6,2]`, the output is `4` because the longest array nesting sequence is `[0,5,6,2]`.
  - For the input `[9,0,4,2,1]`, the output is `3` because the longest array nesting sequence is `[0,9,4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to understand the concept of an `array nesting`. It's a sequence where each element leads to the next index. The brute force approach involves exploring all possible sequences starting from each index and finding the longest one.
- Step-by-step breakdown of the solution:
  1. Iterate over each index `i` in the array.
  2. For each index `i`, start a new sequence and explore all possible sequences by following the index values.
  3. Keep track of the longest sequence found.
- Why this approach comes to mind first: It's the most straightforward way to ensure all possibilities are considered, but it's inefficient due to its exponential time complexity.

```cpp
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n = nums.size();
        int maxLen = 0;
        vector<bool> visited(n, false);
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int len = 0;
                int j = i;
                do {
                    len++;
                    visited[j] = true;
                    j = nums[j];
                } while (!visited[j]);
                maxLen = max(maxLen, len);
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, we might need to traverse the entire array for each starting index.
> - **Space Complexity:** $O(n)$ for the `visited` array.
> - **Why these complexities occur:** The brute force approach has high time complexity because it doesn't avoid revisiting the same sequences multiple times.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of exploring all sequences from each index, we can use a depth-first search (DFS) approach with memoization to avoid revisiting the same sequences.
- Detailed breakdown of the approach:
  1. Use a `visited` array to keep track of the indices that have been visited to avoid infinite loops.
  2. Perform a DFS from each unvisited index.
  3. During the DFS, keep track of the length of the current sequence.
  4. Update the maximum length found so far.
- Proof of optimality: This approach ensures that each index is visited at most once, leading to a significant reduction in time complexity.

```cpp
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n = nums.size();
        int maxLen = 0;
        vector<bool> visited(n, false);
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int len = dfs(nums, visited, i);
                maxLen = max(maxLen, len);
            }
        }
        return maxLen;
    }
    
    int dfs(vector<int>& nums, vector<bool>& visited, int i) {
        if (visited[i]) return 0;
        visited[i] = true;
        return 1 + dfs(nums, visited, nums[i]);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because each index is visited at most once.
> - **Space Complexity:** $O(n)$ for the recursion stack and the `visited` array.
> - **Optimality proof:** The DFS approach with memoization ensures that we explore each sequence exactly once, achieving the optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), memoization.
- Problem-solving patterns identified: Avoiding revisiting the same sequences, using visited arrays for tracking.
- Optimization techniques learned: Memoization to reduce time complexity.
- Similar problems to practice: Other graph traversal and sequence problems that can benefit from memoization.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to mark visited indices, not handling the base case correctly in the DFS.
- Edge cases to watch for: Handling arrays with a single element, arrays with all elements being the same.
- Performance pitfalls: Not using memoization, leading to exponential time complexity.
- Testing considerations: Testing with arrays of different lengths, testing with arrays containing cycles and sequences of different lengths.