## Number of Divisible Substrings
**Problem Link:** https://leetcode.com/problems/number-of-divisible-substrings/description

**Problem Statement:**
- Input: a string `s` consisting of digits and an integer `k`.
- Output: The number of substrings in `s` that are divisible by `k`.
- Key requirements and edge cases:
  - `1 <= k <= 10^9`
  - `1 <= s.length <= 10^5`
  - `s` consists of digits from `0` to `9`.
- Example test cases:
  - `s = "10203", k = 5` should return `3` because `102`, `020`, and `203` are divisible by `5`.
  - `s = "1020", k = 5` should return `2` because `102` and `020` are divisible by `5`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Check every possible substring of `s` to see if it's divisible by `k`.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. For each substring, convert it to an integer.
  3. Check if the integer is divisible by `k`.
- Why this approach comes to mind first: It's straightforward and ensures we consider all substrings.

```cpp
int numberOfDivisibleSubstrings(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substr = s.substr(i, j - i);
            int num = stoi(substr);
            if (num % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the length of `s` and $m$ is the maximum number of digits in a substring, because we generate all substrings and convert each to an integer.
> - **Space Complexity:** $O(m)$ for storing the current substring, because we only need to store the current substring being processed.
> - **Why these complexities occur:** The nested loops generate all substrings, and converting each to an integer and checking divisibility contribute to the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of converting each substring to an integer, we can calculate its value modulo `k` directly from its digits.
- Detailed breakdown:
  1. Iterate over all substrings of `s`.
  2. For each substring, calculate its value modulo `k` by summing the values of its digits multiplied by their respective place values.
  3. Check if the calculated value is `0`, indicating the substring is divisible by `k`.
- Proof of optimality: This approach avoids the overhead of string to integer conversion and directly calculates divisibility, making it more efficient than the brute force approach.

```cpp
int numberOfDivisibleSubstrings(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        int sum = 0;
        for (int j = i; j < s.length(); j++) {
            sum = (sum * 10 + (s[j] - '0')) % k;
            if (sum == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `s`, because we iterate over all substrings and calculate their values modulo `k`.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the sum and indices.
> - **Optimality proof:** This approach is optimal because it directly calculates the divisibility of substrings without unnecessary conversions, achieving the best possible time complexity for this problem.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts: Iteration, modulo arithmetic, and direct calculation of divisibility.
- Problem-solving patterns: Avoiding unnecessary conversions and calculating properties directly.
- Optimization techniques: Using modulo arithmetic to reduce computational overhead.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the value of substrings or misunderstanding the modulo operation.
- Edge cases to watch for: Handling substrings that start with `0` or are single-digit numbers.
- Performance pitfalls: Using inefficient data structures or algorithms that scale poorly with input size.
- Testing considerations: Ensuring the solution works correctly for various inputs, including edge cases and large inputs.