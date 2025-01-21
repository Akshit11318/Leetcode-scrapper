## Count Anagrams
**Problem Link:** https://leetcode.com/problems/count-anagrams/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and a list of strings `words`, find all the anagrams of `s` in `words`.
- Expected output format: Return the number of anagrams found.
- Key requirements and edge cases to consider: 
    - The input string `s` can contain any lowercase letters.
    - The list of strings `words` can contain any number of strings, each containing only lowercase letters.
    - An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.
- Example test cases with explanations:
    - Input: `s = "ab", words = ["a","b","ba","ab"]`, Output: `2`
    - Input: `s = "ab", words = ["a","ab","abc"]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to sort the characters in the input string `s` and then for each word in the list of words, sort its characters and compare it with the sorted `s`. If they match, it means the word is an anagram of `s`.
- Step-by-step breakdown of the solution:
    1. Sort the characters in the input string `s`.
    2. For each word in the list of words, sort its characters.
    3. Compare the sorted word with the sorted `s`. If they are equal, increment the anagram count.
- Why this approach comes to mind first: It's a straightforward method to check for anagrams by rearranging the letters of each word and comparing them with the rearranged letters of `s`.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int countAnagrams(std::string s, std::vector<std::string>& words) {
    std::sort(s.begin(), s.end()); // Sort the characters in s
    int anagramCount = 0;
    for (const auto& word : words) {
        std::string sortedWord = word;
        std::sort(sortedWord.begin(), sortedWord.end()); // Sort the characters in each word
        if (s == sortedWord) { // Compare the sorted word with the sorted s
            anagramCount++;
        }
    }
    return anagramCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot \log m)$, where $n$ is the number of words and $m$ is the maximum length of a word. The sorting operation for each word takes $O(m \cdot \log m)$ time, and this is done for each of the $n$ words.
> - **Space Complexity:** $O(m)$, for sorting the characters in each word.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation performed for each word, and the space complexity is due to the temporary space needed for sorting.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the characters in each word, we can use a frequency count approach. Count the frequency of each character in the input string `s` and then for each word in the list, count the frequency of its characters. If the frequency counts match, it means the word is an anagram of `s`.
- Detailed breakdown of the approach:
    1. Count the frequency of each character in the input string `s`.
    2. For each word in the list of words, count the frequency of its characters.
    3. Compare the frequency counts of the word with the frequency counts of `s`. If they are equal, increment the anagram count.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n \cdot m \cdot \log m)$ to $O(n \cdot m)$ by avoiding the sorting operation.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

int countAnagrams(std::string s, std::vector<std::string>& words) {
    std::unordered_map<char, int> sCount; // Frequency count of characters in s
    for (char c : s) {
        sCount[c]++;
    }
    int anagramCount = 0;
    for (const auto& word : words) {
        if (word.size() != s.size()) continue; // Anagram must have the same length
        std::unordered_map<char, int> wordCount; // Frequency count of characters in the word
        for (char c : word) {
            wordCount[c]++;
        }
        if (sCount == wordCount) { // Compare the frequency counts
            anagramCount++;
        }
    }
    return anagramCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. Counting the frequency of characters in each word takes $O(m)$ time, and this is done for each of the $n$ words.
> - **Space Complexity:** $O(m)$, for storing the frequency counts of characters in each word.
> - **Optimality proof:** The frequency count approach is optimal because it directly compares the character compositions of the input string and each word without the need for sorting, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency count, anagram detection.
- Problem-solving patterns identified: Using frequency counts to compare character compositions.
- Optimization techniques learned: Avoiding unnecessary sorting operations.
- Similar problems to practice: Other anagram-related problems, such as finding all anagrams in a given list of words.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly comparing frequency counts, not checking for equal lengths before comparing frequency counts.
- Edge cases to watch for: Words with different lengths, empty input string or list of words.
- Performance pitfalls: Using inefficient data structures or algorithms for counting frequencies or comparing compositions.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases.