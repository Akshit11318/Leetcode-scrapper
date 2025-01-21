## Word Ladder
**Problem Link:** https://leetcode.com/problems/word-ladder/description

**Problem Statement:**
- Input format: The input will consist of two words `beginWord` and `endWord`, and a list of words `wordList`. 
- Constraints: The length of `wordList` will be in the range `[1, 5000]`, the length of `beginWord` and `endWord` will be in the range `[1, 10]`, and the length of each word in `wordList` will be the same as the length of `beginWord`.
- Expected output format: The function should return the length of the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.
- Key requirements and edge cases to consider: 
  - A word is only one step away from another word if it can be transformed into the other word by changing exactly one character.
  - The same word cannot be used more than once in the sequence.
- Example test cases with explanations: 
  - Input: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`, Output: `5`
  - Input: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]`, Output: `0`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible sequences of words by changing one character at a time and check if the sequence ends with `endWord`.
- Step-by-step breakdown of the solution: 
  1. Start with `beginWord` and generate all possible words by changing one character.
  2. Check if each generated word is in `wordList`.
  3. If a word is in `wordList`, remove it from `wordList` to avoid using it again in the sequence.
  4. Repeat steps 1-3 until we find a sequence that ends with `endWord` or until all possible sequences have been explored.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible sequences, but it is inefficient and may not find the shortest sequence.

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        set<string> wordSet(wordList.begin(), wordList.end());
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        
        while (!q.empty()) {
            string word = q.front().first;
            int length = q.front().second;
            q.pop();
            
            if (word == endWord) {
                return length;
            }
            
            for (int i = 0; i < word.size(); i++) {
                for (char c = 'a'; c <= 'z'; c++) {
                    string nextWord = word;
                    nextWord[i] = c;
                    
                    if (wordSet.find(nextWord) != wordSet.end()) {
                        wordSet.erase(nextWord);
                        q.push({nextWord, length + 1});
                    }
                }
            }
        }
        
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \cdot 26)$, where $N$ is the number of words in `wordList` and $M$ is the length of each word. This is because in the worst case, we might have to generate all possible words by changing one character and check if each word is in `wordList`.
> - **Space Complexity:** $O(N)$, where $N$ is the number of words in `wordList`. This is because we store all words in a set for efficient lookup.
> - **Why these complexities occur:** These complexities occur because we generate all possible words by changing one character and check if each word is in `wordList`, which requires a lot of time and space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a **Breadth-First Search (BFS)** algorithm to find the shortest sequence of words.
- Detailed breakdown of the approach: 
  1. Start with `beginWord` and generate all possible words by changing one character.
  2. Check if each generated word is in `wordList`.
  3. If a word is in `wordList`, remove it from `wordList` to avoid using it again in the sequence.
  4. Repeat steps 1-3 until we find a sequence that ends with `endWord` or until all possible sequences have been explored.
- Proof of optimality: This approach is optimal because it uses BFS to find the shortest sequence, which guarantees that the first sequence found is the shortest one.

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        set<string> wordSet(wordList.begin(), wordList.end());
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        wordSet.erase(beginWord);
        
        while (!q.empty()) {
            string word = q.front().first;
            int length = q.front().second;
            q.pop();
            
            if (word == endWord) {
                return length;
            }
            
            for (int i = 0; i < word.size(); i++) {
                for (char c = 'a'; c <= 'z'; c++) {
                    string nextWord = word;
                    nextWord[i] = c;
                    
                    if (wordSet.find(nextWord) != wordSet.end()) {
                        wordSet.erase(nextWord);
                        q.push({nextWord, length + 1});
                    }
                }
            }
        }
        
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \cdot 26)$, where $N$ is the number of words in `wordList` and $M$ is the length of each word. This is because in the worst case, we might have to generate all possible words by changing one character and check if each word is in `wordList`.
> - **Space Complexity:** $O(N)$, where $N$ is the number of words in `wordList`. This is because we store all words in a set for efficient lookup.
> - **Optimality proof:** This approach is optimal because it uses BFS to find the shortest sequence, which guarantees that the first sequence found is the shortest one.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: **Breadth-First Search (BFS)**, **string manipulation**, and **set operations**.
- Problem-solving patterns identified: **sequence generation**, **word matching**, and **sequence optimization**.
- Optimization techniques learned: **using a set for efficient lookup**, **removing words from the set to avoid duplicates**, and **using BFS to find the shortest sequence**.
- Similar problems to practice: **word chain**, **word ladder II**, and **minimum word length**.

**Mistakes to Avoid:**
- Common implementation errors: **not checking if a word is in the word list**, **not removing words from the word list to avoid duplicates**, and **not using BFS to find the shortest sequence**.
- Edge cases to watch for: **empty word list**, **word list with no valid sequences**, and **word list with multiple valid sequences**.
- Performance pitfalls: **using a slow algorithm**, **not optimizing the code**, and **not using efficient data structures**.
- Testing considerations: **testing with different word lists**, **testing with different begin and end words**, and **testing with edge cases**.