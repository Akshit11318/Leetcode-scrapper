## Compare Strings by Frequency of the Smallest Character

**Problem Link:** https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description

**Problem Statement:**
- Input format: Two strings `query` and `word`
- Constraints: Both strings are non-empty and consist only of lowercase English letters.
- Expected output format: Return the lexicographical order of `query` and `word` based on the frequency of the smallest character in each string.
- Key requirements and edge cases to consider: 
    - Handling strings of different lengths.
    - Dealing with strings that have the same smallest character but different frequencies.
    - Comparing strings with the same frequency of the smallest character.

**Example Test Cases:**
- `query = "aaa", word = "aa"`: Return "aa" because the smallest character 'a' appears twice in "aa" and three times in "aaa".
- `query = "abc", word = "bca"`: Return "abc" because the smallest character 'a' appears once in both strings.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare the frequency of the smallest character in each string.
- Step-by-step breakdown of the solution:
    1. Find the smallest character in `query` and `word`.
    2. Count the frequency of the smallest character in both strings.
    3. Compare the frequencies to determine the lexicographical order.
- Why this approach comes to mind first: It directly addresses the problem statement by comparing the frequency of the smallest character in each string.

```cpp
#include <string>
#include <algorithm>

string numSmallerByFrequency(string query, string word) {
    int countQuery = 0;
    int countWord = 0;
    
    // Find the smallest character in query and count its frequency
    char smallestQuery = *min_element(query.begin(), query.end());
    for (char c : query) {
        if (c == smallestQuery) {
            countQuery++;
        }
    }
    
    // Find the smallest character in word and count its frequency
    char smallestWord = *min_element(word.begin(), word.end());
    for (char c : word) {
        if (c == smallestWord) {
            countWord++;
        }
    }
    
    // Compare the frequencies to determine the lexicographical order
    if (countQuery < countWord) {
        return "query";
    } else if (countQuery > countWord) {
        return "word";
    } else {
        // If frequencies are equal, compare the strings lexicographically
        if (query < word) {
            return "query";
        } else {
            return "word";
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of `query` and `word` respectively. This is because we are iterating over both strings to find the smallest character and count its frequency.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the smallest characters and their frequencies.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each character in the strings. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but we can simplify the code and improve readability.
- Detailed breakdown of the approach: 
    1. Find the smallest character in `query` and `word`.
    2. Count the frequency of the smallest character in both strings.
    3. Compare the frequencies to determine the lexicographical order.
- Proof of optimality: This approach is optimal because it directly addresses the problem statement and has a linear time complexity.

```cpp
#include <string>
#include <algorithm>

int numSmallerByFrequency(string query, string word) {
    auto countSmallest = [](string s) {
        char smallest = *min_element(s.begin(), s.end());
        return count(s.begin(), s.end(), smallest);
    };
    
    int countQuery = countSmallest(query);
    int countWord = countSmallest(word);
    
    return countQuery < countWord;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of `query` and `word` respectively. This is because we are iterating over both strings to find the smallest character and count its frequency.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the smallest characters and their frequencies.
> - **Optimality proof:** This approach is optimal because it directly addresses the problem statement and has a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - Iterating over strings to find the smallest character.
    - Counting the frequency of a character in a string.
    - Comparing frequencies to determine lexicographical order.
- Problem-solving patterns identified: 
    - Directly addressing the problem statement.
    - Simplifying code for improved readability.
- Optimization techniques learned: 
    - Using lambda functions to simplify code.
    - Using standard library functions like `min_element` and `count`.

**Mistakes to Avoid:**
- Common implementation errors: 
    - Not handling edge cases like empty strings.
    - Not comparing frequencies correctly.
- Edge cases to watch for: 
    - Strings of different lengths.
    - Strings with the same smallest character but different frequencies.
- Performance pitfalls: 
    - Using inefficient algorithms with high time complexity.
- Testing considerations: 
    - Testing with different input strings.
    - Testing with edge cases.