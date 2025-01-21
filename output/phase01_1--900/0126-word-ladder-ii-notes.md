## Word Ladder II

**Problem Link:** https://leetcode.com/problems/word-ladder-ii/description

**Problem Statement:**
- Input: `beginWord`, `endWord`, and a list of words `wordList`
- Constraints: 
  - `1 <= beginWord.length <= 5`
  - `endWord.length == beginWord.length`
  - `1 <= wordList.length <= 5000`
  - `wordList.length == endWord.length`
  - All words have the same length
  - All words consist of only lowercase English letters
  - `beginWord`, `endWord`, and `wordList` are non-empty
- Expected output: A list of lists, where each sublist is a sequence of words from `beginWord` to `endWord` such that each word is a single-character modification of the previous word, and each word exists in `wordList`.
- Key requirements: 
  - Find all shortest transformation sequences from `beginWord` to `endWord`
  - A transformation sequence is a sequence of words where each word is a single-character modification of the previous word
  - The sequence should include `beginWord` and `endWord`
- Example test cases: 
  - Input: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`
  - Output: `[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible transformations of each word in the `wordList` to see if we can reach `endWord` from `beginWord`.
- This approach involves generating all possible words that are a single-character modification of each word in the `wordList`.
- We then check if the generated word is in the `wordList`. If it is, we add it to our current sequence and recursively try to find a sequence from the new word to `endWord`.
- Why this approach comes to mind first: It's a straightforward approach to explore all possible transformations.

```cpp
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

void dfs(string beginWord, string endWord, unordered_set<string>& wordList, vector<string>& path, vector<vector<string>>& result) {
    if (beginWord == endWord) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < beginWord.size(); i++) {
        for (char c = 'a'; c <= 'z'; c++) {
            string nextWord = beginWord;
            nextWord[i] = c;
            if (wordList.find(nextWord) != wordList.end()) {
                wordList.erase(nextWord);
                path.push_back(nextWord);
                dfs(nextWord, endWord, wordList, path, result);
                path.pop_back();
                wordList.insert(nextWord);
            }
        }
    }
}

vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
    unordered_set<string> wordSet(wordList.begin(), wordList.end());
    vector<vector<string>> result;
    vector<string> path = {beginWord};
    dfs(beginWord, endWord, wordSet, path, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \times 26^L \times L)$, where $N$ is the number of words in the `wordList` and $L$ is the length of each word. The reason is that in the worst case, we generate all possible words for each word in the `wordList`.
> - **Space Complexity:** $O(N \times L)$, where $N$ is the number of words in the `wordList` and $L$ is the length of each word. The reason is that we store all the words in the `wordList` in the `wordSet`.
> - **Why these complexities occur:** These complexities occur because we are generating all possible transformations of each word in the `wordList` and storing them in the `wordSet`.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a bidirectional BFS to find the shortest transformation sequence from `beginWord` to `endWord`.
- We use two queues to store the words to be processed. One queue starts from `beginWord` and the other queue starts from `endWord`.
- We use two sets to store the words that have been processed. One set stores the words that have been processed from `beginWord` and the other set stores the words that have been processed from `endWord`.
- We generate all possible words that are a single-character modification of each word in the queues and add them to the queues if they have not been processed before.
- We continue this process until we find a word that is in both sets. This word is the meeting point of the two queues.
- We then construct the transformation sequence by backtracking from the meeting point to `beginWord` and `endWord`.
- Why further optimization is impossible: This approach is optimal because it uses the minimum number of operations to find the shortest transformation sequence.

```cpp
#include <vector>
#include <string>
#include <unordered_set>
#include <queue>

using namespace std;

vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
    unordered_set<string> wordSet(wordList.begin(), wordList.end());
    if (wordSet.find(endWord) == wordSet.end()) {
        return {};
    }
    unordered_set<string> beginSet = {beginWord};
    unordered_set<string> endSet = {endWord};
    unordered_map<string, vector<string>> graph;
    bool isForward = true;
    while (!beginSet.empty() && !endSet.empty()) {
        if (beginSet.size() > endSet.size()) {
            swap(beginSet, endSet);
            isForward = !isForward;
        }
        unordered_set<string> tempSet;
        for (const string& word : beginSet) {
            for (int i = 0; i < word.size(); i++) {
                for (char c = 'a'; c <= 'z'; c++) {
                    string nextWord = word;
                    nextWord[i] = c;
                    if (endSet.find(nextWord) != endSet.end()) {
                        if (isForward) {
                            graph[word].push_back(nextWord);
                        } else {
                            graph[nextWord].push_back(word);
                        }
                        return constructLadders(graph, beginWord, endWord);
                    }
                    if (wordSet.find(nextWord) != wordSet.end()) {
                        tempSet.insert(nextWord);
                        if (isForward) {
                            graph[word].push_back(nextWord);
                        } else {
                            graph[nextWord].push_back(word);
                        }
                    }
                }
            }
        }
        for (const string& word : tempSet) {
            wordSet.erase(word);
        }
        beginSet = tempSet;
    }
    return {};
}

vector<vector<string>> constructLadders(unordered_map<string, vector<string>>& graph, string beginWord, string endWord) {
    vector<vector<string>> result;
    vector<string> path = {beginWord};
    dfs(graph, beginWord, endWord, path, result);
    return result;
}

void dfs(unordered_map<string, vector<string>>& graph, string beginWord, string endWord, vector<string>& path, vector<vector<string>>& result) {
    if (beginWord == endWord) {
        result.push_back(path);
        return;
    }
    for (const string& nextWord : graph[beginWord]) {
        path.push_back(nextWord);
        dfs(graph, nextWord, endWord, path, result);
        path.pop_back();
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \times 26^L)$, where $N$ is the number of words in the `wordList` and $L$ is the length of each word. The reason is that we generate all possible words for each word in the `wordList` in the worst case.
> - **Space Complexity:** $O(N \times L)$, where $N$ is the number of words in the `wordList` and $L$ is the length of each word. The reason is that we store all the words in the `wordList` in the `wordSet`.
> - **Optimality proof:** This approach is optimal because it uses the minimum number of operations to find the shortest transformation sequence. The bidirectional BFS ensures that we find the shortest sequence by exploring the words in the `wordList` in both directions.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of bidirectional BFS to find the shortest transformation sequence.
- The problem-solving pattern identified is to use a graph to store the words and their transformations.
- The optimization technique learned is to use a bidirectional BFS to reduce the number of operations.

**Mistakes to Avoid:**
- A common implementation error is to not handle the case where the `endWord` is not in the `wordList`.
- An edge case to watch for is when the `wordList` is empty.
- A performance pitfall is to not use a bidirectional BFS, which can lead to a significant increase in the number of operations.