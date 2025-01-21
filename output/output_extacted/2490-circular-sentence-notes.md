## Circular Sentence

**Problem Link:** https://leetcode.com/problems/circular-sentence/description

**Problem Statement:**
- Input format: a string `sentence` containing only lowercase English letters and spaces.
- Constraints: `1 <= sentence.length <= 1000`.
- Expected output format: a boolean value indicating whether the sentence is circular.
- Key requirements: a sentence is considered circular if it can be formed by concatenating a list of words, and the last word in the list is the same as the first word in the list.
- Example test cases:
  - Input: `sentence = "leetcode exercises sound delightful"`
    Output: `true`
  - Input: `sentence = "eetcode"`
    Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: try all possible ways to split the sentence into words and check if the last word is the same as the first word.
- Step-by-step breakdown of the solution:
  1. Split the sentence into all possible lists of words.
  2. For each list, check if the last word is the same as the first word.
  3. If a circular sentence is found, return `true`.
  4. If no circular sentence is found after checking all possible lists, return `false`.

```cpp
class Solution {
public:
    bool isCircularSentence(string sentence) {
        int n = sentence.length();
        for (int i = 0; i < n; i++) {
            string word = "";
            int j = i;
            while (j < n && sentence[j] != ' ') {
                word += sentence[j];
                j++;
            }
            if (word.empty()) continue;
            bool found = false;
            for (int k = j + 1; k < n; k++) {
                string nextWord = "";
                int l = k;
                while (l < n && sentence[l] != ' ') {
                    nextWord += sentence[l];
                    l++;
                }
                if (nextWord == word) {
                    found = true;
                    break;
                }
            }
            if (found) {
                string lastWord = "";
                int k = n - 1;
                while (k >= 0 && sentence[k] != ' ') {
                    lastWord = sentence[k] + lastWord;
                    k--;
                }
                if (lastWord == word) return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the sentence. This is because we are iterating over the sentence to split it into words, and for each word, we are iterating over the rest of the sentence to check if it is the same as the first word.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the sentence. This is because we are storing the words in the sentence.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach to try all possible ways to split the sentence into words and check if the last word is the same as the first word.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: we can split the sentence into words and then check if the last word is the same as the first word.
- Detailed breakdown of the approach:
  1. Split the sentence into words.
  2. Check if the last word is the same as the first word.
  3. If the last word is the same as the first word, return `true`.
  4. If the last word is not the same as the first word, return `false`.

```cpp
class Solution {
public:
    bool isCircularSentence(string sentence) {
        int n = sentence.length();
        if (sentence[n - 1] != sentence[0]) return false;
        string word = "";
        unordered_set<string> words;
        for (int i = 0; i < n; i++) {
            if (sentence[i] == ' ') {
                if (words.find(word) != words.end()) return false;
                words.insert(word);
                word = "";
            } else {
                word += sentence[i];
            }
        }
        if (words.find(word) != words.end()) return false;
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the sentence. This is because we are iterating over the sentence to split it into words.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the sentence. This is because we are storing the words in the sentence.
> - **Optimality proof:** This approach is optimal because we are only iterating over the sentence once to split it into words, and then checking if the last word is the same as the first word. We are also using a set to keep track of the words we have seen, which allows us to check if a word has been seen before in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, set data structure.
- Problem-solving patterns identified: checking if a sentence is circular by splitting it into words and checking if the last word is the same as the first word.
- Optimization techniques learned: using a set to keep track of words we have seen to avoid duplicates.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the last word is the same as the first word, not using a set to keep track of words we have seen.
- Edge cases to watch for: empty sentence, sentence with only one word.
- Performance pitfalls: using a brute force approach to try all possible ways to split the sentence into words.
- Testing considerations: testing with different types of sentences, including circular and non-circular sentences.