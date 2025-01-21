## Minimum Unique Word Abbreviation

**Problem Link:** https://leetcode.com/problems/minimum-unique-word-abbreviation/description

**Problem Statement:**
- Input format and constraints: Given a list of words and a target word, find the shortest unique abbreviation of the target word.
- Expected output format: The length of the shortest unique abbreviation.
- Key requirements and edge cases to consider: The abbreviation must be unique among all words in the list.
- Example test cases with explanations:
  - Input: `["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]`, target word: `"interval"`
  - Output: `6`
  - Explanation: The shortest unique abbreviation of `"interval"` is `"i6l"`, which has a length of `6`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible abbreviations of the target word and check if they are unique among all words in the list.
- Step-by-step breakdown of the solution:
  1. Generate all possible abbreviations of the target word.
  2. For each abbreviation, check if it is unique among all words in the list.
  3. Keep track of the shortest unique abbreviation found.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
#include <vector>
#include <string>
#include <unordered_set>

int minAbbreviation(std::vector<std::string>& words, std::string target) {
    int n = target.size();
    std::unordered_set<std::string> set(words.begin(), words.end());
    int minLen = INT_MAX;

    for (int mask = 0; mask < (1 << n); mask++) {
        std::string abbrev;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
                abbrev += target[i];
            } else {
                count++;
            }
        }
        if (count > 0) {
            abbrev += std::to_string(count);
        }

        bool unique = true;
        for (const auto& word : set) {
            if (word != target && abbreviationMatch(word, abbrev)) {
                unique = false;
                break;
            }
        }

        if (unique) {
            minLen = std::min(minLen, abbrev.size());
        }
    }

    return minLen;
}

bool abbreviationMatch(const std::string& word, const std::string& abbrev) {
    int i = 0, j = 0;
    while (i < word.size() && j < abbrev.size()) {
        if (abbrev[j] >= 'a' && abbrev[j] <= 'z') {
            if (word[i] != abbrev[j]) {
                return false;
            }
            i++;
            j++;
        } else {
            int count = 0;
            while (j < abbrev.size() && abbrev[j] >= '0' && abbrev[j] <= '9') {
                count = count * 10 + (abbrev[j] - '0');
                j++;
            }
            i += count;
        }
    }
    return i == word.size() && j == abbrev.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot n)$, where $n$ is the length of the target word and $m$ is the number of words in the list. The reason is that we generate all possible abbreviations of the target word, which takes $O(2^n)$ time, and then check if each abbreviation is unique among all words in the list, which takes $O(m \cdot n)$ time.
> - **Space Complexity:** $O(m)$, where $m$ is the number of words in the list. The reason is that we store all words in a set.
> - **Why these complexities occur:** The time complexity occurs because we use a brute force approach to generate all possible abbreviations of the target word. The space complexity occurs because we store all words in a set.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a bitmask to generate all possible abbreviations of the target word and use a set to store all words in the list.
- Detailed breakdown of the approach:
  1. Generate all possible abbreviations of the target word using a bitmask.
  2. For each abbreviation, check if it is unique among all words in the list.
  3. Keep track of the shortest unique abbreviation found.
- Proof of optimality: This approach is optimal because it generates all possible abbreviations of the target word and checks if each abbreviation is unique among all words in the list.

```cpp
int minAbbreviation(std::vector<std::string>& words, std::string target) {
    int n = target.size();
    std::unordered_set<std::string> set(words.begin(), words.end());
    int minLen = INT_MAX;

    for (int mask = 0; mask < (1 << n); mask++) {
        std::string abbrev;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
                abbrev += target[i];
            } else {
                count++;
            }
        }
        if (count > 0) {
            abbrev += std::to_string(count);
        }

        bool unique = true;
        for (const auto& word : set) {
            if (word != target && abbreviationMatch(word, abbrev)) {
                unique = false;
                break;
            }
        }

        if (unique) {
            minLen = std::min(minLen, abbrev.size());
        }
    }

    return minLen;
}

bool abbreviationMatch(const std::string& word, const std::string& abbrev) {
    int i = 0, j = 0;
    while (i < word.size() && j < abbrev.size()) {
        if (abbrev[j] >= 'a' && abbrev[j] <= 'z') {
            if (word[i] != abbrev[j]) {
                return false;
            }
            i++;
            j++;
        } else {
            int count = 0;
            while (j < abbrev.size() && abbrev[j] >= '0' && abbrev[j] <= '9') {
                count = count * 10 + (abbrev[j] - '0');
                j++;
            }
            i += count;
        }
    }
    return i == word.size() && j == abbrev.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot n)$, where $n$ is the length of the target word and $m$ is the number of words in the list. The reason is that we generate all possible abbreviations of the target word, which takes $O(2^n)$ time, and then check if each abbreviation is unique among all words in the list, which takes $O(m \cdot n)$ time.
> - **Space Complexity:** $O(m)$, where $m$ is the number of words in the list. The reason is that we store all words in a set.
> - **Optimality proof:** This approach is optimal because it generates all possible abbreviations of the target word and checks if each abbreviation is unique among all words in the list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: bitmask, set, and string manipulation.
- Problem-solving patterns identified: generating all possible solutions and checking if each solution is valid.
- Optimization techniques learned: using a set to store all words in the list and using a bitmask to generate all possible abbreviations of the target word.
- Similar problems to practice: problems involving string manipulation and set operations.

**Mistakes to Avoid:**
- Common implementation errors: not checking if each abbreviation is unique among all words in the list.
- Edge cases to watch for: handling cases where the target word is empty or where the list of words is empty.
- Performance pitfalls: using a brute force approach to generate all possible abbreviations of the target word without using a bitmask.
- Testing considerations: testing the function with different inputs, including edge cases.