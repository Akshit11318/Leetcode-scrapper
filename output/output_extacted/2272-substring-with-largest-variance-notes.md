## Substring with Largest Variance

**Problem Link:** https://leetcode.com/problems/substring-with-largest-variance/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The maximum variance of a substring of `s`.
- Key requirements and edge cases to consider: The problem requires finding the maximum variance of a substring, where variance is calculated as the difference between the frequency of the most frequent character and the least frequent character in the substring.
- Example test cases with explanations:
  - Input: `s = "abcde"`
    Output: `2`
    Explanation: The substring `"abc"` has a variance of `2`, as the frequency of `'a'` is `1` and the frequency of `'c'` is `0`.
  - Input: `s = "aaaaa"`
    Output: `0`
    Explanation: The substring `"aaaaa"` has a variance of `0`, as the frequency of `'a'` is `5` and the frequency of any other character is `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible substrings of `s`, calculate the frequency of each character in the substring, and find the maximum variance.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, calculate the frequency of each character.
  3. Find the maximum and minimum frequencies in the substring.
  4. Calculate the variance as the difference between the maximum and minimum frequencies.
  5. Update the maximum variance if the current variance is larger.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that directly addresses the problem statement.

```cpp
int maxVariance(string s) {
    int n = s.length();
    int maxVar = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            unordered_map<char, int> freq;
            for (char c : substr) {
                freq[c]++;
            }
            int maxFreq = 0, minFreq = INT_MAX;
            for (auto& pair : freq) {
                maxFreq = max(maxFreq, pair.second);
                minFreq = min(minFreq, pair.second);
            }
            maxVar = max(maxVar, maxFreq - minFreq);
        }
    }
    return maxVar;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because we generate all possible substrings ($O(n^2)$) and for each substring, we calculate the frequency of each character ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we store the frequency of each character in the substring.
> - **Why these complexities occur:** The brute force approach has high time and space complexities due to the generation of all possible substrings and the calculation of frequency for each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible substrings, we can use a sliding window approach to efficiently calculate the variance of each substring.
- Detailed breakdown of the approach:
  1. Initialize a sliding window with two pointers, `left` and `right`.
  2. Move the `right` pointer to the right and calculate the frequency of each character in the current window.
  3. Find the maximum and minimum frequencies in the current window.
  4. Calculate the variance as the difference between the maximum and minimum frequencies.
  5. Update the maximum variance if the current variance is larger.
  6. Move the `left` pointer to the right and repeat steps 2-5.
- Proof of optimality: The sliding window approach reduces the time complexity from $O(n^3)$ to $O(n^2)$, making it more efficient for large inputs.

```cpp
int maxVariance(string s) {
    int n = s.length();
    int maxVar = 0;
    for (int i = 0; i < n; i++) {
        unordered_map<char, int> freq;
        for (int j = i; j < n; j++) {
            freq[s[j]]++;
            int maxFreq = 0, minFreq = INT_MAX;
            for (auto& pair : freq) {
                maxFreq = max(maxFreq, pair.second);
                minFreq = min(minFreq, pair.second);
            }
            maxVar = max(maxVar, maxFreq - minFreq);
        }
    }
    return maxVar;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because we use a sliding window approach to efficiently calculate the variance of each substring.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we store the frequency of each character in the current window.
> - **Optimality proof:** The sliding window approach reduces the time complexity from $O(n^3)$ to $O(n^2)$, making it more efficient for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency calculation, and variance calculation.
- Problem-solving patterns identified: Using a sliding window approach to efficiently calculate the variance of each substring.
- Optimization techniques learned: Reducing the time complexity from $O(n^3)$ to $O(n^2)$ using a sliding window approach.
- Similar problems to practice: Problems that involve calculating the variance or frequency of characters in a string.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the maximum variance correctly, not handling edge cases correctly.
- Edge cases to watch for: Empty string, string with only one character, string with all characters having the same frequency.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the implementation with different inputs, including edge cases and large inputs.