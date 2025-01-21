## Maximum Number of Vowels in a Substring of Given Length
**Problem Link:** https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description

**Problem Statement:**
- Input format: A string `s` and an integer `k`.
- Constraints: `1 <= k <= s.length <= 5 * 10^4`, `s` consists of lowercase English letters.
- Expected output format: The maximum number of vowels in a substring of length `k`.
- Key requirements: Find the maximum number of vowels in any substring of `s` with length `k`.
- Example test cases:
  - Input: `s = "abciiidef", k = 3`
    - Output: `3`
    - Explanation: The substring `"iiidef"` contains 3 vowels.
  - Input: `s = "aeiou", k = 2`
    - Output: `2`
    - Explanation: The substring `"aeiou"` contains 2 vowels.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible substrings of length `k` from `s` and count the vowels in each substring.
- Step-by-step breakdown:
  1. Iterate over the string `s` with a sliding window of size `k`.
  2. For each substring, count the number of vowels.
  3. Keep track of the maximum count of vowels seen so far.
- Why this approach comes to mind first: It's a straightforward way to ensure we don't miss any substrings.

```cpp
int maxVowels(string s, int k) {
    int maxCount = 0;
    for (int i = 0; i <= s.length() - k; i++) {
        int vowelCount = 0;
        for (int j = i; j < i + k; j++) {
            if (s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u') {
                vowelCount++;
            }
        }
        maxCount = max(maxCount, vowelCount);
    }
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the string `s`. This is because for each of the $n - k + 1$ substrings, we are potentially checking all $k$ characters.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum count and the current vowel count.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity. The space complexity is low because we only need a few variables to keep track of the counts.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of counting vowels for each substring from scratch, we can use a sliding window approach to efficiently update the vowel count as we move the window.
- Detailed breakdown:
  1. Initialize a set of vowels for quick lookup.
  2. Initialize the window boundaries and the vowel count within the window.
  3. Move the window to the right, updating the vowel count by adding the vowel count of the new character entering the window and subtracting the vowel count of the character leaving the window.
  4. Keep track of the maximum vowel count seen.
- Proof of optimality: This approach ensures we only need to traverse the string once, resulting in a linear time complexity with respect to the length of the string.

```cpp
int maxVowels(string s, int k) {
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    int maxCount = 0, currentCount = 0;
    for (int i = 0; i < s.length(); i++) {
        if (vowels.find(s[i]) != vowels.end()) {
            currentCount++;
        }
        if (i >= k && vowels.find(s[i - k]) != vowels.end()) {
            currentCount--;
        }
        if (i >= k - 1) {
            maxCount = max(maxCount, currentCount);
        }
    }
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, since the space used does not grow with the size of the input string (the set of vowels is constant).
> - **Optimality proof:** The linear time complexity is optimal because we must at least read the input string once to find the maximum number of vowels in any substring of length `k`.

---

### Final Notes
**Learning Points:**
- The importance of the sliding window technique in string problems.
- How to efficiently update counts within a moving window.
- The trade-off between time and space complexity.

**Mistakes to Avoid:**
- Not considering the sliding window approach for string problems involving substrings.
- Failing to optimize the vowel lookup by using a set.
- Not properly updating the counts when moving the window.