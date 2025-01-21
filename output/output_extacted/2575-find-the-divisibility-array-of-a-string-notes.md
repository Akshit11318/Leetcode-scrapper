## Find the Divisibility Array of a String

**Problem Link:** https://leetcode.com/problems/find-the-divisibility-array-of-a-string/description

**Problem Statement:**
- Input: a string `word` and an integer `m`
- Output: a boolean array `ans` of length `n`, where `ans[i]` is `true` if the prefix of `word` of length `i + 1` is divisible by `m`, and `false` otherwise
- Key requirements:
  - Handle strings of varying lengths
  - Consider divisibility by `m`
  - Produce a boolean array as output
- Edge cases:
  - Empty string
  - `m` is 1
  - `m` is a prime number

**Example Test Cases:**
- `word = "123", m = 3` => `[false, false, true]`
- `word = "1234", m = 12` => `[false, false, false, true]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all prefixes of the input string, convert each prefix to an integer, and check if it's divisible by `m`.
- This approach is straightforward but inefficient for large strings.

```cpp
vector<bool> findDivisibilityArray(string word, int m) {
    int n = word.size();
    vector<bool> ans(n);
    for (int i = 0; i < n; i++) {
        int prefix = 0;
        for (int j = 0; j <= i; j++) {
            prefix = prefix * 10 + (word[j] - '0');
            if (prefix % m == 0) {
                ans[i] = true;
                break;
            }
        }
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because for each character in the string, we potentially generate all prefixes.
> - **Space Complexity:** $O(n)$, as we need to store the boolean array of size $n$.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the space complexity is linear due to the output array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a single variable to keep track of the current prefix's value modulo `m`.
- We can avoid generating all prefixes and instead update the prefix value incrementally.

```cpp
vector<bool> findDivisibilityArray(string word, int m) {
    int n = word.size();
    vector<bool> ans(n);
    int prefix = 0;
    for (int i = 0; i < n; i++) {
        prefix = (prefix * 10 + (word[i] - '0')) % m;
        ans[i] = (prefix == 0);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, as we need to store the boolean array of size $n$.
> - **Optimality proof:** This is the optimal solution because we only need to make a single pass through the input string to generate the output array. Further optimization is impossible because we must examine each character at least once.

---

### Final Notes

**Learning Points:**
- The importance of incremental updates in avoiding redundant computations
- Using modulo arithmetic to efficiently check divisibility
- Optimizing brute force approaches by reducing unnecessary computations

**Mistakes to Avoid:**
- Generating all prefixes of the input string, leading to quadratic time complexity
- Failing to use modulo arithmetic, resulting in overflow for large inputs
- Not considering incremental updates, leading to inefficient solutions

---