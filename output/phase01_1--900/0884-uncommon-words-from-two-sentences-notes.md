## Uncommon Words From Two Sentences
**Problem Link:** https://leetcode.com/problems/uncommon-words-from-two-sentences/description

**Problem Statement:**
- Input format and constraints: We are given two sentences as strings `A` and `B`. Each sentence consists of words separated by spaces. We need to find the words that appear once in total across both sentences.
- Expected output format: The output should be a list of words that are uncommon, meaning they appear exactly once in the combined sentences.
- Key requirements and edge cases to consider: We should ignore the case of words (i.e., treat 'a' and 'A' as the same word), and we should return the uncommon words in any order.

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to count the occurrences of each word in both sentences and then select the words that appear exactly once.
- Step-by-step breakdown of the solution:
  1. Split both sentences into lists of words.
  2. Create a dictionary to store the count of each word.
  3. Iterate over the words in both lists, updating the count in the dictionary.
  4. Iterate over the dictionary, selecting words with a count of 1.
- Why this approach comes to mind first: It's the most intuitive way to solve the problem, as it directly addresses the requirement of finding words that appear once.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>

vector<string> uncommonFromSentences(string A, string B) {
    unordered_map<string, int> wordCount;
    stringstream ssA(A), ssB(B);
    string word;

    // Count words in A
    while (ssA >> word) {
        for (auto &c : word) c = tolower(c); // Convert to lower case
        wordCount[word]++;
    }

    // Count words in B
    while (ssB >> word) {
        for (auto &c : word) c = tolower(c); // Convert to lower case
        wordCount[word]++;
    }

    vector<string> result;
    for (auto &pair : wordCount) {
        if (pair.second == 1) {
            result.push_back(pair.first);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the number of words in sentences $A$ and $B$ respectively. This is because we iterate over each word once to count its occurrences and then over the dictionary to find the uncommon words.
> - **Space Complexity:** $O(n + m)$, as in the worst case, every word could be unique, requiring space in the dictionary.
> - **Why these complexities occur:** These complexities arise from the operations of iterating over the input to count word occurrences and storing these counts in a dictionary.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is essentially the same as the brute force approach, as it involves counting the occurrences of each word and then selecting those that appear exactly once. The key to optimality is using an efficient data structure like an unordered map for word counting.
- Detailed breakdown of the approach: The steps are similar to the brute force approach but with a focus on efficiency.
  1. Split the sentences into words.
  2. Use an unordered map to count the occurrences of each word efficiently.
  3. Filter the map for words that appear exactly once.
- Proof of optimality: This approach is optimal because it only requires a single pass over the input data to count the words and then a pass over the map to find the uncommon words, resulting in a linear time complexity.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>

vector<string> uncommonFromSentences(string A, string B) {
    unordered_map<string, int> wordCount;
    stringstream ssA(A), ssB(B);
    string word;

    // Count words in A and B
    while (ssA >> word) {
        for (auto &c : word) c = tolower(c);
        wordCount[word]++;
    }
    while (ssB >> word) {
        for (auto &c : word) c = tolower(c);
        wordCount[word]++;
    }

    vector<string> result;
    for (auto &pair : wordCount) {
        if (pair.second == 1) result.push_back(pair.first);
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the number of words in sentences $A$ and $B$.
> - **Space Complexity:** $O(n + m)$, for storing the word counts.
> - **Optimality proof:** The linear time complexity is optimal for this problem because we must at least read the input once, and the use of an unordered map allows us to count and filter words in linear time.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of data structures like unordered maps for word counting.
- Problem-solving patterns identified: Counting occurrences and filtering based on counts.
- Optimization techniques learned: Using efficient data structures to reduce time complexity.
- Similar problems to practice: Other problems involving word counting or filtering based on counts.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle case sensitivity or not checking for edge cases like empty strings.
- Edge cases to watch for: Empty input strings, strings with only one word, or strings with no uncommon words.
- Performance pitfalls: Using inefficient data structures like arrays or linked lists for word counting, leading to higher time complexities.