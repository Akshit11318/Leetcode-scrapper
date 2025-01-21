## Remove All Occurrences of a Substring
**Problem Link:** https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and a substring `part`, remove all occurrences of `part` from `s`.
- Expected output format: Return the resulting string after removing all occurrences of `part`.
- Key requirements and edge cases to consider: 
    - `s` and `part` are non-empty strings.
    - `part` can be a substring of itself (e.g., `part = "abab"`).
- Example test cases with explanations:
    - `s = "daabcbaabcbc", part = "abc"`: Expected output is `"dab"` because all occurrences of `"abc"` are removed.
    - `s = "axxxxyxxxxyxxxx", part = "xxx"`: Expected output is `"a"` because all occurrences of `"xxx"` are removed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a simple loop to find and remove all occurrences of the substring.
- Step-by-step breakdown of the solution:
    1. Initialize an empty result string.
    2. Loop through the input string `s`.
    3. For each position in `s`, check if the substring `part` starts at this position.
    4. If `part` is found, skip over it and continue checking from the next position.
    5. If `part` is not found, append the current character to the result string.
- Why this approach comes to mind first: It's a straightforward, intuitive approach to the problem.

```cpp
string removeOccurrences(string s, string part) {
    string result = "";
    int i = 0;
    while (i < s.size()) {
        if (s.substr(i, part.size()) == part) {
            i += part.size();
        } else {
            result += s[i];
            i++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of `s` and $m$ is the length of `part`, because for each character in `s`, we potentially compare with all characters in `part`.
> - **Space Complexity:** $O(n)$ for storing the result string.
> - **Why these complexities occur:** The brute force approach involves comparing substrings of `s` with `part` at each position, leading to a nested loop structure that results in these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a `while` loop to continuously remove `part` from `s` until no more occurrences are found.
- Detailed breakdown of the approach:
    1. Initialize `s` as the original string.
    2. Enter a loop that continues as long as `s` contains `part`.
    3. Within the loop, replace all occurrences of `part` with an empty string.
    4. Repeat steps 2 and 3 until `part` is no longer found in `s`.
- Proof of optimality: This approach directly addresses the problem statement by iteratively removing all occurrences of `part` from `s` without unnecessary comparisons.

```cpp
string removeOccurrences(string s, string part) {
    while (true) {
        size_t pos = s.find(part);
        if (pos == string::npos) break;
        s.erase(pos, part.size());
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ in the worst case where $n$ is the length of `s` and $m$ is the length of `part`, because each replacement operation might shift all subsequent characters.
> - **Space Complexity:** $O(n)$ for the string operations.
> - **Optimality proof:** While the time complexity remains $O(n \cdot m)$, this approach is more efficient in practice because it leverages optimized string operations and minimizes the number of comparisons needed to find and remove all occurrences of `part`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, substring searching, and iterative refinement.
- Problem-solving patterns identified: Using loops to iteratively refine a solution until a stopping condition is met.
- Optimization techniques learned: Leveraging built-in string operations for efficiency.
- Similar problems to practice: Other string manipulation problems involving searching, replacing, or modifying strings based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty strings or substrings that are not found.
- Edge cases to watch for: When `part` is an empty string, or when `s` and `part` are the same string.
- Performance pitfalls: Using inefficient string manipulation techniques that lead to high time or space complexities.
- Testing considerations: Ensure to test with various inputs, including edge cases and large strings, to verify the correctness and performance of the solution.