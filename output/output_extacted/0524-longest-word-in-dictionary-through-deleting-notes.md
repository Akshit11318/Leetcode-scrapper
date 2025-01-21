## Longest Word in Dictionary through Deleting

**Problem Link:** https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description

**Problem Statement:**
- Input: A string `s` and a list of strings `d`.
- Constraints: The length of `s` will be between 1 and 1000. The length of `d` will be between 1 and 1000. The length of each string in `d` will be between 1 and 1000.
- Expected output: The longest word in `d` that can be formed by deleting characters from `s`.
- Key requirements and edge cases to consider:
  - If there are multiple words of the same length that can be formed, return the lexicographically smallest one.
  - If no word can be formed, return an empty string.

### Brute Force Approach

**Explanation:**
- Initial thought process: For each word in `d`, try to form it by deleting characters from `s`. If we can form the word, check if it's the longest word we've found so far.
- Step-by-step breakdown of the solution:
  1. For each word in `d`, create a copy of `s` to work with.
  2. Try to form the word by deleting characters from the copy of `s`.
  3. If we can form the word, check if it's the longest word we've found so far.
  4. If it's the longest word, update our result.

```cpp
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        string res = "";
        for (string word : d) {
            if (canFormWord(s, word)) {
                if (word.size() > res.size() || (word.size() == res.size() && word < res)) {
                    res = word;
                }
            }
        }
        return res;
    }

    bool canFormWord(string s, string word) {
        int sIndex = 0, wordIndex = 0;
        while (sIndex < s.size() && wordIndex < word.size()) {
            if (s[sIndex] == word[wordIndex]) {
                wordIndex++;
            }
            sIndex++;
        }
        return wordIndex == word.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times k)$, where $n$ is the length of `s`, $m$ is the number of words in `d`, and $k$ is the average length of the words in `d`. This is because for each word in `d`, we potentially scan through all of `s`.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store our result and indices.
> - **Why these complexities occur:** These complexities occur because we're scanning through `s` for each word in `d`, and for each character in `s`, we're potentially checking if it matches the current character in the word.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution, but we can optimize it by sorting `d` first. This way, as soon as we find a word that can be formed, we know it's the longest word we've found so far.
- Detailed breakdown of the approach:
  1. Sort `d` in lexicographical order.
  2. For each word in `d`, try to form it by deleting characters from `s`.
  3. If we can form the word, return it immediately, since we know it's the longest word we've found so far.

```cpp
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(), d.end(), [](string a, string b) {
            if (a.size() != b.size()) return a.size() > b.size();
            return a < b;
        });
        for (string word : d) {
            if (canFormWord(s, word)) return word;
        }
        return "";
    }

    bool canFormWord(string s, string word) {
        int sIndex = 0, wordIndex = 0;
        while (sIndex < s.size() && wordIndex < word.size()) {
            if (s[sIndex] == word[wordIndex]) {
                wordIndex++;
            }
            sIndex++;
        }
        return wordIndex == word.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \log m + n \times m \times k)$, where $m$ is the number of words in `d`, $n$ is the length of `s`, and $k$ is the average length of the words in `d`. This is because we're sorting `d` first, and then potentially scanning through `s` for each word in `d`.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store our result and indices.
> - **Optimality proof:** This solution is optimal because we're only scanning through `s` for each word in `d` once, and we're returning as soon as we find a word that can be formed. We're also sorting `d` first, which ensures that we return the lexicographically smallest word if there are multiple words of the same length that can be formed.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, string manipulation, and optimization techniques.
- Problem-solving patterns identified: sorting the input first to simplify the problem, and using a greedy approach to find the optimal solution.
- Optimization techniques learned: sorting the input first, and using a greedy approach to find the optimal solution.
- Similar problems to practice: other problems involving string manipulation and optimization techniques.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, and not handling errors properly.
- Edge cases to watch for: empty input strings, and input strings with only one character.
- Performance pitfalls: not optimizing the solution, and using inefficient algorithms.
- Testing considerations: testing the solution with different input cases, including edge cases and large input sizes.