## Find the Sum of Subsequence Powers
**Problem Link:** https://leetcode.com/problems/find-the-sum-of-subsequence-powers/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`, `0 <= k <= 30`.
- Expected output format: The sum of all subsequence powers of `nums` modulo `10^9 + 7`.
- Key requirements: Calculate the sum of all subsequences of `nums` where each element in the subsequence is raised to a power from `1` to `k`.
- Example test cases:
  - Input: `nums = [1,2,3], k = 2`
  - Output: `6`
  - Explanation: The possible subsequences are `[1,2]`, `[1,3]`, `[2,3]`, `[1]`, `[2]`, `[3]`, `[]`. The sum of powers for each subsequence is `1^1 + 2^1 + 1^2 + 2^2`, `1^1 + 3^1 + 1^2 + 3^2`, `2^1 + 3^1 + 2^2 + 3^2`, `1^1 + 1^2`, `2^1 + 2^2`, `3^1 + 3^2`, `0`. The sum of these sums is `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of `nums`, calculate the sum of powers for each subsequence, and sum up these sums.
- Step-by-step breakdown:
  1. Generate all possible subsequences of `nums`.
  2. For each subsequence, calculate the sum of powers from `1` to `k`.
  3. Sum up the sums of powers for all subsequences.

```cpp
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int sumSubseqWidths(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> powers(k + 1);
    powers[0] = 1;
    for (int i = 1; i <= k; i++) {
        powers[i] = powers[i - 1] * 2 % MOD;
    }

    int res = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) {
                for (int j = 1; j <= k; j++) {
                    sum = (sum + (int)(pow(nums[i], j) % MOD)) % MOD;
                }
            }
        }
        res = (res + sum) % MOD;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot k)$, where $n$ is the length of `nums` and $k$ is the input integer.
> - **Space Complexity:** $O(n + k)$, for storing the powers of 2 and the current subsequence.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences of `nums`, which has a time complexity of $O(2^n)$. For each subsequence, it calculates the sum of powers from `1` to `k`, which has a time complexity of $O(n \cdot k)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of calculating the sum of powers for each subsequence, we can calculate the contribution of each number in `nums` to the sum of powers for all subsequences.
- Detailed breakdown:
  1. Sort `nums` in ascending order.
  2. For each number in `nums`, calculate its contribution to the sum of powers for all subsequences.
  3. Sum up the contributions of all numbers.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

const int MOD = 1e9 + 7;

int sumSubseqWidths(vector<int>& nums, int k) {
    int n = nums.size();
    sort(nums.begin(), nums.end());

    long long res = 0;
    long long pow2 = 1;
    for (int i = 0; i < n; i++) {
        long long sum = 0;
        for (int j = 1; j <= k; j++) {
            sum = (sum + (long long)pow(nums[i], j)) % MOD;
        }
        res = (res + sum * pow2) % MOD;
        pow2 = pow2 * 2 % MOD;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n \cdot k)$, where $n$ is the length of `nums` and $k$ is the input integer.
> - **Space Complexity:** $O(n + k)$, for sorting `nums` and storing the current sum.
> - **Optimality proof:** The optimal approach takes advantage of the fact that the sum of powers for all subsequences can be calculated by summing up the contributions of each number in `nums`. This approach has a much lower time complexity than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, sorting, and modular arithmetic.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems and using dynamic programming to solve them.
- Optimization techniques learned: Using the properties of modular arithmetic to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve bit manipulation, sorting, and modular arithmetic.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where `nums` is empty or `k` is 0.
- Edge cases to watch for: The case where `nums` contains duplicate numbers or `k` is very large.
- Performance pitfalls: Not using modular arithmetic to reduce the time complexity of the solution.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure it is correct and efficient.