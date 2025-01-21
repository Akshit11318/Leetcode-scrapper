## Ugly Number III
**Problem Link:** https://leetcode.com/problems/ugly-number-iii/description

**Problem Statement:**
- Input: `n`, `a`, `b`, `ab`
- Output: The `n^{th}` `ugly` number that is a multiple of `a`, `b`, or `ab`.
- Key requirements: Find the `n^{th}` smallest number that can be divided by `a`, `b`, or `ab` without a remainder.
- Example test cases:
  - Input: `n = 3, a = 2, b = 3, ab = 6`
  - Output: `4`
  - Explanation: The `ugly` numbers are `2, 3, 4, 6, 6, 8, 9, 10, 12` and the `3^{rd}` `ugly` number is `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all numbers starting from `1` and check each one if it's divisible by `a`, `b`, or `ab`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for `ugly` numbers.
  2. Iterate over all numbers starting from `1`.
  3. For each number, check if it's divisible by `a`, `b`, or `ab`.
  4. If it's divisible, increment the counter.
  5. Stop when the counter reaches `n`.

```cpp
int nthUglyNumber(int n, int a, int b, int ab) {
    int count = 0;
    int num = 1;
    while (true) {
        if (num % a == 0 || num % b == 0 || num % ab == 0) {
            count++;
            if (count == n) return num;
        }
        num++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot max(a, b, ab))$ because in the worst case, we need to iterate over all numbers up to `n * max(a, b, ab)`.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is high because we're checking every number one by one, and the space complexity is low because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use the principle of inclusion-exclusion to find the number of multiples of `a`, `b`, or `ab` up to a certain number `x`.
- Detailed breakdown of the approach:
  1. Define a function `count(x)` that returns the number of multiples of `a`, `b`, or `ab` up to `x`.
  2. Use the principle of inclusion-exclusion to calculate `count(x)`.
  3. Perform a binary search to find the `n^{th}` `ugly` number.

```cpp
int nthUglyNumber(int n, int a, int b, int ab) {
    int lcm_ab = lcm(a, b);
    int left = min(a, b), right = n * min(a, b);
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (count(mid, a, b, ab) < n) left = mid + 1;
        else right = mid;
    }
    return left;
}

int count(int x, int a, int b, int ab) {
    return x / a + x / b - x / lcm(a, b);
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n \cdot max(a, b)))$ because we're performing a binary search.
> - **Space Complexity:** $O(1)$ because we're not using any data structures that scale with the input size.
> - **Optimality proof:** This is the optimal solution because we're using the principle of inclusion-exclusion to calculate the number of multiples of `a`, `b`, or `ab` up to a certain number `x`, and then performing a binary search to find the `n^{th}` `ugly` number.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: principle of inclusion-exclusion, binary search.
- Problem-solving patterns identified: using mathematical principles to simplify the problem.
- Optimization techniques learned: using binary search to reduce the search space.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not using the principle of inclusion-exclusion correctly.
- Edge cases to watch for: when `a`, `b`, or `ab` is `1`, when `n` is `1`.
- Performance pitfalls: using a brute force approach, not using binary search.
- Testing considerations: testing with different values of `n`, `a`, `b`, and `ab`.