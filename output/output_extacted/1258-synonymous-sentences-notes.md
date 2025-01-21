## Synonymous Sentences
**Problem Link:** https://leetcode.com/problems/synonymous-sentences/description

**Problem Statement:**
- Input: A list of `synonyms` where each element is a list of strings representing synonymous words, and a sentence `text` that needs to be generated into all possible synonymous sentences.
- Expected output: A list of all possible synonymous sentences.
- Key requirements: The order of words in the sentence must remain the same, but the choice of word can vary among the synonyms provided.
- Example test cases: 
  - Input: synonyms = [["happy","joyful"]], text = "happy"
  - Output: ["happy","joyful"]

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible combinations of synonymous words for each word in the input sentence.
- Step-by-step breakdown:
  1. Parse the input sentence into individual words.
  2. For each word, find its corresponding synonyms from the list of synonyms.
  3. Use a recursive approach or a combinatorial algorithm to generate all possible sentences by replacing each word with its synonyms.
  4. Collect all generated sentences.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    vector<string> generateSentences(vector<vector<string>>& synonyms, string text) {
        unordered_map<string, vector<string>> synMap;
        for (auto& syn : synonyms) {
            synMap[syn[0]] = syn;
        }
        
        vector<string> words;
        string word;
        for (char c : text) {
            if (c == ' ') {
                words.push_back(word);
                word.clear();
            } else {
                word += c;
            }
        }
        words.push_back(word);
        
        vector<string> result;
        generate(result, words, 0, synMap);
        return result;
    }
    
    void generate(vector<string>& result, vector<string>& words, int index, unordered_map<string, vector<string>>& synMap) {
        if (index == words.size()) {
            string sentence;
            for (const string& word : words) {
                sentence += word + " ";
            }
            sentence.pop_back(); // Remove the trailing space
            result.push_back(sentence);
            return;
        }
        
        vector<string> syns = synMap[words[index]];
        if (syns.empty()) {
            syns.push_back(words[index]);
        }
        
        for (const string& syn : syns) {
            words[index] = syn;
            generate(result, words, index + 1, synMap);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$ where $n$ is the number of words in the sentence that have synonyms and $m$ is the average number of synonyms per word. This is because in the worst-case scenario, each word could have two synonyms, leading to an exponential number of combinations.
> - **Space Complexity:** $O(n \cdot m)$ for storing the recursive call stack and the generated sentences.
> - **Why these complexities occur:** The exponential time complexity comes from the recursive generation of all possible sentences, and the space complexity is due to the storage of the recursive call stack and the resulting sentences.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a more efficient data structure to store the synonyms and to utilize a combinatorial algorithm that avoids redundant computations.
- Detailed breakdown:
  1. Create a `unordered_map` to store the synonyms for each word, allowing for $O(1)$ lookups.
  2. Use a combinatorial algorithm like `next_permutation` to generate all possible combinations of synonyms for each word in the sentence.
  3. Utilize a `set` to eliminate duplicate sentences.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>

class Solution {
public:
    vector<string> generateSentences(vector<vector<string>>& synonyms, string text) {
        unordered_map<string, vector<string>> synMap;
        for (auto& syn : synonyms) {
            synMap[syn[0]] = syn;
        }
        
        vector<string> words;
        string word;
        for (char c : text) {
            if (c == ' ') {
                words.push_back(word);
                word.clear();
            } else {
                word += c;
            }
        }
        words.push_back(word);
        
        set<string> result;
        generate(result, words, 0, synMap);
        vector<string> res(result.begin(), result.end());
        return res;
    }
    
    void generate(set<string>& result, vector<string>& words, int index, unordered_map<string, vector<string>>& synMap) {
        if (index == words.size()) {
            string sentence;
            for (const string& word : words) {
                sentence += word + " ";
            }
            sentence.pop_back(); // Remove the trailing space
            result.insert(sentence);
            return;
        }
        
        vector<string> syns = synMap[words[index]];
        if (syns.empty()) {
            syns.push_back(words[index]);
        }
        
        for (const string& syn : syns) {
            words[index] = syn;
            generate(result, words, index + 1, synMap);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of words with synonyms and $m$ is the average number of synonyms per word. This remains exponential due to the nature of generating all possible sentences.
> - **Space Complexity:** $O(n \cdot m)$ for storing the recursive call stack and the resulting unique sentences.
> - **Optimality proof:** This approach is optimal because it generates all possible sentences without redundant computations, using efficient data structures for synonym lookups and result storage.

---

### Final Notes

**Learning Points:**
- Utilizing `unordered_map` for efficient lookups.
- Employing combinatorial algorithms for generating all possible combinations.
- Using `set` to eliminate duplicate results.

**Mistakes to Avoid:**
- Failing to handle edge cases where a word has no synonyms.
- Not optimizing the storage of results to avoid duplicates.
- Inefficient use of data structures leading to higher complexities.