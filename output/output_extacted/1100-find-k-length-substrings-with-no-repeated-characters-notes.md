## Find K-Length Substrings With No Repeated Characters

**Problem Link:** https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= s.length <= 100`.
- Expected Output: A list of all substrings of length `k` that do not have any repeated characters.
- Key Requirements: Find all substrings of `s` with length `k` that have no repeated characters.
- Edge Cases: Empty string, `k` larger than the string length, `k` equals to 1.

**Example Test Cases:**
- Input: `s = "abc", k = 2`, Output: `["ab","bc"]`.
- Input: `s = "abc", k = 3`, Output: `["abc"]`.
- Input: `s = "aa", k = 1`, Output: `["a"]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought is to generate all possible substrings of length `k` and check each one for repeated characters.
- Iterate through the string `s` and for each starting position, extract a substring of length `k`.
- Check each substring for repeated characters by iterating through it and comparing each character with the others.
- If a substring has no repeated characters, add it to the result list.

```cpp
vector<string> findSubstrings(string s, int k) {
    vector<string> result;
    for (int i = 0; i <= s.length() - k; i++) {
        string substring = s.substr(i, k);
        bool hasRepeated = false;
        for (int j = 0; j < k; j++) {
            for (int m = j + 1; m < k; m++) {
                if (substring[j] == substring[m]) {
                    hasRepeated = true;
                    break;
                }
            }
            if (hasRepeated) break;
        }
        if (!hasRepeated) result.push_back(substring);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k^2)$, where $n$ is the length of string `s`. This is because for each of the $n-k+1$ substrings, we are checking for repeated characters in $O(k^2)$ time.
> - **Space Complexity:** $O(n \cdot k)$, for storing the result substrings.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate substrings and check for repeated characters, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a sliding window technique combined with an unordered set to efficiently check for repeated characters in substrings.
- Initialize a set to store unique characters in the current window.
- Iterate through the string, expanding the window to the right and adding characters to the set.
- When the window size equals `k`, check if the set size also equals `k`. If it does, it means there are no repeated characters in the current window, so add the substring to the result.
- Then, slide the window to the right by removing the leftmost character from the set and adding the next character to the right.

```cpp
vector<string> findSubstrings(string s, int k) {
    vector<string> result;
    unordered_set<char> window;
    for (int i = 0; i < s.length(); i++) {
        window.clear();
        for (int j = i; j < s.length(); j++) {
            if (window.find(s[j]) != window.end()) break;
            window.insert(s[j]);
            if (j - i + 1 == k) {
                result.push_back(s.substr(i, k));
                break;
            }
        }
    }
    return result;
}
```

However, a more optimal solution can be achieved by using two pointers to represent the sliding window and maintaining a set of characters within the window.

```cpp
vector<string> findSubstrings(string s, int k) {
    vector<string> result;
    unordered_set<char> window;
    for (int i = 0; i <= s.length() - k; i++) {
        window.clear();
        for (int j = i; j < i + k; j++) {
            if (window.find(s[j]) != window.end()) break;
            window.insert(s[j]);
            if (j == i + k - 1) {
                result.push_back(s.substr(i, k));
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of string `s`. This is because for each starting position, we potentially iterate through `k` characters.
> - **Space Complexity:** $O(k)$, for storing the set of characters in the window.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to check for repeated characters in substrings of length `k`, using a sliding window and a set for efficient lookups.

---

### Final Notes

**Learning Points:**
- The importance of using efficient data structures like unordered sets for fast lookups.
- Applying the sliding window technique to reduce the number of iterations.
- Optimizing the solution by minimizing unnecessary operations.

**Mistakes to Avoid:**
- Not considering edge cases such as empty strings or `k` larger than the string length.
- Not optimizing the solution for repeated character checks.
- Not using the most efficient data structures for the problem.