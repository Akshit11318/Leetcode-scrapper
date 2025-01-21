## Find the Sum of the Power of All Subsequences

**Problem Link:** https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, return the sum of the power of all possible subsequences of `nums` modulo `10^9 + 7`. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The power of a subsequence is the product of all its elements raised to the power of `k`.

**Input Format and Constraints:**
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`
- `1 <= k <= 1000`
- `1 <= mod <= 10^9 + 7`

**Expected Output Format:**
- The sum of the power of all possible subsequences modulo `mod`.

**Key Requirements and Edge Cases to Consider:**
- Handle cases where the input array is empty or contains a single element.
- Ensure the solution can handle large inputs within the given time limit.
- Consider the properties of modular arithmetic to avoid overflow.

**Example Test Cases with Explanations:**
- For `nums = [1, 2, 3]`, `k = 2`, and `mod = 1000000007`, the sum of the power of all possible subsequences is `(1^2) + (2^2) + (3^2) + (1^2 * 2^2) + (1^2 * 3^2) + (2^2 * 3^2) + (1^2 * 2^2 * 3^2)` modulo `mod`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subsequences of the input array and calculating the sum of their powers.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insights.

```cpp
#include <vector>
#include <iostream>
using namespace std;

int sumOfPower(vector<int>& nums, int k, int mod) {
    int n = nums.size();
    int total = 0;
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); mask++) {
        long long product = 1;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                // Calculate the product of the current subsequence
                product = (product * nums[i]) % mod;
            }
        }
        // Update the sum with the power of the current subsequence
        total = (total + powerMod(product, k, mod)) % mod;
    }
    return total;
}

long long powerMod(long long base, int exponent, int mod) {
    long long result = 1;
    base %= mod;
    while (exponent > 0) {
        if (exponent & 1) result = (result * base) % mod;
        exponent >>= 1;
        base = (base * base) % mod;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k \cdot \log{mod})$ due to generating all possible subsequences and calculating the power of each subsequence using modular exponentiation.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the result and temporary variables.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences, which results in an exponential time complexity. The modular exponentiation adds a logarithmic factor to the time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the properties of modular arithmetic and the fact that the sum of the power of all subsequences can be calculated using a dynamic programming approach.
- We can calculate the sum of the power of all subsequences ending at each position and then combine these results to obtain the final sum.

```cpp
#include <vector>
#include <iostream>
using namespace std;

int sumOfPower(vector<int>& nums, int k, int mod) {
    int n = nums.size();
    long long total = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        long long product = 1;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                product = (product * nums[i]) % mod;
            }
        }
        total = (total + powerMod(product, k, mod)) % mod;
    }
    return (int)total;
}

long long powerMod(long long base, int exponent, int mod) {
    long long result = 1;
    base %= mod;
    while (exponent > 0) {
        if (exponent & 1) result = (result * base) % mod;
        exponent >>= 1;
        base = (base * base) % mod;
    }
    return result;
}
```

However, to improve this, consider the following dynamic approach that builds upon the concept of calculating the sum of powers for each possible subsequence length:

```cpp
int sumOfPower(vector<int>& nums, int k, int mod) {
    int n = nums.size();
    vector<long long> dp(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        dp[i] = (dp[i - 1] * (1 + powerMod(nums[i - 1], k, mod))) % mod;
    }
    return (int)(dp[n] - 1);
}

long long powerMod(long long base, int exponent, int mod) {
    long long result = 1;
    base %= mod;
    while (exponent > 0) {
        if (exponent & 1) result = (result * base) % mod;
        exponent >>= 1;
        base = (base * base) % mod;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k \cdot \log{mod})$ due to the dynamic programming approach and modular exponentiation.
> - **Space Complexity:** $O(n)$ for storing the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it avoids generating all possible subsequences and instead calculates the sum of their powers using a dynamic programming approach.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the importance of using dynamic programming to avoid exponential time complexity.
- Modular arithmetic is crucial for handling large numbers and avoiding overflow.
- The power of a subsequence can be calculated efficiently using modular exponentiation.

**Mistakes to Avoid:**
- Failing to use modular arithmetic, leading to overflow and incorrect results.
- Not considering the properties of dynamic programming to reduce time complexity.
- Incorrectly implementing modular exponentiation, leading to incorrect results.