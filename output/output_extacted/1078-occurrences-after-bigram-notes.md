## Occurrences After Bigram
**Problem Link:** https://leetcode.com/problems/occurrences-after-bigram/description

**Problem Statement:**
- Input: Two strings `first` and `second`, and a list of strings `sentence`.
- Constraints: All strings consist of lowercase letters.
- Expected Output: A list of strings, where each string is a word that occurs immediately after `first` followed by `second` in any sentence in `sentence`.
- Key Requirements: Find all occurrences after the specified bigram.
- Example Test Cases:
  - `findOcurrences("alice is a good girl she is a good student", "a", "good")` returns `["girl","student"]`.
  - `findOcurrences("we will we will rock you", "we", "will")` returns `["we","rock"]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through each sentence and checking for the occurrence of the bigram (`first` followed by `second`).
- Step-by-step breakdown:
  1. Split each sentence into words.
  2. Iterate through the words to find the bigram.
  3. When the bigram is found, add the next word to the result list.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each word sequence.

```cpp
vector<string> findOcurrences(string text, string first, string second) {
    vector<string> result;
    size_t pos = 0;
    string sentence = text + " ";
    while ((pos = sentence.find(" ")) != string::npos) {
        string word = sentence.substr(0, pos);
        sentence.erase(0, pos + 1);
        if (word == first) {
            size_t nextPos = sentence.find(" ");
            if (nextPos != string::npos) {
                string nextWord = sentence.substr(0, nextPos);
                if (nextWord == second) {
                    size_t nextNextPos = sentence.find(" ", nextPos + 1);
                    if (nextNextPos != string::npos) {
                        string nextNextWord = sentence.substr(nextPos + 1, nextNextPos - nextPos - 1);
                        result.push_back(nextNextWord);
                    } else {
                        size_t lastSpace = sentence.rfind(" ");
                        if (lastSpace != string::npos) {
                            string nextNextWord = sentence.substr(nextPos + 1, lastSpace - nextPos - 1);
                            result.push_back(nextNextWord);
                        }
                    }
                }
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of sentences and $m$ is the average number of words in a sentence. This is because we are potentially scanning each sentence multiple times to find the bigram and the subsequent word.
> - **Space Complexity:** $O(n \cdot m)$, as we store all the subsequent words after the bigram in the result list.
> - **Why these complexities occur:** These complexities are due to the nested operations of splitting sentences into words and then searching for the bigram within each sentence.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of manually splitting sentences and searching, use the `istringstream` to split the input string into words and then iterate through the words to find the bigram.
- Detailed breakdown:
  1. Use `istringstream` to split the input string into words.
  2. Iterate through the words, maintaining a window of the last two words.
  3. When the current window matches the bigram, add the next word to the result list.
- Proof of optimality: This approach minimizes unnecessary string operations and directly iterates through the words, reducing the time complexity.

```cpp
vector<string> findOcurrences(string text, string first, string second) {
    vector<string> words;
    istringstream iss(text);
    string word;
    while (iss >> word) {
        words.push_back(word);
    }
    
    vector<string> result;
    for (int i = 0; i < words.size() - 2; ++i) {
        if (words[i] == first && words[i + 1] == second) {
            result.push_back(words[i + 2]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of words in the input string. This is because we make a single pass through the words.
> - **Space Complexity:** $O(n)$, for storing the words and the result list.
> - **Optimality proof:** This is optimal because we only iterate through the input string once to split it into words and then make a single pass through the words to find the bigram and subsequent words.

---

### Final Notes

**Learning Points:**
- Using `istringstream` for efficient string splitting.
- Maintaining a window of previous elements for pattern matching.
- Optimizing string operations by minimizing unnecessary splits and searches.

**Mistakes to Avoid:**
- Manually splitting strings without considering performance.
- Not considering the use of standard library functions for string operations.
- Failing to optimize the search for patterns within strings.