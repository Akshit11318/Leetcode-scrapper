## Sentence Similarity
**Problem Link:** https://leetcode.com/problems/sentence-similarity/description

**Problem Statement:**
- Input format: Two lists of strings `sentences1` and `sentences2`, and a list of pairs of words `similarPairs`.
- Constraints: `1 <= sentences1.length, sentences2.length <= 100`, `1 <= similarPairs.length <= 1000`, `1 <= sentences1[i].length, sentences2[i].length <= 100`, `1 <= similarPairs[i][0].length, similarPairs[i][1].length <= 20`.
- Expected output format: A list of booleans indicating whether each sentence in `sentences1` is similar to the corresponding sentence in `sentences2`.
- Key requirements: Two sentences are similar if they contain the same number of words, and each word in one sentence is similar to the corresponding word in the other sentence. Two words are similar if they are the same, or if they are in the `similarPairs` list.
- Example test cases:
  - `sentences1 = ["My sentence1", "is Similar"]`, `sentences2 = ["Your sentence1", "is Similar"]`, `similarPairs = [["great","fine"],["acting","drama"],["skills","talent"]]`, output: `[false,true]`
  - `sentences1 = ["My sentence1", "is Similar"]`, `sentences2 = ["Your sentence1", "is Similar"]`, `similarPairs = [["great","fine"],["acting","drama"],["My","Your"],["sentence1","sentence2"],["Similar","Similar"]]`, output: `[true,true]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to compare each word in the sentences and check if they are similar based on the `similarPairs` list.
- We can create a graph where each word is a node, and two nodes are connected if the corresponding words are similar.
- Then, for each pair of sentences, we compare each word and check if they are similar by traversing the graph.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool areSimilar(const string& word1, const string& word2, const vector<vector<string>>& similarPairs) {
    if (word1 == word2) return true;
    for (const auto& pair : similarPairs) {
        if ((pair[0] == word1 && pair[1] == word2) || (pair[0] == word2 && pair[1] == word1)) return true;
    }
    return false;
}

vector<bool> areSentencesSimilar(vector<string> sentences1, vector<string> sentences2, vector<vector<string>> similarPairs) {
    vector<bool> result;
    for (int i = 0; i < sentences1.size(); i++) {
        string sentence1 = sentences1[i];
        string sentence2 = sentences2[i];
        istringstream iss1(sentence1);
        istringstream iss2(sentence2);
        string word1, word2;
        bool similar = true;
        while (iss1 >> word1 && iss2 >> word2) {
            if (!areSimilar(word1, word2, similarPairs)) {
                similar = false;
                break;
            }
        }
        if (iss1 >> word1 || iss2 >> word2) similar = false; // sentences have different lengths
        result.push_back(similar);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of sentence pairs, $m$ is the maximum number of words in a sentence, and $k$ is the number of similar pairs. The reason is that for each sentence pair, we compare each word, and for each word comparison, we iterate over the similar pairs.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result and temporary variables.
> - **Why these complexities occur:** The time complexity is high because we have to compare each word in the sentences and check if they are similar by iterating over the similar pairs. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- We can improve the brute force approach by creating a `unordered_map` to store the similar words for each word. This way, we can quickly check if two words are similar without having to iterate over the similar pairs.
- We can also use a `unordered_set` to store the words that are similar to a given word, so that we can quickly check if a word is similar to another word.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

void buildSimilarWordsMap(const vector<vector<string>>& similarPairs, unordered_map<string, unordered_set<string>>& similarWordsMap) {
    for (const auto& pair : similarPairs) {
        similarWordsMap[pair[0]].insert(pair[1]);
        similarWordsMap[pair[1]].insert(pair[0]);
    }
}

bool areSimilar(const string& word1, const string& word2, const unordered_map<string, unordered_set<string>>& similarWordsMap) {
    if (word1 == word2) return true;
    if (similarWordsMap.find(word1) != similarWordsMap.end() && similarWordsMap.at(word1).find(word2) != similarWordsMap.at(word1).end()) return true;
    return false;
}

vector<bool> areSentencesSimilar(vector<string> sentences1, vector<string> sentences2, vector<vector<string>> similarPairs) {
    unordered_map<string, unordered_set<string>> similarWordsMap;
    buildSimilarWordsMap(similarPairs, similarWordsMap);
    vector<bool> result;
    for (int i = 0; i < sentences1.size(); i++) {
        string sentence1 = sentences1[i];
        string sentence2 = sentences2[i];
        istringstream iss1(sentence1);
        istringstream iss2(sentence2);
        string word1, word2;
        bool similar = true;
        while (iss1 >> word1 && iss2 >> word2) {
            if (!areSimilar(word1, word2, similarWordsMap)) {
                similar = false;
                break;
            }
        }
        if (iss1 >> word1 || iss2 >> word2) similar = false; // sentences have different lengths
        result.push_back(similar);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + k)$, where $n$ is the number of sentence pairs, $m$ is the maximum number of words in a sentence, and $k$ is the number of similar pairs. The reason is that we first build the similar words map in $O(k)$ time, and then for each sentence pair, we compare each word in $O(m)$ time.
> - **Space Complexity:** $O(k)$, as we use a map to store the similar words for each word.
> - **Optimality proof:** This is the optimal solution because we have reduced the time complexity of comparing two words from $O(k)$ to $O(1)$ by using a map to store the similar words for each word.

---

### Final Notes

**Learning Points:**
- We learned how to improve the brute force approach by using a map to store the similar words for each word.
- We learned how to reduce the time complexity of comparing two words from $O(k)$ to $O(1)$.
- We learned how to use a map to store the similar words for each word.

**Mistakes to Avoid:**
- Not using a map to store the similar words for each word, which can lead to a high time complexity.
- Not checking if the sentences have the same length before comparing the words.
- Not handling the case where a word is not in the similar words map.