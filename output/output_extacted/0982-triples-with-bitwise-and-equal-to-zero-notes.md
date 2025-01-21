## Triiples with Bitwise AND Equal to Zero

**Problem Link:** https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/description

**Problem Statement:**
- Given an integer `n`, find the number of triples `(a, b, c)` where `a`, `b`, `c` are integers in the range `[0, n - 1]` such that `a & b & c == 0`.
- Input format: `n` is an integer.
- Expected output format: The number of triples `(a, b, c)` that satisfy the condition.
- Key requirements and edge cases to consider: 
  - The range of `n` is from `1` to `1000`.
  - The integers `a`, `b`, `c` are in the range `[0, n - 1]`.
- Example test cases with explanations:
  - For `n = 1`, the only possible triple is `(0, 0, 0)`, so the answer is `1`.
  - For `n = 2`, the possible triples are `(0, 0, 0)`, `(0, 0, 1)`, `(0, 1, 0)`, `(1, 0, 0)`, so the answer is `4`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over all possible values of `a`, `b`, `c` in the given range and check if `a & b & c == 0`.
- This approach involves checking every possible triple, which is straightforward but inefficient for larger values of `n`.

```cpp
int countTriplets(int n) {
    int count = 0;
    for (int a = 0; a < n; a++) {
        for (int b = 0; b < n; b++) {
            for (int c = 0; c < n; c++) {
                if ((a & b & c) == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, because we are iterating over all possible triples.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The brute force approach involves checking every possible triple, resulting in a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is recognizing that for any given bit position, `a`, `b`, and `c` must all have a `0` in that position if their bitwise AND is to be `0`.
- We can calculate the number of valid triples by considering each bit position separately and then combining these counts.
- For each bit position `i`, there are $2^i$ numbers in the range `[0, n-1]` that have a `0` in the `i-th` position. However, not all these numbers are valid for our calculation because we must consider the actual range `[0, n-1]`.
- We calculate the number of valid triples by considering all possible combinations of `a`, `b`, and `c` that satisfy the condition for each bit position.

```cpp
int countTriplets(int n) {
    int count = 0;
    for (int a = 0; a < n; a++) {
        for (int b = 0; b < n; b++) {
            int c = 0;
            while (c < n) {
                if ((a & b & c) == 0) {
                    count++;
                }
                c++;
            }
        }
    }
    return count;
}
```
However, the above solution still has a time complexity of $O(n^3)$.

A more optimal solution would involve using the properties of bitwise operations to directly calculate the number of valid triples without iterating over all possible values of `a`, `b`, and `c`.

For any given bit position `i`, if `a` has a `1` in the `i-th` position, then `b` and `c` must both have a `0` in the `i-th` position for their bitwise AND to be `0`. Conversely, if `a` has a `0` in the `i-th` position, then `b` and `c` can have either a `0` or a `1` in the `i-th` position.

Let's consider the bits of `n-1` (since the range is `[0, n-1]`). For each bit position `i`:
- If the `i-th` bit of `n-1` is `1`, there are $2^{i-1}$ possible values for `a` that have a `1` in the `i-th` position (since the bits to the left of the `i-th` position can be any combination of `0`s and `1`s, and there are $2^{i-1}$ such combinations). For each of these values of `a`, there are $2^{i-1}$ possible values for `b` that have a `0` in the `i-th` position, and similarly $2^{i-1}$ possible values for `c`.
- If the `i-th` bit of `n-1` is `0`, then `a`, `b`, and `c` must all have a `0` in the `i-th` position.

We can use this insight to directly calculate the number of valid triples.

However, there is a much simpler and more efficient way to solve this problem using the properties of bitwise operations.

```cpp
int countTriplets(int n) {
    int count = 0;
    for (int a = 0; a < n; a++) {
        for (int b = 0; b < n; b++) {
            int mask = ~(a & b);
            count += (n - 1) - (mask & (n - 1));
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because we are iterating over all possible pairs of `a` and `b`.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count.
> - **Optimality proof:** This solution is optimal because it uses the properties of bitwise operations to directly calculate the number of valid triples without iterating over all possible values of `a`, `b`, and `c`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, iteration, and optimization.
- Problem-solving patterns identified: Using properties of bitwise operations to simplify the problem.
- Optimization techniques learned: Avoiding unnecessary iterations and using bitwise operations to directly calculate results.
- Similar problems to practice: Other problems involving bitwise operations and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of bitwise operations, unnecessary iterations.
- Edge cases to watch for: Boundary values of `n`, such as `n = 1` or `n = 1000`.
- Performance pitfalls: Using brute force approaches for large values of `n`.
- Testing considerations: Testing with different values of `n`, including boundary values and large values.