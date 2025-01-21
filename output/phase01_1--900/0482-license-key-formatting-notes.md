## License Key Formatting

**Problem Link:** https://leetcode.com/problems/license-key-formatting/description

**Problem Statement:**
- Input format: a string `S` containing alphanumeric characters and hyphens, and an integer `K`.
- Constraints: `S` consists of uppercase and lowercase letters, digits, and hyphens, and `K` is between 2 and 10 (inclusive).
- Expected output format: a formatted string where all hyphens are removed and the string is divided into groups of `K` characters separated by hyphens.
- Key requirements: 
    1. The first group should have a length of `x` where `x` is the remainder of the total length of `S` (excluding hyphens) divided by `K`.
    2. All subsequent groups should have a length of `K`.
- Edge cases to consider: 
    1. Empty string `S`.
    2. `K` is larger than the length of `S` (excluding hyphens).
    3. `S` contains only hyphens.
- Example test cases with explanations:
    1. `S = "2-4A0r7-4k", K = 4`, expected output: `"24A0-R74K"`.
    2. `S = "5F3Z-2e-9-w", K = 4`, expected output: `"5F3Z-2E9W"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Remove all hyphens from the string `S`, then iterate over the resulting string and insert a hyphen every `K` characters.
- Step-by-step breakdown of the solution:
    1. Remove all hyphens from `S`.
    2. Calculate the length of the first group `x`.
    3. Initialize an empty result string `result`.
    4. Iterate over the characters in `S` and add them to `result`.
    5. Every `K` characters, add a hyphen to `result`.
- Why this approach comes to mind first: It is straightforward and easy to understand, making it a good starting point.

```cpp
string licenseKeyFormatting(string S, int K) {
    string s = "";
    for (char c : S) {
        if (c != '-') {
            s += toupper(c);
        }
    }
    int n = s.length();
    int x = n % K;
    string result = "";
    for (int i = 0; i < n; i++) {
        result += s[i];
        if ((i + 1) % K == 0 && i != n - 1) {
            result += "-";
        }
    }
    if (x == 0) {
        result = s.substr(0, K) + "-" + result.substr(K);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `S`, because we iterate over `S` twice.
> - **Space Complexity:** $O(n)$ because we create a new string `s` and a new string `result`.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each character in `S`. The space complexity is also linear because we create new strings that can be as large as `S`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of removing all hyphens and then adding them back in, we can build the result string from left to right, adding hyphens as needed.
- Detailed breakdown of the approach:
    1. Initialize an empty result string `result`.
    2. Initialize a counter `count` to keep track of the number of characters in the current group.
    3. Iterate over the characters in `S` from left to right.
    4. If the character is not a hyphen, add it to `result` and increment `count`.
    5. If `count` equals `K`, add a hyphen to `result` and reset `count` to 0.
- Proof of optimality: This approach has the same time complexity as the brute force approach but avoids the need to create a temporary string without hyphens, making it more efficient in terms of space.

```cpp
string licenseKeyFormatting(string S, int K) {
    string result = "";
    int count = 0;
    for (int i = S.length() - 1; i >= 0; i--) {
        if (S[i] != '-') {
            if (count == K) {
                result = "-" + result;
                count = 0;
            }
            result = toupper(S[i]) + result;
            count++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `S`, because we iterate over `S` once.
> - **Space Complexity:** $O(n)$ because we create a new string `result`.
> - **Optimality proof:** This is the optimal solution because we only iterate over `S` once and avoid creating unnecessary temporary strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, iteration, and conditional statements.
- Problem-solving patterns identified: building a result string from left to right and using counters to keep track of group sizes.
- Optimization techniques learned: avoiding unnecessary temporary strings and iterating over input strings only once.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, such as empty strings or strings with only hyphens.
- Edge cases to watch for: strings with lengths that are not multiples of `K`, strings with leading or trailing hyphens.
- Performance pitfalls: creating unnecessary temporary strings or iterating over input strings multiple times.
- Testing considerations: testing with different input lengths, `K` values, and edge cases to ensure correctness.