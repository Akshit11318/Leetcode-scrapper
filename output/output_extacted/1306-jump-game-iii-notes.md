## Jump Game III

**Problem Link:** https://leetcode.com/problems/jump-game-iii/description

**Problem Statement:**
- Input format: An array `arr` of integers and an integer `start`.
- Constraints: `1 <= arr.length <= 5 * 10^4`, `0 <= arr[i] <= 4 * 10^6`, and `0 <= start < arr.length`.
- Expected output format: `true` if we can reach the end of the array, `false` otherwise.
- Key requirements: Determine if we can reach the end of the array from the `start` index, given that we can jump to any index `i + arr[i]` or `i - arr[i]`.
- Example test cases:
  - `arr = [4,2,3,0,3,1,2]`, `start = 5`, Expected output: `true`
  - `arr = [4,2,3,0,3,1,2]`, `start = 0`, Expected output: `true`
  - `arr = [3,2,1,0,4]`, `start = 2`, Expected output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible jumps from the `start` index and recursively check if we can reach the end of the array.
- Step-by-step breakdown:
  1. Start at the `start` index.
  2. For each index `i`, try to jump to `i + arr[i]` and `i - arr[i]`.
  3. Recursively check if we can reach the end of the array from the new index.
  4. If we can reach the end, return `true`.
  5. If we've tried all possible jumps and can't reach the end, return `false`.

```cpp
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        if (start < 0 || start >= arr.size() || arr[start] < 0) return false;
        if (arr[start] == 0) return true;
        int jump = arr[start];
        arr[start] = -1; // mark as visited
        return canReach(arr, start + jump) || canReach(arr, start - jump);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of indices in the array, because in the worst case, we try all possible jumps.
> - **Space Complexity:** $O(n)$, because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible jumps, resulting in exponential time complexity, and uses recursive calls, resulting in linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a `visited` set to keep track of indices we've already visited to avoid infinite loops.
- Detailed breakdown:
  1. Create a `visited` set to store indices we've already visited.
  2. Start at the `start` index.
  3. For each index `i`, try to jump to `i + arr[i]` and `i - arr[i]`.
  4. If we've already visited the new index, skip it.
  5. If we can reach the end of the array from the new index, return `true`.
  6. If we've tried all possible jumps and can't reach the end, return `false`.

```cpp
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        unordered_set<int> visited;
        return dfs(arr, start, visited);
    }
    
    bool dfs(vector<int>& arr, int i, unordered_set<int>& visited) {
        if (i < 0 || i >= arr.size() || visited.count(i)) return false;
        if (arr[i] == 0) return true;
        visited.insert(i);
        return dfs(arr, i + arr[i], visited) || dfs(arr, i - arr[i], visited);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of indices in the array, because we visit each index at most once.
> - **Space Complexity:** $O(n)$, because of the recursive call stack and the `visited` set.
> - **Optimality proof:** This approach is optimal because we visit each index at most once, avoiding infinite loops and reducing the time complexity to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: depth-first search (DFS), recursive functions, and using a `visited` set to avoid infinite loops.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems and using recursion to solve them.
- Optimization techniques learned: using a `visited` set to avoid infinite loops and reducing the time complexity to linear.

**Mistakes to Avoid:**
- Common implementation errors: not checking for out-of-bounds indices, not handling the base case correctly, and not using a `visited` set to avoid infinite loops.
- Edge cases to watch for: indices that are out of bounds, indices that have already been visited, and the base case where `arr[i] == 0`.
- Performance pitfalls: using a brute force approach that tries all possible jumps, resulting in exponential time complexity.
- Testing considerations: testing the function with different inputs, including edge cases, to ensure it works correctly.