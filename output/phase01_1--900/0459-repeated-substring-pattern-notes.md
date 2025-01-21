## Repeated Substring Pattern

**Problem Link:** https://leetcode.com/problems/repeated-substring-pattern/description

**Problem Statement:**
- Given a non-empty string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
- Input: A string `s`.
- Expected output: `true` if `s` is a repeated substring pattern, `false` otherwise.
- Key requirements and edge cases to consider:
  - The input string `s` is non-empty.
  - The substring must be non-empty.
- Example test cases:
  - Input: `"abab"` - Output: `true` because it can be constructed by taking the substring `"ab"` and appending it to itself.
  - Input: `"aba"` - Output: `false` because no non-empty substring can be repeated to form `"aba"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of `s` to see if repeating it can form `s`.
- Step-by-step breakdown:
  1. Generate all possible non-empty substrings of `s`.
  2. For each substring, check if the length of `s` is divisible by the length of the substring (since a repeated pattern requires the lengths to be divisible).
  3. If the length condition is met, attempt to reconstruct `s` by repeating the substring and compare it with the original string `s`.
  4. If any repeated substring matches `s`, return `true`.
  5. If no matching repeated substring is found after checking all substrings, return `false`.

```cpp
bool repeatedSubstringPattern(string s) {
    int n = s.length();
    for (int len = 1; len <= n / 2; len++) {
        if (n % len == 0) {
            bool match = true;
            for (int i = len; i < n; i++) {
                if (s[i] != s[i % len]) {
                    match = false;
                    break;
                }
            }
            if (match) return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, for every substring length up to $n/2$, we are potentially comparing characters up to $n$ times.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with input size $n$.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure where we iterate over possible substring lengths and then over the string itself to compare characters. The space complexity is constant because we only use a fixed amount of space to store variables like `n`, `len`, and `match`, regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking every possible substring, we can observe that if `s` is a repeated substring pattern, then `s` must be a substring of `s + s` (where `s` is concatenated with itself) excluding the first and last characters of the concatenated string.
- Detailed breakdown:
  1. Concatenate `s` with itself to form a new string `ss`.
  2. Check if `s` is a substring of `ss` excluding the first and last characters of `ss`.
  3. If `s` is found as a substring, return `true`; otherwise, return `false`.

```cpp
bool repeatedSubstringPattern(string s) {
    string ss = s + s;
    return ss.find(s, 1) != string::npos && ss.find(s, 1) < s.length() + 1;
}
```

Alternatively, a more intuitive implementation directly checks if `s` is a substring of `ss` (excluding the first and last character by adjusting the start index and ensuring the found substring is within the bounds of the first `s.length()` characters of `ss`):

```cpp
bool repeatedSubstringPattern(string s) {
    string ss = s + s;
    return ss.substr(1, s.length()) == s || ss.substr(s.length(), s.length()) == s;
}
```

However, a more elegant and efficient solution exists:

```cpp
bool repeatedSubstringPattern(string s) {
    return (s + s).find(s, 1) != string::npos;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because the `find` operation in the best case has a linear time complexity.
> - **Space Complexity:** $O(n)$ because we create a new string `ss` that is twice the size of `s`.
> - **Optimality proof:** This is optimal because we are reducing the problem to a single operation that checks for the existence of `s` as a substring in `ss`, which inherently covers all possible repeated patterns without explicitly iterating over them. The space complexity is also justified as necessary for the operation.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated here is the use of string manipulation and substring searching to solve a pattern recognition problem.
- Problem-solving patterns identified include reducing complex iteration to simpler, more efficient operations like substring searching.
- Optimization techniques learned include avoiding unnecessary iterations and using built-in functions for efficiency.

**Mistakes to Avoid:**
- Common implementation errors include not properly handling edge cases (like empty strings or strings of length 1) and not optimizing the solution to reduce unnecessary iterations.
- Performance pitfalls include using overly complex or inefficient algorithms that do not scale well with input size.
- Testing considerations should include a variety of input cases, including edge cases and large inputs to ensure the solution is both correct and efficient.