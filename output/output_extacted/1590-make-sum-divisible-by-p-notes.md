## Make Sum Divisible by P
**Problem Link:** https://leetcode.com/problems/make-sum-divisible-by-p/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`, `1 <= k <= 1000`.
- Expected output format: The minimum number of operations required to make the sum of the array divisible by `k`.
- Key requirements and edge cases to consider: Handling cases where the sum is already divisible by `k`, and considering the impact of removing elements on the sum's divisibility.
- Example test cases with explanations: 
    - For `nums = [1,2,3]` and `k = 3`, the output should be `0` because the sum `6` is already divisible by `3`.
    - For `nums = [1,2,3]` and `k = 7`, the output should be `1` because removing `1` makes the sum `5`, which is not divisible by `7`, but removing `2` or `3` also doesn't make the sum divisible by `7`. However, this example highlights a consideration for the minimum removals needed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing elements from the array and check if the sum of the remaining elements is divisible by `k`.
- Step-by-step breakdown of the solution: 
    1. Generate all possible subsets of the given array.
    2. For each subset, calculate the sum of its elements.
    3. Check if the sum is divisible by `k`.
    4. Keep track of the minimum number of elements that need to be removed to achieve divisibility.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered, but it's inefficient for large inputs.

```cpp
#include <vector>
#include <numeric>

int minOperations(std::vector<int>& nums, int k) {
    int n = nums.size();
    int minOps = n; // Initialize with the maximum possible operations
    for (int mask = 0; mask < (1 << n); ++mask) {
        int sum = 0;
        int ops = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) == 0) { // If the bit is not set, include the number in the sum
                sum += nums[i];
            } else {
                ops++; // If the bit is set, it means we're removing this number, so increment ops
            }
        }
        if (sum % k == 0) { // If the sum is divisible by k
            minOps = std::min(minOps, ops); // Update the minimum operations
        }
    }
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in `nums`. The reason is we're generating all possible subsets (which is $2^n$) and for each subset, we're calculating the sum and checking divisibility, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, not considering the space needed for the input and output. We're only using a constant amount of space to store the mask, sum, and operations.
> - **Why these complexities occur:** The time complexity is high because we're exploring all possible subsets, and for each subset, we perform a linear operation. The space complexity is low because we're not using any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all subsets, we can use a more targeted approach by considering the remainder when the sum of the array is divided by `k`. We then aim to remove elements such that the sum's remainder becomes `0`.
- Detailed breakdown of the approach: 
    1. Calculate the total sum of the array modulo `k` to find the target remainder.
    2. Initialize a DP table to store the minimum number of operations required to achieve each possible remainder.
    3. Iterate through the array and update the DP table based on whether including or excluding the current number results in a smaller number of operations to reach a remainder of `0`.
- Proof of optimality: This dynamic programming approach ensures that we consider the optimal substructure of the problem (the minimum operations for each possible sum modulo `k`) and avoid the overlapping subproblems by storing and reusing the solutions to these subproblems.

```cpp
int minOperations(std::vector<int>& nums, int k) {
    int sum = 0;
    for (int num : nums) sum += num;
    sum %= k; // Calculate the remainder of the total sum when divided by k
    if (sum == 0) return 0; // If the sum is already divisible by k, no operations needed
    
    int n = nums.size();
    std::vector<int> dp(k, n + 1); // Initialize DP table with a value larger than any possible answer
    dp[0] = 0; // Base case: 0 operations to have a remainder of 0
    
    for (int i = 0; i < n; ++i) {
        std::vector<int> nextDp = dp; // Create a copy for the next iteration
        for (int j = 0; j < k; ++j) {
            int nextRemainder = (j + nums[i]) % k;
            nextDp[nextRemainder] = std::min(nextDp[nextRemainder], dp[j] + 1);
        }
        dp = nextDp; // Update DP table for the next iteration
    }
    
    return dp[sum] > n ? -1 : dp[sum]; // Return the minimum operations if achievable, otherwise -1
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in `nums` and $k$ is the divisor. This is because we iterate through the array and for each element, we update the DP table which has $k$ entries.
> - **Space Complexity:** $O(k)$, for storing the DP table.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to efficiently explore the solution space, avoiding redundant calculations and ensuring the minimum number of operations is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic Programming, Modulo Arithmetic.
- Problem-solving patterns identified: Using DP to solve problems with optimal substructure and overlapping subproblems.
- Optimization techniques learned: Avoiding redundant calculations by storing intermediate results, using modulo arithmetic to reduce the problem size.
- Similar problems to practice: Other problems involving divisibility, subset sums, and dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing the DP table, failing to update the DP table correctly, not considering the base case properly.
- Edge cases to watch for: When the sum is already divisible by `k`, when no operations can make the sum divisible by `k`.
- Performance pitfalls: Using brute force for large inputs, not optimizing the solution for the specific constraints of the problem.
- Testing considerations: Testing with various inputs, including edge cases, to ensure the solution works correctly and efficiently.