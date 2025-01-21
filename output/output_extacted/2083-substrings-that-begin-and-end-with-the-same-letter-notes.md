## Substrings That Begin and End with the Same Letter

**Problem Link:** https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/description

**Problem Statement:**
- Input: A string `s` containing only lowercase English letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output: An array of integers representing the number of substrings that begin and end with the same letter for each possible letter.
- Key requirements and edge cases:
  - Handle all lowercase English letters.
  - Consider substrings of all lengths.
  - Include single-character substrings.
- Example test cases:
  - For input `s = "abc"`, the output should be `[1, 1, 1]` because there is one substring that begins and ends with 'a' ("a"), one with 'b' ("b"), and one with 'c' ("c").
  - For input `s = "aba"`, the output should be `[2, 0, 0]` because there are two substrings that begin and end with 'a' ("a" and "aba"), none with 'b', and none with 'c'.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of the input string `s`.
- For each substring, check if the first and last characters are the same.
- Count the number of substrings that satisfy this condition for each letter.

```cpp
vector<int> countSubstrings(string s) {
    vector<int> counts(26, 0); // Initialize counts for each letter
    int n = s.size();
    
    // Iterate over all possible substrings
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            string substr = s.substr(i, j - i + 1);
            if (substr[0] == substr.back()) {
                counts[substr[0] - 'a']++; // Increment count for the corresponding letter
            }
        }
    }
    
    return counts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because for each of the $n$ characters, we are generating up to $n$ substrings, and for each substring, we are checking if the first and last characters match, which takes constant time but is done within a loop that runs $n$ times.
> - **Space Complexity:** $O(n)$ for the substrings generated, but the space complexity of the output is $O(1)$ since we are always returning an array of size 26.
> - **Why these complexities occur:** The cubic time complexity comes from the nested loops that generate all substrings and then check each one. The linear space complexity for the substrings is due to the `substr` function call, which creates a new string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to avoid generating all substrings and instead count the occurrences of each letter as we iterate through the string.
- We can achieve this by iterating through the string with two pointers, one starting from the beginning and one from the end of the potential substring.
- This approach significantly reduces the time complexity by avoiding the generation of all substrings.

```cpp
vector<int> countSubstrings(string s) {
    vector<int> counts(26, 0); // Initialize counts for each letter
    int n = s.size();
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (s[i] == s[j]) {
                counts[s[i] - 'a']++; // Increment count for the corresponding letter
            }
        }
    }
    
    return counts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because we are iterating over the string with two nested loops, each of which runs up to $n$ times.
> - **Space Complexity:** $O(1)$, because we are using a fixed-size array to store the counts, regardless of the input size.
> - **Optimality proof:** This is optimal because we must at least read the input string once, which takes $O(n)$ time. Since we are counting substrings, which can be quadratic in the number of characters, an $O(n^2)$ time complexity is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: substring generation, iteration, and counting.
- Problem-solving patterns identified: reducing time complexity by avoiding unnecessary operations (like generating all substrings).
- Optimization techniques learned: using two pointers to efficiently compare characters in a string.
- Similar problems to practice: other string manipulation and counting problems.

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, forgetting to initialize counts, or not checking for edge cases.
- Edge cases to watch for: empty strings, strings with only one character, and strings with all characters being the same.
- Performance pitfalls: generating all substrings without considering the impact on time complexity.
- Testing considerations: ensure to test with strings of varying lengths and compositions to cover all possible scenarios.