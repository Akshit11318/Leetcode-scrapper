## Number of Valid Words in a Sentence
**Problem Link:** https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description

**Problem Statement:**
- Input: A sentence containing words with optional `*` wildcards, and a dictionary of words.
- Constraints: Sentence and dictionary words are lowercase and contain only letters and `*`.
- Expected output: The number of valid words in the sentence.
- Key requirements: Determine if each word in the sentence matches any word in the dictionary, considering `*` as a wildcard for any sequence of letters.
- Example test cases:
  - Sentence: "cat and dog", Dictionary: ["cat","dog"], Expected output: 3.
  - Sentence: "cat and dog", Dictionary: ["cat","dog","tandog"], Expected output: 3.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking each word in the sentence against each word in the dictionary, considering the wildcard `*`.
- Step-by-step breakdown:
  1. Split the sentence into words.
  2. For each word in the sentence, iterate through the dictionary.
  3. Check if the word matches any dictionary word, treating `*` as a wildcard.
- Why this approach comes to mind first: It directly addresses the problem statement by comparing each word in the sentence with each word in the dictionary.

```cpp
#include <vector>
#include <string>
#include <iostream>

bool isMatch(const std::string& word1, const std::string& word2) {
    if (word1.size() != word2.size()) return false;
    for (int i = 0; i < word1.size(); ++i) {
        if (word1[i] != '*' && word2[i] != '*' && word1[i] != word2[i]) {
            return false;
        }
    }
    return true;
}

int countValidWords(std::string sentence, std::vector<std::string>& dictionary) {
    std::istringstream iss(sentence);
    std::string word;
    int count = 0;
    while (iss >> word) {
        for (const auto& dictWord : dictionary) {
            if (isMatch(word, dictWord)) {
                count++;
                break; // Move to the next word in the sentence
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of words in the sentence, $m$ is the number of words in the dictionary, and $k$ is the average length of a word. This is because for each word in the sentence, we potentially compare it with each word in the dictionary, and the comparison itself takes time proportional to the length of the words.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, since we only use a constant amount of space to store the current word and the count of valid words.
> - **Why these complexities occur:** The time complexity is high due to the nested loop structure (each word in the sentence compared with each word in the dictionary), and the comparison operation itself depends on the length of the words.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of comparing each word in the sentence with each word in the dictionary, we can use a more efficient data structure like a `Trie` (prefix tree) to store the dictionary words. However, since the problem involves wildcards, a straightforward Trie won't work. We can still improve by using a simpler approach that leverages the fact that we're dealing with a specific set of characters (lowercase letters and `*`).
- Detailed breakdown:
  1. Preprocess the dictionary to create a set of words for efficient lookup.
  2. For each word in the sentence, iterate through the dictionary set to check for matches.
  3. To handle `*`, use a function that checks for a match between a word and a dictionary word, considering `*` as a wildcard.
- Proof of optimality: This approach is more efficient than the brute force because it reduces the time complexity of looking up dictionary words. However, the core comparison operation remains similar due to the nature of the problem (involving wildcards).

```cpp
#include <vector>
#include <string>
#include <iostream>
#include <unordered_set>

bool isMatch(const std::string& word1, const std::string& word2) {
    if (word1.size() != word2.size()) return false;
    for (int i = 0; i < word1.size(); ++i) {
        if (word1[i] != '*' && word2[i] != '*' && word1[i] != word2[i]) {
            return false;
        }
    }
    return true;
}

int countValidWords(std::string sentence, std::vector<std::string>& dictionary) {
    std::istringstream iss(sentence);
    std::string word;
    int count = 0;
    std::unordered_set<std::string> dictSet(dictionary.begin(), dictionary.end());
    while (iss >> word) {
        for (const auto& dictWord : dictSet) {
            if (isMatch(word, dictWord)) {
                count++;
                break; // Move to the next word in the sentence
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of words in the sentence, $m$ is the number of unique words in the dictionary, and $k$ is the average length of a word. The use of an `unordered_set` for the dictionary improves lookup efficiency but doesn't change the overall time complexity due to the need to compare each word.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique words in the dictionary, for storing the dictionary in an `unordered_set`.
> - **Optimality proof:** This approach is optimal given the constraints of the problem, as it efficiently stores the dictionary for lookup and correctly handles the wildcard comparisons. Further optimization might involve more complex data structures or algorithms tailored to specific aspects of the input data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: String comparison, wildcard matching, and the use of data structures like `unordered_set` for efficient lookup.
- Problem-solving patterns: Breaking down the problem into smaller tasks (word comparison, dictionary lookup) and optimizing each task.
- Optimization techniques: Using efficient data structures for lookup and minimizing unnecessary comparisons.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of the `*` wildcard, not considering the case where a word in the sentence matches multiple words in the dictionary.
- Edge cases to watch for: Empty input, words with only `*`, dictionary containing duplicate words.
- Performance pitfalls: Using inefficient data structures or algorithms for lookup and comparison.
- Testing considerations: Ensure coverage of various input scenarios, including edge cases and large inputs.