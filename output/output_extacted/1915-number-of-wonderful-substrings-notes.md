## Number of Wonderful Substrings
**Problem Link:** https://leetcode.com/problems/number-of-wonderful-substrings/description

**Problem Statement:**
- Input: A string `word` containing only lowercase letters.
- Expected Output: The number of wonderful substrings in `word`. A substring is wonderful if it contains at least one of each of the characters 'a' through 'e' (inclusive).
- Key Requirements:
  - Handle substrings of varying lengths.
  - Identify the presence of all characters 'a' through 'e' in each substring.
- Edge Cases:
  - Empty string.
  - Strings containing characters outside 'a' to 'e'.
  - Strings with length less than 5.
- Example Test Cases:
  - Input: "aec"
    - Output: 0 (No substring contains all characters 'a' through 'e')
  - Input: "aabbccde"
    - Output: 1 (Substring "abcde" contains all characters)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each substring of the input string, check if it contains all the characters 'a' through 'e'.
- Step-by-step breakdown:
  1. Generate all possible substrings of the input string.
  2. For each substring, check the presence of characters 'a' through 'e'.
  3. Count the number of substrings that contain all characters 'a' through 'e'.

```cpp
int wonderfulSubstrings(string word) {
    int count = 0;
    int n = word.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = word.substr(i, j - i);
            bool found[5] = {false};
            for (char c : substr) {
                if (c >= 'a' && c <= 'e') {
                    found[c - 'a'] = true;
                }
            }
            bool isWonderful = true;
            for (bool f : found) {
                if (!f) {
                    isWonderful = false;
                    break;
                }
            }
            if (isWonderful) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. The outer two loops generate all substrings ($O(n^2)$), and the inner loop checks each character in the substring ($O(n)$).
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space to store the `found` array and other variables.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible substrings and checks each one individually, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all substrings, use a sliding window approach combined with a bitmask to efficiently track the presence of characters 'a' through 'e'.
- Detailed breakdown:
  1. Initialize a bitmask `mask` to keep track of the characters 'a' through 'e' in the current window.
  2. Iterate through the string, updating the `mask` as characters enter and leave the window.
  3. Count the number of times the `mask` indicates the presence of all characters 'a' through 'e'.

```cpp
int wonderfulSubstrings(string word) {
    int n = word.size();
    int count = 0;
    for (int mask = 0; mask < (1 << 5); mask++) {
        int freq[26] = {0};
        int windowStart = 0;
        int wonderfulCount = 0;
        for (int windowEnd = 0; windowEnd < n; windowEnd++) {
            char rightChar = word[windowEnd];
            if (rightChar >= 'a' && rightChar <= 'e') {
                freq[rightChar - 'a']++;
            }
            while (windowStart <= windowEnd && freq[rightChar - 'a'] > 1 + ((mask >> (rightChar - 'a')) & 1)) {
                char leftChar = word[windowStart];
                if (leftChar >= 'a' && leftChar <= 'e') {
                    freq[leftChar - 'a']--;
                }
                windowStart++;
            }
            bool isWonderful = true;
            for (int i = 0; i < 5; i++) {
                if ((mask >> i) & 1 && freq[i] == 0) {
                    isWonderful = false;
                    break;
                }
            }
            if (isWonderful) {
                wonderfulCount++;
            }
        }
        if (mask == (1 << 5) - 1) {
            count += wonderfulCount;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^5)$, where $n$ is the length of the input string. The outer loop iterates over all possible bitmasks ($O(2^5)$), and the inner loop iterates over the string ($O(n)$).
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space to store the `freq` array and other variables.
> - **Optimality proof:** This approach is optimal because it efficiently uses a bitmask to track the presence of characters 'a' through 'e' in the current window, reducing the time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- **Bitmasking:** Used to efficiently track the presence of characters 'a' through 'e' in the current window.
- **Sliding Window Technique:** Applied to reduce the time complexity by avoiding the generation of all possible substrings.
- **Optimization Techniques:** Demonstrated how to optimize the solution by using a bitmask and sliding window approach.

**Mistakes to Avoid:**
- **Inefficient Substring Generation:** Avoid generating all possible substrings, as this leads to high time complexity.
- **Incorrect Bitmasking:** Ensure correct usage of bitmasks to track character presence.
- **Insufficient Window Management:** Properly manage the sliding window to avoid incorrect counts.