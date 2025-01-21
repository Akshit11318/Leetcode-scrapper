## Count Complete Substrings
**Problem Link:** https://leetcode.com/problems/count-complete-substrings/description

**Problem Statement:**
- Input format: A string `s`.
- Constraints: The length of `s` is between 1 and 1000.
- Expected output format: The number of complete substrings in `s`.
- Key requirements and edge cases to consider:
  - A complete substring is a substring that contains all unique characters.
  - The substring can be of any length.
- Example test cases with explanations:
  - For `s = "abc"`, there are 6 complete substrings: `"a"`, `"b"`, `"c"`, `"ab"`, `"bc"`, `"abc"`.
  - For `s = "aaa"`, there are 3 complete substrings: `"a"`, `"aa"`, `"aaa"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of `s` and check if each one contains all unique characters.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if it contains all unique characters.
  3. Count the number of substrings that contain all unique characters.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it is not efficient for large inputs.

```cpp
int countCompleteSubstrings(string s) {
    int count = 0;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substring = s.substr(i, j - i);
            unordered_set<char> uniqueChars(substring.begin(), substring.end());
            if (uniqueChars.size() == substring.length()) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. The reason is that we generate all possible substrings of `s` ($O(n^2)$), and for each substring, we check if it contains all unique characters ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. The reason is that we use an `unordered_set` to store the unique characters in each substring.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it generates all possible substrings of `s` and checks each one individually.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible substrings of `s`, we can use a sliding window approach to efficiently count the number of complete substrings.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the beginning of `s`.
  2. Use an `unordered_set` to store the unique characters in the current window.
  3. Move the `right` pointer to the right and add the character at the `right` pointer to the `unordered_set`.
  4. If the size of the `unordered_set` is equal to the number of characters in the current window, increment the count of complete substrings.
  5. Move the `left` pointer to the right and remove the character at the `left` pointer from the `unordered_set`.
- Proof of optimality: The optimal approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.

```cpp
int countCompleteSubstrings(string s) {
    int count = 0;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        unordered_set<char> uniqueChars;
        for (int j = i; j < n; j++) {
            uniqueChars.insert(s[j]);
            if (uniqueChars.size() == j - i + 1) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `s`. The reason is that we use a sliding window approach to efficiently count the number of complete substrings.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. The reason is that we use an `unordered_set` to store the unique characters in the current window.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, use of `unordered_set` to store unique characters.
- Problem-solving patterns identified: Use of two pointers to efficiently traverse the string.
- Optimization techniques learned: Avoid generating all possible substrings of `s` and instead use a sliding window approach.
- Similar problems to practice: Counting the number of substrings with a given property.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the `unordered_set` is empty before accessing its elements.
- Edge cases to watch for: Handling the case where `s` is an empty string.
- Performance pitfalls: Generating all possible substrings of `s` instead of using a sliding window approach.
- Testing considerations: Testing the function with different inputs, including edge cases.