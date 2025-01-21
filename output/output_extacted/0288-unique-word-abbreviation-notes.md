## Unique Word Abbreviation
**Problem Link:** https://leetcode.com/problems/unique-word-abbreviation/description

**Problem Statement:**
- Input format: A list of unique words and a dictionary of words.
- Constraints: The list of unique words is non-empty, and each word is a non-empty string consisting only of lowercase letters.
- Expected output format: A function that takes a word and returns whether it is a unique abbreviation of the dictionary words.
- Key requirements and edge cases to consider: A word is a unique abbreviation of a dictionary word if it matches the word after replacing sequences of non-overlapping, non-adjacent groups of characters with the count of characters in the group. For example, "a2b" is a unique abbreviation of "abb".
- Example test cases with explanations:
  - Input: word = "internationalization", dictionary = ["international","ize"]
  - Output: true
  - Explanation: "internationalization" can be abbreviated as "i12iz4n" which is a unique abbreviation of "international" and "ize".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible abbreviations of each word in the dictionary and check if the input word matches any of them.
- Step-by-step breakdown of the solution:
  1. Generate all possible abbreviations of each word in the dictionary.
  2. Check if the input word matches any of the generated abbreviations.
- Why this approach comes to mind first: It is a straightforward approach that involves checking all possible cases.

```cpp
class ValidWordAbbr {
public:
    unordered_map<string, int> mp;
    ValidWordAbbr(vector<string>& dictionary) {
        for (string word : dictionary) {
            string abbr = getAbbr(word);
            if (mp.find(abbr) != mp.end()) {
                mp[abbr]++;
            } else {
                mp[abbr] = 1;
            }
        }
    }

    bool isUnique(string word) {
        string abbr = getAbbr(word);
        if (mp.find(abbr) == mp.end()) return true;
        if (mp[abbr] == 1) {
            for (string dictWord : dictionary_) {
                if (dictWord == word) return false;
            }
        }
        return false;
    }

private:
    vector<string> dictionary_;
    string getAbbr(string word) {
        string abbr;
        int count = 1;
        for (int i = 1; i < word.size(); i++) {
            if (word[i] == word[i - 1]) {
                count++;
            } else {
                if (count > 1) {
                    abbr += to_string(count);
                }
                abbr += word[i - 1];
                count = 1;
            }
        }
        if (count > 1) {
            abbr += to_string(count);
        }
        abbr += word[word.size() - 1];
        return abbr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words in the dictionary and $m$ is the maximum length of a word. This is because we generate all possible abbreviations of each word in the dictionary.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of words in the dictionary and $m$ is the maximum length of a word. This is because we store all possible abbreviations of each word in the dictionary.
> - **Why these complexities occur:** These complexities occur because we generate all possible abbreviations of each word in the dictionary and store them in a hashmap.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible abbreviations of each word in the dictionary, we can generate the abbreviation of the input word and check if it matches any word in the dictionary.
- Detailed breakdown of the approach:
  1. Generate the abbreviation of the input word.
  2. Check if the abbreviation matches any word in the dictionary.
- Proof of optimality: This approach is optimal because we only generate the abbreviation of the input word and check if it matches any word in the dictionary, which reduces the time complexity.

```cpp
class ValidWordAbbr {
public:
    unordered_map<string, int> mp;
    ValidWordAbbr(vector<string>& dictionary) {
        for (string word : dictionary) {
            string abbr = getAbbr(word);
            if (mp.find(abbr) != mp.end()) {
                mp[abbr]++;
            } else {
                mp[abbr] = 1;
            }
        }
    }

    bool isUnique(string word) {
        string abbr = getAbbr(word);
        if (mp.find(abbr) == mp.end()) return true;
        if (mp[abbr] == 1) {
            for (string dictWord : dictionary_) {
                if (dictWord == word) return false;
            }
        }
        return false;
    }

private:
    vector<string> dictionary_;
    string getAbbr(string word) {
        if (word.size() <= 2) return word;
        return word[0] + to_string(word.size() - 2) + word[word.size() - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words in the dictionary and $m$ is the maximum length of a word. This is because we generate the abbreviation of each word in the dictionary and store it in a hashmap.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of words in the dictionary and $m$ is the maximum length of a word. This is because we store the abbreviation of each word in the dictionary in a hashmap.
> - **Optimality proof:** This approach is optimal because we only generate the abbreviation of each word in the dictionary and store it in a hashmap, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashmap, string manipulation.
- Problem-solving patterns identified: Generating abbreviations of words and checking for uniqueness.
- Optimization techniques learned: Reducing time complexity by generating abbreviations of input words instead of all possible abbreviations.
- Similar problems to practice: Word abbreviation, string manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for uniqueness correctly.
- Edge cases to watch for: Words with length less than or equal to 2, words with repeated characters.
- Performance pitfalls: Generating all possible abbreviations of each word in the dictionary, not using a hashmap to store abbreviations.
- Testing considerations: Testing with different input words and dictionaries, checking for correctness and performance.