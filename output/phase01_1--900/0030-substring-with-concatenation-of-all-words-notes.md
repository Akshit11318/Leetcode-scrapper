## Substring with Concatenation of All Words

**Problem Link:** [https://leetcode.com/problems/substring-with-concatenation-of-all-words/description](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description)

**Problem Statement:**
- Input format: `string s`, `vector<string> words`
- Constraints: `1 <= s.length <= 10^4`, `1 <= words.length <= 5000`, `1 <= words[i].length <= 10`
- Expected output format: `vector<int>` containing the starting indices of substrings where all words are concatenated
- Key requirements and edge cases to consider: 
    - Handling cases where `words` is empty or `s` is shorter than the total length of all words in `words`.
    - Ensuring that each word in `words` is used exactly once in the concatenated substring.
- Example test cases with explanations:
    - For `s = "barfoothefoobarman"`, `words = ["foo","bar"]`, the output should be `[0,9]`.
    - For `s = "wordgoodgoodgoodbestword"`, `words = ["word","good","best","word"]`, the output should be `[]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible substrings of `s` and check if they contain all words from `words`.
- Step-by-step breakdown of the solution:
    1. Generate all possible substrings of `s`.
    2. For each substring, check if it contains all words from `words` by trying all permutations of words and concatenating them.
    3. If a match is found, record the starting index of the substring.
- Why this approach comes to mind first: It's a straightforward approach that tries all possibilities, which can be intuitive but often inefficient.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> findSubstring(string s, vector<string>& words) {
    vector<int> result;
    if (s.empty() || words.empty()) return result;
    
    int wordCount = words.size();
    int wordLength = words[0].size();
    int totalLength = wordCount * wordLength;
    
    for (int i = 0; i <= s.size() - totalLength; i++) {
        string substring = s.substr(i, totalLength);
        vector<string> wordsCopy = words;
        bool match = true;
        
        for (int j = 0; j < totalLength; j += wordLength) {
            string word = substring.substr(j, wordLength);
            auto it = find(wordsCopy.begin(), wordsCopy.end(), word);
            if (it == wordsCopy.end()) {
                match = false;
                break;
            }
            wordsCopy.erase(it);
        }
        
        if (match) {
            result.push_back(i);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k \cdot l)$ where $n$ is the length of `s`, $m$ is the number of words, $k$ is the length of each word, and $l$ is the number of words. This is because we are generating all substrings, checking each word in each substring, and potentially removing words from the list of words.
> - **Space Complexity:** $O(m)$ for storing the copy of `words` and other variables.
> - **Why these complexities occur:** The brute force approach tries all possible substrings and checks each one against all permutations of words, leading to high time complexity. The space complexity is relatively low because we only need to store a copy of the list of words and a few other variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all substrings, we can use a sliding window approach to efficiently check substrings of the same length as the total length of all words.
- Detailed breakdown of the approach:
    1. Calculate the total length of all words.
    2. Use a sliding window of this length to scan through `s`.
    3. For each position of the window, check if the substring contains all words by creating a copy of `words` and removing each word as it's found in the substring.
    4. If all words are found, record the starting index of the window.
- Why further optimization is impossible: This approach checks each character in `s` exactly once and uses a constant amount of extra space to store the copy of `words`, making it optimal.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<int> findSubstring(string s, vector<string>& words) {
    vector<int> result;
    if (s.empty() || words.empty()) return result;
    
    int wordCount = words.size();
    int wordLength = words[0].size();
    int totalLength = wordCount * wordLength;
    
    unordered_map<string, int> wordCountMap;
    for (const string& word : words) {
        wordCountMap[word]++;
    }
    
    for (int i = 0; i <= s.size() - totalLength; i++) {
        unordered_map<string, int> copy = wordCountMap;
        for (int j = 0; j < totalLength; j += wordLength) {
            string word = s.substr(i + j, wordLength);
            if (copy.find(word) == copy.end() || --copy[word] < 0) {
                break;
            }
            if (j == totalLength - wordLength) {
                result.push_back(i);
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of `s` and $m` is the number of words. This is because we are scanning through `s` once and checking each word in the window.
> - **Space Complexity:** $O(m)$ for storing the `wordCountMap` and its copy.
> - **Optimality proof:** This approach is optimal because it only checks each character in `s` once and uses a constant amount of extra space to store the `wordCountMap`, making it the most efficient solution possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, using hash maps for efficient lookups.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving them efficiently.
- Optimization techniques learned: Reducing the number of iterations and using extra space to store intermediate results.
- Similar problems to practice: Other problems involving string matching and sliding window techniques.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty input strings or words.
- Edge cases to watch for: Handling cases where `words` is empty or `s` is shorter than the total length of all words in `words`.
- Performance pitfalls: Using inefficient data structures or algorithms, such as checking all permutations of words.
- Testing considerations: Testing the solution with different input cases, including edge cases and large inputs.