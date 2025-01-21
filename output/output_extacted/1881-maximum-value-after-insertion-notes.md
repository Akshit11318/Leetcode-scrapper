## Maximum Value After Insertion

**Problem Link:** https://leetcode.com/problems/maximum-value-after-insertion/description

**Problem Statement:**
- Given a string `num` and an integer `x`, find the maximum possible integer after inserting `x` into `num`.
- The input string `num` consists of digits only, and the integer `x` is a single digit.
- The goal is to find the maximum possible integer after inserting `x` into `num`.
- Key requirements and edge cases to consider:
  - Handle cases where `num` is empty or `x` is 0.
  - Consider the impact of inserting `x` at different positions in `num`.
- Example test cases with explanations:
  - Input: `num = "99", x = 9`, Output: `"999"`
  - Input: `num = "99", x = 0`, Output: `"990"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try inserting `x` at every possible position in `num` and compare the resulting integers.
- Step-by-step breakdown of the solution:
  1. Iterate over each position in `num`.
  2. Insert `x` at the current position to form a new string.
  3. Compare the new string with the maximum found so far.
- Why this approach comes to mind first: It's a straightforward way to explore all possible insertions of `x` into `num`.

```cpp
string maximumValueAfterInsertion(string num, int x) {
    string maxStr = num;
    for (int i = 0; i <= num.size(); i++) {
        string newStr = num.substr(0, i) + to_string(x) + num.substr(i);
        if (newStr > maxStr) {
            maxStr = newStr;
        }
    }
    return maxStr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `num`, since we iterate over each position in `num` once.
> - **Space Complexity:** $O(n)$, as we create new strings for each insertion.
> - **Why these complexities occur:** The iteration over `num` and the creation of new strings for each insertion contribute to the time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can determine the optimal insertion point by comparing `x` with the digits in `num`.
- Detailed breakdown of the approach:
  1. Iterate over `num` from left to right.
  2. If we find a digit that is less than `x`, insert `x` at the current position.
  3. If we reach the end of `num` without finding a smaller digit, append `x` to the end.
- Proof of optimality: This approach ensures that `x` is inserted at the position that maximizes the resulting integer.

```cpp
string maximumValueAfterInsertion(string num, int x) {
    string result = "";
    bool inserted = false;
    for (char c : num) {
        if (!inserted && c - '0' < x) {
            result += to_string(x);
            inserted = true;
        }
        result += c;
    }
    if (!inserted) {
        result += to_string(x);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `num`, since we iterate over `num` once.
> - **Space Complexity:** $O(n)$, as we build the resulting string.
> - **Optimality proof:** This approach ensures that `x` is inserted at the optimal position, resulting in the maximum possible integer.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, string manipulation, and comparison.
- Problem-solving patterns identified: Determining the optimal insertion point based on comparisons.
- Optimization techniques learned: Avoiding unnecessary iterations and string creations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty `num` or `x` being 0.
- Edge cases to watch for: Handling cases where `x` is greater than or equal to all digits in `num`.
- Performance pitfalls: Unnecessary iterations or string creations.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases.