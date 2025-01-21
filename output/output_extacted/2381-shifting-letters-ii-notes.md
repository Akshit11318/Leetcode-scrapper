## Shifting Letters II
**Problem Link:** https://leetcode.com/problems/shifting-letters-ii/description

**Problem Statement:**
- Input format: A string `s` and a 2D array `shifts` where each subarray contains two integers, `start` and `end`, representing a range `[start, end]`.
- Constraints: `1 <= s.length <= 10^5`, `s` consists only of lowercase English letters, `1 <= shifts.length <= 10^5`, and `0 <= start <= end < s.length`.
- Expected output format: The modified string `s` after applying all shifts.
- Key requirements and edge cases to consider: Applying shifts to the characters in `s` within the specified ranges, wrapping around the alphabet when shifting, and handling overlapping ranges.

**Example Test Cases:**
- Input: `s = "abc", shifts = [[0,1],[1,2]]`
  Output: `"acc"`
- Input: `s = "dfl", shifts = [[0,1],[1,2],[0,2]]`
  Output: `"def"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Apply each shift to the characters in the specified range, updating the string `s` after each shift.
- Step-by-step breakdown of the solution:
  1. Iterate over each shift in `shifts`.
  2. For each shift, iterate over the characters in `s` within the specified range.
  3. Apply the shift to each character, wrapping around the alphabet if necessary.
  4. Update the string `s` with the shifted characters.
- Why this approach comes to mind first: It directly follows the problem description, applying each shift to the specified range in `s`.

```cpp
string shiftingLetters(string s, vector<vector<int>>& shifts) {
    string result = s;
    for (auto& shift : shifts) {
        int start = shift[0], end = shift[1];
        for (int i = start; i <= end; i++) {
            // Apply shift, wrapping around alphabet
            result[i] = 'a' + (result[i] - 'a' + 1) % 26;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `s` and $m$ is the number of shifts, because in the worst case, we apply each shift to every character in `s`.
> - **Space Complexity:** $O(n)$, for storing the result string, assuming the input string is not modified in-place.
> - **Why these complexities occur:** The nested loops over shifts and characters in `s` lead to the time complexity, and storing the result requires space proportional to the length of `s`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of applying each shift individually, we can calculate the net effect of all shifts on each character.
- Detailed breakdown of the approach:
  1. Initialize an array `diff` of size `n+1`, where `diff[i]` represents the net shift applied to the character at index `i`.
  2. For each shift, increment `diff[start]` and decrement `diff[end+1]`.
  3. Calculate the prefix sum of `diff` to get the net shift for each character.
  4. Apply the net shift to each character in `s`.
- Proof of optimality: This approach processes each shift and character once, leading to a linear time complexity.

```cpp
string shiftingLetters(string s, vector<vector<int>>& shifts) {
    int n = s.size();
    vector<int> diff(n + 1, 0);
    for (auto& shift : shifts) {
        int start = shift[0], end = shift[1];
        diff[start]++;
        if (end + 1 < n) diff[end + 1]--;
    }
    for (int i = 1; i <= n; i++) {
        diff[i] += diff[i - 1];
    }
    string result = "";
    for (int i = 0; i < n; i++) {
        result += 'a' + (s[i] - 'a' + diff[i]) % 26;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `s` and $m` is the number of shifts, because we process each shift and character once.
> - **Space Complexity:** $O(n)$, for storing the `diff` array and the result string.
> - **Optimality proof:** This approach is optimal because it processes each input element (shifts and characters) a constant number of times, achieving linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum calculation for efficient accumulation of shifts.
- Problem-solving patterns identified: Processing each input element a constant number of times to achieve linear time complexity.
- Optimization techniques learned: Calculating the net effect of operations instead of applying them individually.
- Similar problems to practice: Problems involving range updates and prefix sum calculations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the `diff` array or applying shifts.
- Edge cases to watch for: Handling shifts that span the entire string or applying multiple shifts to the same range.
- Performance pitfalls: Using a brute force approach that applies each shift individually, leading to quadratic time complexity.
- Testing considerations: Thoroughly testing with different shift ranges and string lengths to ensure correctness.