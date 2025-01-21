## Most Common Word
**Problem Link:** [https://leetcode.com/problems/most-common-word/description](https://leetcode.com/problems/most-common-word/description)

**Problem Statement:**
- Input format: a paragraph of text and a list of banned words
- Constraints: the paragraph contains only letters, spaces, and punctuation marks
- Expected output format: the most common word that is not banned
- Key requirements and edge cases to consider: 
  - Words are case-insensitive and should be compared in lower case
  - Punctuation marks should be ignored
  - If there are multiple words with the same highest frequency, return any one of them
- Example test cases with explanations:
  - For the input "Bob. hIt, baLl" and banned words ["bob", "hit"], the output should be "ball"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: remove punctuation, split the paragraph into words, and count the frequency of each word
- Step-by-step breakdown of the solution:
  1. Remove punctuation from the paragraph
  2. Split the paragraph into words
  3. Convert each word to lower case
  4. Count the frequency of each word
  5. Filter out banned words
  6. Find the word with the highest frequency
- Why this approach comes to mind first: it is a straightforward and intuitive solution

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

string mostCommonWord(string paragraph, vector<string>& banned) {
    // Remove punctuation
    for (char& c : paragraph) {
        if (!isalnum(c) && !isspace(c)) {
            c = ' ';
        }
    }

    // Split the paragraph into words
    istringstream iss(paragraph);
    vector<string> words;
    string word;
    while (iss >> word) {
        words.push_back(word);
    }

    // Convert each word to lower case
    for (string& w : words) {
        transform(w.begin(), w.end(), w.begin(), ::tolower);
    }

    // Count the frequency of each word
    unordered_map<string, int> wordCount;
    for (const string& w : words) {
        wordCount[w]++;
    }

    // Filter out banned words
    unordered_set<string> bannedSet(banned.begin(), banned.end());
    for (string& w : banned) {
        transform(w.begin(), w.end(), w.begin(), ::tolower);
    }
    for (auto it = wordCount.begin(); it != wordCount.end();) {
        if (bannedSet.count(it->first)) {
            it = wordCount.erase(it);
        } else {
            ++it;
        }
    }

    // Find the word with the highest frequency
    string mostCommon;
    int maxCount = 0;
    for (const auto& pair : wordCount) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            mostCommon = pair.first;
        }
    }

    return mostCommon;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of words in the paragraph and $m$ is the number of banned words. This is because we iterate over each word in the paragraph and each banned word.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of words in the paragraph and $m$ is the number of banned words. This is because we store each word in the paragraph and each banned word in separate data structures.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each word in the paragraph and each banned word. The space complexity occurs because we store each word in the paragraph and each banned word in separate data structures.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: use an unordered_map to count the frequency of each word and an unordered_set to store banned words
- Detailed breakdown of the approach:
  1. Remove punctuation from the paragraph
  2. Split the paragraph into words
  3. Convert each word to lower case
  4. Count the frequency of each word using an unordered_map
  5. Filter out banned words using an unordered_set
  6. Find the word with the highest frequency
- Proof of optimality: this solution has the same time complexity as the brute force approach, but it uses more efficient data structures, making it optimal

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

string mostCommonWord(string paragraph, vector<string>& banned) {
    // Remove punctuation
    for (char& c : paragraph) {
        if (!isalnum(c) && !isspace(c)) {
            c = ' ';
        }
    }

    // Split the paragraph into words
    istringstream iss(paragraph);
    vector<string> words;
    string word;
    while (iss >> word) {
        words.push_back(word);
    }

    // Convert each word to lower case
    for (string& w : words) {
        transform(w.begin(), w.end(), w.begin(), ::tolower);
    }

    // Count the frequency of each word and filter out banned words
    unordered_map<string, int> wordCount;
    unordered_set<string> bannedSet(banned.begin(), banned.end());
    for (string& w : banned) {
        transform(w.begin(), w.end(), w.begin(), ::tolower);
    }
    for (const string& w : words) {
        if (bannedSet.count(w) == 0) {
            wordCount[w]++;
        }
    }

    // Find the word with the highest frequency
    string mostCommon;
    int maxCount = 0;
    for (const auto& pair : wordCount) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            mostCommon = pair.first;
        }
    }

    return mostCommon;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of words in the paragraph and $m$ is the number of banned words. This is because we iterate over each word in the paragraph and each banned word.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of words in the paragraph and $m$ is the number of banned words. This is because we store each word in the paragraph and each banned word in separate data structures.
> - **Optimality proof:** This solution is optimal because it uses the most efficient data structures (unordered_map and unordered_set) to count the frequency of each word and filter out banned words, resulting in the minimum possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: using unordered_map and unordered_set to count the frequency of each word and filter out banned words
- Problem-solving patterns identified: removing punctuation, splitting the paragraph into words, and converting each word to lower case
- Optimization techniques learned: using efficient data structures to reduce time complexity
- Similar problems to practice: word frequency problems, string manipulation problems

**Mistakes to Avoid:**
- Common implementation errors: not removing punctuation, not converting each word to lower case, and not filtering out banned words
- Edge cases to watch for: empty paragraph, empty banned list, and words with punctuation
- Performance pitfalls: using inefficient data structures, such as arrays or linked lists, to count the frequency of each word and filter out banned words
- Testing considerations: testing with different inputs, such as paragraphs with different lengths and banned lists with different sizes.