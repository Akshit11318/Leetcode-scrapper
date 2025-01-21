## Sum of Scores of Built Strings

**Problem Link:** https://leetcode.com/problems/sum-of-scores-of-built-strings/description

**Problem Statement:**
- Input: A list of strings `words`.
- Output: The sum of scores of all strings that can be built from the characters in `words`.
- Key requirements: 
  - Each character in a string can only be used once.
  - The score of a string is the length of the string.
- Example test cases:
  - Input: `["cat","cat","cat","dog","dog","dog"]`
  - Output: `3 + 3 + 3 + 3 + 3 + 3 = 18`
  - Explanation: Each string has a score of 3 because it has 3 characters.

---

### Brute Force Approach

**Explanation:**
- Generate all permutations of characters from the input strings.
- For each permutation, check if it forms a valid string that can be built from the characters in `words`.
- Calculate the score of each valid string and sum them up.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int calculateScore(std::vector<std::string>& words) {
    int totalScore = 0;
    for (int mask = 0; mask < (1 << words.size()); mask++) {
        std::string str;
        for (int i = 0; i < words.size(); i++) {
            if (mask & (1 << i)) {
                str += words[i];
            }
        }
        std::sort(str.begin(), str.end());
        std::string uniqueStr;
        for (char c : str) {
            if (uniqueStr.find(c) == std::string::npos) {
                uniqueStr += c;
            }
        }
        if (uniqueStr.size() == str.size()) {
            totalScore += str.size();
        }
    }
    return totalScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m \cdot log(m))$, where $n$ is the number of strings and $m$ is the maximum length of a string. The reason is that we generate all subsets of strings, and for each subset, we sort the characters.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. The reason is that we store the characters of each subset of strings.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible subsets of strings and checks each subset. The space complexity is high because we store the characters of each subset.

---

### Optimal Approach (Required)

**Explanation:**
- Count the frequency of each character across all strings.
- For each character, calculate the number of strings that can be built using this character.
- Calculate the score of each string by multiplying the length of the string by the number of strings that can be built using the characters in the string.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

int maxScoreWords(std::vector<std::string>& words) {
    std::unordered_map<char, int> charCount;
    for (const std::string& word : words) {
        for (char c : word) {
            charCount[c]++;
        }
    }
    int totalScore = 0;
    for (const std::string& word : words) {
        int score = 0;
        std::unordered_map<char, int> wordCharCount;
        for (char c : word) {
            wordCharCount[c]++;
        }
        for (const auto& pair : wordCharCount) {
            score += std::min(charCount[pair.first], pair.second);
        }
        totalScore += score;
    }
    return totalScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. The reason is that we iterate over each character in each string twice.
> - **Space Complexity:** $O(m)$, where $m$ is the size of the character set. The reason is that we store the frequency of each character.
> - **Optimality proof:** This approach is optimal because it only iterates over each character in each string twice, and it uses a hash map to store the frequency of each character. This reduces the time complexity from exponential to linear.

---

### Final Notes

**Learning Points:**
- Counting the frequency of each character is a useful technique for solving string problems.
- Using a hash map to store the frequency of each character can reduce the time complexity of the solution.
- The optimal approach is often the one that has the lowest time complexity.

**Mistakes to Avoid:**
- Generating all permutations of characters is not necessary and can lead to high time complexity.
- Not using a hash map to store the frequency of each character can lead to high time complexity.
- Not considering the frequency of each character can lead to incorrect results.