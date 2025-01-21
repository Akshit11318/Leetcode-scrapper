## Maximum Score After Splitting a String

**Problem Link:** https://leetcode.com/problems/maximum-score-after-splitting-a-string/description

**Problem Statement:**
- Input: A string `s` consisting of lowercase letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected Output: The maximum score that can be achieved by splitting the string into two non-empty parts.
- Key Requirements: The score of a string is the sum of the frequencies of its most frequent character.
- Edge Cases: If the input string is empty or contains only one character, the score is 0.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible splits of the string and calculate the score for each split.
- Step-by-step breakdown:
  1. Iterate over all possible split positions in the string.
  2. For each split position, calculate the score of the left and right parts of the string.
  3. The score of a string is the sum of the frequencies of its most frequent character.
  4. Keep track of the maximum score achieved.

```cpp
class Solution {
public:
    int maxScore(string s) {
        int n = s.length();
        int maxScore = 0;
        for (int i = 1; i < n; i++) {
            string left = s.substr(0, i);
            string right = s.substr(i, n - i);
            int leftScore = getScore(left);
            int rightScore = getScore(right);
            maxScore = max(maxScore, leftScore + rightScore);
        }
        return maxScore;
    }

    int getScore(string s) {
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        int maxFreq = 0;
        for (auto& pair : freq) {
            maxFreq = max(maxFreq, pair.second);
        }
        return maxFreq;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we are iterating over all possible split positions and calculating the score for each split, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are storing the frequencies of characters in the `freq` map, which can contain up to $n$ entries in the worst case.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it tries all possible splits of the string and calculates the score for each split.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a single pass to calculate the score of the left and right parts of the string.
- Step-by-step breakdown:
  1. Initialize two arrays, `left` and `right`, to store the frequencies of characters in the left and right parts of the string.
  2. Iterate over the string from left to right, updating the `left` array and calculating the score of the left part.
  3. Iterate over the string from right to left, updating the `right` array and calculating the score of the right part.
  4. Keep track of the maximum score achieved.

```cpp
class Solution {
public:
    int maxScore(string s) {
        int n = s.length();
        int maxScore = 0;
        unordered_map<char, int> left, right;
        for (int i = 0; i < n; i++) {
            right[s[i]]++;
        }
        for (int i = 0; i < n - 1; i++) {
            left[s[i]]++;
            right[s[i]]--;
            if (right[s[i]] == 0) {
                right.erase(s[i]);
            }
            int leftScore = getScore(left);
            int rightScore = getScore(right);
            maxScore = max(maxScore, leftScore + rightScore);
        }
        return maxScore;
    }

    int getScore(unordered_map<char, int> freq) {
        int maxFreq = 0;
        for (auto& pair : freq) {
            maxFreq = max(maxFreq, pair.second);
        }
        return maxFreq;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are iterating over the string twice, once from left to right and once from right to left.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are storing the frequencies of characters in the `left` and `right` maps, which can contain up to $n$ entries in the worst case.
> - **Optimality proof:** This approach is optimal because it uses a single pass to calculate the score of the left and right parts of the string, resulting in a time complexity of $O(n)$.

### Final Notes

**Learning Points:**
- The problem demonstrates the importance of using a single pass to calculate the score of the left and right parts of the string.
- The optimal approach uses two arrays to store the frequencies of characters in the left and right parts of the string.
- The `getScore` function is used to calculate the score of a given string.

**Mistakes to Avoid:**
- Not using a single pass to calculate the score of the left and right parts of the string, resulting in a high time complexity.
- Not storing the frequencies of characters in the `left` and `right` maps, resulting in a high space complexity.
- Not keeping track of the maximum score achieved, resulting in an incorrect output.