## Word Abbreviation
**Problem Link:** https://leetcode.com/problems/word-abbreviation/description

**Problem Statement:**
- Input format: a list of words
- Constraints: words will contain only lowercase letters, and the list will not be empty
- Expected output format: a list of unique abbreviations for the given words
- Key requirements and edge cases to consider: 
  - An abbreviation is unique if no other word from the list can represent the same abbreviation.
  - The goal is to find the shortest abbreviation that is unique for each word.
  - Example test cases: 
    - Input: ["like", "god", "internal", "me", "internet"]
    - Expected Output: ["l", "g", "i6", "me", "i9"]

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible abbreviations for each word and check if they are unique.
- Step-by-step breakdown of the solution:
  1. For each word, generate all possible abbreviations by taking the first character and the last character, and then adding characters from the start of the word until we find a unique abbreviation.
  2. For each abbreviation, check if it is unique by comparing it with all other words.
  3. If an abbreviation is not unique, add more characters to the abbreviation until it becomes unique.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it is not efficient.

```cpp
class ValidWordAbbr {
public:
    unordered_map<string, int> m;
    ValidWordAbbr(vector<string>& dictionary) {
        for (auto word : dictionary) {
            string abbr = getAbbr(word);
            m[abbr]++;
        }
    }

    string getAbbr(string word) {
        if (word.size() <= 2) return word;
        return word[0] + to_string(word.size() - 2) + word[word.size() - 1];
    }

    bool isUnique(string word) {
        string abbr = getAbbr(word);
        return m[abbr] == 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the maximum length of a word. The reason is that we are generating all possible abbreviations for each word and checking their uniqueness.
> - **Space Complexity:** $O(n \cdot m)$ as we need to store all the abbreviations in the `m` map.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach, which involves generating all possible abbreviations and checking their uniqueness.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible abbreviations, we can generate the shortest possible abbreviation for each word and then check its uniqueness.
- Detailed breakdown of the approach:
  1. For each word, generate the shortest possible abbreviation by taking the first character and the last character, and then adding characters from the start of the word until we find a unique abbreviation.
  2. Use a hashmap to store the frequency of each abbreviation.
  3. For each word, check if its abbreviation is unique by looking up the hashmap.
- Proof of optimality: This approach is optimal because it generates the shortest possible abbreviation for each word and checks its uniqueness in constant time using a hashmap.

```cpp
class ValidWordAbbr {
public:
    unordered_map<string, vector<string>> m;
    ValidWordAbbr(vector<string>& dictionary) {
        for (auto word : dictionary) {
            string abbr = getAbbr(word, 0);
            m[abbr].push_back(word);
        }
    }

    string getAbbr(string word, int i) {
        if (word.size() <= 2 || i >= word.size() - 2) return word.substr(0, i + 1) + word.substr(word.size() - 1);
        return word[0] + to_string(word.size() - i - 2) + word[word.size() - 1];
    }

    bool isUnique(string word) {
        string abbr = getAbbr(word, 0);
        return m[abbr].size() == 1 && m[abbr][0] == word;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the maximum length of a word. The reason is that we are generating the shortest possible abbreviation for each word and checking its uniqueness.
> - **Space Complexity:** $O(n \cdot m)$ as we need to store all the abbreviations in the `m` map.
> - **Optimality proof:** This approach is optimal because it generates the shortest possible abbreviation for each word and checks its uniqueness in constant time using a hashmap.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hashmap, string manipulation, and optimization techniques.
- Problem-solving patterns identified: generating all possible abbreviations and checking their uniqueness.
- Optimization techniques learned: using a hashmap to store the frequency of each abbreviation and generating the shortest possible abbreviation for each word.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not checking for uniqueness correctly.
- Edge cases to watch for: words with length less than or equal to 2, words with the same abbreviation.
- Performance pitfalls: using a brute force approach, not optimizing the abbreviation generation process.
- Testing considerations: testing with different input sizes, testing with different types of input data.