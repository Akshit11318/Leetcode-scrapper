## Sentence Similarity III

**Problem Link:** https://leetcode.com/problems/sentence-similarity-iii/description

**Problem Statement:**
- Input format and constraints: Given two sentences `sentence1` and `sentence2`, return `true` if they are similar, and `false` otherwise. Two sentences are similar if they are identical or if one sentence can be made identical to the other by adding, removing, and rearranging words in one sentence.
- Expected output format: A boolean value indicating whether the two sentences are similar.
- Key requirements and edge cases to consider:
  - Handling identical sentences.
  - Handling sentences with different word orders.
  - Handling sentences with different word counts (i.e., adding or removing words).
- Example test cases with explanations:
  - Input: `sentence1 = "My name is Haley", sentence2 = "My name is Haley"` Output: `true`
  - Input: `sentence1 = "of", sentence2 = "A lot of words were deleted"` Output: `false`
  - Input: `sentence1 = "create","lit", sentence2 = "in fact we need","to lit"` Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check if the two sentences are identical. If not, try rearranging the words in one sentence to match the other.
- Step-by-step breakdown of the solution:
  1. Split the sentences into words.
  2. Compare the two lists of words.
  3. If the lists are identical, return `true`.
  4. If the lists are not identical, try rearranging the words in one list to match the other.
- Why this approach comes to mind first: It's a straightforward approach that checks for identical sentences and then tries to rearrange the words to match.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

bool areSentencesSimilar(const std::string& sentence1, const std::string& sentence2) {
    std::vector<std::string> words1;
    std::vector<std::string> words2;
    std::string word;
    
    // Split sentence1 into words
    for (char c : sentence1) {
        if (c == ' ') {
            words1.push_back(word);
            word.clear();
        } else {
            word += c;
        }
    }
    words1.push_back(word);
    
    // Split sentence2 into words
    for (char c : sentence2) {
        if (c == ' ') {
            words2.push_back(word);
            word.clear();
        } else {
            word += c;
        }
    }
    words2.push_back(word);
    
    // Compare the two lists of words
    if (words1 == words2) {
        return true;
    }
    
    // Try rearranging the words in one list to match the other
    std::sort(words1.begin(), words1.end());
    std::sort(words2.begin(), words2.end());
    return words1 == words2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of words in both sentences. This is because we're sorting the lists of words.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of words in both sentences. This is because we're storing the lists of words.
> - **Why these complexities occur:** The time complexity occurs because we're sorting the lists of words, and the space complexity occurs because we're storing the lists of words.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying to rearrange the words in one sentence to match the other, we can use a two-pointer technique to find the longest common prefix and suffix of the two sentences.
- Detailed breakdown of the approach:
  1. Split the sentences into words.
  2. Use two pointers to find the longest common prefix of the two sentences.
  3. Use two pointers to find the longest common suffix of the two sentences.
  4. If the sum of the lengths of the longest common prefix and suffix is equal to the length of the shorter sentence, return `true`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the sentences, and it uses a two-pointer technique to find the longest common prefix and suffix.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

bool areSentencesSimilar(const std::string& sentence1, const std::string& sentence2) {
    std::istringstream iss1(sentence1);
    std::istringstream iss2(sentence2);
    std::vector<std::string> words1;
    std::vector<std::string> words2;
    std::string word;
    
    // Split sentence1 into words
    while (iss1 >> word) {
        words1.push_back(word);
    }
    
    // Split sentence2 into words
    while (iss2 >> word) {
        words2.push_back(word);
    }
    
    int i = 0;
    int j = words1.size() - 1;
    int k = 0;
    int l = words2.size() - 1;
    
    // Find the longest common prefix
    while (i <= j && k <= l && words1[i] == words2[k]) {
        i++;
        k++;
    }
    
    // Find the longest common suffix
    while (j >= i && l >= k && words1[j] == words2[l]) {
        j--;
        l--;
    }
    
    // If the sum of the lengths of the longest common prefix and suffix is equal to the length of the shorter sentence, return true
    return i > j || k > l;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of words in both sentences. This is because we're using a two-pointer technique to find the longest common prefix and suffix.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of words in both sentences. This is because we're storing the lists of words.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the sentences, and it uses a two-pointer technique to find the longest common prefix and suffix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, longest common prefix and suffix.
- Problem-solving patterns identified: Using a two-pointer technique to find the longest common prefix and suffix.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity.
- Similar problems to practice: Longest common prefix, longest common suffix, two-pointer technique.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not using a two-pointer technique.
- Edge cases to watch for: Identical sentences, sentences with different word orders.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Testing for identical sentences, sentences with different word orders, sentences with different word counts.