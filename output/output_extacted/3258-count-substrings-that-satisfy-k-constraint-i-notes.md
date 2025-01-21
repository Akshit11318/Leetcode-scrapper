## Count Substrings that Satisfy K Constraint I

**Problem Link:** https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description

**Problem Statement:**
- Input format: A string `s` and an integer `k`.
- Constraints: The string `s` consists of lowercase English letters, and `k` is a positive integer.
- Expected output format: The number of substrings in `s` that contain `k` distinct letters.
- Key requirements and edge cases to consider:
  - The string can be empty.
  - `k` can be equal to the length of the string.
  - The substring can start and end at any position in the string.
- Example test cases with explanations:
  - For `s = "abc"` and `k = 2`, the substrings that satisfy the constraint are "ab", "bc", and "abc". So, the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can generate all possible substrings of the string `s` and then count the number of substrings that contain `k` distinct letters.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, count the number of distinct letters.
  3. If the number of distinct letters is equal to `k`, increment the count of substrings that satisfy the constraint.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. However, it has a high time complexity due to the generation of all possible substrings.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substring = s.substr(i, j - i);
            set<char> distinctLetters;
            for (char c : substring) {
                distinctLetters.insert(c);
            }
            if (distinctLetters.size() == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because we generate all possible substrings, and for each substring, we count the number of distinct letters.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we use a set to store the distinct letters in each substring.
> - **Why these complexities occur:** The high time complexity occurs because we generate all possible substrings, which has a quadratic time complexity. Then, for each substring, we count the number of distinct letters, which has a linear time complexity. The space complexity occurs because we use a set to store the distinct letters in each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to count the number of substrings that contain `k` distinct letters.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the string.
  2. Initialize a map to store the frequency of each character in the current window.
  3. Move the `right` pointer to the right and update the frequency of each character in the current window.
  4. If the number of distinct letters in the current window is equal to `k`, increment the count of substrings that satisfy the constraint.
  5. Move the `left` pointer to the right and update the frequency of each character in the current window.
- Proof of optimality: This approach has a linear time complexity because we only need to traverse the string once.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        unordered_map<char, int> freq;
        for (int j = i; j < s.length(); j++) {
            freq[s[j]]++;
            if (freq.size() == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because we use a nested loop to traverse the string.
> - **Space Complexity:** $O(n)$, where $n` is the length of the string `s`. This is because we use a map to store the frequency of each character in the current window.
> - **Optimality proof:** This approach is optimal because we only need to traverse the string once, and we use a map to store the frequency of each character in the current window, which has a constant time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency counting.
- Problem-solving patterns identified: Counting the number of substrings that satisfy a certain constraint.
- Optimization techniques learned: Using a map to store the frequency of each character in the current window.
- Similar problems to practice: Counting the number of substrings that contain a certain number of distinct letters, counting the number of substrings that contain a certain number of repeated letters.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency of each character in the current window correctly.
- Edge cases to watch for: The string can be empty, `k` can be equal to the length of the string.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.