## Find Kth Bit in Nth Binary String

**Problem Link:** https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description

**Problem Statement:**
- Input format: The function takes two integers, `n` and `k`, where `n` represents the nth binary string and `k` represents the position of the bit to find in the string.
- Constraints: `1 <= n <= 20`, `1 <= k <= 2^n`.
- Expected output format: The function should return a single character, either `'0'` or `'1'`, representing the kth bit in the nth binary string.
- Key requirements and edge cases to consider:
  - Understanding the pattern of binary strings and how they are generated.
  - Handling edge cases where `n` is 1 or `k` is at the boundary of the string length.
- Example test cases with explanations:
  - For `n = 1` and `k = 1`, the output should be `'0'` because the first binary string is `'0'`.
  - For `n = 2` and `k = 3`, the output should be `'1'` because the second binary string is `'01'` and the third bit is `'1'`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate the nth binary string by following the pattern of operations provided in the problem statement and then find the kth bit in the generated string.
- Step-by-step breakdown of the solution:
  1. Initialize the first binary string as `'0'`.
  2. For each subsequent binary string up to the nth string, apply the operation of replacing `'0'` with `'01'` and `'1'` with `'10'`.
  3. Once the nth binary string is generated, find the kth bit in the string.

```cpp
string findKthBit(int n, int k) {
    string s = "0";
    for (int i = 1; i < n; ++i) {
        string t = "";
        for (char c : s) {
            if (c == '0') {
                t += "01";
            } else {
                t += "10";
            }
        }
        s = t;
    }
    return s[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the input number. This is because in the worst case, we generate a string of length $2^n$.
> - **Space Complexity:** $O(2^n)$, as we need to store the generated binary string of length $2^n$.
> - **Why these complexities occur:** The brute force approach requires generating the entire nth binary string and then finding the kth bit, leading to exponential time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating the entire binary string, we can find the kth bit directly by analyzing the pattern of the string generation process.
- Detailed breakdown of the approach:
  - Start with the initial string `'0'`.
  - For each iteration up to `n`, calculate the length of the current string and check if `k` falls within the range of the current string or its complement.
  - If `k` falls within the range of the current string, return the corresponding bit from the current string.
  - Otherwise, update `k` to its corresponding position in the next iteration and continue.

```cpp
string findKthBit(int n, int k) {
    string s = "0";
    for (int i = 1; i < n; ++i) {
        int len = s.length();
        if (k <= len) {
            return s[k - 1];
        }
        if (k == len + 1) {
            return '1';
        }
        if (k <= 2 * len) {
            return (s[(2 * len - k) - 1] == '0') ? '1' : '0';
        }
        k -= 2 * len;
    }
    return s[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we only iterate up to `n` times.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space.
> - **Optimality proof:** This is optimal because we directly calculate the kth bit without generating the entire string, reducing both time and space complexities significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Pattern recognition, string manipulation, and optimization techniques.
- Problem-solving patterns identified: Breaking down complex problems into simpler, manageable parts.
- Optimization techniques learned: Avoiding unnecessary computations by directly calculating the desired output.
- Similar problems to practice: Other string manipulation and pattern recognition problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the string or the position `k`.
- Edge cases to watch for: Handling the cases when `n` is 1 or `k` is at the boundary of the string length.
- Performance pitfalls: Generating the entire binary string when it's not necessary.
- Testing considerations: Thoroughly testing the function with different inputs, especially edge cases.