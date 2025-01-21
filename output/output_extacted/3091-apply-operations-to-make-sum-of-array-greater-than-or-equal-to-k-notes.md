## Apply Operations to Make Sum of Array Greater Than or Equal to K
**Problem Link:** https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/description

**Problem Statement:**
- Input: An array of integers `nums`, an integer `k`.
- Constraints: $1 \leq nums.length \leq 10^5$, $1 \leq nums[i] \leq 10^6$, $1 \leq k \leq 10^{15}$.
- Expected output: The minimum number of operations required to make the sum of the array greater than or equal to `k`.
- Key requirements: We can perform two types of operations:
  1. Multiply any element by 2.
  2. Add 1 to any element.
- Edge cases: Empty array, single-element array, array sum already greater than or equal to `k`.

**Example Test Cases:**
- `nums = [4, 5, 6], k = 20`: The minimum number of operations is 2 (multiply 4 by 2 and add 1 to 6).
- `nums = [1, 2, 3], k = 10`: The minimum number of operations is 3 (add 1 to each element).

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of operations and find the minimum number of operations that make the sum greater than or equal to `k`.
- We can use a recursive approach to generate all possible combinations of operations.

```cpp
int minOperations(vector<int>& nums, long long k) {
    int n = nums.size();
    int minOps = INT_MAX;

    function<void(int, int, long long)> dfs = [&](int idx, int ops, long long sum) {
        if (idx == n) {
            if (sum >= k && ops < minOps) {
                minOps = ops;
            }
            return;
        }

        // Multiply by 2
        dfs(idx + 1, ops + 1, sum + nums[idx] * 2);

        // Add 1
        dfs(idx + 1, ops + 1, sum + nums[idx] + 1);

        // No operation
        dfs(idx + 1, ops, sum + nums[idx]);
    };

    dfs(0, 0, 0);
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$, where $n$ is the number of elements in the array. This is because we have three possible operations for each element.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of operations, resulting in exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a greedy approach to minimize the number of operations. We should prioritize multiplying the smallest numbers by 2, as this will increase the sum more efficiently.
- We can use a priority queue to store the numbers and their corresponding operations.

```cpp
int minOperations(vector<int>& nums, long long k) {
    int n = nums.size();
    long long sum = 0;
    for (int num : nums) {
        sum += num;
    }

    if (sum >= k) {
        return 0;
    }

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int num : nums) {
        pq.push(num);
    }

    int ops = 0;
    while (sum < k) {
        int num = pq.top();
        pq.pop();
        sum += num;
        pq.push(num * 2);
        ops++;
    }

    return ops;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array. This is because we use a priority queue to store the numbers.
> - **Space Complexity:** $O(n)$, due to the priority queue.
> - **Optimality proof:** The greedy approach ensures that we minimize the number of operations by prioritizing the smallest numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, priority queue.
- Problem-solving patterns identified: Minimizing the number of operations by prioritizing the smallest numbers.
- Optimization techniques learned: Using a priority queue to store the numbers and their corresponding operations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the sum is already greater than or equal to `k`.
- Edge cases to watch for: Empty array, single-element array, array sum already greater than or equal to `k`.
- Performance pitfalls: Using a brute force approach, resulting in exponential time complexity.