## Powerful Integers
**Problem Link:** https://leetcode.com/problems/powerful-integers/description

**Problem Statement:**
- Input format and constraints: Given two integers `x` and `y`, and a limit `limit`, return a list of all powerful integers that can be expressed in the form `x^i + y^j` where `i` and `j` are non-negative integers and `x^i + y^j` is less than or equal to `limit`.
- Expected output format: A list of powerful integers.
- Key requirements and edge cases to consider: Handle cases where `x` or `y` is 0 or 1, and cases where `limit` is very large.
- Example test cases with explanations:
  - Example 1: `x = 2`, `y = 3`, `limit = 10`. The powerful integers are `[2, 3, 4, 5, 7, 9]`.
  - Example 2: `x = 3`, `y = 5`, `limit = 15`. The powerful integers are `[2, 4, 6, 8, 10, 14]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of `i` and `j` to generate all powerful integers.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set to store unique powerful integers.
  2. Iterate over all possible values of `i` and `j` using two nested loops.
  3. For each pair of `i` and `j`, calculate `x^i + y^j` and check if it is less than or equal to `limit`.
  4. If it is, add it to the set of powerful integers.
  5. Finally, return the set of powerful integers as a list.
- Why this approach comes to mind first: It is a straightforward way to generate all possible powerful integers.

```cpp
vector<int> powerfulIntegers(int x, int y, int limit) {
    unordered_set<int> powerful;
    for (int i = 0; ; i++) {
        long long val = pow(x, i);
        if (val > limit) break;
        for (int j = 0; ; j++) {
            long long sum = val + pow(y, j);
            if (sum > limit) break;
            powerful.insert(sum);
            if (y == 1) break;
        }
        if (x == 1) break;
    }
    vector<int> result(powerful.begin(), powerful.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log_{x} limit \cdot \log_{y} limit)$, where $x$ and $y$ are the bases and $limit$ is the given limit.
> - **Space Complexity:** $O(\log_{x} limit \cdot \log_{y} limit)$, as we need to store all generated powerful integers.
> - **Why these complexities occur:** The time complexity is due to the nested loops over all possible values of `i` and `j`, and the space complexity is due to storing all generated powerful integers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution but with some optimizations to reduce the number of iterations.
- Detailed breakdown of the approach:
  1. Initialize an empty set to store unique powerful integers.
  2. Iterate over all possible values of `i` and `j` using two nested loops, but with a condition to break the inner loop when `y^j` exceeds `limit - x^i`.
  3. For each pair of `i` and `j`, calculate `x^i + y^j` and check if it is less than or equal to `limit`.
  4. If it is, add it to the set of powerful integers.
  5. Finally, return the set of powerful integers as a list.
- Proof of optimality: This approach generates all possible powerful integers while minimizing the number of iterations.
- Why further optimization is impossible: We must check all possible combinations of `i` and `j` to ensure that we generate all powerful integers.

```cpp
vector<int> powerfulIntegers(int x, int y, int limit) {
    unordered_set<int> powerful;
    for (int i = 0; ; i++) {
        long long val = pow(x, i);
        if (val > limit) break;
        for (int j = 0; ; j++) {
            long long sum = val + pow(y, j);
            if (sum > limit) break;
            powerful.insert(sum);
            if (y == 1) break;
        }
        if (x == 1) break;
    }
    vector<int> result(powerful.begin(), powerful.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log_{x} limit \cdot \log_{y} limit)$, where $x$ and $y$ are the bases and $limit$ is the given limit.
> - **Space Complexity:** $O(\log_{x} limit \cdot \log_{y} limit)$, as we need to store all generated powerful integers.
> - **Optimality proof:** This approach generates all possible powerful integers while minimizing the number of iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using nested loops to generate all possible combinations of `i` and `j`, and using a set to store unique powerful integers.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using optimization techniques to reduce the number of iterations.
- Optimization techniques learned: Using a condition to break the inner loop when `y^j` exceeds `limit - x^i`, and using a set to store unique powerful integers.
- Similar problems to practice: Generating all possible combinations of numbers, and using optimization techniques to reduce the number of iterations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the condition to break the inner loop, and not using a set to store unique powerful integers.
- Edge cases to watch for: Handling cases where `x` or `y` is 0 or 1, and cases where `limit` is very large.
- Performance pitfalls: Not using optimization techniques to reduce the number of iterations, and not using a set to store unique powerful integers.
- Testing considerations: Testing the solution with different values of `x`, `y`, and `limit`, and checking for correct output and performance.