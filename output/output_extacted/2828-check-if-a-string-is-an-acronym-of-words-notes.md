## Check if a String is an Acronym of Words

**Problem Link:** https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description

**Problem Statement:**
- Input: A string `s` and a list of strings `words`.
- Output: Return `true` if `s` is an acronym of some permutation of `words`, and `false` otherwise.
- Key requirements and edge cases:
  - Each word in `words` can only be used once.
  - `s` is case-sensitive.
  - `s` is guaranteed to be an acronym of some permutation of `words` if the solution returns `true`.
- Example test cases:
  - `s = "internationalization", words = ["international","ion","ization"]` returns `true`.
  - `s = "laid", words = ["Laid"]` returns `false`.

---

### Brute Force Approach

**Explanation:**
- Generate all permutations of `words`.
- For each permutation, concatenate the first letter of each word to form a string.
- Check if the formed string is equal to `s`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool isAcronym(string s, vector<string>& words) {
    // Generate all permutations of words
    sort(words.begin(), words.end());
    do {
        string acronym;
        for (auto& word : words) {
            acronym += word[0];
        }
        if (acronym == s) {
            return true;
        }
    } while (next_permutation(words.begin(), words.end()));
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because we generate all permutations of `words` and for each permutation, we concatenate the first letter of each word.
> - **Space Complexity:** $O(n)$, where $n$ is the number of words. This is because we need to store the current permutation of `words`.
> - **Why these complexities occur:** The high time complexity occurs because generating all permutations of `words` has a factorial time complexity. The space complexity is linear because we only need to store the current permutation of `words`.

---

### Optimal Approach (Required)

**Explanation:**
- Count the frequency of each character in `s`.
- For each word in `words`, decrement the frequency of the first character of the word.
- If the frequency of any character becomes negative, return `false`.
- If we have processed all words and all frequencies are non-negative, return `true`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

bool isAcronym(string s, vector<string>& words) {
    unordered_map<char, int> freq;
    for (auto& c : s) {
        freq[c]++;
    }
    for (auto& word : words) {
        freq[word[0]]--;
        if (freq[word[0]] < 0) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `s` and $m` is the total number of characters in `words`. This is because we count the frequency of each character in `s` and then process each word in `words`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique characters in `s`. This is because we need to store the frequency of each character in `s`.
> - **Optimality proof:** This approach is optimal because we only need to process each character in `s` and `words` once. We use an unordered map to store the frequency of each character, which allows us to look up and update the frequency in constant time.

---

### Final Notes

**Learning Points:**
- The importance of counting frequency of characters in a string.
- Using an unordered map to store frequency of characters.
- The concept of permutations and how to generate them.
- Optimizing the solution by avoiding unnecessary operations.

**Mistakes to Avoid:**
- Generating all permutations of `words` unnecessarily.
- Not checking for negative frequencies.
- Not handling edge cases such as empty strings or words.
- Not optimizing the solution for large inputs.