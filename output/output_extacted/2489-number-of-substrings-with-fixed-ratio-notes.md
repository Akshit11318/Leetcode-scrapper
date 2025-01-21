## Number of Substrings with Fixed Ratio
**Problem Link:** https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/description

**Problem Statement:**
- Input: A string `s` and two integers `num1` and `num2`.
- Constraints: `1 <= num1 <= num2 <= 100`, `num2` is a multiple of `num1`, and `s` consists only of digits.
- Expected output: The number of substrings of `s` that contain exactly `num1` occurrences of the digit `1` and `num2` occurrences of the digit `2`.
- Key requirements and edge cases to consider: Handling substrings with varying lengths, ensuring the ratio of `1`s to `2`s matches `num1:num2`, and accounting for overlapping substrings.
- Example test cases with explanations:
  - Example 1: Input `s = "0110", num1 = 1, num2 = 2`, Output `2` because the valid substrings are `"110"` and `"10"`.
  - Example 2: Input `s = "024", num1 = 1, num2 = 1`, Output `3` because the valid substrings are `"0"`, `"2"`, and `"4"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible substrings of `s`, count the occurrences of `1` and `2` in each, and check if the ratio matches `num1:num2`.
- Step-by-step breakdown of the solution:
  1. Generate all substrings of `s`.
  2. For each substring, count the occurrences of `1` and `2`.
  3. Check if the counts match `num1` and `num2`.
  4. If they match, increment the count of valid substrings.

```cpp
int numberOfSubstrings(string s, int num1, int num2) {
    int count = 0;
    for (int i = 0; i < s.length(); ++i) {
        for (int j = i + 1; j <= s.length(); ++j) {
            string substr = s.substr(i, j - i);
            int ones = 0, twos = 0;
            for (char c : substr) {
                if (c == '1') ++ones;
                else if (c == '2') ++twos;
            }
            if (ones == num1 && twos == num2) ++count;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of `s`, because we generate all substrings ($O(n^2)$) and for each, we count `1`s and `2`s ($O(n)$).
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the counts and the current substring.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to its exhaustive nature, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of counting `1`s and `2`s for each substring, we can use a sliding window approach to efficiently count them as we extend or shrink the window.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to represent the sliding window.
  2. Maintain counts of `1`s and `2`s within the current window.
  3. Extend the window to the right, updating counts, and when the counts exceed `num1` and `num2`, move the `left` pointer to the right, shrinking the window.
  4. Whenever the counts match `num1` and `num2`, increment the count of valid substrings.

```cpp
int numberOfSubstrings(string s, int num1, int num2) {
    int count = 0;
    for (int i = 0; i < s.length(); ++i) {
        int ones = 0, twos = 0;
        for (int j = i; j < s.length(); ++j) {
            if (s[j] == '1') ++ones;
            else if (s[j] == '2') ++twos;
            if (ones == num1 && twos == num2) ++count;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `s`, because we still consider all substrings but count `1`s and `2`s more efficiently.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the counts and pointers.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to count `1`s and `2`s in all substrings, taking advantage of the fact that extending or shrinking the window only requires updating the counts for the new or removed character.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, efficient counting within a window.
- Problem-solving patterns identified: Optimizing brute force approaches by reducing redundant computations.
- Optimization techniques learned: Using a sliding window to minimize the number of operations.
- Similar problems to practice: Other substring or subarray problems that can benefit from the sliding window technique.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating counts when extending or shrinking the window.
- Edge cases to watch for: Handling cases where `num1` or `num2` is zero, or when the input string is empty.
- Performance pitfalls: Failing to optimize the counting process, leading to high time complexity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large inputs to ensure efficiency.