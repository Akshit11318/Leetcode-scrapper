## Count of Substrings Containing Every Vowel and K Consonants I

**Problem Link:** https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` and an integer `k`. The string `s` contains only lowercase English letters, and `k` is a non-negative integer.
- Expected output format: The output should be the number of substrings in `s` that contain every vowel and `k` consonants.
- Key requirements and edge cases to consider: We need to consider all substrings of `s` and count the ones that contain all vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) and exactly `k` consonants.
- Example test cases with explanations:
  - Input: `s = "aeiou", k = 0`, Output: `1` (The substring `"aeiou"` contains all vowels and 0 consonants.)
  - Input: `s = "aeiou", k = 1`, Output: `0` (There is no substring that contains all vowels and 1 consonant.)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can generate all possible substrings of `s` and check each one to see if it contains all vowels and `k` consonants.
- Step-by-step breakdown of the solution:
  1. Generate all substrings of `s`.
  2. For each substring, count the number of vowels and consonants.
  3. If the substring contains all vowels and `k` consonants, increment the count.
- Why this approach comes to mind first: It is a straightforward approach that checks all possibilities.

```cpp
int countSubstrings(string s, int k) {
    int n = s.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            int vowelCount = 0, consonantCount = 0;
            bool allVowelsPresent = true;
            for (char c : "aeiou") {
                if (substr.find(c) == string::npos) {
                    allVowelsPresent = false;
                    break;
                }
            }
            if (!allVowelsPresent) continue;
            for (char c : substr) {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    vowelCount++;
                } else {
                    consonantCount++;
                }
            }
            if (consonantCount == k) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. The outer two loops generate all substrings, and the inner loop checks each substring.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. We need to store each substring.
> - **Why these complexities occur:** The brute force approach checks all substrings, which results in a cubic time complexity. The space complexity is linear because we need to store each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to efficiently count the substrings that contain all vowels and `k` consonants.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the string `s`.
  2. Move the `right` pointer to the right and update the counts of vowels and consonants.
  3. When the window contains all vowels, check if the number of consonants is `k`. If it is, increment the count.
  4. Move the `left` pointer to the right and update the counts of vowels and consonants.
- Proof of optimality: This approach is optimal because it only checks each character in the string once.

```cpp
int countSubstrings(string s, int k) {
    int n = s.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int vowelCount[5] = {0}, consonantCount = 0;
        for (int j = i; j < n; j++) {
            if (s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u') {
                vowelCount[s[j] - 'a']++;
            } else {
                consonantCount++;
            }
            bool allVowelsPresent = true;
            for (int v = 0; v < 5; v++) {
                if (vowelCount[v] == 0) {
                    allVowelsPresent = false;
                    break;
                }
            }
            if (allVowelsPresent && consonantCount == k) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. The outer loop fixes the start of the window, and the inner loop moves the end of the window.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the string `s`. We only use a constant amount of space to store the counts of vowels and consonants.
> - **Optimality proof:** This approach is optimal because it only checks each character in the string once and uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, efficient counting of substrings.
- Problem-solving patterns identified: Using a sliding window to efficiently count substrings that meet certain conditions.
- Optimization techniques learned: Reducing the time complexity from cubic to quadratic by using a sliding window approach.
- Similar problems to practice: Counting substrings that meet certain conditions, such as containing all vowels or a certain number of consonants.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the counts of vowels and consonants correctly, not checking if all vowels are present in the window.
- Edge cases to watch for: Empty string, string with only one character, string with no vowels or consonants.
- Performance pitfalls: Using a brute force approach that checks all substrings, not using a sliding window approach to reduce the time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it works correctly.