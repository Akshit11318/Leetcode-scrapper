## Prefix and Suffix Search
**Problem Link:** https://leetcode.com/problems/prefix-and-suffix-search/description

**Problem Statement:**
- Input format and constraints: Given a list of words, design a class that supports searching for words by prefix and suffix.
- Expected output format: Return the index of the word in the list if it matches the given prefix and suffix, otherwise return -1.
- Key requirements and edge cases to consider: 
    - The input list of words may be empty.
    - The prefix and suffix may be empty.
    - The prefix and suffix may be longer than the word.
- Example test cases with explanations:
    - Searching for a word with a prefix and suffix that matches a word in the list should return the index of the word.
    - Searching for a word with a prefix and suffix that does not match any word in the list should return -1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each word in the list and check if it matches the given prefix and suffix.
- Step-by-step breakdown of the solution:
    1. Iterate over each word in the list.
    2. Check if the word starts with the given prefix.
    3. Check if the word ends with the given suffix.
    4. If both conditions are met, return the index of the word.
- Why this approach comes to mind first: It is a straightforward and simple approach that checks each word in the list.

```cpp
class WordFilter {
public:
    vector<string> words;
    WordFilter(vector<string>& words) {
        this->words = words;
    }
    int f(string prefix, string suffix) {
        for (int i = 0; i < words.size(); i++) {
            if (words[i].find(prefix) == 0 && words[i].rfind(suffix) == words[i].size() - suffix.size()) {
                return i;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where n is the number of words and m is the maximum length of a word. This is because we iterate over each word and check if it matches the prefix and suffix.
> - **Space Complexity:** $O(n)$, where n is the number of words. This is because we store the list of words.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each word and perform string operations. The space complexity occurs because we store the list of words.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `unordered_map` to store the words with their indices, and use the prefix and suffix as keys.
- Detailed breakdown of the approach:
    1. Create an `unordered_map` to store the words with their indices.
    2. Iterate over each word and create a key by concatenating the prefix and suffix.
    3. Store the word and its index in the `unordered_map` with the key.
    4. When searching for a word, create the key by concatenating the prefix and suffix.
    5. Check if the key exists in the `unordered_map` and return the index of the word if it does.
- Proof of optimality: This approach has a time complexity of $O(1)$ for searching, which is optimal.

```cpp
class WordFilter {
public:
    unordered_map<string, int> wordMap;
    WordFilter(vector<string>& words) {
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j <= words[i].size(); j++) {
                for (int k = 0; k <= words[i].size(); k++) {
                    string key = words[i].substr(0, j) + "#" + words[i].substr(k);
                    wordMap[key] = i;
                }
            }
        }
    }
    int f(string prefix, string suffix) {
        string key = prefix + "#" + suffix;
        if (wordMap.find(key) != wordMap.end()) {
            return wordMap[key];
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for searching, $O(n \cdot m^2)$ for building the `unordered_map`, where n is the number of words and m is the maximum length of a word.
> - **Space Complexity:** $O(n \cdot m^2)$, where n is the number of words and m is the maximum length of a word.
> - **Optimality proof:** The time complexity of $O(1)$ for searching is optimal, as we can directly access the index of the word using the key.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an `unordered_map` to store words with their indices, and using prefix and suffix as keys.
- Problem-solving patterns identified: Using a data structure to store information and then searching for it.
- Optimization techniques learned: Using a `unordered_map` to reduce the time complexity of searching.
- Similar problems to practice: Problems that involve searching for words or strings in a list.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the key exists in the `unordered_map` before accessing it.
- Edge cases to watch for: Empty input list, empty prefix and suffix, prefix and suffix longer than the word.
- Performance pitfalls: Using a data structure with a high time complexity for searching.
- Testing considerations: Test the function with different inputs, including edge cases.