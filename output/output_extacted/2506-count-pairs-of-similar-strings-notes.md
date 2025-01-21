## Count Pairs of Similar Strings
**Problem Link:** https://leetcode.com/problems/count-pairs-of-similar-strings/description

**Problem Statement:**
- Input: An array of strings `words`.
- Constraints: `1 <= words.length <= 100`, `1 <= words[i].length <= 10`, `words[i]` consists of lowercase English letters.
- Expected Output: The number of pairs of similar strings.
- Key Requirements and Edge Cases:
  - Two strings are similar if they have the same characters, but not necessarily in the same order.
  - A pair of strings can only be counted once.

### Brute Force Approach
**Explanation:**
- The initial thought process is to compare each pair of strings in the array to check if they are similar.
- Step-by-step breakdown:
  1. Generate all possible pairs of strings from the input array.
  2. For each pair, compare the sorted strings. If they are equal, it means the original strings are similar.
  3. Count the number of similar pairs.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int countSimilarPairs(std::vector<std::string>& words) {
    int count = 0;
    for (int i = 0; i < words.size(); i++) {
        for (int j = i + 1; j < words.size(); j++) {
            std::string word1 = words[i];
            std::string word2 = words[j];
            std::sort(word1.begin(), word1.end());
            std::sort(word2.begin(), word2.end());
            if (word1 == word2) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m \log m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we are generating $n^2$ pairs and sorting each word in $m \log m$ time.
> - **Space Complexity:** $O(m)$, as we need to store the sorted versions of the strings.
> - **Why these complexities occur:** The brute force approach involves comparing each pair of strings and sorting them, which leads to these complexities.

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of sorting each string for every comparison, we can sort each string once and store it in a map with its frequency.
- Detailed breakdown:
  1. Sort each string in the array and store it in a map with its frequency.
  2. For each string, calculate the number of similar pairs by multiplying its frequency by the frequency of the same sorted string minus one and dividing by two (to avoid counting each pair twice).
  3. Sum up the counts for all strings.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

int countSimilarPairs(std::vector<std::string>& words) {
    std::unordered_map<std::string, int> freq;
    for (const auto& word : words) {
        std::string sortedWord = word;
        std::sort(sortedWord.begin(), sortedWord.end());
        freq[sortedWord]++;
    }
    int count = 0;
    for (const auto& pair : freq) {
        int f = pair.second;
        count += (f * (f - 1)) / 2;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \log m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we are sorting each word once and storing it in a map.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the sorted strings in a map.
> - **Optimality proof:** This approach is optimal because we are minimizing the number of sorting operations and using a map to store the frequencies, which allows us to calculate the number of similar pairs in linear time.

### Final Notes
**Learning Points:**
- Key algorithmic concepts: sorting, frequency counting, and combinatorics.
- Problem-solving patterns: reducing the number of operations by sorting each string once and using a map to store frequencies.
- Optimization techniques: minimizing the number of sorting operations and using a map to store frequencies.

**Mistakes to Avoid:**
- Common implementation errors: not sorting each string before comparing it with others, not using a map to store frequencies.
- Edge cases to watch for: empty input array, strings with different lengths.
- Performance pitfalls: not minimizing the number of sorting operations, not using a map to store frequencies.
- Testing considerations: testing with different input sizes, testing with strings of different lengths.