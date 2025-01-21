## Rearrange Words in a Sentence

**Problem Link:** https://leetcode.com/problems/rearrange-words-in-a-sentence/description

**Problem Statement:**
- Input format and constraints: The input is a sentence where each word is separated by a single space, and the words contain only lowercase English letters. The length of the sentence will not exceed $10^4$ characters.
- Expected output format: The output should be a rearranged sentence where the words are ordered based on the length of the words.
- Key requirements and edge cases to consider: The words should be rearranged based on their lengths in ascending order. If two or more words have the same length, their original order should be maintained.
- Example test cases with explanations:
  - Input: "i love eating burger"
  - Output: "i love eating burger"
  - Explanation: The words are rearranged based on their lengths. The word "i" has a length of 1, "love" has a length of 4, "eating" has a length of 6, and "burger" has a length of 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a brute force method where we split the sentence into words, sort the words based on their lengths, and then join them back into a sentence.
- Step-by-step breakdown of the solution:
  1. Split the input sentence into words using the space character as a delimiter.
  2. Create a list of pairs where each pair contains a word and its length.
  3. Sort the list of pairs based on the length of the words.
  4. Join the sorted words back into a sentence.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

string rearrangeSentence(string sentence) {
    istringstream iss(sentence);
    vector<string> words;
    string word;

    // Split the sentence into words
    while (iss >> word) {
        words.push_back(word);
    }

    // Create a list of pairs where each pair contains a word and its length
    vector<pair<int, string>> wordLengths;
    for (const auto& w : words) {
        wordLengths.push_back({w.length(), w});
    }

    // Sort the list of pairs based on the length of the words
    stable_sort(wordLengths.begin(), wordLengths.end(), [](const auto& a, const auto& b) {
        return a.first < b.first;
    });

    // Join the sorted words back into a sentence
    string result;
    for (const auto& wl : wordLengths) {
        result += wl.second + " ";
    }

    // Remove the trailing space
    if (!result.empty()) {
        result.pop_back();
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of words in the sentence. The sorting operation dominates the time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the number of words in the sentence. We need to store the words and their lengths in a list of pairs.
> - **Why these complexities occur:** The sorting operation is the main contributor to the time complexity. The space complexity is due to the storage of the words and their lengths.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient sorting algorithm, such as `stable_sort`, to maintain the relative order of words with the same length.
- Detailed breakdown of the approach:
  1. Split the input sentence into words using the space character as a delimiter.
  2. Create a list of pairs where each pair contains a word and its length.
  3. Use `stable_sort` to sort the list of pairs based on the length of the words.
  4. Join the sorted words back into a sentence.
- Proof of optimality: This approach is optimal because it uses a stable sorting algorithm, which maintains the relative order of words with the same length.
- Why further optimization is impossible: The time complexity of $O(n \log n)$ is optimal for comparison-based sorting algorithms.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

string rearrangeSentence(string sentence) {
    istringstream iss(sentence);
    vector<string> words;
    string word;

    // Split the sentence into words
    while (iss >> word) {
        words.push_back(word);
    }

    // Sort the words based on their lengths
    stable_sort(words.begin(), words.end(), [](const auto& a, const auto& b) {
        return a.length() < b.length();
    });

    // Join the sorted words back into a sentence
    string result;
    for (const auto& w : words) {
        result += w + " ";
    }

    // Remove the trailing space
    if (!result.empty()) {
        result.pop_back();
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of words in the sentence. The sorting operation dominates the time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the number of words in the sentence. We need to store the words in a vector.
> - **Optimality proof:** The use of `stable_sort` ensures that the relative order of words with the same length is maintained.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, stable sorting, and string manipulation.
- Problem-solving patterns identified: Splitting the input into words, sorting the words based on a criteria, and joining the sorted words back into a sentence.
- Optimization techniques learned: Using a stable sorting algorithm to maintain the relative order of words with the same length.
- Similar problems to practice: Other string manipulation and sorting problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to remove the trailing space from the result, using an unstable sorting algorithm, and not handling edge cases.
- Edge cases to watch for: Empty input sentence, sentence with a single word, and sentence with multiple words of the same length.
- Performance pitfalls: Using an inefficient sorting algorithm or not using a stable sorting algorithm.
- Testing considerations: Testing with different input sentences, including edge cases, to ensure the solution works correctly.