## 132 Pattern

**Problem Link:** https://leetcode.com/problems/132-pattern/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^9`.
- Expected output: A boolean indicating whether the `132` pattern exists in the array.
- Key requirements: The `132` pattern means finding three numbers `i`, `j`, `k` in the array such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.
- Example test cases:
  - Input: `nums = [1,2,3,4]`, Output: `False`
  - Input: `nums = [3,1,4,2]`, Output: `True`
  - Input: `nums = [-1,3,2,0]`, Output: `True`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible combination of three numbers in the array to see if the `132` pattern exists.
- Step-by-step breakdown:
  1. Iterate over the array with three nested loops to consider all possible combinations of `i`, `j`, and `k`.
  2. For each combination, check if `i < j < k` and `nums[i] < nums[k] < nums[j]`.
  3. If such a combination is found, return `True`.
  4. If no such combination is found after checking all possibilities, return `False`.

```cpp
bool find132pattern(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (nums[i] < nums[k] && nums[k] < nums[j]) {
                    return true;
                }
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array `nums`, because we are using three nested loops to iterate over all possible combinations of `i`, `j`, and `k`.
> - **Space Complexity:** $O(1)$, because we are not using any additional data structures that scale with input size.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it checks all possible combinations without any optimization, leading to a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a stack to keep track of potential `j` values and their corresponding `nums[j]` values, and then iterate through the array to find a `k` that satisfies the condition for any `j` in the stack.
- Detailed breakdown:
  1. Initialize an empty stack `s` to store pairs of indices and values that could potentially be `j`.
  2. Initialize a variable `s3` to keep track of the maximum value seen so far that could be `nums[k]`.
  3. Iterate over the array from right to left.
  4. For each `nums[i]`, while the stack is not empty and the top of the stack's value is less than `nums[i]`, pop the stack and update `s3` if necessary.
  5. After popping, if the stack is not empty and `s3` is greater than the top of the stack's value, return `True` because we found a `132` pattern.
  6. Push the current index and value onto the stack.
  7. If the loop completes without finding a `132` pattern, return `False`.

```cpp
bool find132pattern(vector<int>& nums) {
    int n = nums.size();
    vector<int> s; // Stack to store potential j values
    int s3 = INT_MIN; // Maximum value seen so far for k
    for (int i = n - 1; i >= 0; i--) {
        if (nums[i] < s3) return true; // Found a 132 pattern
        while (!s.empty() && nums[i] > s.back()) {
            s3 = max(s3, s.back());
            s.pop_back();
        }
        s.push_back(nums[i]);
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array `nums`, because we are iterating over the array once and performing constant time operations for each element.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store every element in the stack.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array and uses a stack to efficiently keep track of potential `j` values, avoiding the need for nested loops or excessive comparisons.

---

### Final Notes

**Learning Points:**
- The importance of using data structures like stacks to optimize algorithmic solutions.
- How to approach pattern recognition problems in arrays by considering the constraints and requirements of the pattern.
- The value of iterating through arrays in reverse to simplify certain types of problems.

**Mistakes to Avoid:**
- Not considering the use of stacks or other data structures to simplify the solution.
- Failing to iterate in the correct direction (in this case, from right to left) to take advantage of the problem's constraints.
- Not optimizing the solution to reduce unnecessary comparisons or iterations.