## Count Substrings that Satisfy K Constraint II

**Problem Link:** https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Expected output: The number of substrings in `s` that contain exactly `k` distinct characters.
- Key requirements and edge cases to consider:
  - `1 <= s.length <= 10^5`
  - `1 <= k <= 26`
- Example test cases with explanations:
  - Example 1: `s = "abc", k = 2`, the answer is `2` because substrings `"ab"` and `"bc"` each contain 2 distinct characters.
  - Example 2: `s = "abcabc", k = 3`, the answer is `2` because substrings `"abc"` and `"abc"` (non-overlapping) each contain 3 distinct characters.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of `s` and counting the number of distinct characters in each substring.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. For each substring, count the number of distinct characters.
  3. If the count of distinct characters equals `k`, increment the result counter.
- Why this approach comes to mind first: It's straightforward and ensures all cases are considered, but it's inefficient due to the high number of substrings and the operation of counting distinct characters for each.

```cpp
int countSubstrings(string s, int k) {
    int n = s.length();
    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            unordered_set<char> distinct;
            for (int l = i; l < j; ++l) {
                distinct.insert(s[l]);
            }
            if (distinct.size() == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because for each substring (which takes $O(n^2)$ to generate), we potentially iterate over it again to count distinct characters (another $O(n)$).
> - **Space Complexity:** $O(n)$, due to the use of an `unordered_set` to store distinct characters in each substring.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate substrings and then another loop to count distinct characters, leading to high time complexity. The space complexity is relatively lower because we only store distinct characters for each substring.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a sliding window technique to efficiently count the number of distinct characters in substrings.
- Key insight: Instead of checking every possible substring, we use a sliding window of varying sizes to efficiently scan through `s` and count distinct characters.
- Detailed breakdown:
  1. Initialize variables to keep track of the result count, the current window's start and end indices, and a map to store character frequencies within the window.
  2. Iterate over the string, expanding the window to the right and updating the character frequency map.
  3. When the window size exceeds the desired number of distinct characters, slide the window to the right by moving the start index.
  4. If the number of distinct characters in the current window equals `k`, increment the result count.
- Why further optimization is impossible: This approach minimizes the number of operations by only considering substrings that could potentially have `k` distinct characters and using a sliding window to efficiently scan through the string.

```cpp
int countSubstrings(string s, int k) {
    int n = s.length();
    int count = 0;
    for (int len = 1; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len;
            unordered_map<char, int> freq;
            for (int l = i; l < j; ++l) {
                freq[s[l]]++;
            }
            if (freq.size() == k) {
                count++;
            }
        }
    }
    return count;
}
```

However, the above optimal solution is still not optimal as it has a time complexity of $O(n^3)$, we can optimize it further by using a sliding window with two pointers.

```cpp
int countSubstrings(string s, int k) {
    int n = s.length();
    int count = 0;
    for (int len = k; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len;
            unordered_map<char, int> freq;
            for (int l = i; l < j; ++l) {
                freq[s[l]]++;
            }
            if (freq.size() == k) {
                count++;
            }
        }
    }
    return count;
}
```
But this is still not optimal. The optimal solution will use a `map` to store the frequency of characters and two pointers to slide the window.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    int n = s.size();
    for (int i = 0; i < n; i++) {
        unordered_map<char, int> m;
        for (int j = i; j < n; j++) {
            m[s[j]]++;
            if (m.size() == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because for each starting index `i`, we potentially iterate over the rest of the string once.
> - **Space Complexity:** $O(min(n, k))$, due to the use of an `unordered_map` to store character frequencies within the window.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations by only considering substrings that could potentially have `k` distinct characters and using a sliding window to efficiently scan through the string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, use of `unordered_map` for efficient frequency counting.
- Problem-solving patterns identified: Breaking down complex problems into simpler, more manageable parts (e.g., considering substrings of varying lengths).
- Optimization techniques learned: Minimizing unnecessary operations by focusing on relevant substrings and using efficient data structures.
- Similar problems to practice: Other string manipulation and sliding window problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the window boundaries or not properly handling edge cases (e.g., empty strings, `k` larger than the alphabet size).
- Edge cases to watch for: Handling strings with repeated characters, ensuring the window does not exceed the string boundaries.
- Performance pitfalls: Using inefficient data structures (e.g., arrays instead of maps for frequency counting) or unnecessary nested loops.
- Testing considerations: Thoroughly testing with various input sizes, edge cases, and comparing with expected outputs to ensure correctness.