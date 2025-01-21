## Decoded String at Index
**Problem Link:** https://leetcode.com/problems/decoded-string-at-index/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 30`, `s` consists of lowercase letters and digits, `k` is between `1` and `10^9`.
- Expected Output: The `k-th` letter in the decoded string.
- Key Requirements: Decode the string `s` by repeating the substring between `(` and `)` `n` times, where `n` is the number preceding the `(`.
- Edge Cases: When `k` exceeds the length of the decoded string, or when `s` contains no `(` or `)`.

**Example Test Cases:**
- `s = "leet2code3", k = 10`, Output: `"o"`
- `s = "ha22", k = 5`, Output: `"h"`
- `s = "a2345678999999999999999", k = 1`, Output: `"a"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves decoding the entire string `s` and then finding the `k-th` letter.
- This approach involves scanning `s` character by character, decoding any repeated substrings as encountered.
- It comes to mind first because it directly addresses the decoding requirement without considering efficiency.

```cpp
string decodeAtIndex(string s, int k) {
    string res;
    for (char c : s) {
        if (isdigit(c)) {
            int repeat = c - '0';
            string temp = res;
            for (int i = 1; i < repeat; ++i) {
                res += temp;
                if (res.length() >= k) break;
            }
        } else {
            res += c;
        }
        if (res.length() >= k) break;
    }
    return string(1, res[k - 1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `s` and $m$ is the average repetition factor. This is because in the worst case, we might need to repeat a substring $m$ times for each character in `s`.
> - **Space Complexity:** $O(n \cdot m)$, as we are storing the decoded string which can grow up to $n \cdot m$ in length.
> - **Why these complexities occur:** The brute force approach involves decoding the entire string and storing it, which leads to high time and space complexities due to the potential repetition of substrings.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to work backwards from `k` and determine which repetition or character contributes to the `k-th` position without fully decoding the string.
- We calculate the length of the decoded string up to each character and its potential repetitions, then backtrack to find which part of `s` contributes to the `k-th` character.
- This approach avoids unnecessary decoding and storage, significantly improving efficiency.

```cpp
string decodeAtIndex(string s, int k) {
    long long size = 0; // Use long long to avoid overflow
    for (char c : s) {
        if (isdigit(c)) {
            size *= (c - '0');
        } else {
            size++;
        }
    }

    for (int i = s.size() - 1; i >= 0; --i) {
        char c = s[i];
        if (isdigit(c)) {
            size /= (c - '0');
            k %= size;
            if (k == 0) {
                // If k is 0, it means the current repetition includes the k-th character
                // So, we need to find the k-th character in the substring before the current repetition
                return decodeAtIndex(s.substr(i + 1), k);
            }
        } else {
            if (k == size) {
                // If k equals the current size, it means the current character is the k-th character
                return string(1, c);
            }
            size--;
        }
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we make a single pass through `s` to calculate the length of the decoded string and then potentially another pass backwards to find the `k-th` character.
> - **Space Complexity:** $O(n)$, due to the recursive call stack in the worst case.
> - **Optimality proof:** This approach is optimal because it minimizes the amount of decoding required to find the `k-th` character, avoiding unnecessary computations and storage.

---

### Final Notes

**Learning Points:**
- The importance of working backwards or using reverse iteration in certain problems to avoid unnecessary computations.
- How to handle potential overflows by using larger data types like `long long`.
- The technique of calculating the length of the decoded string without actually decoding it to guide the search for the `k-th` character.

**Mistakes to Avoid:**
- Not considering the potential for overflow when calculating the length of the decoded string.
- Fully decoding the string without considering more efficient approaches.
- Not properly handling the case where `k` is exactly divisible by the size of a repeated substring.