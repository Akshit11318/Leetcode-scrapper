## Maximum Sum Queries
**Problem Link:** https://leetcode.com/problems/maximum-sum-queries/description

**Problem Statement:**
- Input: An array of integers `nums` and a list of queries where each query is an array `[left, right, index]`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= queries.length <= 10^5`, `0 <= left <= right < nums.length`, `0 <= index < queries.length`.
- Expected Output: Return the maximum sum of queries.
- Key Requirements: For each query, calculate the sum of elements in the range `[left, right]` and store it in the `index` position of the result array. The goal is to maximize the sum of the result array.
- Example Test Cases:
  - Input: `nums = [1, 2, 3, 4, 5]`, `queries = [[0, 3, 0], [2, 4, 1]]`
  - Output: `[16, 20]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each query and calculating the sum of elements in the specified range.
- This approach comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
vector<int> answerQueries(vector<int>& nums, vector<vector<int>>& queries) {
    vector<int> result(queries.size());
    for (int i = 0; i < queries.size(); i++) {
        int left = queries[i][0];
        int right = queries[i][1];
        int index = queries[i][2];
        int sum = 0;
        for (int j = left; j <= right; j++) {
            sum += nums[j];
        }
        result[index] = sum;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$ where $n$ is the number of queries, $m$ is the average length of the query range, and $k$ is the number of elements in `nums`. This complexity occurs because for each query, we are potentially iterating over the entire range specified by the query.
> - **Space Complexity:** $O(n)$ for storing the result array, where $n$ is the number of queries.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops over the queries and the elements within the query ranges.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix sum array to store the cumulative sum of elements in `nums`. This allows for efficient calculation of the sum of any range in constant time.
- Detailed breakdown: First, create a prefix sum array `prefixSum` where `prefixSum[i]` is the sum of elements from index `0` to `i-1` in `nums`. Then, for each query, calculate the sum of the range `[left, right]` by subtracting `prefixSum[left]` from `prefixSum[right+1]`.

```cpp
vector<int> answerQueries(vector<int>& nums, vector<vector<int>>& queries) {
    vector<int> prefixSum(nums.size() + 1, 0);
    for (int i = 0; i < nums.size(); i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    vector<int> result(queries.size());
    for (int i = 0; i < queries.size(); i++) {
        int left = queries[i][0];
        int right = queries[i][1];
        int index = queries[i][2];
        int sum = prefixSum[right + 1] - prefixSum[left];
        result[index] = sum;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the size of `nums` and $m$ is the number of queries. The prefix sum array is created in $O(n)$ time, and then each query is processed in constant time.
> - **Space Complexity:** $O(n + m)$ for the prefix sum array and the result array.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of calculating the sum for each query from linear to constant, leveraging the prefix sum technique to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: **Prefix Sum** technique for efficient range sum calculations.
- Problem-solving pattern: Using auxiliary data structures (like prefix sum arrays) to reduce computational complexity.
- Optimization technique: Avoiding redundant calculations by precomputing and storing intermediate results.

**Mistakes to Avoid:**
- Not considering the use of auxiliary data structures for optimization.
- Failing to recognize the applicability of the prefix sum technique for range sum queries.
- Overlooking the potential for reducing time complexity through precomputation.