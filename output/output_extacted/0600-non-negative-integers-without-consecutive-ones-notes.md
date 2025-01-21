## Non-Negative Integers Without Consecutive Ones

**Problem Link:** https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description

**Problem Statement:**
- Input format: An integer `n` representing the number of bits.
- Constraints: `1 <= n <= 30`.
- Expected output format: The number of non-negative integers without consecutive ones for the given number of bits.
- Key requirements and edge cases to consider: The integers should not have consecutive ones in their binary representation.
- Example test cases with explanations:
  - For `n = 2`, the valid integers are `0`, `1`, `2`, `3` except for `3` which is `11` in binary, so the answer is `3`.
  - For `n = 3`, the valid integers are `0` through `7` except for `3` (`011`), `5` (`101`), `6` (`110`), and `7` (`111`), so the answer is `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible integers for a given number of bits and check each one for consecutive ones.
- Step-by-step breakdown of the solution:
  1. Generate all integers from `0` to `2^n - 1`.
  2. For each integer, convert it to binary and check for consecutive ones.
  3. Count the integers without consecutive ones.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
int findIntegers(int n) {
    int count = 0;
    for (int i = 0; i < (1 << n); i++) {
        bool hasConsecutiveOnes = false;
        string binary = bitset<32>(i).to_string().substr(32 - n, n);
        for (int j = 0; j < binary.length() - 1; j++) {
            if (binary[j] == '1' && binary[j + 1] == '1') {
                hasConsecutiveOnes = true;
                break;
            }
        }
        if (!hasConsecutiveOnes) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of bits. This is because we generate $2^n$ integers and for each, we potentially check $n$ bits.
> - **Space Complexity:** $O(n)$, for storing the binary representation of each integer.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it checks every possible integer, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to keep track of the number of valid integers ending at each bit position with a `0` or a `1`.
- Detailed breakdown of the approach:
  1. Initialize two arrays, `dp0` and `dp1`, where `dp0[i]` represents the number of valid integers of length `i` ending with `0`, and `dp1[i]` represents the number of valid integers of length `i` ending with `1`.
  2. For each bit position from `1` to `n`, calculate `dp0[i]` and `dp1[i]` based on the previous positions. A valid integer ending in `0` can be formed by appending `0` to any valid integer of the previous length, and a valid integer ending in `1` can only be formed by appending `1` to a valid integer of the previous length that ends with `0`.
  3. The total number of valid integers is the sum of `dp0[n]` and `dp1[n]`.
- Proof of optimality: This approach avoids the exponential time complexity of the brute force method by only considering the necessary information for each bit position, reducing the time complexity to linear with respect to the number of bits.

```cpp
int findIntegers(int n) {
    vector<int> dp0(n + 1, 0), dp1(n + 1, 0);
    dp0[1] = 1; // Single bit '0' is valid
    dp1[1] = 1; // Single bit '1' is valid
    for (int i = 2; i <= n; i++) {
        dp0[i] = dp0[i - 1] + dp1[i - 1]; // Append '0' to any valid integer of length i-1
        dp1[i] = dp0[i - 1]; // Append '1' only to valid integers of length i-1 ending with '0'
    }
    return dp0[n] + dp1[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bits.
> - **Space Complexity:** $O(n)$, for storing the dynamic programming arrays.
> - **Optimality proof:** This solution is optimal because it minimizes the number of operations required to calculate the result, achieving linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for solving problems with overlapping subproblems.
- Problem-solving patterns identified: Recognizing the potential for using dynamic programming to reduce time complexity.
- Optimization techniques learned: Avoiding brute force approaches by identifying patterns that allow for more efficient solutions.
- Similar problems to practice: Other dynamic programming problems, such as Fibonacci sequence, Longest Common Subsequence, etc.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of dynamic programming arrays, misunderstanding the transition between states.
- Edge cases to watch for: Handling the base cases correctly, ensuring the solution works for the smallest possible inputs.
- Performance pitfalls: Failing to recognize the potential for dynamic programming, leading to inefficient brute force solutions.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases, to ensure correctness.