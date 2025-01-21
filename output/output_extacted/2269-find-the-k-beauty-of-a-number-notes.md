## Find the K-Beauty of a Number
**Problem Link:** https://leetcode.com/problems/find-the-k-beauty-of-a-number/description

**Problem Statement:**
- Input: A number `n` and an integer `k`.
- Constraints: `7 <= n <= 2 * 10^9`, `1 <= k <= 7`.
- Expected Output: The `k`-beauty of `n`, which is the maximum number of divisors of `n` that are less than or equal to `k`.
- Key Requirements:
  - Find all divisors of `n`.
  - Count the divisors that are less than or equal to `k`.
- Edge Cases:
  - `n` is a prime number.
  - `k` is greater than the square root of `n`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every number from `1` to `n` to see if it's a divisor of `n`.
- We then check if the divisor is less than or equal to `k` and count it if so.
- This approach comes to mind first because it's straightforward and easy to implement.

```cpp
int findKBeauty(int n, int k) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0 && i <= k) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach checks every number up to `n`, resulting in a linear time complexity. The space complexity is constant because we only use a fixed amount of space to store the count.

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to check up to the square root of `n` to find all divisors.
- We can use a loop to check for divisors and count them if they are less than or equal to `k`.
- We also need to check if the corresponding divisor (i.e., `n / i`) is less than or equal to `k` and count it if so.
- This approach is optimal because it reduces the number of iterations significantly.

```cpp
int findKBeauty(int n, int k) {
    int count = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            if (i <= k) {
                count++;
            }
            if (i != n / i && n / i <= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$, where $n$ is the input number.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it reduces the number of iterations from $O(n)$ to $O(\sqrt{n})$, which is the best possible time complexity for this problem.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: loop optimization, divisor counting.
- Problem-solving patterns identified: reducing the number of iterations by using mathematical properties.
- Optimization techniques learned: using the square root of `n` as an upper bound for the loop.
- Similar problems to practice: finding the number of divisors of a number, finding the sum of divisors of a number.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the corresponding divisor (`n / i`).
- Edge cases to watch for: `n` is a prime number, `k` is greater than the square root of `n`.
- Performance pitfalls: using the brute force approach for large inputs.
- Testing considerations: testing with large inputs, testing with edge cases.