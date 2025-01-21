## Merge Strings Alternately
**Problem Link:** https://leetcode.com/problems/merge-strings-alternately/description

**Problem Statement:**
- Input format and constraints: The function takes two strings `word1` and `word2` as input. The length of each string can be up to 100 characters. The strings consist of lowercase English letters.
- Expected output format: The function returns a string that is the result of merging `word1` and `word2` alternately.
- Key requirements and edge cases to consider: The function should handle cases where one string is longer than the other. In such cases, the remaining characters from the longer string should be appended to the end of the result.
- Example test cases with explanations:
  - `word1 = "abc", word2 = "pqr"`: The output should be `"apbqcr"`.
  - `word1 = "abcd", word2 = "pqr"`: The output should be `"apbqcrd"`.
  - `word1 = "ab", word2 = "pqrs"`: The output should be `"apbqrs"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through both strings simultaneously, appending characters from each string to the result in an alternating manner.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string `result` to store the merged string.
  2. Initialize two pointers, `i` and `j`, to 0 to track the current position in `word1` and `word2`, respectively.
  3. Iterate through both strings using a while loop until one of the strings is exhausted.
  4. Inside the loop, append the current character from `word1` to `result`, then increment `i`.
  5. If `j` is still within the bounds of `word2`, append the current character from `word2` to `result`, then increment `j`.
  6. After the loop, if there are remaining characters in either `word1` or `word2`, append them to `result`.

```cpp
string mergeAlternately(string word1, string word2) {
    string result = "";
    int i = 0, j = 0;
    while (i < word1.size() || j < word2.size()) {
        if (i < word1.size()) {
            result += word1[i];
            i++;
        }
        if (j < word2.size()) {
            result += word2[j];
            j++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `word1` and `word2`, respectively. This is because we are iterating through both strings once.
> - **Space Complexity:** $O(n + m)$, as we are storing the merged string in `result`.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each character in the input strings. The space complexity is also linear because the size of the output string is proportional to the total number of characters in the input strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a simple loop that iterates through both strings simultaneously, appending characters to the result in an alternating manner. This is similar to the brute force approach but is presented here as the optimal solution due to its efficiency and simplicity.
- Detailed breakdown of the approach: The approach involves using two pointers to track the current position in each string and a loop to iterate through both strings.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input strings, resulting in a time complexity of $O(n + m)$.

```cpp
string mergeAlternately(string word1, string word2) {
    string result = "";
    int i = 0, j = 0;
    while (i < word1.size() || j < word2.size()) {
        if (i < word1.size()) {
            result += word1[i];
            i++;
        }
        if (j < word2.size()) {
            result += word2[j];
            j++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `word1` and `word2`, respectively.
> - **Space Complexity:** $O(n + m)$, as we are storing the merged string in `result`.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for this problem, which is linear with respect to the total number of characters in the input strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration through strings, use of pointers, and string concatenation.
- Problem-solving patterns identified: The problem involves a simple iterative approach to merge two strings alternately.
- Optimization techniques learned: The optimal solution involves a single pass through the input strings, resulting in a time complexity of $O(n + m)$.
- Similar problems to practice: Other string manipulation problems, such as string reversal or substring extraction.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for the end of each string, resulting in out-of-bounds access.
- Edge cases to watch for: Handling cases where one string is longer than the other.
- Performance pitfalls: Using inefficient string concatenation methods, such as using the `+` operator in a loop.
- Testing considerations: Testing the function with different input strings, including empty strings and strings of varying lengths.