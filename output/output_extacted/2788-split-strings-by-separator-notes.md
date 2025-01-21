## Split Strings by Separator
**Problem Link:** https://leetcode.com/problems/split-strings-by-separator/description

**Problem Statement:**
- Input: A string `s` and a separator `sep`.
- Expected output: Split the string `s` into a list of substrings using `sep` as the separator.
- Key requirements: Handle edge cases such as an empty string or a separator that is not found in the string.
- Example test cases: 
  - `s = "hello world", sep = " "` should return `["hello", "world"]`.
  - `s = "hello", sep = " "` should return `["hello"]`.
  - `s = "", sep = " "` should return `[""]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a loop to iterate over the string and find the separator.
- Step-by-step breakdown:
  1. Initialize an empty list to store the substrings.
  2. Initialize two pointers, `start` and `end`, to the beginning of the string.
  3. Loop until `end` reaches the end of the string.
  4. Check if the substring from `start` to `end` matches the separator.
  5. If it does, add the substring from `start` to the index before the separator to the list and move `start` to the index after the separator.
  6. If `end` reaches the end of the string, add the remaining substring to the list.
- Why this approach comes to mind first: It's a straightforward approach that uses basic string manipulation techniques.

```cpp
vector<string> splitString(string s, string sep) {
    vector<string> result;
    int start = 0;
    int end = 0;
    while (end < s.size()) {
        if (s.substr(end, sep.size()) == sep) {
            result.push_back(s.substr(start, end - start));
            start = end + sep.size();
            end += sep.size();
        } else {
            end++;
        }
    }
    if (start < s.size()) {
        result.push_back(s.substr(start));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the string and $m$ is the length of the separator, because in the worst case, we need to compare every character in the string with the separator.
> - **Space Complexity:** $O(n)$, because in the worst case, we need to store every character in the string as a separate substring.
> - **Why these complexities occur:** The brute force approach uses nested loops and string comparisons, which lead to high time complexity. The space complexity is high because we need to store all the substrings in the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use the `find` method of the `string` class to find the separator in the string.
- Detailed breakdown:
  1. Initialize an empty list to store the substrings.
  2. Initialize a pointer `start` to the beginning of the string.
  3. Use the `find` method to find the separator in the string, starting from `start`.
  4. If the separator is found, add the substring from `start` to the index before the separator to the list and move `start` to the index after the separator.
  5. If the separator is not found, add the remaining substring to the list.
- Why further optimization is impossible: This approach uses the most efficient method to find the separator in the string, which is the `find` method.

```cpp
vector<string> splitString(string s, string sep) {
    vector<string> result;
    size_t start = 0;
    size_t pos = s.find(sep);
    while (pos != string::npos) {
        result.push_back(s.substr(start, pos - start));
        start = pos + sep.size();
        pos = s.find(sep, start);
    }
    result.push_back(s.substr(start));
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because the `find` method has a linear time complexity.
> - **Space Complexity:** $O(n)$, because in the worst case, we need to store every character in the string as a separate substring.
> - **Optimality proof:** This approach uses the most efficient method to find the separator in the string, which is the `find` method. Therefore, it has the optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: String manipulation, separator finding, and substring extraction.
- Problem-solving patterns: Using the `find` method to find a separator in a string.
- Optimization techniques: Using the most efficient method to find the separator in the string.

**Mistakes to Avoid:**
- Not checking for edge cases such as an empty string or a separator that is not found in the string.
- Not using the most efficient method to find the separator in the string.
- Not handling the remaining substring after the last separator is found.