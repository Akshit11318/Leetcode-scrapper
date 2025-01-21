## Sorting the Sentence

**Problem Link:** https://leetcode.com/problems/sorting-the-sentence/description

**Problem Statement:**
- Input: A string `s` containing a sentence with words that have their original position as a suffix (e.g., "is2 Thi1s T4est 3a").
- Output: A string where the words are sorted based on their suffix (the number at the end of each word), and the numbers are removed from the words.
- Key requirements and edge cases to consider:
  - The input string will contain at least one word and at most 9 words.
  - Each word will have a unique number as its suffix.
  - The numbers will be in the range [1, 9].
- Example test cases with explanations:
  - Input: "is2 Thi1s T4est 3a"
    Output: "Thi1s is2 3a T4est"
    Explanation: The words are sorted based on their suffixes, and the suffixes are removed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Split the input string into words, then for each word, extract the number at the end, and sort the words based on these numbers.
- Step-by-step breakdown of the solution:
  1. Split the input string into words.
  2. For each word, extract the number at the end.
  3. Store the word and its corresponding number in a data structure (e.g., a vector of pairs).
  4. Sort the vector of pairs based on the numbers.
  5. Construct the output string by concatenating the words in the sorted order, without their numbers.
- Why this approach comes to mind first: It directly addresses the problem statement by explicitly sorting the words based on their suffixes.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::string sortSentence(std::string s) {
    std::vector<std::pair<std::string, int>> words;
    std::string word = "";
    for (char c : s) {
        if (c == ' ') {
            int num = 0;
            while (word.back() >= '0' && word.back() <= '9') {
                num = num * 10 + (word.back() - '0');
                word.pop_back();
            }
            words.push_back({word, num});
            word = "";
        } else {
            word += c;
        }
    }
    // Handle the last word
    if (!word.empty()) {
        int num = 0;
        while (word.back() >= '0' && word.back() <= '9') {
            num = num * 10 + (word.back() - '0');
            word.pop_back();
        }
        words.push_back({word, num});
    }
    std::sort(words.begin(), words.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
    });
    std::string result = "";
    for (const auto& pair : words) {
        result += pair.first + " ";
    }
    // Remove the trailing space
    if (!result.empty()) {
        result.pop_back();
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \log n)$, where $n$ is the number of words and $m$ is the average length of a word. The sorting operation dominates the complexity.
> - **Space Complexity:** $O(n \cdot m)$, as we store each word and its corresponding number.
> - **Why these complexities occur:** The sorting step is the main contributor to the time complexity, while the space complexity arises from storing all the words and their numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the words after they have been processed, we can directly place each word at its correct position based on its suffix. This avoids the need for a separate sorting step.
- Detailed breakdown of the approach:
  1. Create an array of strings where each index corresponds to a word's position (based on its suffix).
  2. Iterate through the input string, splitting it into words.
  3. For each word, extract its suffix (the number at the end) and use this number as the index to place the word in the array.
  4. After processing all words, concatenate the words from the array in order to form the final sorted sentence.
- Proof of optimality: This approach has a linear time complexity because it processes each character in the input string once and places each word directly into its final position, avoiding the overhead of a separate sorting step.

```cpp
std::string sortSentence(std::string s) {
    std::vector<std::string> words(9);
    std::string word = "";
    for (char c : s) {
        if (c == ' ') {
            int pos = word.back() - '0' - 1;
            word.pop_back();
            words[pos] = word;
            word = "";
        } else {
            word += c;
        }
    }
    // Handle the last word
    if (!word.empty()) {
        int pos = word.back() - '0' - 1;
        word.pop_back();
        words[pos] = word;
    }
    std::string result = "";
    for (const auto& w : words) {
        if (!w.empty()) {
            result += w + " ";
        }
    }
    // Remove the trailing space
    if (!result.empty()) {
        result.pop_back();
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because we process each character once.
> - **Space Complexity:** $O(n \cdot m)$, for storing the words.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to sort the sentence, directly placing each word in its final position without the need for a separate sorting step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct placement of elements into their final positions based on certain criteria, avoiding unnecessary sorting steps.
- Problem-solving patterns identified: Processing input strings character by character, using suffixes to determine word positions.
- Optimization techniques learned: Minimizing the number of operations by directly placing elements into their final positions.
- Similar problems to practice: Other string manipulation and sorting problems where direct placement or clever indexing can simplify the solution.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the last word in the input string, forgetting to remove the trailing space from the result.
- Edge cases to watch for: Empty input strings, strings with a single word, words with multiple-digit suffixes.
- Performance pitfalls: Using inefficient sorting algorithms or data structures that do not take advantage of the problem's specific constraints.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness and robustness.