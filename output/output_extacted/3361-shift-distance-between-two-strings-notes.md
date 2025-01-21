## Shift Distance Between Two Strings
**Problem Link:** https://leetcode.com/problems/shift-distance-between-two-strings/description

**Problem Statement:**
- Input format: Two strings `s1` and `s2` of the same length.
- Constraints: `1 <= s1.length <= 100` and `s1.length == s2.length`.
- Expected output format: The minimum number of shifts to make `s1` equal to `s2`.
- Key requirements: If the strings cannot be made equal by shifting, return `-1`.
- Example test cases:
  - Input: `s1 = "cdeo", s2 = "dceo"`
    Output: `2`
    Explanation: Rotate `s1` two times to get `s2`.
  - Input: `s1 = "a", s2 = "a"`
    Output: `0`
    Explanation: No shifts are needed.
  - Input: `s1 = "abc", s2 = "bca"`
    Output: `1`
    Explanation: Rotate `s1` one time to get `s2`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible shifts of `s1` and compare each with `s2`.
- Step-by-step breakdown:
  1. For each possible shift from 0 to `s1.length - 1`, rotate `s1` by that amount.
  2. Compare the rotated `s1` with `s2`.
  3. If they match, return the shift amount.
  4. If no match is found after trying all shifts, return `-1`.
- Why this approach comes to mind first: It's straightforward and ensures all possibilities are considered.

```cpp
int shiftDistance(string s1, string s2) {
    int n = s1.length();
    for (int shift = 0; shift < n; shift++) {
        string rotated = s1.substr(shift, n - shift) + s1.substr(0, shift);
        if (rotated == s2) return shift;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `s1`. This is because for each shift, we're creating a new string which takes $O(n)$ time, and we do this $n$ times.
> - **Space Complexity:** $O(n)$, as we're storing the rotated string in each iteration.
> - **Why these complexities occur:** The nested operations (rotation and comparison) within the loop cause these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of rotating `s1` and comparing, we can concatenate `s1` with itself and check if `s2` is a substring of the concatenated string.
- Detailed breakdown:
  1. Concatenate `s1` with itself to create a new string `s1s1`.
  2. Check if `s2` is a substring of `s1s1`.
  3. If `s2` is found, the starting index of `s2` in `s1s1` gives the shift amount.
  4. If `s2` is not found, return `-1`.
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the need to rotate `s1` in each iteration.

```cpp
int shiftDistance(string s1, string s2) {
    string s1s1 = s1 + s1;
    size_t found = s1s1.find(s2);
    if (found != string::npos) return found % s1.length();
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s1`. This is because the `find` operation in the concatenated string takes linear time.
> - **Space Complexity:** $O(n)$, for storing the concatenated string.
> - **Optimality proof:** This is optimal because we've reduced the operation to a single pass through the concatenated string, which is necessary to check all possible shifts.

---

### Final Notes
**Learning Points:**
- Key algorithmic concept: Using string concatenation to simplify the problem.
- Problem-solving pattern: Looking for ways to reduce the number of operations by preprocessing or transforming the input.
- Optimization technique: Avoiding unnecessary rotations by using a concatenated string.

**Mistakes to Avoid:**
- Implementing the brute force approach in production code due to its high time complexity.
- Not considering edge cases, such as when the input strings are of different lengths or when one string is not a rotation of the other.