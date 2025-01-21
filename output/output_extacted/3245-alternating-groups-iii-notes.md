## Alternating Groups III
**Problem Link:** https://leetcode.com/problems/alternating-groups-iii/description

**Problem Statement:**
- Given a binary string `s` of length `n`, find the maximum length of an alternating group.
- The string `s` only contains `0` and `1`.
- An alternating group is a group of consecutive characters that alternate between `0` and `1`.
- For example, `010` or `101` are alternating groups.
- The input string `s` is guaranteed to be non-empty.
- Expected output is the maximum length of an alternating group.

**Example Test Cases:**
- Input: `s = "10101"`
  Output: `5`
- Input: `s = "1111"`
  Output: `1`
- Input: `s = "0000"`
  Output: `1`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to check every possible substring of `s` to see if it forms an alternating group.
- We then keep track of the maximum length of such groups found.
- This approach comes to mind first because it directly addresses the requirement of finding alternating groups within the string.

```cpp
int maxAlternatingGroup(string s) {
    int n = s.length();
    int maxLength = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substring = s.substr(i, j - i);
            bool isAlternating = true;
            for (int k = 1; k < substring.length(); k++) {
                if (substring[k] == substring[k - 1]) {
                    isAlternating = false;
                    break;
                }
            }
            if (isAlternating) {
                maxLength = max(maxLength, (int)substring.length());
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because for each of the $n$ starting positions, we potentially generate $n$ substrings and check each of them in $O(n)$ time.
> - **Space Complexity:** $O(n)$, due to the creation of substrings.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate all possible substrings and then checks each one to see if it's an alternating group, leading to high time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to realize that an alternating group can be extended as long as the next character is different from the last character in the group.
- We can iterate through the string once, keeping track of the current group's length and the maximum length seen so far.
- If the current character is different from the previous one, we extend the current group. Otherwise, we start a new group.
- This approach is optimal because it only requires a single pass through the string.

```cpp
int maxAlternatingGroup(string s) {
    int n = s.length();
    if (n == 0) return 0;
    
    int maxLength = 1;
    int currentLength = 1;
    
    for (int i = 1; i < n; i++) {
        if (s[i] != s[i - 1]) {
            currentLength++;
            maxLength = max(maxLength, currentLength);
        } else {
            currentLength = 1;
        }
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our variables.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the maximum length of an alternating group, only needing to iterate through the string once.

---

### Final Notes
**Learning Points:**
- The importance of recognizing patterns in strings, such as alternating characters.
- How to optimize string processing algorithms by reducing the number of passes through the string.
- The use of variables to keep track of current and maximum lengths of alternating groups.

**Mistakes to Avoid:**
- Assuming that every possible substring must be checked, leading to inefficient algorithms.
- Not recognizing the alternating pattern in the string, which allows for a much simpler and efficient solution.
- Failing to initialize variables properly, such as the maximum length, which could lead to incorrect results.