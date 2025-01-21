## Construct the Minimum Bitwise Array I

**Problem Link:** https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description

**Problem Statement:**
- Given an integer `n`, find the minimum bitwise array of size `n` such that the bitwise AND of all elements is `1`.
- The input `n` is a positive integer.
- The expected output is a vector of integers representing the minimum bitwise array.
- Key requirements and edge cases to consider:
  - The bitwise AND of all elements must be `1`.
  - The array should be as small as possible.

Example test cases with explanations:
- For `n = 1`, the output should be `[1]` because the bitwise AND of `[1]` is `1`.
- For `n = 2`, the output should be `[1, 3]` because the bitwise AND of `[1, 3]` is `1`.
- For `n = 3`, the output should be `[1, 3, 5]` because the bitwise AND of `[1, 3, 5]` is `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible arrays of size `n` and check if the bitwise AND of all elements is `1`.
- Step-by-step breakdown of the solution:
  1. Generate all possible arrays of size `n`.
  2. For each array, calculate the bitwise AND of all elements.
  3. If the bitwise AND is `1`, add the array to the result.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it generates all possible arrays, which is a large number.

```cpp
vector<int> minBitwiseArray(int n) {
    vector<int> result;
    for (int i = 1; i <= n; i++) {
        result.push_back(i);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because we generate all possible arrays of size `n`.
> - **Space Complexity:** $O(2^n)$ because we store all possible arrays of size `n`.
> - **Why these complexities occur:** These complexities occur because we generate all possible arrays of size `n`, which is a large number.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to start with `1` and then add `2` raised to the power of `i-1` to the result for each `i` from `2` to `n`.
- Detailed breakdown of the approach:
  1. Start with `1` as the first element of the result.
  2. For each `i` from `2` to `n`, add `2` raised to the power of `i-1` to the result.
- Proof of optimality: This approach is optimal because it generates the minimum bitwise array of size `n` such that the bitwise AND of all elements is `1`.
- Why further optimization is impossible: This approach is already optimal because it uses the minimum number of elements to achieve the desired bitwise AND.

```cpp
vector<int> minBitwiseArray(int n) {
    vector<int> result;
    for (int i = 1; i <= n; i++) {
        if (i == 1) {
            result.push_back(1);
        } else {
            result.push_back(1 << (i - 1));
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we iterate over the range from `1` to `n`.
> - **Space Complexity:** $O(n)$ because we store the result of size `n`.
> - **Optimality proof:** This approach is optimal because it generates the minimum bitwise array of size `n` such that the bitwise AND of all elements is `1`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, array construction.
- Problem-solving patterns identified: Using a loop to construct an array.
- Optimization techniques learned: Using a mathematical formula to generate the minimum bitwise array.
- Similar problems to practice: Other problems involving bitwise operations and array construction.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of bitwise operators, off-by-one errors.
- Edge cases to watch for: Handling the case where `n` is `1`.
- Performance pitfalls: Using a brute force approach that generates all possible arrays.
- Testing considerations: Testing the function with different values of `n`, including edge cases.