## Word Break II
**Problem Link:** https://leetcode.com/problems/word-break-ii/description

**Problem Statement:**
- Input: A non-empty string `s` and a dictionary `wordDict` containing a list of non-empty words.
- Constraints: `1 <= s.length <= 20`, `1 <= wordDict.length <= 1000`, `1 <= wordDict[i].length <= 20`, `s` and `wordDict[i]` consist of lowercase English letters.
- Expected Output: A list of strings representing all possible sentence combinations that can be formed using the words in `wordDict` to split `s`.
- Key Requirements: Use the words in `wordDict` to split `s` into sentences. Each word can be used more than once.
- Edge Cases: Handle cases where `s` cannot be split into sentences using the words in `wordDict`.
- Example Test Cases:
  - Input: `s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]`
  - Output: `["cat sand dog","cats and dog"]`
  - Explanation: Both "cat sand dog" and "cats and dog" are valid sentences.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves generating all possible combinations of words from `wordDict` and checking if they can form a valid sentence.
- Start by checking all possible word combinations that can form a valid sentence using the first word in `wordDict`.
- For each combination, check if the remaining part of `s` can be split into sentences using the remaining words in `wordDict`.
- If a valid combination is found, add it to the result list.
- Repeat this process for all possible combinations of words.

```cpp
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> result;
        vector<string> path;
        backtrack(s, wordDict, 0, path, result);
        return result;
    }
    
    void backtrack(string s, vector<string>& wordDict, int start, vector<string>& path, vector<string>& result) {
        if (start == s.size()) {
            string sentence;
            for (int i = 0; i < path.size(); i++) {
                sentence += path[i];
                if (i < path.size() - 1) {
                    sentence += " ";
                }
            }
            result.push_back(sentence);
            return;
        }
        
        for (int i = start; i < s.size(); i++) {
            string word = s.substr(start, i - start + 1);
            if (isWordInDict(word, wordDict)) {
                path.push_back(word);
                backtrack(s, wordDict, i + 1, path, result);
                path.pop_back();
            }
        }
    }
    
    bool isWordInDict(string word, vector<string>& wordDict) {
        for (string dictWord : wordDict) {
            if (dictWord == word) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the length of `s` and $m$ is the number of words in `wordDict`. This is because in the worst-case scenario, we are generating all possible combinations of words and checking each combination.
> - **Space Complexity:** $O(n + m)$, where $n$ is the length of `s` and $m$ is the number of words in `wordDict`. This is because we are storing the result list and the path list.
> - **Why these complexities occur:** These complexities occur because the brute force approach involves generating all possible combinations of words and checking each combination, resulting in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a `HashSet` to store the words in `wordDict` for efficient lookup.
- Use a `backtrack` function to generate all possible combinations of words that can form a valid sentence.
- Use a `memo` map to store the intermediate results to avoid redundant computation.
- Start by checking all possible word combinations that can form a valid sentence using the first word in `wordDict`.
- For each combination, check if the remaining part of `s` can be split into sentences using the remaining words in `wordDict`.
- If a valid combination is found, add it to the result list.
- Repeat this process for all possible combinations of words.

```cpp
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        unordered_map<int, vector<string>> memo;
        return backtrack(s, dict, 0, memo);
    }
    
    vector<string> backtrack(string s, unordered_set<string>& dict, int start, unordered_map<int, vector<string>>& memo) {
        if (memo.find(start) != memo.end()) {
            return memo[start];
        }
        
        vector<string> result;
        if (start == s.size()) {
            result.push_back("");
            return result;
        }
        
        for (int i = start; i < s.size(); i++) {
            string word = s.substr(start, i - start + 1);
            if (dict.find(word) != dict.end()) {
                vector<string> next = backtrack(s, dict, i + 1, memo);
                for (string n : next) {
                    if (n.empty()) {
                        result.push_back(word);
                    } else {
                        result.push_back(word + " " + n);
                    }
                }
            }
        }
        
        memo[start] = result;
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `s`. This is because in the worst-case scenario, we are generating all possible combinations of words.
> - **Space Complexity:** $O(n + m)$, where $n$ is the length of `s` and $m` is the number of words in `wordDict`. This is because we are storing the result list and the memo map.
> - **Optimality proof:** This approach is optimal because it uses a `HashSet` to store the words in `wordDict` for efficient lookup and a `memo` map to store the intermediate results to avoid redundant computation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, memoization, and efficient lookup using a `HashSet`.
- Problem-solving patterns identified: using a `memo` map to store intermediate results and avoiding redundant computation.
- Optimization techniques learned: using a `HashSet` to store the words in `wordDict` for efficient lookup.
- Similar problems to practice: word break, word ladder, and other problems involving backtracking and memoization.

**Mistakes to Avoid:**
- Common implementation errors: not using a `memo` map to store intermediate results, not using a `HashSet` to store the words in `wordDict` for efficient lookup.
- Edge cases to watch for: handling cases where `s` cannot be split into sentences using the words in `wordDict`.
- Performance pitfalls: not using memoization and efficient lookup, resulting in an exponential time complexity.
- Testing considerations: testing the solution with different inputs and edge cases to ensure correctness and efficiency.