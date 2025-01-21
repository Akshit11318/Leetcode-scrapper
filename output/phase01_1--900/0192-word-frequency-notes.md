## Word Frequency
**Problem Link:** https://leetcode.com/problems/word-frequency/description

**Problem Statement:**
- Input format and constraints: The input will be a string `s` containing words separated by spaces, and an integer `k` representing the kth most frequent word.
- Expected output format: The kth most frequent word in the string `s`.
- Key requirements and edge cases to consider:
  - Handling multiple words with the same frequency.
  - Case sensitivity (words are case-sensitive).
  - Punctuation attached to words (treat as separate words).
- Example test cases with explanations:
  - Input: `s = "i am am", k = 2`, Output: `"am"`.
  - Input: `s = "i i i i i i", k = 1`, Output: `"i"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the frequency of each word in the string `s` using a dictionary, then sort the words by frequency and return the kth most frequent word.
- Step-by-step breakdown of the solution:
  1. Split the input string `s` into words.
  2. Create a dictionary to store the frequency of each word.
  3. Iterate over the words and update the frequency in the dictionary.
  4. Sort the words by frequency and return the kth most frequent word.
- Why this approach comes to mind first: It's a straightforward solution that involves counting word frequencies and sorting.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

string kthMostFrequent(string s, int k) {
    // Split the input string into words
    vector<string> words;
    string word;
    for (char c : s) {
        if (c == ' ') {
            words.push_back(word);
            word.clear();
        } else {
            word += c;
        }
    }
    words.push_back(word);

    // Create a dictionary to store the frequency of each word
    unordered_map<string, int> frequency;
    for (string word : words) {
        frequency[word]++;
    }

    // Sort the words by frequency and return the kth most frequent word
    vector<pair<string, int>> wordFrequency;
    for (auto& pair : frequency) {
        wordFrequency.push_back(pair);
    }
    sort(wordFrequency.begin(), wordFrequency.end(), [](pair<string, int> a, pair<string, int> b) {
        return a.second > b.second;
    });
    return wordFrequency[k - 1].first;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique words in the string `s`. This is because we sort the words by frequency using a comparison-based sorting algorithm.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique words in the string `s`. This is because we store the frequency of each word in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we sort the words by frequency, and the space complexity occurs because we store the frequency of each word in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to store the words and their frequencies, and then pop the kth most frequent word from the queue.
- Detailed breakdown of the approach:
  1. Split the input string `s` into words.
  2. Create a dictionary to store the frequency of each word.
  3. Iterate over the words and update the frequency in the dictionary.
  4. Create a priority queue and push the words and their frequencies into the queue.
  5. Pop the kth most frequent word from the queue and return it.
- Proof of optimality: This approach is optimal because it avoids sorting the words by frequency, which has a time complexity of $O(n \log n)$. Instead, it uses a priority queue to store the words and their frequencies, which has a time complexity of $O(n \log k)$.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>

string kthMostFrequent(string s, int k) {
    // Split the input string into words
    vector<string> words;
    string word;
    for (char c : s) {
        if (c == ' ') {
            words.push_back(word);
            word.clear();
        } else {
            word += c;
        }
    }
    words.push_back(word);

    // Create a dictionary to store the frequency of each word
    unordered_map<string, int> frequency;
    for (string word : words) {
        frequency[word]++;
    }

    // Create a priority queue and push the words and their frequencies into the queue
    priority_queue<pair<int, string>> queue;
    for (auto& pair : frequency) {
        queue.push({pair.second, pair.first});
    }

    // Pop the kth most frequent word from the queue and return it
    for (int i = 0; i < k - 1; i++) {
        queue.pop();
    }
    return queue.top().second;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of unique words in the string `s` and $k$ is the kth most frequent word. This is because we use a priority queue to store the words and their frequencies.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique words in the string `s`. This is because we store the frequency of each word in a dictionary and the priority queue.
> - **Optimality proof:** This approach is optimal because it avoids sorting the words by frequency, which has a time complexity of $O(n \log n)$. Instead, it uses a priority queue to store the words and their frequencies, which has a time complexity of $O(n \log k)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, dictionaries, and string manipulation.
- Problem-solving patterns identified: Using a priority queue to store words and their frequencies, and popping the kth most frequent word from the queue.
- Optimization techniques learned: Avoiding sorting by using a priority queue.
- Similar problems to practice: Word frequency problems, priority queue problems, and string manipulation problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty input strings or words with the same frequency.
- Edge cases to watch for: Handling multiple words with the same frequency, case sensitivity, and punctuation attached to words.
- Performance pitfalls: Using sorting algorithms with high time complexities, such as comparison-based sorting algorithms.
- Testing considerations: Testing with different input strings, words, and frequencies to ensure the solution works correctly.