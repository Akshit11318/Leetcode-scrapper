## Handling Sum Queries After Update
**Problem Link:** https://leetcode.com/problems/handling-sum-queries-after-update/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `nums` and a list of queries `queries`, where each query is a list of three integers `[val, idx, op]`. If `op` is `0`, update the value at `idx` in `nums` to `val`. If `op` is `1`, return the sum of `nums` from index `0` to `idx`.
- Expected output format: A list of integers, where each integer is the result of a query with `op` equal to `1`.
- Key requirements and edge cases to consider: Update the value at a given index, and calculate the sum of the list up to a given index.
- Example test cases with explanations: For example, given `nums = [1, 2, 3, 4, 5]` and `queries = [[1, 0, 0], [2, 0, 1], [3, 1, 0], [4, 1, 1]]`, the output should be `[2, 6]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the list of queries and perform the specified operation for each query.
- Step-by-step breakdown of the solution: 
  1. Iterate over the list of queries.
  2. For each query, check the operation type.
  3. If the operation type is `0`, update the value at the specified index in `nums`.
  4. If the operation type is `1`, calculate the sum of `nums` from index `0` to the specified index.
- Why this approach comes to mind first: It is a straightforward and intuitive way to solve the problem, as it directly follows the problem statement.

```cpp
#include <vector>

std::vector<int> handleQuery(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
    std::vector<int> results;
    for (const auto& query : queries) {
        int val = query[0];
        int idx = query[1];
        int op = query[2];
        if (op == 0) {
            nums[idx] = val;
        } else {
            int sum = 0;
            for (int i = 0; i <= idx; i++) {
                sum += nums[i];
            }
            results.push_back(sum);
        }
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \times n)$, where $q$ is the number of queries and $n$ is the number of elements in `nums`. This is because for each query, we potentially iterate over the entire list of `nums`.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output. This is because we only use a constant amount of space to store the current query and the sum.
> - **Why these complexities occur:** These complexities occur because we are using a naive approach that involves iterating over the list of `nums` for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to store the cumulative sum of `nums`, which allows us to calculate the sum of `nums` from index `0` to any index in constant time.
- Detailed breakdown of the approach: 
  1. Create a prefix sum array `prefix_sum` of the same length as `nums`, where `prefix_sum[i]` is the sum of `nums` from index `0` to `i`.
  2. Iterate over the list of queries.
  3. For each query, check the operation type.
  4. If the operation type is `0`, update the value at the specified index in `nums` and update the corresponding values in `prefix_sum`.
  5. If the operation type is `1`, calculate the sum of `nums` from index `0` to the specified index using the prefix sum array.
- Proof of optimality: This approach is optimal because it reduces the time complexity of calculating the sum of `nums` from index `0` to any index from $O(n)$ to $O(1)$.

```cpp
#include <vector>

std::vector<int> handleQuery(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
    int n = nums.size();
    std::vector<int> prefix_sum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefix_sum[i + 1] = prefix_sum[i] + nums[i];
    }
    std::vector<int> results;
    for (const auto& query : queries) {
        int val = query[0];
        int idx = query[1];
        int op = query[2];
        if (op == 0) {
            int diff = val - nums[idx];
            nums[idx] = val;
            for (int i = idx + 1; i <= n; i++) {
                prefix_sum[i] += diff;
            }
        } else {
            results.push_back(prefix_sum[idx + 1]);
        }
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q + n)$, where $q$ is the number of queries and $n$ is the number of elements in `nums`. This is because we only need to iterate over the list of `nums` once to create the prefix sum array, and then we can calculate the sum of `nums` from index `0` to any index in constant time.
> - **Space Complexity:** $O(n)$, excluding the space needed for the output. This is because we need to store the prefix sum array.
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity of calculating the sum of `nums` from index `0` to any index.