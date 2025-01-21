## Number of Substrings Containing All Three Characters
**Problem Link:** https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description

**Problem Statement:**
- Input: A string `s` containing only lowercase letters.
- Constraints: The length of `s` is at least 3 and at most $10^5$.
- Expected Output: The number of substrings in `s` that contain all three characters 'a', 'b', and 'c'.
- Key Requirements and Edge Cases:
  - The string may contain characters other than 'a', 'b', and 'c'.
  - A substring is defined as a contiguous sequence of characters within `s`.
- Example Test Cases:
  - Input: `s = "abc"`
    - Output: `1`
    - Explanation: The only substring containing all three characters is `"abc"`.
  - Input: `s = "aaaa"`
    - Output: `0`
    - Explanation: No substring contains all three characters.

---

### Brute Force Approach
**Explanation:**
- Initial Thought Process: The most straightforward approach to solving this problem is to generate all possible substrings of `s` and check each one for the presence of 'a', 'b', and 'c'.
- Step-by-Step Breakdown:
  1. Generate all substrings of `s`.
  2. For each substring, check if it contains 'a', 'b', and 'c'.
  3. Count the substrings that satisfy the condition.

```cpp
int numberOfSubstrings(string s) {
    int count = 0;
    int n = s.length();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 3; j <= n; ++j) {
            string substr = s.substr(i, j - i);
            if (substr.find('a') != string::npos && 
                substr.find('b') != string::npos && 
                substr.find('c') != string::npos) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because for each starting position `i`, we generate substrings of varying lengths up to `n`, and for each substring, we perform a search operation that takes $O(n)$ time in the worst case.
> - **Space Complexity:** $O(n)$, primarily due to the creation of substrings.
> - **Why these complexities occur:** The brute force approach involves generating all possible substrings and performing a search operation on each, leading to high time complexity. The space complexity is relatively lower because we only store one substring at a time.

---

### Optimal Approach (Required)
**Explanation:**
- Key Insight: Instead of checking all substrings, we can use a sliding window approach to efficiently find substrings containing all three characters.
- Detailed Breakdown:
  1. Initialize a sliding window with two pointers, `left` and `right`, both at the start of `s`.
  2. Expand the window to the right by moving `right` until we find a substring containing 'a', 'b', and 'c'.
  3. Once a valid substring is found, try to minimize the window by moving `left` to the right while maintaining the presence of 'a', 'b', and 'c'.
  4. Count the number of substrings that can be formed by expanding the window to the right from the current `left` position.

```cpp
int numberOfSubstrings(string s) {
    int count = 0;
    int n = s.length();
    for (int i = 0; i < n; ++i) {
        int a = 0, b = 0, c = 0;
        for (int j = i; j < n; ++j) {
            if (s[j] == 'a') a++;
            else if (s[j] == 'b') b++;
            else if (s[j] == 'c') c++;
            if (a > 0 && b > 0 && c > 0) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because for each starting position `i`, we potentially scan the rest of the string once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counts of 'a', 'b', and 'c'.
> - **Optimality Proof:** This approach is optimal because it minimizes the number of operations required to find all substrings containing 'a', 'b', and 'c'. By iterating through the string and expanding a potential window to the right, we ensure that every substring is considered exactly once.

---

### Final Notes

**Learning Points:**
- The importance of the sliding window technique in solving string problems.
- How to optimize brute force approaches by reducing unnecessary operations.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Failing to consider all edge cases, such as an empty string or a string without 'a', 'b', or 'c'.
- Not optimizing the algorithm for large inputs, leading to performance issues.
- Incorrectly implementing the sliding window technique, resulting in missed or double-counted substrings.